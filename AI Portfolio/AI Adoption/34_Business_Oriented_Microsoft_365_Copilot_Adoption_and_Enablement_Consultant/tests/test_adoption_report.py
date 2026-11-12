import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from adoption_report import load, report

class AdoptionReportTests(unittest.TestCase):
    def test_data_and_week_four(self):
        rows = load()
        self.assertEqual(len(rows), 12)
        x = report(rows, 4)
        self.assertEqual(x["licensed"], 180)
        self.assertEqual(x["active"], 126)
        self.assertEqual(x["reviewed_outputs"], 135)
        self.assertAlmostEqual(x["adoption_rate"], 0.7)
        self.assertAlmostEqual(x["quality_pass_rate"], 118 / 135, places=4)

    def test_growth_is_hypothetical(self):
        rows = load()
        self.assertLess(report(rows, 1)["adoption_rate"], report(rows, 4)["adoption_rate"])
        self.assertIn("Fictional", report(rows, 4)["limitation"])

    def test_bad_active_count(self):
        rows = load()
        rows[0]["active_users"] = 999
        with self.assertRaises(ValueError):
            report(rows, 1)

    def test_no_period(self):
        with self.assertRaises(ValueError):
            report(load(), 99)

if __name__ == "__main__":
    unittest.main()
