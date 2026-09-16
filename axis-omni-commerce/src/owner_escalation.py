"""Owner escalation decision layer for AXIS OMNI.

The runtime emits an escalation request only when internal resolution cannot
answer a blocking question. Delivery is performed through the authorized
connected Gmail integration; no credentials are stored here.
"""
from __future__ import annotations
from dataclasses import dataclass

OWNER_EMAIL = "bdennis36@outlook.com"
ESCALATION_REASONS = {
    "missing_required_information",
    "owner_decision_required",
    "authorization_required",
    "ambiguous_instruction_blocks_execution",
    "external_action_requires_owner_input",
    "repeated_agent_failure",
}

@dataclass(frozen=True)
class OwnerEscalation:
    workflow_id: str
    handoff_id: str
    asking_agent: str
    reason: str
    exact_question: str
    why_blocked: str
    attempted_resolutions: tuple[str, ...] = ()
    recommended_options: tuple[str, ...] = ()

    def validate(self) -> None:
        if self.reason not in ESCALATION_REASONS:
            raise ValueError("reason is not an owner-escalation trigger")
        if not self.exact_question.strip():
            raise ValueError("exact_question is required")

    def subject(self) -> str:
        return f"[AXIS OWNER INPUT] {self.workflow_id} | {self.asking_agent}"

    def body(self) -> str:
        attempted = "\n".join(f"- {x}" for x in self.attempted_resolutions) or "- Internal resolution exhausted"
        options = "\n".join(f"- {x}" for x in self.recommended_options) or "- Reply with the missing information or decision"
        return (
            f"Workflow-ID: {self.workflow_id}\n"
            f"Handoff-ID: {self.handoff_id}\n"
            f"Asking-Agent: {self.asking_agent}\n"
            f"Reason: {self.reason}\n\n"
            f"QUESTION\n{self.exact_question}\n\n"
            f"WHY THIS IS BLOCKED\n{self.why_blocked}\n\n"
            f"ATTEMPTED RESOLUTION\n{attempted}\n\n"
            f"OPTIONS / NEXT MOVE\n{options}\n\n"
            "Reply directly to this email. AXIS should preserve the workflow ID and resume the blocked workflow from your answer."
        )


def should_escalate(reason: str, internal_resolution_available: bool, duplicate_pending: bool = False) -> bool:
    return reason in ESCALATION_REASONS and not internal_resolution_available and not duplicate_pending
