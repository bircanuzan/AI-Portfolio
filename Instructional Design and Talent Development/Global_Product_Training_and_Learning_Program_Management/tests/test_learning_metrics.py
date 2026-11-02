"""Unit tests for the synthetic programme example. Run from repo project root."""
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from learning_metrics import summarize, read_csv  # noqa: E402

class MetricsTests(unittest.TestCase):
    def test_bundled_synthetic_cohort(self):
        result = summarize(read_csv(ROOT / "data" / "synthetic_learning_results.csv"))
        self.assertEqual(result["assigned"], 12)
        self.assertEqual(result["completed"], 10)
        self.assertEqual(result["completion_pct"], 83.3)
        self.assertEqual(result["assessed"], 10)
        self.assertEqual(result["passed"], 7)
        self.assertEqual(result["pass_pct_of_assessed"], 70.0)
        self.assertEqual(result["critical_errors"], 1)
        self.assertEqual(result["manager_observed"], 6)
        self.assertEqual(result["manager_observation_pct"], 50.0)

    def test_critical_error_blocks_high_score(self):
        row = dict(learner_id="T1", region="GCC", role="partner",
                   assigned="1", completed="1", assessment_score="25",
                   critical_error="1", manager_observed="1")
        self.assertEqual(summarize([row])["passed"], 0)

    def test_reject_score_when_not_complete(self):
        row = dict(learner_id="T1", region="GCC", role="seller",
                   assigned="1", completed="0", assessment_score="22",
                   critical_error="0", manager_observed="0")
        with self.assertRaises(ValueError):
            summarize([row])

    def test_reject_duplicate_id(self):
        row = dict(learner_id="T1", region="GCC", role="seller",
                   assigned="1", completed="1", assessment_score="22",
                   critical_error="0", manager_observed="0")
        with self.assertRaises(ValueError):
            summarize([row, row])

if __name__ == "__main__":
    unittest.main()
