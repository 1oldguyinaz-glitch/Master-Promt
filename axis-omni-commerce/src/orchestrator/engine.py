from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .state import RunState, RunStatus
from ..agents.registry import AgentRegistry
from ..database.models import AxisOmniDB
from ..policy.engine import PolicyEngine


class AxisOmniEngine:
    """Minimal deterministic runtime for routing AXIS → VERITY → BEACON.

    This class does not call an LLM by itself. A model/tool adapter can be injected
    later. The important behavior here is state, routing, policy gates, approvals,
    persistence, and auditability.
    """

    def __init__(self, registry: AgentRegistry, db: AxisOmniDB,
                 policy: PolicyEngine | None = None) -> None:
        self.registry = registry
        self.db = db
        self.policy = policy or PolicyEngine()

    def start(self, objective: str) -> RunState:
        state = RunState(objective=objective, status=RunStatus.RUNNING)
        state.record("run_started", role="AXIS_OMNI")
        self.db.save_run(state)
        self._audit(state, "run_started", "AXIS_OMNI", {"objective": objective})
        return state

    def route(self, state: RunState, role: str, stage: str) -> RunState:
        self.registry.get(role)
        state.current_role = role
        state.stage = stage
        state.record("routed", role=role, stage=stage)
        self.db.save_run(state)
        self._audit(state, "routed", "AXIS_OMNI", {"role": role, "stage": stage})
        return state

    def verity_gate(self, state: RunState, product: dict[str, Any]) -> RunState:
        decision = self.policy.check_product(product)
        state.current_role = "VERITY"
        state.record("verity_gate", allowed=decision.allowed, reason=decision.reason)
        if not decision.allowed:
            state.status = RunStatus.BLOCKED
            state.risk_flags.append(decision.reason)
        self.db.save_run(state)
        self._audit(state, "verity_gate", "VERITY", {
            "allowed": decision.allowed,
            "approval_required": decision.approval_required,
            "reason": decision.reason,
        })
        return state

    def request_action(self, state: RunState, action: str, amount: float = 0.0) -> RunState:
        decision = self.policy.check_action(action, amount)
        if decision.approval_required:
            state.status = RunStatus.WAITING_APPROVAL
            if action not in state.approvals_required:
                state.approvals_required.append(action)
        elif not decision.allowed:
            state.status = RunStatus.BLOCKED
        state.record("action_gate", action=action, amount=amount,
                     allowed=decision.allowed, reason=decision.reason)
        self.db.save_run(state)
        self._audit(state, "action_gate", "AXIS_OMNI", {
            "action": action,
            "amount": amount,
            "allowed": decision.allowed,
            "approval_required": decision.approval_required,
            "reason": decision.reason,
        })
        return state

    def complete(self, state: RunState) -> RunState:
        state.status = RunStatus.COMPLETED
        state.stage = "COMPLETE"
        state.current_role = "AXIS_OMNI"
        state.record("run_completed")
        self.db.save_run(state)
        self._audit(state, "run_completed", "AXIS_OMNI", {})
        return state

    def _audit(self, state: RunState, event_type: str, actor: str,
               payload: dict[str, Any]) -> None:
        self.db.add_audit_event(
            state.run_id,
            event_type,
            actor,
            payload,
            datetime.now(timezone.utc).isoformat(),
        )
