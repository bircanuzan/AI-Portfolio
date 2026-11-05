"""Regression check of synthetic maker/checker scenarios."""
import json
from pathlib import Path
from mobility_workflow import Case, process

def evaluate(path=None):
    path = Path(path) if path else Path(__file__).resolve().parents[1] / "data/scenarios.json"
    cases=json.loads(path.read_text(encoding="utf-8"))
    outcomes=[{"id":row["id"],"passed":process(Case(**row["case"]))["state"]==row["expected"]} for row in cases]
    return {"total":len(outcomes),"passed":sum(int(x["passed"]) for x in outcomes),"cases":outcomes}

if __name__=="__main__":
    print(evaluate())
