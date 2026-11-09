"""Safety and behavior regression tests; uses only synthetic fixtures."""
import unittest
from src.mobility_pipeline import MobilityPipeline, checker, maker, validate


def event(**updates):
    base = {
        "event_id": "evt-test-1", "case_id": "MOB-T1",
        "tenant_id": "fake-tenant", "category": "case_routing",
        "jurisdiction": "AE", "source": "test",
        "contains_sensitive_data": False
    }
    base.update(updates)
    return base


class MobilityTests(unittest.TestCase):
    def setUp(self):
        self.pipeline = MobilityPipeline()

    def test_low_risk_routes_without_employment_mutation(self):
        d = self.pipeline.process(event())
        self.assertEqual(d.proposed_action, "route_to_team")
        self.assertEqual(d.disposition, "internal_routing_only")
        self.assertTrue(d.checker_passed)

    def test_payroll_requires_human_signoff(self):
        d = self.pipeline.process(event(category="payroll_mismatch"))
        self.assertEqual(d.disposition, "human_approval_required")
        self.assertEqual(d.proposed_action, "create_discrepancy_ticket")

    def test_immigration_requires_human_signoff(self):
        d = self.pipeline.process(event(category="immigration_document"))
        self.assertEqual(d.disposition, "human_approval_required")

    def test_identity_requires_human_review(self):
        d = self.pipeline.process(event(category="identity_change"))
        self.assertEqual(d.disposition, "human_approval_required")

    def test_sensitive_data_is_quarantined(self):
        d = self.pipeline.process(event(contains_sensitive_data=True))
        self.assertFalse(d.checker_passed)
        self.assertEqual(d.reason_code, "sensitive_data_quarantine")

    def test_unknown_jurisdiction_fails_closed(self):
        d = self.pipeline.process(event(jurisdiction="ZZ"))
        self.assertEqual(d.disposition, "manual_escalation")

    def test_unknown_category_fails_closed(self):
        d = self.pipeline.process(event(category="arbitrary"))
        self.assertEqual(d.disposition, "manual_escalation")

    def test_policy_draft_must_be_grounded(self):
        no_citation = self.pipeline.process(event(category="policy_question"))
        self.assertEqual(no_citation.reason_code, "missing_approved_policy_evidence")
        approved = MobilityPipeline().process(
            event(category="policy_question", approved_policy_id="POLICY-GEN-001"))
        self.assertEqual(approved.disposition, "draft_only")

    def test_maker_checker_disagreement_fails_closed(self):
        passed, status, reason = checker(event(category="payroll_mismatch"), "post_payroll")
        self.assertFalse(passed)
        self.assertEqual(status, "manual_escalation")
        self.assertEqual(reason, "maker_checker_disagreement")

    def test_event_deduplication(self):
        e = event()
        self.pipeline.process(e)
        second = self.pipeline.process(e)
        self.assertEqual(second.disposition, "duplicate_event")
        self.assertEqual(len(self.pipeline.audit), 1)

    def test_same_id_different_tenant_is_distinct(self):
        self.pipeline.process(event())
        second = self.pipeline.process(event(tenant_id="other-fake-tenant"))
        self.assertNotEqual(second.disposition, "duplicate_event")

    def test_reject_unapproved_pii_fields(self):
        with self.assertRaisesRegex(ValueError, "unapproved_fields_present"):
            validate(event(email="should-not-log@example.com"))

    def test_boolean_validation(self):
        with self.assertRaisesRegex(ValueError, "invalid_sensitivity_flag"):
            validate(event(contains_sensitive_data="false"))

    def test_logs_have_no_raw_payload_or_personal_fields(self):
        self.pipeline.process(event())
        audit = str(self.pipeline.audit).lower()
        for token in ["email", "passport", "salary", "full_name", "document_url"]:
            self.assertNotIn(token, audit)
        self.assertNotIn("fake-tenant", audit)


if __name__ == "__main__":
    unittest.main()
