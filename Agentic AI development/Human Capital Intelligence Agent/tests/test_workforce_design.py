"""Workforce architecture assurance tests; only synthetic data."""
import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.hcia.workforce_design import assess_redesign,load_design,model_capacity,validate

class TestWorkforceDesign(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case=load_design()

    def test_baseline_task_volume(self):
        out=assess_redesign(self.case)
        self.assertEqual(out["capacity"]["baseline_hours"],4813)
        self.assertEqual(len(out["capacity"]["activities"]),7)

    def test_redeployable_capacity_subtracts_oversight(self):
        base=assess_redesign(self.case)["capacity"]
        self.assertAlmostEqual(base["net_redeployable_hours_hypothesis"],1460.55,places=2)
        self.assertLess(base["net_redeployable_hours_hypothesis"],base["gross_candidate_hours"])
        self.assertAlmostEqual(base["potential_capacity_to_redeploy_fte_equivalent"],0.974,places=3)

    def test_high_impact_decisions_excluded(self):
        output=assess_redesign(self.case)["capacity"]["activities"]
        reserved=[a for a in output if a["risk"]=="reserved_decision"]
        self.assertEqual(len(reserved),2)
        self.assertTrue(all(a["net_redeployable_hours_hypothesis"]==0 for a in reserved))
        self.assertTrue(all(not a["agent_may_approve_people_decisions"] for a in output))

    def test_all_future_roles_have_architecture(self):
        roles={j["role"] for j in self.case["job_architecture"]}
        self.assertEqual(len(roles),8)
        self.assertTrue(all(a["future_role"] in roles for a in self.case["activities"]))

    def test_future_org_chart_has_no_orphans(self):
        self.assertEqual(len(self.case["future_structure"]),7)
        validate(self.case)

    def test_reinvestment_is_allocated_not_cash_savings(self):
        result=assess_redesign(self.case)
        rows=result["capacity"]["capacity_reinvestment"]
        self.assertEqual(len(rows),4)
        self.assertAlmostEqual(sum(r["hours_reinvested"] for r in rows),
                               result["capacity"]["net_redeployable_hours_hypothesis"],places=1)
        self.assertEqual(result["capacity"]["cash_savings_evidenced_aed"],0)
        self.assertEqual(result["capacity"]["authorized_headcount_changes"],0)

    def test_zero_adoption_no_capacity(self):
        x=model_capacity(self.case,0)
        self.assertEqual(x["net_redeployable_hours_hypothesis"],0)
        self.assertEqual(x["remaining_workload_fte_equivalent"],x["workload_fte_equivalent_before"])

    def test_optimistic_multiplier_does_not_remove_rights(self):
        x=model_capacity(self.case,1.2)
        self.assertGreater(x["net_redeployable_hours_hypothesis"],model_capacity(self.case,1)["net_redeployable_hours_hypothesis"])
        self.assertTrue(all(not a["agent_may_approve_people_decisions"] for a in x["activities"]))

    def test_cannot_automate_job_grades(self):
        invalid=copy.deepcopy(self.case)
        invalid["activities"][4]["eligible_share"]=0.5
        with self.assertRaises(ValueError):
            validate(invalid)

    def test_cannot_automate_employee_relations_decisions(self):
        invalid=copy.deepcopy(self.case)
        invalid["activities"][5]["eligible_share"]=0.4
        with self.assertRaises(ValueError):
            validate(invalid)

    def test_missing_role_rejected(self):
        invalid=copy.deepcopy(self.case)
        invalid["activities"][0]["future_role"]="Unapproved Ghost Position"
        with self.assertRaises(ValueError):
            validate(invalid)

    def test_reporting_loop_rejected(self):
        invalid=copy.deepcopy(self.case)
        invalid["future_structure"][0]["reports_to"]="Group OE & Workforce Architecture"
        with self.assertRaises(ValueError):
            validate(invalid)

    def test_invalid_capacity_denominator(self):
        invalid=copy.deepcopy(self.case)
        invalid["meta"]["productive_hours_per_fte"]=0
        with self.assertRaises(ValueError):
            validate(invalid)

    def test_false_real_client_flag_rejected(self):
        invalid=copy.deepcopy(self.case)
        invalid["meta"]["fictional"]=False
        with self.assertRaises(ValueError):
            validate(invalid)
if __name__=="__main__":
    unittest.main()
