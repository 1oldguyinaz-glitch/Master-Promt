import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from gmail_transport import GmailHandoff, parse_internal_message, to_runtime_payload


class GmailTransportTests(unittest.TestCase):
    def test_internal_round_trip(self):
        h = GmailHandoff("HF-LIVE-001", "WF-LIVE-001", "STAN", "VERITY", "validate_test_handoff", "idem-live-001")
        parsed = parse_internal_message(h.subject(), h.body())
        self.assertEqual(parsed, h)
        payload = to_runtime_payload(parsed)
        self.assertTrue(payload["axis_internal"])
        self.assertEqual(payload["to_agent"], "VERITY")

    def test_customer_email_is_not_internal(self):
        self.assertIsNone(parse_internal_message("Website question", "Hi, can you help with my website?"))

    def test_marker_required(self):
        body = "Handoff-ID: x\nWorkflow-ID: y\nFrom-Agent: STAN\nTo-Agent: VERITY\nRequested-Action: test\nIdempotency-Key: z\n"
        self.assertIsNone(parse_internal_message("[AXIS-HANDOFF] y STAN->VERITY", body))


if __name__ == "__main__":
    unittest.main()
