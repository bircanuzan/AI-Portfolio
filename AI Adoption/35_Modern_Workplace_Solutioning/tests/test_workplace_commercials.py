import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/"src"))
from workplace_commercials import load_rates, estimate

class WorkplaceCommercialTests(unittest.TestCase):
    def test_service_catalogue(self):
        rows = load_rates()
        self.assertEqual(len(rows), 7)
        self.assertEqual(sum(r["base_monthly_aed_per_user"] for r in rows), 157)

    def test_synthetic_baseline(self):
        x = estimate(4500, [157])
        self.assertEqual(x["monthly_per_user_aed"], 157)
        self.assertEqual(x["annual_recurring_aed"], 9078000)
        self.assertEqual(x["transition_with_contingency_aed"], 1980000)
        self.assertEqual(x["total_term_cost_aed"], 29214000)

    def test_sensitivity(self):
        a = estimate(4500, [157])["total_term_cost_aed"]
        b = estimate(5400, [157])["total_term_cost_aed"]
        self.assertGreater(b, a)

    def test_invalid_users(self):
        with self.assertRaises(ValueError): estimate(-10, [25])
        with self.assertRaises(ValueError): estimate(4500.5, [25])

    def test_no_negative_rates(self):
        with self.assertRaises(ValueError): estimate(4500, [-2])
    def test_invalid_contingency(self):
        with self.assertRaises(ValueError): estimate(4500, [25], contingency_rate=2)

if __name__ == "__main__":
    unittest.main()
