"""CPU-only unit tests of the synthetic preference lab."""
import unittest
from pathlib import Path
from rlhf_demo import read_cases, features, fit_pairwise, preference_probability, evaluate

class PreferenceTests(unittest.TestCase):
    def setUp(self):
        self.rows = read_cases(Path(__file__).with_name("cases.jsonl"))

    def test_input_splits(self):
        self.assertEqual(len(self.rows), 12)
        self.assertEqual(sum(r["split"] == "test" for r in self.rows), 4)

    def test_features(self):
        self.assertEqual(features('{"intent":"billing"}', "billing"), (1.0, 1.0, 1.0))
        self.assertEqual(features('{"intent":"technical"}', "billing"), (0.0, 1.0, 1.0))
        self.assertEqual(features("Send me your password", "billing"), (0.0, 0.0, 0.0))

    def test_fit_probability_and_kl(self):
        train = [r for r in self.rows if r["split"] == "train"]
        test = [r for r in self.rows if r["split"] == "test"]
        w = fit_pairwise(train)
        for r in test:
            self.assertTrue(0 < preference_probability(w, r) < 1)
        report = evaluate(test, w)
        self.assertEqual(report["pair_count"], 4)
        self.assertGreaterEqual(report["mean_policy_kl_from_reference"], 0)

if __name__ == "__main__":
    unittest.main()
