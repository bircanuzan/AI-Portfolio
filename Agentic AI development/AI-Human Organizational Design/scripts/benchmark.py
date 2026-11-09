"""Reproducible synthetic scenario benchmark; not production latency or ROI."""
import json
import statistics
import sys
import time
from datetime import datetime,timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from src.hcia.engine import load_data,execute

SCENARIOS=[
 ("talent_acquisition","ALL","hires",60),
 ("talent_acquisition","CORP","hires",16),
 ("employer_brand","CORP","ctr_pct",4.0),
 ("human_capital_operations","CORP","cases",170),
 ("human_capital_operations","INF","exceptions",44),
 ("talent_management","INV","critical_roles",8),
 ("talent_management","INV","successors_ready",3),
 ("workforce_intelligence","ALL","approved_positions",102),
 ("workforce_intelligence","ALL","filled_positions",89),
 ("workforce_intelligence","CORP","vacancies",3),
 ("workforce_intelligence","ALL","headroom_aed",2130000),
 ("total_rewards","CORP","suppressed_cohorts",0)
]
def run_benchmark(repetitions=50):
    data=load_data()
    assertions=[];latencies=[]
    for tool,entity,field,expected in SCENARIOS:
        result=execute(data,tool,entity)
        actual=result["metrics"][field]
        assertions.append({"tool":tool,"entity":entity,"metric":field,
                           "expected":expected,"actual":actual,"pass":actual==expected})
    for _ in range(repetitions):
        start=time.perf_counter()
        result=execute(data,"executive_brief","ALL")
        latencies.append((time.perf_counter()-start)*1000)
        assert result["write_actions_executed"]==0
    s=sorted(latencies)
    return {
      "timestamp_utc":datetime.now(timezone.utc).isoformat(),
      "environment":"local in-process Python, synthetic only",
      "model":"deterministic allowed-tool orchestrator; NO LLM invoked",
      "scenarios":len(assertions),"passed":sum(x["pass"] for x in assertions),
      "scenario_results":assertions,"loops":repetitions,
      "latency_p50_ms":round(statistics.median(s),4),
      "latency_p95_ms":round(s[min(len(s)-1,int(len(s)*0.95))],4),
      "observed_errors":0,
      "limitations":"No network, concurrency, enterprise integration, real workforce, production SLA, bias audit or time saved evidenced."
    }
if __name__=="__main__":
    report=run_benchmark()
    print(json.dumps(report,indent=2))
    if report["passed"]!=report["scenarios"]:
        raise SystemExit("Scenario benchmark failed")
