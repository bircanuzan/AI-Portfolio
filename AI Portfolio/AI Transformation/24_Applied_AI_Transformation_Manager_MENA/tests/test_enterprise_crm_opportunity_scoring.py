import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from enterprise_crm_opportunity_scoring import score, prioritize

class PrioritizationTests(unittest.TestCase):
    def make(self,name,impact=4,feasibility=5,confidence=4,risk=1):
        return dict(use_case=name,impact_1to5=str(impact),feasibility_1to5=str(feasibility),
                    confidence_1to5=str(confidence),risk_1to5=str(risk))
    def test_low_risk_pilot(self):
        self.assertTrue(score(self.make("faq"))["pilot_eligible"])
    def test_high_risk_blocked_even_if_high_impact(self):
        self.assertFalse(score(self.make("sensitive",5,5,5,5))["pilot_eligible"])
    def test_invalid_scale(self):
        with self.assertRaises(ValueError): score(self.make("invalid",risk=0))
    def test_sort_eligible_first(self):
        rows = prioritize([self.make("blocked",5,5,5,5),self.make("safe",3,3,3,1)])
        self.assertEqual(rows[0]["use_case"],"safe")
if __name__ == "__main__": unittest.main()
