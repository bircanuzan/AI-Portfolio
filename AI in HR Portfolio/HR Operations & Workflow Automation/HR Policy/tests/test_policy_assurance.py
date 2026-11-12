"""Standard-library unit tests for the independent synthetic HR Policy case."""
import copy
from datetime import date
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from policy_assurance import assess_policy, finance_case, run  # noqa: E402


class PolicyAssuranceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (ROOT / "data" / "synthetic_policy_register.json").open(encoding="utf-8") as f:
            cls.data = json.load(f)
        cls.as_of = date(2026, 11, 5)

    def record(self, i=0):
        return copy.deepcopy(self.data["policies"][i])

    def test_approved_fixture_passes_simulated_document_gates(self):
        self.assertEqual(assess_policy(self.record(0), self.as_of), [])

    def test_draft_is_blocked(self):
        self.assertIn("NOT_APPROVED_STATUS", assess_policy(self.record(1), self.as_of))

    def test_missing_local_addendum_is_blocked(self):
        r = self.record()
        r["local_addendum_attached"] = False
        self.assertIn("MISSING_COUNTRY_ADDENDUM", assess_policy(r, self.as_of))

    def test_missing_legal_reviewer_is_blocked(self):
        r = self.record()
        r["legal_approval"]["reviewer"] = None
        self.assertIn("MISSING_SIMULATED_COUNTRY_LEGAL_SIGNOFF", assess_policy(r, self.as_of))

    def test_missing_payroll_signoff_for_pay_change(self):
        self.assertIn("PAYROLL_CONTROL_NOT_APPROVED", assess_policy(self.record(2), self.as_of))

    def test_hris_configuration_is_a_required_gate(self):
        r = self.record()
        r["hris_approved"] = False
        self.assertIn("HRIS_UAT_NOT_APPROVED", assess_policy(r, self.as_of))

    def test_review_overdue_is_flagged(self):
        r = self.record()
        r["next_review"] = "2026-10-01"
        self.assertIn("REVIEW_OVERDUE", assess_policy(r, self.as_of))

    def test_invalid_version_and_date_are_flagged(self):
        r = self.record()
        r["version"] = "final"
        r["effective_date"] = "tomorrow"
        blockers = assess_policy(r, self.as_of)
        self.assertIn("INVALID_VERSION", blockers)
        self.assertIn("INVALID_EFFECTIVE_DATE", blockers)

    def test_future_dated_legal_signoff_is_blocked(self):
        r = self.record()
        r["legal_approval"]["approved_on"] = "2027-01-01"
        self.assertIn("LEGAL_APPROVAL_FUTURE_DATED", assess_policy(r, self.as_of))

    def test_financial_case_is_reproducible(self):
        result = finance_case(self.data["financial_scenario"])
        self.assertEqual(result["recurring_annual_value_aed"], "48000.00")
        self.assertEqual(result["year_one_net_aed"], "-17000.00")
        self.assertEqual(result["simple_payback_months"], "16.25")

    def test_no_positive_benefit_has_no_payback(self):
        inputs = copy.deepcopy(self.data["financial_scenario"])
        inputs["hours_after"] = inputs["hours_before"]
        inputs["corrections_after"] = inputs["corrections_before"]
        self.assertIsNone(finance_case(inputs)["simple_payback_months"])

    def test_run_reports_three_records_and_holds(self):
        result = run(self.data, self.as_of)
        self.assertEqual(result["policies_checked"], 3)
        self.assertEqual(
            [x["document_control_readiness"] for x in result["document_control_results"]],
            ["PASS_SYNTHETIC", "HOLD", "HOLD"],
        )


if __name__ == "__main__":
    unittest.main()
