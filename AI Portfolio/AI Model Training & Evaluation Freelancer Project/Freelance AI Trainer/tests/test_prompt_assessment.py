import unittest
import importlib.util
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"src"/"prompt_assessment.py"
spec=importlib.util.spec_from_file_location("prompt",p)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class PromptTests(unittest.TestCase):
    def test_full(self):
        self.assertEqual(m.assess({k:2 for k in m.KEYS})["score_of_10"],10)
    def test_privacy_gap(self):
        x={k:2 for k in m.KEYS};x["privacy_and_approval"]=0
        self.assertIn("privacy_and_approval",m.assess(x)["priority_gaps"])
    def test_invalid(self):
        x={k:2 for k in m.KEYS};x["format_defined"]=3
        with self.assertRaises(ValueError):m.assess(x)
if __name__=="__main__":unittest.main()
