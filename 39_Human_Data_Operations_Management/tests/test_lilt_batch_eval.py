"""Deterministic QA for fabricated evaluation batch."""
import unittest
from src.lilt_batch_eval import summarize

def item(id="L1", a="A", b="A", gold="A"):
    return {"id": id, "language": "en", "modality": "text",
            "reviewer_a": a, "reviewer_b": b, "gold": gold,
            "minutes": 5, "cost_usd": 1.0}

class LiltSyntheticEvalTests(unittest.TestCase):
    def test_agreement_passes_on_consistent_gold(self):
        result = summarize([item()])
        self.assertEqual(result["decision"], "PASS")
        self.assertEqual(result["metrics"]["paired_agreement"], 1.0)

    def test_disagreement_causes_hold(self):
        result = summarize([item(), item("L2", "A", "B", "A")])
        self.assertEqual(result["decision"], "HOLD")
        self.assertEqual(result["metrics"]["paired_agreement"], .5)

    def test_throughput_and_cost(self):
        result = summarize([item(), item("L2")])
        self.assertEqual(result["throughput_tasks_per_hour"], 12.0)
        self.assertEqual(result["average_cost_usd_per_task"], 1.0)

    def test_duplicate_rejected(self):
        with self.assertRaises(ValueError):
            summarize([item(), item()])

    def test_invalid_label_rejected(self):
        with self.assertRaises(ValueError):
            summarize([item(a="unknown")])

    def test_empty_rejected(self):
        with self.assertRaises(ValueError):
            summarize([])

if __name__ == "__main__":
    unittest.main()
