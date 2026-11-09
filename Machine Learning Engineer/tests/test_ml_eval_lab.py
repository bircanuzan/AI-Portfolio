"""Deterministic acceptance and negative tests for the ML reliability lab."""
import unittest
import numpy as np

from src.ml_eval_lab import (
    FEATURES, LEAKY_FEATURE, TARGET,
    chronological_split, corrupt_training_labels,
    evaluate, fit_model, make_synthetic_data, run_experiment, valid_features,
)


class ReliabilityLabTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.frame = make_synthetic_data(600, seed=7)
        cls.train, cls.valid, cls.test = chronological_split(cls.frame)

    def test_deterministic_synthetic_data(self):
        other = make_synthetic_data(600, seed=7)
        self.assertTrue(other.equals(self.frame))

    def test_temporal_order_and_no_overlap(self):
        a, b, c = self.train, self.valid, self.test
        self.assertEqual([len(a), len(b), len(c)], [360, 120, 120])
        self.assertLess(a["event_time"].max(), b["event_time"].min())
        self.assertLess(b["event_time"].max(), c["event_time"].min())
        self.assertEqual(len(set(a.index) | set(b.index) | set(c.index)), 600)

    def test_reject_target_leakage(self):
        with self.assertRaises(ValueError):
            valid_features(FEATURES + (LEAKY_FEATURE,))
        with self.assertRaises(ValueError):
            valid_features(FEATURES + (TARGET,))
        with self.assertRaises(ValueError):
            fit_model("logistic", self.train, FEATURES + (LEAKY_FEATURE,))

    def test_reject_unsorted_time(self):
        reverse = self.frame.iloc[::-1]
        with self.assertRaises(ValueError):
            chronological_split(reverse)

    def test_review_capacity_and_metrics(self):
        model = fit_model("logistic", self.train)
        result = evaluate(model, self.test)
        self.assertEqual(result["reviewed"], 12)
        self.assertGreaterEqual(result["precision_at_capacity"], 0)
        self.assertLessEqual(result["precision_at_capacity"], 1)
        self.assertGreaterEqual(result["brier_score"], 0)

    def test_corrupt_only_copy_of_training_labels(self):
        labels = self.train[TARGET].to_numpy()
        original = labels.copy()
        modified = corrupt_training_labels(labels, 0.10, seed=7)
        self.assertTrue(np.array_equal(labels, original))
        self.assertEqual(np.sum(labels != modified), 36)
        self.assertTrue(np.array_equal(self.valid[TARGET], self.frame.iloc[360:480][TARGET]))

    def test_experiment_is_not_production_claim(self):
        report = run_experiment(rows=600, seed=7)
        self.assertFalse(report["review_outcome"]["production_approved"])
        self.assertEqual(report["source"], "synthetic_only_no_real_client_data")
        self.assertFalse(
            report["stress_tests"]["intentional_target_leakage_INVALID"]["deployment_eligible"]
        )
        self.assertIn(report["selected_on_validation"],
                      ("baseline", "logistic", "gradient_boosting"))


if __name__ == "__main__":
    unittest.main()
