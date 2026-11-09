"""Native function-call orchestration and safety test suite. Uses scripted provider, not LLM."""
import json
import unittest
from pathlib import Path
from types import SimpleNamespace
from src.hcia.workforce_architect import (
    AgentBoundaryError,ScriptedResponsesClient,run_agent,load_design,
    execute_tool,_validated_blueprint,BLUEPRINT_SCHEMA,TOOLS,_args
)

GOAL="Design synthetic human-AI roles, model alternative workforce capacity and assess employee protections."

class WorkforceArchitectTests(unittest.TestCase):
    def test_protocol_calls_and_submission(self):
        client=ScriptedResponsesClient()
        x=run_agent(GOAL,client,mode="SCRIPTED_MODEL_STUB_NOT_LLM")
        self.assertEqual(x.mode,"SCRIPTED_MODEL_STUB_NOT_LLM")
        self.assertEqual(len(x.tool_trace),6)
        self.assertEqual(x.blueprint["status"],"DRAFT_ONLY_HUMAN_REVIEW_REQUIRED")
        self.assertEqual(x.blueprint["real_world_actions_taken"],0)
        self.assertEqual(x.blueprint["approved_workforce_changes"],0)

    def test_required_evidence_all_used(self):
        x=run_agent(GOAL,ScriptedResponsesClient())
        self.assertEqual([t["tool"] for t in x.tool_trace],
            ["inspect_work","simulate_capacity","compare_scenarios",
             "inspect_future_organization","review_governance","submit_blueprint"])

    def test_reserved_decisions_human_only(self):
        case=load_design();x=run_agent(GOAL,ScriptedResponsesClient())
        reserved={a["id"] for a in case["activities"] if a["risk"]=="reserved_decision"}
        self.assertGreater(len(reserved),0)
        self.assertTrue(all(a["allocation"]=="HUMAN_ONLY"
            for a in x.blueprint["task_assignments"] if a["task_id"] in reserved))

    def test_unsafe_final_allocation_denied(self):
        case=load_design()
        good=run_agent(GOAL,ScriptedResponsesClient(),case=case).blueprint
        bad={k:v for k,v in good.items() if k in BLUEPRINT_SCHEMA["properties"]}
        bad["task_assignments"]=[dict(x) for x in good["task_assignments"]]
        flagged=next(x for x in bad["task_assignments"] if x["task_id"]=="A6")
        flagged["allocation"]="AGENT_CANDIDATE"
        with self.assertRaisesRegex(AgentBoundaryError,"Reserved"):
            _validated_blueprint(case,bad,{"inspect_work","simulate_capacity","compare_scenarios",
                                         "inspect_future_organization","review_governance"})

    def test_eight_future_roles_are_really_redesigned(self):
        case=load_design()
        x=run_agent(GOAL,ScriptedResponsesClient(),case=case).blueprint
        self.assertEqual({r["base_role"] for r in x["role_redesigns"]},
                         {r["role"] for r in case["job_architecture"]})
        self.assertEqual(len(x["organization_reporting_proposal"]),len(case["future_structure"]))

    def test_unverified_role_rejected(self):
        case=load_design()
        good=run_agent(GOAL,ScriptedResponsesClient(),case=case).blueprint
        bad={k:v for k,v in good.items() if k in BLUEPRINT_SCHEMA["properties"]}
        bad["role_redesigns"]=[dict(x) for x in bad["role_redesigns"]]
        bad["role_redesigns"][0]["base_role"]="Made Up Role"
        with self.assertRaises(AgentBoundaryError):
            _validated_blueprint(case,bad,{"inspect_work","simulate_capacity","compare_scenarios",
                                          "inspect_future_organization","review_governance"})

    def test_cycle_in_future_reporting_blocked(self):
        case=load_design()
        good=run_agent(GOAL,ScriptedResponsesClient(),case=case).blueprint
        bad={k:v for k,v in good.items() if k in BLUEPRINT_SCHEMA["properties"]}
        bad["organization_reporting_proposal"]=[dict(x) for x in bad["organization_reporting_proposal"]]
        units=bad["organization_reporting_proposal"]
        units[0]["reports_to"]=units[1]["unit"]
        units[1]["reports_to"]=units[0]["unit"]
        with self.assertRaises(AgentBoundaryError):
            _validated_blueprint(case,bad,{"inspect_work","simulate_capacity","compare_scenarios",
                                          "inspect_future_organization","review_governance"})

    def test_sensitive_controlled_not_auto_agent(self):
        case=load_design()
        good=run_agent(GOAL,ScriptedResponsesClient(),case=case).blueprint
        bad={k:v for k,v in good.items() if k in BLUEPRINT_SCHEMA["properties"]}
        bad["task_assignments"]=[dict(x) for x in bad["task_assignments"]]
        controlled=next(x for x in bad["task_assignments"] if x["task_id"]=="A3")
        controlled["allocation"]="AGENT_CANDIDATE"
        with self.assertRaises(AgentBoundaryError):
            _validated_blueprint(case,bad,{"inspect_work","simulate_capacity","compare_scenarios",
                                          "inspect_future_organization","review_governance"})

    def test_invented_org_rejected(self):
        case=load_design()
        good=run_agent(GOAL,ScriptedResponsesClient(),case=case).blueprint
        bad={k:v for k,v in good.items() if k in BLUEPRINT_SCHEMA["properties"]}
        bad["future_org_units"]=["Imaginary RPA Unit"]
        with self.assertRaises(AgentBoundaryError):
            _validated_blueprint(case,bad,{"inspect_work","simulate_capacity","compare_scenarios",
                                          "inspect_future_organization","review_governance"})

    def test_missing_evidence_refuses_approval(self):
        with self.assertRaises(AgentBoundaryError):
            execute_tool(load_design(),"submit_blueprint",
                {"task_assignments":[],"future_org_units":[],"design_tradeoffs":[],"next_validation_steps":[]},
                set())

    def test_invalid_model_tool_denied(self):
        with self.assertRaises(AgentBoundaryError):
            _args("execute_payroll",{})

    def test_invalid_multiplier_denied(self):
        with self.assertRaises(AgentBoundaryError):
            execute_tool(load_design(),"simulate_capacity",{"adoption_multiplier":8},set())

    def test_tool_calls_are_actual_existing_model(self):
        c=load_design()
        result=execute_tool(c,"simulate_capacity",{"adoption_multiplier":0.4},set())
        self.assertGreater(len(result["result"]["activities"]),0)
        self.assertEqual(result["result"]["authorized_headcount_changes"],0)

    def test_sensitivity_has_two_actual_runs(self):
        r=execute_tool(load_design(),"compare_scenarios",{"adoption_low":0,"adoption_high":1},set())
        self.assertLessEqual(r["low"]["capacity_fte"],r["high"]["capacity_fte"])

    def test_repeated_call_ids_rejected(self):
        class Bad:
            def __init__(self):self.responses=self
            def create(self,**kw):return SimpleNamespace(output=[
                SimpleNamespace(type="function_call",call_id="same",name="inspect_work",arguments="{}")])
        with self.assertRaises(AgentBoundaryError):
            run_agent(GOAL,Bad())

    def test_early_final_answer_rejected(self):
        class Early:
            def __init__(self):self.responses=self
            def create(self,**kw):return SimpleNamespace(output=[
                SimpleNamespace(type="message",content=[])])
        with self.assertRaises(AgentBoundaryError):
            run_agent(GOAL,Early())

    def test_protected_employee_id_rejected(self):
        with self.assertRaises(AgentBoundaryError):
            run_agent("Design work for employee id 83752 using these tools",ScriptedResponsesClient())

    def test_missing_model_does_not_claim_live(self):
        x=run_agent(GOAL,ScriptedResponsesClient(),mode="SCRIPTED_MODEL_STUB_NOT_LLM")
        self.assertNotEqual(x.mode,"LIVE_MODEL_TOOL_CALLS")

    def test_models_have_schemas_and_no_writes(self):
        self.assertEqual(len(TOOLS),6)
        self.assertTrue(all(t["type"]=="function" and t["strict"] for t in TOOLS))
        self.assertTrue(all("delete" not in t["name"] and "hire" not in t["name"] for t in TOOLS))

if __name__=="__main__":
    unittest.main()
