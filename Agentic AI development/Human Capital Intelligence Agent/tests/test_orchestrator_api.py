
"""Authorization and safe multi-step tool execution through the HTTP API."""
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from fastapi.testclient import TestClient
from src.hcia.security import Authorizer
from src.hcia.audit import AuditLedger
from src.hcia.service import create_app

LEADER="leader-authorization-demo-testing-12345"
ANALYST="analyst-authorization-demo-testing-12345"

class TestGoalApi(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        auth=Authorizer({
          LEADER:{"actor_id":"cpo","role":"people_leader","entities":["ALL","CORP"]},
          ANALYST:{"actor_id":"ta","role":"recruitment_analyst","entities":["CORP"]}
        })
        ledger=AuditLedger(Path(self.tmp.name)/"audit.sqlite3",key="test-verified-orchestration-audit-1234")
        self.client=TestClient(create_app(auth=auth,audit=ledger))
        self.headers={"Authorization":"Bearer "+LEADER}

    def test_no_token_denied(self):
        r=self.client.post("/v1/agent/orchestrate",json={"goal":"Review recruiting and headcount","entity":"CORP"})
        self.assertEqual(r.status_code,401)

    def test_cross_domain_analyst_denied(self):
        r=self.client.post("/v1/agent/orchestrate",headers={"Authorization":"Bearer "+ANALYST},
                           json={"goal":"Review recruiting and headcount","entity":"CORP"})
        self.assertEqual(r.status_code,403)

    def test_valid_two_step_plan_with_audit(self):
        r=self.client.post("/v1/agent/orchestrate",headers=self.headers,
                           json={"goal":"Review recruiting and headcount","entity":"CORP"})
        self.assertEqual(r.status_code,200)
        out=r.json()
        self.assertEqual(out["tools_selected"],["talent_acquisition","workforce_intelligence"])
        self.assertEqual(len(out["steps"]),2)
        self.assertTrue(out["event_id"])
        self.assertEqual(out["planning_mode"],"deterministic_offline")
        self.assertEqual(out["write_actions_executed"],0)

    def test_privacy_instruction_denied(self):
        r=self.client.post("/v1/agent/orchestrate",headers=self.headers,
                           json={"goal":"Find salary of candidate ID ABC","entity":"CORP"})
        self.assertEqual(r.status_code,422)

    def test_llm_not_configured_is_not_misrepresented(self):
        import os
        from unittest.mock import patch
        with patch.dict(os.environ,{"HCIA_LLM_ENDPOINT":"","HCIA_LLM_API_KEY":""}):
            r=self.client.post("/v1/agent/orchestrate",headers=self.headers,
                               json={"goal":"Assess recruitment funnel","entity":"CORP",
                                     "use_model_planner":True})
        self.assertEqual(r.status_code,422)

    def test_unapproved_entity_denied(self):
        r=self.client.post("/v1/agent/orchestrate",headers=self.headers,
                           json={"goal":"Review workforce budget","entity":"INF"})
        self.assertEqual(r.status_code,403)

if __name__=="__main__":
    unittest.main()
