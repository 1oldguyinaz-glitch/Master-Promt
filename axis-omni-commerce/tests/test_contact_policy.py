import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from contact_policy import evaluate_outbound, read_suppressions


class ContactPolicyTests(unittest.TestCase):
    def setUp(self):
        self.lead = {
            "business_id": "axis-company-001",
            "identity_links_verified": True,
            "identities": {
                "email": ["office@example-plumbing.test"],
                "domain": ["example-plumbing.test"],
                "phone": ["+1 253 555 0136"],
                "facebook": ["123456789"],
                "linkedin": ["https://www.linkedin.com/company/example-plumbing/"],
            },
        }
        self.ready = {"owner_approved": True, "provider_permission_verified": True}

    def test_opt_out_email_blocks_other_channels_on_same_verified_business(self):
        dnc = [{"suppression_id": "dnc-1", "scope": "email",
                "value": "office@example-plumbing.test", "reason": "OPT_OUT_STOP",
                "status": "ACTIVE_NO_CONTACT"}]
        for ch in ("email", "sms", "facebook", "linkedin"):
            with self.subTest(ch=ch):
                result = evaluate_outbound(self.lead, ch, dnc, **self.ready)
                self.assertFalse(result.permitted_for_provider_review)
                self.assertEqual(result.reason, "business_or_contact_dnc")

    def test_domain_opt_out_blocks_linked_phone(self):
        dnc = [{"suppression_id": "dnc-domain", "scope": "domain",
                "value": "example-plumbing.test", "reason": "OPT_OUT_NOT_INTERESTED",
                "status": "ACTIVE_NO_CONTACT"}]
        self.assertEqual(evaluate_outbound(self.lead, "sms", dnc, **self.ready).suppression_id, "dnc-domain")

    def test_hard_bounce_only_restricts_email(self):
        rows = [{"suppression_id": "bounce-1", "scope": "email",
                 "value": "office@example-plumbing.test", "reason": "HARD_BOUNCE",
                 "status": "ACTIVE_NO_RETRY"}]
        self.assertFalse(evaluate_outbound(self.lead, "email", rows, **self.ready).permitted_for_provider_review)
        self.assertTrue(evaluate_outbound(self.lead, "sms", rows, **self.ready).permitted_for_provider_review)

    def test_matching_business_name_alone_does_not_create_link(self):
        lead = {"business_id": "axis-company-002", "business_name": "Example Plumbing",
                "identity_links_verified": True, "identities": {"email": ["other@another.test"]}}
        rows = [{"suppression_id": "dnc-other", "scope": "email",
                 "value": "office@example-plumbing.test", "business_name": "Example Plumbing",
                 "reason": "OPT_OUT_STOP", "status": "ACTIVE_NO_CONTACT"}]
        self.assertTrue(evaluate_outbound(lead, "email", rows, **self.ready).permitted_for_provider_review)

    def test_unverified_merge_fails_closed(self):
        lead = {**self.lead, "identity_links_verified": False}
        result = evaluate_outbound(lead, "sms", [], **self.ready)
        self.assertFalse(result.permitted_for_provider_review)
        self.assertEqual(result.reason, "unverified_business_identity")

    def test_social_channel_without_verified_account_fails(self):
        self.assertEqual(evaluate_outbound(self.lead, "instagram", [], **self.ready).reason,
                         "channel_identity_missing")

    def test_no_unapproved_outbound(self):
        result = evaluate_outbound(self.lead, "email", [], provider_permission_verified=True)
        self.assertFalse(result.permitted_for_provider_review)
        self.assertEqual(result.reason, "owner_approval_required")

    def test_no_unverified_provider_permission(self):
        result = evaluate_outbound(self.lead, "sms", [], owner_approved=True)
        self.assertFalse(result.permitted_for_provider_review)
        self.assertEqual(result.reason, "provider_permission_unverified")

    def test_existing_csv_remains_compatible(self):
        path = Path(__file__).resolve().parents[1] / "outreach" / "suppressions.csv"
        if path.exists():
            rows = read_suppressions(path)
            self.assertTrue(rows)
            self.assertIn("scope", rows[0])


if __name__ == "__main__":
    unittest.main()
