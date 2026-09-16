import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from owner_escalation import OwnerEscalation, OWNER_EMAIL, should_escalate

class OwnerEscalationTests(unittest.TestCase):
    def test_unresolved_blocker_triggers_owner(self):
        self.assertTrue(should_escalate("owner_decision_required", False))

    def test_internal_answer_prevents_unnecessary_email(self):
        self.assertFalse(should_escalate("owner_decision_required", True))

    def test_duplicate_pending_question_is_suppressed(self):
        self.assertFalse(should_escalate("missing_required_information", False, True))

    def test_message_targets_owner_and_preserves_workflow(self):
        e = OwnerEscalation("WF-OWNER-001", "HF-OWNER-001", "AXIS_OMNI", "owner_decision_required", "Which option should AXIS execute?", "Two safe options remain and owner preference is required.")
        e.validate()
        self.assertEqual(OWNER_EMAIL, "bdennis36@outlook.com")
        self.assertIn("WF-OWNER-001", e.subject())
        self.assertIn("Reply directly", e.body())

if __name__ == "__main__":
    unittest.main()
