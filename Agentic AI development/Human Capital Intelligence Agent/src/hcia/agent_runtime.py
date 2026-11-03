"""Human Capital agent execution runtime, not a static analytics presentation.

Finite-state, observation-driven tool-call loop with real Python function execution.
The offline policy is deterministic and is NOT a language model. A separate
allowlisted HTTPS model policy supports live action proposals once configured.
No production data, HR actions or external model calls are made in offline demo.
"""
from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from .engine import execute, load_data
from .planner import guard_goal
from .security import PERMISSIONS
from .workforce_design import load_design, model_capacity

AGENT_TOOLS = {
    "read_workforce": "Read synthetic group workforce and position data",
    "model_capacity": "Analyse synthetic work activities, job architecture and capacity",
    "stress_test": "Run a bounded alternative AI adoption scenario",
    "review_governance": "Check human-only rights, approvals and assurance gates",
}
MAX_CALLS = 5
FTE_TARGET = re.compile(r"\b(?:at\s+least\s+|target\s+)?([0-9]+(?:\.[0-9]+)?)\s*fte\b", re.I)

class AgentError(Exception):
    pass

@dataclass(frozen=True)
class Decision:
    action: str
    tool: str | None = None
    args: dict | None = None
    reason: str = ""

def _target(goal):
    m = FTE_TARGET.search(goal)
    return float(m.group(1)) if m else 0.8

class OfflineAdaptivePolicy:
    """Offline deterministic test policy; each choice reads prior observations."""
    name = "OFFLINE_ADAPTIVE_POLICY_NOT_AN_LLM"
    def choose(self, goal, observations, entity):
        seen = {a["tool"]: a["result"] for a in observations}
        if "read_workforce" not in seen:
            return Decision("tool", "read_workforce", {}, "Establish baseline vacancies and aggregate positions")
        if "model_capacity" not in seen:
            return Decision("tool", "model_capacity", {}, "Analyse job architecture and task-level human/agent allocation")
        if "stress_test" not in seen:
            base = seen["model_capacity"]["capacity_fte"]
            factor = 0.65 if base >= _target(goal) else 0.0
            why = "Base scenario meets target: test lower adoption" if factor else "Base below target: test zero adoption"
            return Decision("tool", "stress_test", {"adoption_multiplier":factor}, why)
        if "review_governance" not in seen:
            return Decision("tool", "review_governance", {}, "Sensitive decisions require human approval")
        return Decision("finish", reason="Four independent observations now available; compile bounded answer")

class OpenAICompatiblePolicy:
    """Optional real LLM tool selector; no run until operator supplies credentials."""
    name = "OPERATOR_CONFIGURED_LLM_TOOL_SELECTION"
    def __init__(self, endpoint=None, api_key=None, model=None, host_allowlist=None):
        self.endpoint = endpoint or os.getenv("HCIA_LLM_ENDPOINT", "")
        self.api_key = api_key or os.getenv("HCIA_LLM_API_KEY", "")
        self.model = model or os.getenv("HCIA_LLM_MODEL", "")
        hosts = host_allowlist or os.getenv("HCIA_LLM_HOST_ALLOWLIST", "")
        self.allowlist = {x.strip().lower() for x in hosts.split(",") if x.strip()}
        parsed = urlparse(self.endpoint)
        if not (parsed.scheme=="https" and parsed.hostname and
                parsed.hostname.lower() in self.allowlist and not parsed.username and
                not parsed.password and self.api_key and self.model):
            raise AgentError("Live model requires allowlisted HTTPS endpoint, model and API credentials")

    def choose(self, goal, observations, entity):
        system = (
            "You select one tool action for a read-only synthetic HR analyst. "
            'Reply JSON only: {"action":"tool","tool":"read_workforce|model_capacity|stress_test|review_governance",'
            '"args":{},"reason":"short reason"} or {"action":"finish","reason":"short reason"}. '
            "Gather baseline, capacity, stress, and governance evidence before finishing. "
            "For stress_test supply adoption_multiplier in [0, 1.25]. "
            "Never approve personnel decisions or invent tool observations."
        )
        history = [{"tool":x["tool"],"observation":x["result"]} for x in observations]
        payload = {"model":self.model,"temperature":0,"max_tokens":180,
            "messages":[{"role":"system","content":system},
                        {"role":"user","content":json.dumps({"goal":goal,"entity":entity,
                          "previous_tool_observations":history})}]}
        req=Request(self.endpoint,data=json.dumps(payload).encode(),method="POST",
            headers={"Content-Type":"application/json","Authorization":"Bearer "+self.api_key})
        try:
            with urlopen(req,timeout=12) as rsp:
                content=json.loads(rsp.read(100000))["choices"][0]["message"]["content"]
            obj=json.loads(content)
        except Exception as exc:
            raise AgentError("Live model unavailable or malformed; no action taken") from exc
        if not isinstance(obj,dict) or obj.get("action") not in {"tool","finish"} or (
            set(obj)-{"action","tool","args","reason"}):
            raise AgentError("Model proposed an invalid action structure")
        return Decision(obj["action"],obj.get("tool"),obj.get("args",{}),
                        str(obj.get("reason",""))[:120])

