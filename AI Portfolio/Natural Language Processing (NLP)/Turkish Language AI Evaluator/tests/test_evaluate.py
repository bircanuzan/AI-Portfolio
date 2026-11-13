import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from evaluate import summarize, validate

def sample(issues=None):
    return {
        "item_id":"T1", "language":"tr", "prompt":"Türkçe cevap ver.",
        "ai_output":"Merhaba.", "reference_evidence":"Instruction only",
        "visual_reference": None,
        "annotations":[{
            "rater":"A",
            "scores": {"alignment":3,"coherence":3,"groundedness":3,"fluency":3,"cultural_tone":3},
            "issue_codes": issues or [],
            "severity":"low",
            "feedback":"İfade uygun ve anlaşılır."
        }]
    }

class EvaluationTests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate([sample()]), [])
    def test_aggregates(self):
        result = summarize([sample(["message_drift"])])
        self.assertEqual(result["issue_counts"]["message_drift"], 1)
        self.assertEqual(result["mean_dimension_scores_0_to_3"]["alignment"], 3)
    def test_out_of_range(self):
        row=sample()
        row["annotations"][0]["scores"]["fluency"] = 4
        self.assertEqual(summarize([row])["status"], "INVALID_INPUT")
    def test_missing_visual_reference(self):
        self.assertTrue(validate([sample(["visual_attribute_mismatch"])]))
    def test_critical_escalation(self):
        row=sample()
        row["annotations"][0]["severity"]="critical"
        self.assertEqual(summarize([row])["adjudication_item_ids"], ["T1"])
    def test_disagreement_escalation(self):
        row=sample()
        other=dict(row["annotations"][0])
        other["rater"]="B"
        other["scores"]={**other["scores"],"alignment":1}
        row["annotations"].append(other)
        self.assertEqual(summarize([row])["adjudication_item_ids"], ["T1"])
    def test_duplicate_id(self):
        self.assertTrue(validate([sample(),sample()]))

if __name__ == "__main__":
    unittest.main()
