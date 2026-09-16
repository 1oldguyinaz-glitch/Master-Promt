"""AXIS connected-Gmail transport adapter.

This module defines the deterministic wire format used by the connected Gmail
account. Gmail is transport only; AXIS Back Office/runtime state remains
canonical. Actual Gmail reads/writes are performed by the authorized connected
Gmail integration, never by embedded credentials.
"""
from __future__ import annotations

from dataclasses import dataclass
from email.parser import Parser
from typing import Mapping

INTERNAL_MARKER = "X-AXIS-Internal"
SUBJECT_PREFIX = "[AXIS-HANDOFF]"


@dataclass(frozen=True)
class GmailHandoff:
    handoff_id: str
    workflow_id: str
    from_agent: str
    to_agent: str
    requested_action: str
    idempotency_key: str
    hop_count: int = 0
    priority: str = "normal"

    def subject(self) -> str:
        return f"{SUBJECT_PREFIX} {self.workflow_id} {self.from_agent}->{self.to_agent}"

    def body(self) -> str:
        return "\n".join([
            f"{INTERNAL_MARKER}: true",
            f"Handoff-ID: {self.handoff_id}",
            f"Workflow-ID: {self.workflow_id}",
            f"From-Agent: {self.from_agent}",
            f"To-Agent: {self.to_agent}",
            f"Requested-Action: {self.requested_action}",
            f"Priority: {self.priority}",
            f"Hop-Count: {self.hop_count}",
            f"Idempotency-Key: {self.idempotency_key}",
        ])


def parse_internal_message(subject: str, body: str) -> GmailHandoff | None:
    """Parse an AXIS internal Gmail message; ignore ordinary customer email."""
    if not subject.startswith(SUBJECT_PREFIX):
        return None
    headers: Mapping[str, str] = Parser().parsestr(body)
    if headers.get(INTERNAL_MARKER, "").lower() != "true":
        return None
    return GmailHandoff(
        handoff_id=headers["Handoff-ID"],
        workflow_id=headers["Workflow-ID"],
        from_agent=headers["From-Agent"],
        to_agent=headers["To-Agent"],
        requested_action=headers["Requested-Action"],
        priority=headers.get("Priority", "normal"),
        hop_count=int(headers.get("Hop-Count", "0")),
        idempotency_key=headers["Idempotency-Key"],
    )


def to_runtime_payload(handoff: GmailHandoff) -> dict:
    return {
        "handoff_id": handoff.handoff_id,
        "workflow_id": handoff.workflow_id,
        "from_agent": handoff.from_agent,
        "to_agent": handoff.to_agent,
        "requested_action": handoff.requested_action,
        "priority": handoff.priority,
        "hop_count": handoff.hop_count,
        "idempotency_key": handoff.idempotency_key,
        "axis_internal": True,
    }
