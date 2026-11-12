import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from value_model import calculate, run

def row(**updates):
    x = dict(task="Synthetic", monthly_volume="600", minutes_per_task="20",
             assistable_share="0.5", minutes_saved_per_assisted_task="10",
             review_minutes_per_assisted_task="2", loaded_hourly_cost_aed="60",
             monthly_platform_cost_aed="100")
    x.update(updates)
    return x

class EconomicsTests(unittest.TestCase):
    def test_released_time(self):
        self.assertEqual(calculate(row())["modeled_net_hours_released_per_month"], 40)
    def test_review_matters(self):
        self.assertGreater(calculate(row(review_minutes_per_assisted_task="2"))["modeled_net_hours_released_per_month"],
                           calculate(row(review_minutes_per_assisted_task="6"))["modeled_net_hours_released_per_month"])
    def test_more_review_can_create_negative_value(self):
        self.assertLess(calculate(row(review_minutes_per_assisted_task="15"))["modeled_net_opportunity_aed_per_month"], 0)
    def test_zero_eligible(self):
        self.assertEqual(calculate(row(assistable_share="0"))["modeled_net_hours_released_per_month"], 0)
    def test_no_fake_cash_savings_or_roi(self):
        x = calculate(row())
        self.assertEqual(x["verified_cash_savings_aed"], 0)
        self.assertFalse(x["actual_roi_verified"])
    def test_invalid_share(self):
        with self.assertRaises(ValueError):
            calculate(row(assistable_share="1.2"))
    def test_impossible_saved_minutes(self):
        with self.assertRaises(ValueError):
            calculate(row(minutes_saved_per_assisted_task="30"))
    def test_negative_cost(self):
        with self.assertRaises(ValueError):
            calculate(row(monthly_platform_cost_aed="-1"))
    def test_dataset(self):
        self.assertEqual(len(run()), 4)

if __name__ == "__main__":
    unittest.main()