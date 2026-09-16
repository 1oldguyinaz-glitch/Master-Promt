import unittest
from datetime import datetime, timedelta, timezone
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from runtime import Event, MAX_HOPS, build_default_runtime


class RuntimeTests(unittest.TestCase):
    def test_axis_to_verity_handoff_executes(self):
        rt = build_default_runtime()
        event = Event(
            workflow_id="WF-TEST-1",
            event_type="agent_handoff",
            payload={"from_agent": "AXIS_OMNI", "to_agent": "VERITY", "requested_action": "validate_contactability"},
            idempotency_key="idem-1",
        )
        receipt = rt.ingest(event)
        self.assertEqual(receipt.status, "executed")
        self.assertEqual(receipt.agent, "VERITY")
        self.assertEqual(rt.state["WF-TEST-1"]["last_agent"], "VERITY")

    def test_duplicate_is_suppressed(self):
        rt = build_default_runtime()
        e1 = Event("WF-2", "agent_handoff", idempotency_key="same")
        e2 = Event("WF-2", "agent_handoff", idempotency_key="same")
        rt.ingest(e1)
        self.assertEqual(rt.ingest(e2).status, "duplicate_suppressed")

    def test_max_hops_blocks_loop(self):
        rt = build_default_runtime()
        event = Event("WF-3", "agent_handoff", hop_count=MAX_HOPS + 1)
        self.assertEqual(rt.ingest(event).status, "blocked_max_hops")

    def test_expired_handoff_is_blocked(self):
        rt = build_default_runtime()
        expired = (datetime.now(timezone.utc) - timedelta(minutes=1)).isoformat()
        event = Event("WF-4", "agent_handoff", expires_at=expired)
        self.assertEqual(rt.ingest(event).status, "blocked_expired")

    def test_unknown_event_does_not_execute(self):
        rt = build_default_runtime()
        event = Event("WF-5", "unknown_event")
        self.assertEqual(rt.ingest(event).status, "unroutable")


if __name__ == "__main__":
    unittest.main()
