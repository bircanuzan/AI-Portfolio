"""Local regression tests with synthetic fixture."""
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from pipeline import assess, run


class IngestionTests(unittest.TestCase):
    def test_sample_counts_and_traceability(self):
        accepted, rejected, quality = assess(ROOT / "data/synthetic_events.csv")
        self.assertEqual(len(accepted), 3)
        self.assertEqual(len(rejected), 3)
        self.assertEqual(quality["processed_rows"], 6)
        self.assertEqual(len(quality["input_sha256"]), 64)

    def test_output_contract(self):
        with tempfile.TemporaryDirectory() as tmp:
            quality = run(ROOT / "data/synthetic_events.csv", tmp)
            self.assertEqual(quality["accepted_rows"], 3)
            self.assertTrue((Path(tmp) / "clean_events.csv").exists())
            self.assertTrue((Path(tmp) / "quarantine.json").exists())
            self.assertTrue((Path(tmp) / "quality_report.json").exists())

    def test_bad_columns_fail_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "wrong.csv"
            source.write_text("id,value\na,1\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                assess(source)

    def test_naive_timestamps_quarantined(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "naive.csv"
            source.write_text(
                "event_id,account_id,occurred_at,event_type,units\n"
                "x1,demo-team,2026-11-01T10:00:00,query,1\n",
                encoding="utf-8")
            accepted, rejected, _ = assess(source)
            self.assertEqual(len(accepted), 0)
            self.assertIn("timezone_required", rejected[0]["reason"])


if __name__ == "__main__":
    unittest.main()
