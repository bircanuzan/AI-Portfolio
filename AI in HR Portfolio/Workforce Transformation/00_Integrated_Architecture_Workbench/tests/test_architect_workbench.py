"""Integration tests over every existing module and output format, all using synthetic inputs."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from architect_workbench import ROOT, SOURCES, build_evidence, markdown_report, html_dashboard, write_outputs

class WorkbenchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=build_evidence()

    def test_all_eight_modules_are_integrated(self):
        self.assertEqual(len(SOURCES),8)
        self.assertTrue(all((ROOT/p).is_dir() for p in SOURCES.values()))
        self.assertTrue(all(k in self.data for k in (
            "01_capacity","02_role_architecture","03_transition_metrics","04_org_options",
            "05_agent_routing","06_forecasts","06_skill_gaps","07_product_backlog","08_economics")))

    def test_current_state_capacity_is_from_existing_work(self):
        self.assertEqual(len(self.data["01_capacity"]),3)
        self.assertTrue(all(r["decision"]=="HUMAN_VALIDATION_REQUIRED" for r in self.data["01_capacity"]))

    def test_role_and_transition_data_are_connected(self):
        self.assertGreaterEqual(len(self.data["02_role_architecture"]),3)
        self.assertGreaterEqual(len(self.data["03_transition_metrics"]),5)

    def test_nonviable_org_models_are_blocked(self):
        options=self.data["04_org_options"]
        self.assertTrue(any(x["status"]=="HOLD" for x in options))
        self.assertTrue(all(x["score"] is None for x in options if x["status"]!="DISCUSS"))

    def test_routing_matches_expected_and_high_impact_is_human(self):
        rows=self.data["05_agent_routing"]
        self.assertEqual(self.data["05_routing_matches"]["matched"],len(rows))
        self.assertTrue(all(x["actual"]=="HUMAN_REVIEW" for x in rows if x["task"]=="termination_decision"))

    def test_forecasts_have_three_scenarios(self):
        self.assertEqual(len(self.data["06_forecasts"]),9)
        for x in self.data["06_forecasts"]:
            self.assertEqual(set(x),{"reference","guarded_assist","demand_shock"})
            self.assertEqual(x["reference"]["year"],x["guarded_assist"]["year"])

    def test_future_skills_are_group_level_only(self):
        self.assertEqual(len(self.data["06_skill_gaps"]),7)
        self.assertTrue(all("illustrative_priority" in x for x in self.data["06_skill_gaps"]))

    def test_high_risk_product_is_held(self):
        cards=self.data["07_product_backlog"]
        self.assertGreaterEqual(len(cards),4)
        self.assertTrue(any(c["triage"]["decision"]=="HOLD" for c in cards))
        self.assertTrue(all(c["triage"]["human_approval_required"] for c in cards))
        self.assertFalse(any(c["triage"]["action_executed"] for c in cards))

    def test_undeclared_cash_savings_and_roi_are_blocked(self):
        self.assertEqual(self.data["metrics"]["verified_cash_savings_aed"],0)
        self.assertTrue(all(x["verified_cash_savings_aed"]==0 and not x["actual_roi_verified"]
                            for x in self.data["08_economics"]))
        self.assertFalse(self.data["metadata"]["verified_roi"])

    def test_release_hold_and_data_provenance(self):
        self.assertIn("HOLD",self.data["executive_gate"])
        self.assertFalse(self.data["metadata"]["real_customer_data"])
        self.assertFalse(self.data["metadata"]["live_llm"])
        self.assertFalse(self.data["metadata"]["production_hris_connected"])
        self.assertFalse(self.data["metadata"]["employment_decision_executed"])

    def test_executive_pack_contains_every_module(self):
        report=markdown_report(self.data)
        for index in range(1,9):
            self.assertIn("{:02d}".format(index),report)
        self.assertIn("Finance",report)
        self.assertIn("HOLD",report)
        self.assertIn("No",report)

    def test_dashboard_is_self_contained_and_interactive(self):
        page=html_dashboard(self.data)
        self.assertIn("addEventListener",page)
        self.assertIn("document.getElementById",page)
        self.assertIn('id="scenario"',page)
        self.assertIn("Human–AI Workforce",page)
        self.assertNotIn("__PAYLOAD__",page)
        self.assertNotIn("https://",page)
        self.assertNotIn("<iframe",page)

    def test_files_are_written_validly(self):
        with tempfile.TemporaryDirectory() as temp:
            paths=write_outputs(self.data,temp)
            self.assertEqual(len(paths),3)
            self.assertEqual(json.loads(paths["json"].read_text(encoding="utf-8"))["executive_gate"],
                             self.data["executive_gate"])
            self.assertIn("executive evidence pack",paths["markdown"].read_text(encoding="utf-8"))
            self.assertIn("synthetic",paths["html"].read_text(encoding="utf-8").lower())

if __name__=="__main__":
    unittest.main()
