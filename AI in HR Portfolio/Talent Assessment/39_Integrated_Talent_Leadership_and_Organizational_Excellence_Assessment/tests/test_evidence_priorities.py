"""Organisational evidence triage: fictional inputs, no candidate or employer grading."""
import json,sys,unittest
from copy import deepcopy
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(HERE/"src"))
from evidence_priorities import prioritise
CASE=json.loads((HERE/"data/synthetic_organisational_evidence.json").read_text())
class ExecutiveEvidenceTests(unittest.TestCase):
    def test_six_divergent_domains(self):
        r=prioritise(CASE)
        self.assertEqual(r["domains_checked"],6)
    def test_missing_evidence_prioritized(self):
        r=prioritise(CASE)["evidence_review_queue"]
        self.assertEqual(r[0]["investigation_priority_index"],15)
    def test_priority_order(self):
        scores=[x["investigation_priority_index"] for x in prioritise(CASE)["evidence_review_queue"]]
        self.assertEqual(scores,sorted(scores,reverse=True))
    def test_no_performance_or_employment_grade(self):
        r=prioritise(CASE)
        self.assertFalse(r["actual_organisation_maturity_assessed"])
        self.assertFalse(r["individual_assessment_performed"])
        self.assertTrue(all(x["performance_or_maturity_grade"] is None for x in r["evidence_review_queue"]))
    def test_provenance_must_be_fictional(self):
        v=deepcopy(CASE);v["classification"]="ACTUAL_ORGANISATION"
        with self.assertRaises(ValueError):prioritise(v)
    def test_duplicate_domain_rejected(self):
        v=deepcopy(CASE);v["domains"][1]["id"]=v["domains"][0]["id"]
        with self.assertRaises(ValueError):prioritise(v)
    def test_bad_impact_rejected(self):
        v=deepcopy(CASE);v["domains"][0]["impact_weight"]=7
        with self.assertRaises(ValueError):prioritise(v)
    def test_boolean_impact_rejected(self):
        v=deepcopy(CASE);v["domains"][0]["impact_weight"]=True
        with self.assertRaises(ValueError):prioritise(v)
    def test_missing_owner_rejected(self):
        v=deepcopy(CASE);v["domains"][0]["owner"]=""
        with self.assertRaises(ValueError):prioritise(v)
    def test_unknown_evidence_state_rejected(self):
        v=deepcopy(CASE);v["domains"][0]["evidence_status"]="verified_employer"
        with self.assertRaises(ValueError):prioritise(v)
    def test_human_release_gate(self):
        self.assertEqual(prioritise(CASE)["release"],"HOLD_FOR_HUMAN_VALIDATION")
if __name__=="__main__":unittest.main()