class HumanCapitalAgent:
    def __init__(self, policy=None, data=None):
        self.policy = policy if policy is not None else OfflineAdaptivePolicy()
        self.data = data if data is not None else load_data()

    def call_tool(self, tool, args, role, entity):
        if tool not in AGENT_TOOLS:
            raise AgentError("Non-allowlisted tool refused")
        if role not in PERMISSIONS:
            raise AgentError("Unknown actor role")
        if tool=="read_workforce":
            if args: raise AgentError("Unexpected tool arguments")
            if "workforce_intelligence" not in PERMISSIONS[role]:
                raise AgentError("RBAC: insufficient workforce intelligence access")
            m=execute(self.data,"workforce_intelligence",entity)["metrics"]
            return {"approved_positions":m["approved_positions"],"occupied":m["filled_positions"],
                    "vacancies":m["vacancies"],"source":"fictional workforce fixture"}
        if entity!="ALL" or "workforce_redesign" not in PERMISSIONS[role]:
            raise AgentError("RBAC: group workforce design restricted")
        if tool=="model_capacity":
            if args: raise AgentError("Unexpected tool arguments")
            m=execute(self.data,"workforce_redesign",entity)
            c=m["capacity"]
            return {"baseline_hours":c["baseline_hours"],
                    "net_candidate_hours":c["net_redeployable_hours_hypothesis"],
                    "capacity_fte":c["potential_capacity_to_redeploy_fte_equivalent"],
                    "future_human_roles":len(m["job_architecture"]),
                    "future_org_units":len(m["future_structure"]),
                    "headcount_reductions_approved":0,
                    "source":"fictional work redesign fixture"}
        if tool=="stress_test":
            if not isinstance(args,dict) or set(args)!={"adoption_multiplier"}:
                raise AgentError("Stress test requires adoption_multiplier only")
            factor=args["adoption_multiplier"]
            if isinstance(factor,bool) or not isinstance(factor,(int,float)) or not 0<=factor<=1.25:
                raise AgentError("Adoption multiplier refused")
            c=model_capacity(load_design(),factor)
            return {"adoption_multiplier":factor,
                    "capacity_fte":c["potential_capacity_to_redeploy_fte_equivalent"],
                    "candidate_hours":c["net_redeployable_hours_hypothesis"],
                    "source":"synthetic adoption sensitivity"}
        if tool=="review_governance":
            if args: raise AgentError("Unexpected tool arguments")
            return {"decision":"HUMAN_REVIEW_REQUIRED",
                    "reserved_actions":["job grade approval","hiring","pay","employee relations"],
                    "approval_owners":["CPO","Finance","Legal/ER","AI assurance"],
                    "agent_write_authority":False,
                    "source":"illustrative human oversight policy"}
        raise AgentError("Tool refused")

    def run(self, goal, role="people_leader", entity="ALL"):
        goal=guard_goal(goal)  # rejects employee IDs and state-changing instructions
        if role not in PERMISSIONS or entity not in {"ALL","CORP","INV","INF"}:
            raise AgentError("Unknown actor or entity")
        observations=[];trace=[{"type":"USER_GOAL","text":goal},
                              {"type":"PLANNER_MODE","text":self.policy.name}]
        called=set()
        for turn in range(1,MAX_CALLS+2):
            try:
                decision=self.policy.choose(goal,observations,entity)
            except Exception as exc:
                raise AgentError("Agent policy failed closed") from exc
            if not isinstance(decision,Decision):
                raise AgentError("Invalid policy result")
            if decision.action=="finish":
                if set(AGENT_TOOLS)-called:
                    raise AgentError("Premature completion refused: missing evidence")
                facts={o["tool"]:o["result"] for o in observations}
                b=facts["model_capacity"];s=facts["stress_test"];limit=_target(goal)
                final={"outcome":"PROPOSAL_FOR_HUMAN_REVIEW","goal":goal,
                       "target_fte":limit,"base_capacity_fte":b["capacity_fte"],
                       "stress_capacity_fte":s["capacity_fte"],
                       "base_meets_target":b["capacity_fte"]>=limit,
                       "stress_meets_target":s["capacity_fte"]>=limit,
                       "vacancies":facts["read_workforce"]["vacancies"],
                       "proposed_roles":b["future_human_roles"],
                       "proposed_org_units":b["future_org_units"],
                       "actual_staff_changes":0,"financial_savings_evidenced":False,
                       "human_approval_required":True,
                       "synthetic":True,
                       "sources":[o["result"]["source"] for o in observations]}
                trace.append({"type":"AGENT_FINAL","result":final})
                return {"synthetic":True,"planning_mode":self.policy.name,
                        "trace":trace,"final":final,"tool_calls":len(observations)}
            if decision.action!="tool" or not decision.tool or not isinstance(decision.args,dict):
                raise AgentError("Invalid model tool selection")
            if turn>MAX_CALLS: raise AgentError("Maximum tool calls reached")
            if decision.tool in called: raise AgentError("Repeated tool refused")
            trace.append({"type":"AGENT_ACTION","turn":turn,"tool":decision.tool,
                          "args":decision.args,"reason":decision.reason})
            observation=self.call_tool(decision.tool,decision.args,role,entity)
            trace.append({"type":"TOOL_OBSERVATION","turn":turn,"tool":decision.tool,
                          "result":observation})
            observations.append({"tool":decision.tool,"result":observation})
            called.add(decision.tool)
        raise AgentError("Agent failed step limit")
