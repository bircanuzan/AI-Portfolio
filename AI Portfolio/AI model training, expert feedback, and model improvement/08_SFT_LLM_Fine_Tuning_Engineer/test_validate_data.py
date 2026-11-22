"""CPU-only tests; run: python -m unittest -v test_validate_data.py"""
import json
import tempfile
import unittest
from pathlib import Path

from evaluate_model import score
from validate_data import audit, read_rows


class SFTDataTests(unittest.TestCase):
    def test_real_synthetic_splits_have_no_exact_leakage(self):
        counts = audit(Path(__file__).parent / "data")
        self.assertEqual(counts, {"train": 18, "validation": 6, "test": 6})

    def test_schema_and_intent_are_distinct_metrics(self):
        self.assertEqual(score('{"intent":"billing"}', "billing"), (True, True))
        self.assertEqual(score('{"intent":"billing"}', "technical"), (True, False))
        self.assertEqual(score('{"intent":"billing","note":"extra"}', "billing"), (False, False))
        self.assertEqual(score("not JSON", "billing"), (False, False))

    def test_invalid_label_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "one.jsonl"
            path.write_text(json.dumps({"id": "1", "message": "example", "intent": "other"}) + "\n")
            with self.assertRaises(ValueError):
                read_rows(path)


if __name__ == "__main__":
    unittest.main()
