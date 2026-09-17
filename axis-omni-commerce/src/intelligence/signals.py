from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import json
from typing import Any

from database.models import AxisOmniDB


class HistoricalSignalStore:
    def __init__(self, db: AxisOmniDB) -> None:
        self.db = db

    def load_json(self, path: str | Path) -> list[dict[str, Any]]:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        signals = payload.get("signals", [])
        now = datetime.now(timezone.utc).isoformat()
        for signal in signals:
            self.db.upsert_signal(
                signal_id=signal["signal_id"],
                source=signal["source"],
                category=signal["category"],
                weight=float(signal["weight"]),
                evidence={"evidence": signal.get("evidence", []), "status": payload.get("status")},
                updated_at=now,
            )
        return signals

    @staticmethod
    def prior_score(product: dict[str, Any], signals: list[dict[str, Any]]) -> float:
        haystack = " ".join(str(product.get(k, "")) for k in ("title", "category", "tags", "description")).lower()
        matched = [float(s["weight"]) for s in signals if str(s["category"]).replace("_", " ").lower() in haystack]
        if not matched:
            return 0.0
        return round(sum(matched) / len(matched), 4)
