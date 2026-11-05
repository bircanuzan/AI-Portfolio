"""Reproducible deterministic tests, NOT business UAT or model validation."""
import csv
import unittest
from pathlib import Path
from handover_router import route_case, normalize_csv_row, RULE_VERSION

CASES = Path(__file__).resolve().parents[1] / "data" / "synthetic_handover_cases.csv"


class HandoverRoutingTests(unittest.TestCase):
    def test_all_twelve_synthetic_fixtures(self):
        with CASES.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 12)
        for row in rows:
            with self.subTest(case_id=row["case_id"]):
                result = route_case(normalize_csv_row(row))
                self.assertEqual(result["decision"], row["expected_decision"])
                self.assertTrue(result["needs_human"])
                self.assertEqual(result["rule_version"], RULE_VERSION)
                self.assertNotEqual(result["decision"], "HANDOVER_APPROVED")

    def test_unsafe_or_unknown_clearance_never_auto_passes(self):
        case = dict(case_id="T01", unit_id="UNIT-X", customer_ref="CUST-X",
                    has_id_proof=True, has_contract=True, has_payment_clearance_doc=True,
                    payment_cleared="UNKNOWN", project_ready="YES", duplicate_flag=False,
                    mismatch_flag=False)
        result = route_case(case)
        self.assertEqual(result["decision"], "HUMAN_REVIEW")
        self.assertIn("finance_clearance_review", result["reasons"])

    def test_missing_document_precedes_other_checks(self):
        case = dict(case_id="T02", unit_id="UNIT-Y", customer_ref="CUST-Y",
                    has_id_proof=False, has_contract=True, has_payment_clearance_doc=True,
                    payment_cleared="NO", project_ready="YES", duplicate_flag=False,
                    mismatch_flag=False)
        result = route_case(case)
        self.assertEqual(result["decision"], "NEEDS_DOCUMENTS")
        self.assertIn("missing_or_invalid:has_id_proof", result["reasons"])

    def test_empty_identifiers_are_not_accepted(self):
        case = dict(case_id=" ", unit_id="U", customer_ref="C",
                    has_id_proof=True, has_contract=True, has_payment_clearance_doc=True,
                    payment_cleared="YES", project_ready="YES", duplicate_flag=False,
                    mismatch_flag=False)
        self.assertEqual(route_case(case)["decision"], "NEEDS_DOCUMENTS")


if __name__ == "__main__":
    unittest.main()
