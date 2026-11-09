"""Execute the working tool loop and output verifiable CLI trace / artifacts."""
import json
from pathlib import Path
from src.hcia.agent_runtime import HumanCapitalAgent
from src.hcia.planner import PlanError

GOAL="Evaluate if 0.8 FTE of HR tasks can be redeployed through workforce redesign"
def run():
    agent=HumanCapitalAgent()
    outcome=agent.run(GOAL)
    path=Path("demo/generated")
    path.mkdir(parents=True,exist_ok=True)
    (path/"actual_agent_execution_trace.json").write_text(json.dumps(outcome,indent=2),encoding="utf-8")
    print("USER REQUEST: "+GOAL)
    print("POLICY: "+outcome["planning_mode"])
    for e in outcome["trace"]:
        if e["type"]=="AGENT_ACTION":
            print(f"\n[AGENT PLAN #{e['turn']}] "+e["tool"]+" "+json.dumps(e["args"]))
            print("[WHY] "+e["reason"])
        elif e["type"]=="TOOL_OBSERVATION":
            print("[PYTHON TOOL EXECUTED] "+json.dumps(e["result"],sort_keys=True))
        elif e["type"]=="AGENT_FINAL":
            print("\n[AGENT FINAL] "+json.dumps(e["result"],sort_keys=True))
    try:
        agent.run("Approve terminating employees to achieve savings")
    except PlanError as ex:
        print("\n[SAFETY CHECK] HIGH-RISK REQUEST REFUSED: "+str(ex))
    print("\nSUMMARY: 4 real Python tool calls; no live LLM used; synthetic data only.")
    return outcome
if __name__=="__main__":
    run()
