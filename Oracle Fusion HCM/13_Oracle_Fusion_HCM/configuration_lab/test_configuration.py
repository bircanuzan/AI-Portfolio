"""Synthetic configuration tests; no Oracle APIs or tenant."""
import sys,unittest,json
from copy import deepcopy
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from validate_configuration import validate

class ConfigurationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture=json.loads((HERE/"configuration_synthetic.json").read_text())
    def fails(self,x,reason):
        result=validate(x)
        self.assertFalse(result["valid"])
        self.assertTrue(any(reason in y for y in result["errors"]),result["errors"])
    def test_valid_model(self):
        v=validate(self.fixture)
        self.assertTrue(v["valid"],v["errors"])
        self.assertFalse(v["oracle_configured"])
    def test_missing_legal_employer(self):
        v=deepcopy(self.fixture);v["business_units"][0]["legal_employer"]="MISSING"
        self.fails(v,"UNKNOWN_LEGAL_EMPLOYER")
    def test_department_set(self):
        v=deepcopy(self.fixture);v["departments"][0]["set"]="SET_ABD"
        self.fails(v,"DEPARTMENT_SET_MISMATCH")
    def test_wrong_department(self):
        v=deepcopy(self.fixture);v["positions"][0]["department"]="DEP_ABD"
        self.fails(v,"POSITION_DEPARTMENT_MISMATCH")
    def test_inaccessible_job(self):
        v=deepcopy(self.fixture);v["jobs"][0]["set"]="SET_ABD"
        self.fails(v,"INACCESSIBLE_SET_JOBS")
    def test_unknown_grade(self):
        v=deepcopy(self.fixture);v["positions"][0]["grade"]="NONE"
        self.fails(v,"UNKNOWN_GRADES")
    def test_bad_fte(self):
        v=deepcopy(self.fixture);v["positions"][0]["fte"]=2
        self.fails(v,"INVALID_FTE")
    def test_bool_fte(self):
        v=deepcopy(self.fixture);v["positions"][0]["fte"]=True
        self.fails(v,"INVALID_FTE")
    def test_bad_date(self):
        v=deepcopy(self.fixture);v["positions"][0]["effective_start"]="2026-99-03"
        self.fails(v,"INVALID_EFFECTIVE_DATE")
    def test_duplicate_position(self):
        v=deepcopy(self.fixture);v["positions"].append(deepcopy(v["positions"][0]))
        self.fails(v,"DUPLICATE")
    def test_same_approver(self):
        v=deepcopy(self.fixture);v["changes"][0]["approver"]="HR_ANALYST"
        self.fails(v,"CHANGE_SELF_APPROVAL")
    def test_unknown_position_change(self):
        v=deepcopy(self.fixture);v["changes"][0]["position"]="NO"
        self.fails(v,"CHANGE_UNKNOWN_POSITION")
    def test_invalid_status(self):
        v=deepcopy(self.fixture);v["model_status"]="LIVE"
        self.fails(v,"NOT_SYNTHETIC_NONPRODUCTION")
if __name__=="__main__":unittest.main()
