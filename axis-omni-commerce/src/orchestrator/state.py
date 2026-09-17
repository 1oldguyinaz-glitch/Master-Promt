from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from enum import Enum
from typing import Any
import json
import uuid


class RunStatus(str, Enum):
    CREATED = "CREATED"
    RUNNING = "RUNNING"
    WAITING_APPROVAL = "WAITING_APPROVAL"
    BLOCKED = "BLOCKED"
    COMPLETED = "COMPLETED"
    STOPPED = "STOPPED"


@dataclass
class RunState:
    objective: str
    run_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    status: RunStatus = RunStatus.CREATED
    stage: str = "INTAKE"
    supplier_id: str | None = None
    product_id: str | None = None
    hypothesis_id: str | None = None
    current_role: str = "AXIS_OMNI"
    confidence: float = 0.0
    approvals_required: list[str] = field(default_factory=list)
    risk_flags: list[str] = field(default_factory=list)
    evidence: list[dict[str, Any]] = field(default_factory=list)
    artifacts: list[str] = field(default_factory=list)
    history: list[dict[str, Any]] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def record(self, event: str, **details: Any) -> None:
        self.updated_at = datetime.now(timezone.utc).isoformat()
        self.history.append({"timestamp": self.updated_at, "event": event, "details": details})

    def to_json(self) -> str:
        payload = asdict(self)
        payload["status"] = self.status.value
        return json.dumps(payload, indent=2)
