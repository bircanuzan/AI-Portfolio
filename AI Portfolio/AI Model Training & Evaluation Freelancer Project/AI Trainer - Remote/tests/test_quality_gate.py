import unittest
import importlib.util
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"src"/"quality_gate.py"
spec=importlib.util.spec_from_file_location("quality_gate",p)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

class TestQualityGate(unittest.TestCase):
    def record(self):
        return dict(id="demo",domain="business",rubric_version="1",
           source_context="A synthetic source",scores={k:4 for k in module.WEIGHTS},
           labels=["acceptable"],feedback="Good quality")
    def test_full_score(self):
        self.assertEqual(module.assess(self.record())["disposition"],"accept")
    def test_factual_zero_escalates(self):
        r=self.record();r["scores"]["factual_support"]=0
        self.assertEqual(module.assess(r)["disposition"],"human_escalation")
    def test_out_of_range_rejected(self):
        r=self.record();r["scores"]["coherence"]=5
        with self.assertRaises(ValueError):module.assess(r)

if __name__=="__main__":unittest.main()
