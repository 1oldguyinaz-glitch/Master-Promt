#!/usr/bin/env python3
"""AXIS OMNI minimal event-driven runtime core.

Dependency-free reference implementation for deterministic routing, idempotency,
hop/TTL safeguards, execution receipts, and canonical workflow state.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable
import uuid

MAX_HOPS = 6


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class Event:
    workflow_id: str
    event_type: str
    payload: dict[str, Any] = field(default_factory=dict)
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    idempotency_key: str = field(default_factory=lambda: str(uuid.uuid4()))
    hop_count: int = 0
    expires_at: str | None = None


@dataclass
class Receipt:
    event_id: str
    workflow_id: str
    status: str
    agent: str
    next_action: str
    timestamp: str = field(default_factory=utcnow)


class AxisRuntime:
    """Small executable kernel matching the Master Prompter runtime contract."""

    def __init__(self) -> None:
        self.handlers: dict[str, Callable[[Event, dict[str, Any]], str]] = {}
        self.seen: set[str] = set()
        self.state: dict[str, dict[str, Any]] = {}
        self.receipts: list[Receipt] = []

    def register(self, event_type: str, handler: Callable[[Event, dict[str, Any]], str]) -> None:
        self.handlers[event_type] = handler

    def _expired(self, event: Event) -> bool:
        if not event.expires_at:
            return False
        return datetime.fromisoformat(event.expires_at.replace("Z", "+00:00")) <= datetime.now(timezone.utc)

    def ingest(self, event: Event) -> Receipt:
        if event.idempotency_key in self.seen:
            return self._receipt(event, "duplicate_suppressed", "AXIS_OMNI", "none")
        if event.hop_count > MAX_HOPS:
            return self._receipt(event, "blocked_max_hops", "AXIS_OMNI", "owner_review")
        if self._expired(event):
            return self._receipt(event, "blocked_expired", "AXIS_OMNI", "none")

        self.seen.add(event.idempotency_key)
        workflow = self.state.setdefault(event.workflow_id, {"history": [], "status": "active"})
        workflow["history"].append({"event_id": event.event_id, "type": event.event_type, "at": utcnow()})

        handler = self.handlers.get(event.event_type)
        if handler is None:
            workflow["status"] = "blocked"
            return self._receipt(event, "unroutable", "AXIS_OMNI", "register_handler")

        next_action = handler(event, workflow)
        return self._receipt(event, "executed", event.payload.get("to_agent", "AXIS_OMNI"), next_action)

    def _receipt(self, event: Event, status: str, agent: str, next_action: str) -> Receipt:
        receipt = Receipt(event.event_id, event.workflow_id, status, agent, next_action)
        self.receipts.append(receipt)
        return receipt


def handoff_handler(event: Event, workflow: dict[str, Any]) -> str:
    workflow["last_agent"] = event.payload.get("to_agent", "AXIS_OMNI")
    workflow["status"] = "routed"
    return event.payload.get("requested_action", "process_handoff")


def build_default_runtime() -> AxisRuntime:
    runtime = AxisRuntime()
    runtime.register("agent_handoff", handoff_handler)
    return runtime
