"""Stdlib regression tests; run from the case-study directory."""
import importlib.util
from pathlib import Path
import unittest

SOURCE=Path(__file__).resolve().parents[1]/"src"/"lead_triage.py"
spec=importlib.util.spec_from_file_location("lead_triage", SOURCE)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class LeadTriageTest(unittest.TestCase):
    def base(self, **overrides):
        row={"lead_id":"L001","consent_to_contact":"true","language":"en",
             "listing_id":"P100","received_at":"2026-10-01T08:00:00+00:00",
             "response_at":"","booked_viewing":"false"}
        row.update(overrides)
        return row

    def test_no_consent_is_blocked(self):
        result=module.workflow_decision(self.base(consent_to_contact="false"))
        self.assertFalse(result["draft_allowed"])
        self.assertEqual(result["action"],"hold_no_consent")

    def test_unsupported_language_routes_to_human(self):
        self.assertEqual(module.workflow_decision(self.base(language="ur"))["action"],"manual_language_review")

    def test_missing_listing_requires_human(self):
        self.assertFalse(module.workflow_decision(self.base(listing_id=""))["draft_allowed"])

    def test_response_is_not_reopened(self):
        self.assertEqual(module.workflow_decision(self.base(response_at="2026-10-01T08:04:00+00:00"))["action"],"already_answered")

    def test_eligible_waiting_lead_can_be_reviewed(self):
        self.assertEqual(module.workflow_decision(self.base())["action"],"human_review_pending")

    def test_summary_uses_eligible_denominator(self):
        r=module.summarize([self.base(booked_viewing="true"),
                            self.base(lead_id="L002",consent_to_contact="false",booked_viewing="true")])
        self.assertEqual(r["eligible_leads"],1)
        self.assertEqual(r["booked_viewings"],1)
        self.assertEqual(r["booking_rate"],1.0)

if __name__=="__main__":
    unittest.main()
