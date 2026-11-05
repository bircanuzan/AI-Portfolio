import json
from pathlib import Path
from product_agent import answer
def evaluate(path=None):
    p=Path(path) if path else Path(__file__).resolve().parents[1]/"data/scenarios.json"
    cases=json.loads(p.read_text(encoding="utf-8"))
    output=[{"id":c["id"],"pass":answer(c["prompt"])["status"]==c["expect"]} for c in cases]
    return {"passed":sum(int(x["pass"]) for x in output),"total":len(output),"cases":output}
if __name__=="__main__":print(evaluate())
