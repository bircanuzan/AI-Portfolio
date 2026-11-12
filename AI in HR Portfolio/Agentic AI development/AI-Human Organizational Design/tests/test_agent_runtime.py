"""Test true tool execution loop, observation-driven planning and boundaries."""
import unittest
from src.hcia.agent_runtime import HumanCapitalAgent,AgentError,Decision,OpenAICompatiblePolicy
from src.hcia.planner import PlanError

class TestAgentRuntime(unittest.TestCase):
    def test_observation_replans_and_calls_real_tools(self):
        r=HumanCapitalAgent().run("Evaluate if 0.8 FTE of HR tasks can be redeployed through workforce redesign")
        self.assertEqual(r["tool_calls"],4)
        acts=[e for e in r["trace"] if e["type"]=="AGENT_ACTION"]
        self.assertEqual([e["tool"] for e in acts],
                         ["read_workforce","model_capacity","stress_test","review_governance"])
        self.assertEqual(acts[2]["args"]["adoption_multiplier"],0.65)
        self.assertTrue(r["final"]["base_meets_target"])
        self.assertFalse(r["final"]["stress_meets_target"])
        self.assertEqual(r["final"]["actual_staff_changes"],0)

    def test_target_changes_branch(self):
        r=HumanCapitalAgent().run("Evaluate 5 FTE target for workforce redesign")
        acts=[e for e in r["trace"] if e["type"]=="AGENT_ACTION"]
        self.assertEqual(acts[2]["args"]["adoption_multiplier"],0.0)
        self.assertEqual(r["final"]["stress_capacity_fte"],0)

    def test_unapproved_personnel_change_refused(self):
        with self.assertRaises(PlanError):
            HumanCapitalAgent().run("Approve terminating employees to achieve savings")

    def test_employee_id_refused(self):
        with self.assertRaises(PlanError):
            HumanCapitalAgent().run("Review employee id A123 workforce data")

    def test_cross_role_access_refused(self):
        with self.assertRaisesRegex(AgentError,"RBAC"):
            HumanCapitalAgent().run("Assess 0.8 FTE task capacity",role="recruitment_analyst")

    def test_nonallowlisted_model_tool_refused(self):
        class Adversarial:
            name="TEST"
            def choose(self,goal,observations,entity):
                return Decision("tool","delete_employee",{},"")
        with self.assertRaisesRegex(AgentError,"allowlisted"):
            HumanCapitalAgent(policy=Adversarial()).run("Assess 0.8 FTE workforce capacity")

    def test_model_cannot_finish_without_evidence(self):
        class Lazy:
            name="TEST"
            def choose(self,goal,observations,entity):
                return Decision("finish",reason="Done")
        with self.assertRaisesRegex(AgentError,"Premature"):
            HumanCapitalAgent(policy=Lazy()).run("Assess 0.8 FTE workforce capacity")

    def test_repeated_tool_refused(self):
        class Looping:
            name="TEST"
            def choose(self,goal,observations,entity):
                return Decision("tool","read_workforce",{},"again")
        with self.assertRaisesRegex(AgentError,"Repeated"):
            HumanCapitalAgent(policy=Looping()).run("Assess 0.8 FTE workforce capacity")

    def test_no_live_llm_without_credentials(self):
        with self.assertRaises(AgentError):
            OpenAICompatiblePolicy(endpoint="http://localhost:3000",
                                   api_key="test",model="test",host_allowlist="localhost")
