import unittest
import importlib.util
from pathlib import Path
path=Path(__file__).resolve().parents[1]/"src"/"evaluation_pipeline.py"
spec=importlib.util.spec_from_file_location("pipeline",path)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
class EvaluationTests(unittest.TestCase):
    def sample(self,domain="business"):
        return {"task_id":"T1","domain":domain,"reviewer":"A","rubric_version":"1",
                "feedback":"Synthetic", "scores":{k:4 for k in mod.WEIGHTS}}
    def test_perfect(self):
        self.assertEqual(mod.evaluate(self.sample())["rating_of_4"],4)
    def test_finance_low_evidence_escalates(self):
        r=self.sample("finance");r["scores"]["factual_accuracy"]=2
        self.assertEqual(mod.evaluate(r)["decision"],"expert_review")
    def test_bad_score_is_rejected(self):
        r=self.sample();r["scores"]["relevance"]=5
        with self.assertRaises(ValueError):mod.evaluate(r)
    def test_domain_summary(self):
        self.assertEqual(mod.summary([self.sample(),self.sample()])["domain_metrics"]["business"]["n"],2)
if __name__=="__main__":unittest.main()
