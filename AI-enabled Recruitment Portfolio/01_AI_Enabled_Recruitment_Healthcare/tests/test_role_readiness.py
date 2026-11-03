"""No real healthcare, visa, or employment authorization."""
import sys,unittest,json
from copy import deepcopy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from role_readiness import report,assess
FIX=json.loads((ROOT/"data/synthetic_healthcare_role_briefs.json").read_text())
class RoleReadinessTests(unittest.TestCase):
    def test_three_fictional_roles(self):
        self.assertEqual(report(FIX)["role_count"],3)
    def test_all_on_hold(self):
        self.assertTrue(all(r["status"]=="HOLD" for r in report(FIX)["results"]))
    def test_never_issues_licence_clearance(self):
        self.assertTrue(all(not r["licence_verified"] and not r["hiring_authorized"] for r in report(FIX)["results"]))
    def test_missing_market_blocks(self):
        r=deepcopy(FIX["roles"][0]);r["market"]=""
        self.assertIn("market",assess(r)["gaps"])
    def test_official_source_verification_blocks(self):
        self.assertIn("OFFICIAL_RULE_NOT_VERIFIED",assess(FIX["roles"][1])["gaps"])
    def test_missing_clinical_approval_blocks(self):
        self.assertIn("HUMAN_ROLE_APPROVAL_PENDING",assess(FIX["roles"][2])["gaps"])
    def test_admin_role_ready_for_further_review_never_hire(self):
        r=deepcopy(FIX["roles"][2]);r["role_brief_signed"]=True
        x=assess(r)
        self.assertEqual(x["status"],"READY_FOR_FURTHER_HUMAN_VERIFICATION")
        self.assertFalse(x["hiring_authorized"])
    def test_duplicated_role_id_rejected(self):
        r=deepcopy(FIX);r["roles"][1]["id"]=r["roles"][0]["id"]
        with self.assertRaises(ValueError):report(r)
    def test_untrusted_provenance_rejected(self):
        r=deepcopy(FIX);r["classification"]="REAL_EMPLOYER"
        with self.assertRaises(ValueError):report(r)
    def test_non_mapping_safe(self):
        self.assertEqual(assess(None)["status"],"HOLD")
if __name__=="__main__":unittest.main()
