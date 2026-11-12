import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from retail_roi import roi
class RetailROITests(unittest.TestCase):
    def test_baseline_hours(self):
        self.assertAlmostEqual(roi()["hours_released_month"],166.67,places=2)
    def test_zero_volume(self):
        self.assertIsNone(roi(monthly_returns=0)["simple_payback_months"])
    def test_bad_data(self):
        with self.assertRaises(ValueError):roi(to_be_min=30)
if __name__=="__main__":unittest.main()
