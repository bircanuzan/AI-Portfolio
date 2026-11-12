import copy
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from report_ops import load_events, report

class OperationsReportingTests(unittest.TestCase):
    def test_synthetic_metrics(self):
        x = report(load_events())
        self.assertEqual(x["cases"], 18)
        self.assertEqual(x["needs_review"], 4)
        self.assertEqual(x["accepted"], 14)
        self.assertEqual(x["days_covered"], 6)
        self.assertAlmostEqual(x["rework_rate"], 4/18, places=4)

    def test_invalid_status(self):
        data = copy.deepcopy(load_events())
        data[0]["status"] = "unknown"
        with self.assertRaises(ValueError):
            report(data)

    def test_empty_events(self):
        with self.assertRaises(ValueError): report([])

if __name__ == "__main__":
    unittest.main()
