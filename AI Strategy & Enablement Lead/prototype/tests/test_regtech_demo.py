"""Execute with: python -m unittest discover -s tests -v"""
import unittest
from datetime import date
from regtech_demo import evaluate_case


GOOD = {
    "case_id": "SYN-001",
    "declared": {
        "legal_name": "Example Crescent LLC",
        "registry_number": "REG-0001",
        "jurisdiction": "AE",
        "beneficial_owners": [
            {"name": "Synthetic Owner A", "ownership_pct": 60},
            {"name": "Synthetic Owner B", "ownership_pct": 40}
        ]
    },
    "mock_extracted_document": {
        "legal_name": "Example Crescent LLC",
        "registry_number": "REG-0001",
        "jurisdiction": "AE",
        "expiry_date": "2028-01-01"
    }
}


class KYBTests(unittest.TestCase):
    def test_clean_case_still_needs_human(self):
        result = evaluate_case(GOOD, date(2026, 11, 4))
        self.assertEqual(result["flags"], [])
        self.assertEqual(result["status"], "standard_human_review")
        self.assertTrue(result["human_decision_required"])

    def test_registry_mismatch_is_flagged(self):
        case = {**GOOD, "mock_extracted_document": {
            **GOOD["mock_extracted_document"], "registry_number": "REG-WRONG"
        }}
        self.assertIn("mismatch_registry_number", evaluate_case(case)["flags"])

    def test_expired_evidence_is_flagged(self):
        case = {**GOOD, "mock_extracted_document": {
            **GOOD["mock_extracted_document"], "expiry_date": "2020-01-01"
        }}
        self.assertIn("expired_document", evaluate_case(case)["flags"])

    def test_inconsistent_ownership_is_flagged(self):
        case = {**GOOD, "declared": {**GOOD["declared"], "beneficial_owners": [
            {"name": "A", "ownership_pct": 50}, {"name": "B", "ownership_pct": 30}
        ]}}
        self.assertIn("ownership_total_not_100", evaluate_case(case)["flags"])

    def test_missing_document_field_and_invalid_date(self):
        case = {**GOOD, "mock_extracted_document": {
            "legal_name": "Example Crescent LLC", "jurisdiction": "AE",
            "expiry_date": "not-a-date"
        }}
        result = evaluate_case(case)
        self.assertIn("missing_document_registry_number", result["flags"])
        self.assertIn("invalid_expiry_date", result["flags"])
        self.assertEqual(result["status"], "priority_human_review")

    def test_evidence_hash_is_deterministic(self):
        self.assertEqual(evaluate_case(GOOD)["evidence_sha256"], evaluate_case(GOOD)["evidence_sha256"])


if __name__ == "__main__":
    unittest.main()
