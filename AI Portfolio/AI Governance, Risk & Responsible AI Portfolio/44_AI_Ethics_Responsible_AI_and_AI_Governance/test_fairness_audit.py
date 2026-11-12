"""Reproducibility tests for invented model-output labels; no trained model."""
from pathlib import Path
import unittest
from fairness_audit import read_rows, audit_rows

class FairnessLabTests(unittest.TestCase):
    def test_synthetic_metrics(self):
        path = Path(__file__).parent / "synthetic_fairness_cases.csv"
        metrics = audit_rows(read_rows(path))
        self.assertEqual(metrics["A"]["n"], 10)
        self.assertEqual(metrics["B"]["n"], 10)
        self.assertEqual(metrics["A"]["selected"], 7)
        self.assertEqual(metrics["B"]["selected"], 4)
        self.assertEqual(metrics["A"]["qualified"], 7)
        self.assertEqual(metrics["B"]["qualified"], 7)
        self.assertAlmostEqual(metrics["A"]["selection_rate"], 0.7)
        self.assertAlmostEqual(metrics["B"]["selection_rate"], 0.4)
        self.assertAlmostEqual(metrics["A"]["true_positive_rate"], 6/7)
        self.assertAlmostEqual(metrics["B"]["true_positive_rate"], 4/7)
        self.assertEqual(metrics["B"]["false_rejected_qualified"], 3)

if __name__ == "__main__":
    unittest.main()
