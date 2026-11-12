import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from compare_models import load_options, score_option

def sample(**extra):
    row = dict(option="Test", handoffs="3", accountability_gaps="0",
               unmitigated_high_risks="0", learning_pathways="1",
               coordination_cost_index="4")
    row.update(extra)
    return row

class OrgDesignTest(unittest.TestCase):
    def test_valid_discussion(self):
        self.assertEqual(score_option(sample())["status"], "DISCUSS")
    def test_missing_accountability_blocks(self):
        self.assertEqual(score_option(sample(accountability_gaps="1"))["status"], "HOLD")
    def test_risk_blocks(self):
        self.assertEqual(score_option(sample(unmitigated_high_risks="1"))["status"], "HOLD")
    def test_apprenticeship_is_required(self):
        self.assertEqual(score_option(sample(learning_pathways="0"))["status"], "HOLD_NO_LEARNING")
    def test_negative_invalid(self):
        with self.assertRaises(ValueError):
            score_option(sample(handoffs="-1"))
    def test_schema_invalid(self):
        with self.assertRaises(ValueError):
            score_option({"option": "Test"})
    def test_sample_file_has_three_models(self):
        self.assertEqual(len(load_options()), 3)

if __name__ == "__main__":
    unittest.main()