import unittest
from src.hcia.organization_platform import blueprint, compare_scenarios, _org_tree, PRODUCT, FEATURE_STATUS
from src.hcia.workforce_design import load_design

class OrganizationalDesignTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.b = blueprint()

    def test_name_and_holds(self):
        self.assertEqual(self.b["product"], "AI-Human Organizational Design")
        self.assertIn("NOT_PRODUCTION", self.b["state"])
        self.assertEqual(self.b["write_actions_executed"], 0)

    def test_full_architecture(self):
        self.assertEqual(len(self.b["work_task_intelligence"]), 7)
        self.assertEqual(len(self.b["role_and_skills_architecture"]), 8)
        self.assertEqual(len(self.b["organizational_digital_twin"]), 7)

    def test_sensitive_decisions_are_human_only(self):
        restricted=[x for x in self.b["work_task_intelligence"] if x["risk"]=="reserved_decision"]
        self.assertEqual(len(restricted), 2)
        self.assertTrue(all(x["allocation"]=="HUMAN_ONLY" for x in restricted))
        self.assertTrue(all(not x["agent_can_approve_people_decisions"] for x in self.b["work_task_intelligence"]))

    def test_agent_register_cannot_act(self):
        a=self.b["digital_agent_candidates"]
        self.assertTrue(a)
        self.assertTrue(all(x["lifecycle"]=="DRAFT_NOT_DEPLOYED" for x in a))
        self.assertTrue(all(x["decision_authority"]=="RECOMMEND_ONLY" for x in a))
        self.assertTrue(all(x["human_manager"] for x in a))

    def test_human_unit_owners(self):
        self.assertTrue(all(x["accountable_human"] for x in self.b["organizational_digital_twin"]))
        self.assertEqual(sum(x["reports_to"] is None for x in self.b["organizational_digital_twin"]),1)

    def test_reject_multiple_org_roots(self):
        case=load_design()
        case["future_structure"][1]["reports_to"]=None
        with self.assertRaises(ValueError):
            _org_tree(case)

    def test_role_skills_without_employee_inference(self):
        roles=self.b["role_and_skills_architecture"]
        self.assertTrue(all(x["skills"] for x in roles))
        self.assertTrue(all(x["individual_skill_assessment"]=="NOT_PERFORMED" for x in roles))

    def test_zero_adoption_zero_net_capacity(self):
        cap=blueprint(0)["net_capacity_scenario"]
        self.assertEqual(cap["net_redeployable_hours_hypothesis"],0)

    def test_oversight_deducted(self):
        cap=self.b["net_capacity_scenario"]
        self.assertGreater(cap["oversight_hours"],0)
        self.assertGreater(cap["gross_candidate_hours"],cap["net_redeployable_hours_hypothesis"])

    def test_no_financial_return_claims(self):
        e=self.b["workforce_economics"]
        self.assertIsNone(e["validated_roi"])
        self.assertIsNone(e["actual_cash_savings"])

    def test_economic_scenario_labeled(self):
        e=blueprint(value_per_hour_aed=120,yearly_agent_cost_aed=10000,startup_cost_aed=2000)["workforce_economics"]
        self.assertIn("hypothetical_capacity_opportunity_aed",e)
        self.assertTrue(e["this_is_not_cash_saving"])
        self.assertIsNone(e["validated_roi"])

    def test_invalid_inputs(self):
        for kw in [{"value_per_hour_aed":-1},{"adoption_multiplier":9},{"adoption_multiplier":True}]:
            with self.assertRaises(ValueError):
                blueprint(**kw)

    def test_separate_fictional_sources(self):
        self.assertTrue(self.b["workforce_analytics_separate_case"]["evidence"]["synthetic"])
        self.assertTrue(self.b["source"]["fictional"])

    def test_no_false_integration(self):
        self.assertEqual(self.b["enterprise_connector_status"]["Inception42 Catalyst"],"ACCESS_NOT_VERIFIED")
        self.assertEqual(FEATURE_STATUS["G42 sovereign LLM and enterprise platform integration"],"NOT_CONNECTED")

    def test_scenarios_all_hold(self):
        cs=compare_scenarios()
        self.assertEqual(len(cs["scenarios"]),3)
        self.assertTrue(all(x["approval"]=="HOLD" for x in cs["scenarios"]))

if __name__=="__main__": unittest.main()
