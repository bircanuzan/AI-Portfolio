"""Reproducible control tests with deliberately missing real-world approvals."""
import json,sys,unittest
from copy import deepcopy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from catalog_integrity import check
from release_assurance import report
class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest=json.loads((ROOT/"workflow_catalog.json").read_text())
    def test_all_17_original_claude_skills_and_guardrails(self):
        x=check(self.manifest)
        self.assertTrue(x["valid"],x["errors"])
        self.assertEqual(x["claude_workflows"],17)
    def test_missing_skill_detected(self):
        a=deepcopy(self.manifest);a["flows"][0]["folder"]="Claude AI in HR - UNKNOWN"
        self.assertFalse(check(a)["valid"])
    def test_duplicate_skill_detected(self):
        a=deepcopy(self.manifest);a["flows"][0]["folder"]=a["flows"][1]["folder"]
        self.assertFalse(check(a)["valid"])
    def test_unknown_stage_detected(self):
        a=deepcopy(self.manifest);a["flows"][0]["stage"]="AUTONOMOUS_HIRE"
        self.assertFalse(check(a)["valid"])
    def test_flawed_screener_is_held(self):
        x=report()
        self.assertEqual(x["production_release"],"HOLD")
        self.assertIn("UNJUSTIFIED_FLAWED_SCREENING_FLIPS",x["release_blockers"])
    def test_controlled_reference_does_not_equal_approval(self):
        x=report()
        self.assertEqual(x["unjustified_controlled_reference_flips"],0)
        self.assertFalse(x["controlled_reference_approved"])
    def test_16_pairs_and_14_risks(self):
        x=report()
        self.assertEqual(x["paired_tests"],16);self.assertEqual(x["risk_items"],14)
    def test_no_external_actions_or_decisions(self):
        x=report()
        self.assertFalse(x["external_actions_performed"])
        self.assertTrue(x["human_hiring_decision_required"])
    def test_unverified_legal_and_model_gates(self):
        x=report()
        self.assertIn("NO_REAL_SELECTION_VALIDITY_OR_FAIRNESS_STUDY",x["release_blockers"])
if __name__=="__main__":unittest.main()
