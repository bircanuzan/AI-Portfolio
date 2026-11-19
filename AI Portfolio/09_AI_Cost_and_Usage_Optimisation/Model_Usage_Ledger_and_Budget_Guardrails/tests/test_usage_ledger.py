"""Regression tests for hypothetical model-cost calculations."""
import json
import sys
import tempfile
import unittest
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from usage_ledger import estimate, run


class LedgerTests(unittest.TestCase):
    def test_synthetic_ledger_and_budget_exception(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = run(ROOT / "data/fictional_usage.csv",
                         ROOT / "data/fictional_budgets.json",
                         Path(tmp) / "report.json")
            by_dept = {d["department"]: d for d in report["department_summary"]}
            self.assertEqual(len(by_dept), 3)
            self.assertTrue(by_dept["HR"]["over_example_budget"])
            self.assertFalse(by_dept["Support"]["over_example_budget"])
            self.assertGreater(Decimal(by_dept["HR"]["spend_per_success_usd"]), 0)
            self.assertEqual(report["evidence_type"], "synthetic_illustrative_not_actual")

    def test_reject_more_successes_than_requests(self):
        row = self.example()
        row["successful_requests"] = "9"
        with self.assertRaises(ValueError):
            estimate([row], {"Test": "10"})

    def test_zero_success_has_no_cost_per_success(self):
        row = self.example()
        row["successful_requests"] = "0"
        report = estimate([row], {"Test": "10"})
        self.assertIsNone(report["department_summary"][0]["spend_per_success_usd"])

    def test_reject_negative_price(self):
        row = self.example()
        row["input_usd_per_million"] = "-0.10"
        with self.assertRaises(ValueError):
            estimate([row], {"Test": "10"})

    @staticmethod
    def example():
        return {"department": "Test", "model_tier": "example",
                "requests": "3", "successful_requests": "2",
                "avg_input_tokens": "100", "avg_output_tokens": "100",
                "input_usd_per_million": "1", "output_usd_per_million": "2"}


if __name__ == "__main__":
    unittest.main()
