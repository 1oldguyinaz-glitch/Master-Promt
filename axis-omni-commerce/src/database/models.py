from __future__ import annotations

from pathlib import Path
import json
import sqlite3
from typing import Any


SCHEMA = """
CREATE TABLE IF NOT EXISTS runs (
  run_id TEXT PRIMARY KEY,
  status TEXT NOT NULL,
  stage TEXT NOT NULL,
  objective TEXT NOT NULL,
  payload_json TEXT NOT NULL,
  updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS audit_events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  run_id TEXT NOT NULL,
  event_type TEXT NOT NULL,
  actor TEXT NOT NULL,
  payload_json TEXT NOT NULL,
  created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS suppliers (
  supplier_id TEXT PRIMARY KEY,
  name TEXT,
  authorization_status TEXT,
  payload_json TEXT NOT NULL DEFAULT '{}'
);
CREATE TABLE IF NOT EXISTS products (
  product_id TEXT PRIMARY KEY,
  supplier_id TEXT,
  sku TEXT,
  title TEXT,
  status TEXT,
  payload_json TEXT NOT NULL DEFAULT '{}'
);
CREATE TABLE IF NOT EXISTS signals (
  signal_id TEXT PRIMARY KEY,
  source TEXT NOT NULL,
  category TEXT NOT NULL,
  weight REAL NOT NULL,
  evidence_json TEXT NOT NULL,
  updated_at TEXT NOT NULL
);
"""


class AxisOmniDB:
    def __init__(self, path: str | Path = "axis_omni.db") -> None:
        self.path = str(path)
        self.conn = sqlite3.connect(self.path)
        self.conn.execute("PRAGMA foreign_keys=ON")
        self.conn.executescript(SCHEMA)
        self.conn.commit()

    def save_run(self, state: Any) -> None:
        payload = json.loads(state.to_json())
        self.conn.execute(
            """INSERT INTO runs(run_id,status,stage,objective,payload_json,updated_at)
               VALUES(?,?,?,?,?,?)
               ON CONFLICT(run_id) DO UPDATE SET
                 status=excluded.status, stage=excluded.stage,
                 objective=excluded.objective, payload_json=excluded.payload_json,
                 updated_at=excluded.updated_at""",
            (state.run_id, state.status.value, state.stage, state.objective,
             json.dumps(payload), state.updated_at),
        )
        self.conn.commit()

    def add_audit_event(self, run_id: str, event_type: str, actor: str,
                        payload: dict[str, Any], created_at: str) -> None:
        self.conn.execute(
            "INSERT INTO audit_events(run_id,event_type,actor,payload_json,created_at) VALUES(?,?,?,?,?)",
            (run_id, event_type, actor, json.dumps(payload), created_at),
        )
        self.conn.commit()

    def upsert_signal(self, signal_id: str, source: str, category: str,
                      weight: float, evidence: dict[str, Any], updated_at: str) -> None:
        self.conn.execute(
            """INSERT INTO signals(signal_id,source,category,weight,evidence_json,updated_at)
               VALUES(?,?,?,?,?,?)
               ON CONFLICT(signal_id) DO UPDATE SET source=excluded.source,
               category=excluded.category, weight=excluded.weight,
               evidence_json=excluded.evidence_json, updated_at=excluded.updated_at""",
            (signal_id, source, category, weight, json.dumps(evidence), updated_at),
        )
        self.conn.commit()
