import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from adoption import load_accounts, summarize, divide

class AdoptionAnalyticsTests(unittest.TestCase):
    def test_synthetic_totals(self):
        data = load_accounts(ROOT / "synthetic_data/accounts.csv")
        report = summarize(data)
        self.assertEqual(report["accounts_onboarded"], 6)
        self.assertEqual(report["accounts_activated"], 4)
        self.assertEqual(report["conversations"], 720)
        self.assertAlmostEqual(report["activation_rate"], 4/6)
        self.assertAlmostEqual(report["success_rate"], 473/720)

    def test_zero_denominator(self):
        self.assertEqual(divide(0, 0), 0.0)

    def test_failed_and_unknown_separate(self):
        report = summarize(load_accounts(ROOT / "synthetic_data/accounts.csv"))
        self.assertAlmostEqual(report["failure_rate"] + report["unknown_rate"] + report["success_rate"], 1.0)

    def test_at_risk(self):
        report = summarize(load_accounts(ROOT / "synthetic_data/accounts.csv"))
        self.assertIn("Fictional Training", report["at_risk_accounts"])
        self.assertIn("Fictional Logistics", report["at_risk_accounts"])

if __name__ == "__main__":
    unittest.main()
