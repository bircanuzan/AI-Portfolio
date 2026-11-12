"""Unit tests for the deterministic *synthetic* governance policy checker."""
import json
import unittest
from pathlib import Path
from governance_gate import assess, assess_all


class GovernanceGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = json.loads(
            (Path(__file__).parent / "synthetic_gate_cases.json").read_text(encoding="utf-8")
        )
        cls.by_id = {c["case_id"]: c for c in cls.cases}

    def test_expected_synthetic_decisions(self):
        expected = {
            "SC-001": "HOLD",
            "SC-002": "HOLD",
            "SC-003": "NO_GO",
            "SC-004": "GO",
            "SC-005": "HOLD",
            "SC-006": "GO",
            "SC-007": "NO_GO",
            "SC-008": "GO",
            "SC-009": "HOLD",
            "SC-010": "NO_GO",
        }
        actual = {v["case_id"]: v["decision"] for v in assess_all(self.cases)}
        self.assertEqual(actual, expected)

    def test_fail_closed_when_evidence_missing(self):
        case = dict(self.by_id["SC-004"])
        case.pop("evidence_verified")
        result = assess(case)
        self.assertEqual(result["decision"], "HOLD")
        self.assertIn("verified evidence", result["reasons"][0])

    def test_prohibited_automation_is_no_go_even_when_all_flags_pass(self):
        case = dict(self.by_id["SC-008"])
        case["autonomous_adverse_decision"] = True
        self.assertEqual(assess(case)["decision"], "NO_GO")

    def test_missing_owner_is_no_go(self):
        case = dict(self.by_id["SC-006"])
        case["owner"] = ""
        self.assertEqual(assess(case)["decision"], "NO_GO")

    def test_material_change_requires_revalidation(self):
        case = dict(self.by_id["SC-004"])
        case["material_change"] = True
        self.assertEqual(assess(case)["decision"], "HOLD")
        case["change_revalidated"] = True
        self.assertEqual(assess(case)["decision"], "GO")

    def test_unsupported_tier_is_no_go(self):
        case = dict(self.by_id["SC-006"])
        case["tier"] = "unknown"
        self.assertEqual(assess(case)["decision"], "NO_GO")

    def test_unauthorized_sensitive_export_is_no_go(self):
        case = dict(self.by_id["SC-004"])
        case["unapproved_sensitive_export"] = True
        self.assertEqual(assess(case)["decision"], "NO_GO")


if __name__ == "__main__":
    unittest.main()
