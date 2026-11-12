"""Tests on synthetic option scores, including security knockout logic."""
import csv
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from score_options import rank_options

class SelectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (HERE / "synthetic_vendor_scores.csv").open(encoding="utf-8", newline="") as f:
            cls.sample = list(csv.DictReader(f))

    def test_security_failure_is_ineligible_despite_high_score(self):
        results = rank_options(self.sample)
        self.assertEqual(results[0]["option"], "Option A")
        self.assertEqual(results[-1]["option"], "Option B")
        self.assertFalse(results[-1]["eligible"])

    def test_all_eligible_options_are_ranked_first(self):
        results = rank_options(self.sample)
        self.assertTrue(all(x["eligible"] for x in results[:-1]))

    def test_bad_score_is_rejected(self):
        bad = dict(self.sample[0], security="8")
        with self.assertRaises(ValueError):
            rank_options([bad])

    def test_missing_name_is_rejected(self):
        with self.assertRaises(ValueError):
            rank_options([dict(self.sample[0], name="")])

if __name__ == "__main__":
    unittest.main()
