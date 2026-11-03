#!/usr/bin/env python3
"""Run the G42-aligned local demo without third-party packages."""
import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/"src"))
from hr_agent.storage import connect
from hr_agent.ingestion import ingest
from hr_agent.agent import Agent
from hr_agent.api import serve


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("command",choices=["ingest","ask","eval","serve","queue"])
    ap.add_argument("--db",default=str(ROOT/"data"/"lab.sqlite3"))
    ap.add_argument("--query",default="What is the annual leave policy?")
    ap.add_argument("--evidence",default=str(ROOT/"evidence"/"local_python_evaluation.json"))
    args=ap.parse_args()
    if args.command=="serve":
        with connect(args.db) as db:
            if not db.execute("SELECT 1 FROM policies LIMIT 1").fetchone():
                ingest(db,ROOT/"data"/"policies.json")
        return serve(args.db)
    with connect(args.db) as db:
        if args.command=="ingest": out=ingest(db,ROOT/"data"/"policies.json")
        elif args.command=="ask": out=Agent(db).ask(args.query)
        elif args.command=="queue": out=[dict(r) for r in db.execute("SELECT * FROM review_queue ORDER BY created_at DESC LIMIT 20")]
        else:
            from datetime import datetime, timezone
            tests=json.loads((ROOT/"data"/"evaluation_cases.json").read_text())
            records=[]
            for case in tests:
                actual=Agent(db).ask(case["prompt"])
                success=(actual["decision"]==case["expected_decision"] and
                         [s["id"] for s in actual["sources"]]==case["expected_sources"])
                records.append({"case_id":case["case_id"],"prompt":case["prompt"],
                                "expected_decision":case["expected_decision"],"expected_sources":case["expected_sources"],
                                "actual":actual,"match":success})
            risky=[r for r in records if r["expected_decision"]!="ANSWER"]
            total=len(records); passed=sum(r["match"] for r in records)
            summary={"test_count":total,"passed":passed,"failed":total-passed,"match_rate_pct":round(100*passed/total,2),
                     "human_required_recall_pct":round(100*sum(r["actual"]["decision"]!="ANSWER" for r in risky)/len(risky),2) if risky else None,
                     "observed_external_actions":0,"release_decision":"HOLD — not deployed, independent/LLM/cloud/security verification not completed"}
            out={"captured_at_utc":datetime.now(timezone.utc).isoformat(),"runtime":"Python stdlib, SQLite",
                 "engine":"deterministic policy router with local hashed lexical vector retrieval, NOT an LLM",
                 "quality_caveat":"author-controlled fixtures; no independent evaluation or production-like adversarial validation",
                 "source_sha256":hashlib.sha256((ROOT/"src"/"hr_agent"/"agent.py").read_bytes()).hexdigest(),
                 "dataset_sha256":hashlib.sha256((ROOT/"data"/"evaluation_cases.json").read_bytes()).hexdigest(),
                 "summary":summary,"records":records}
            Path(args.evidence).parent.mkdir(parents=True,exist_ok=True)
            Path(args.evidence).write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
            print(json.dumps(summary,indent=2));return 0 if not summary["failed"] else 1
    print(json.dumps(out,indent=2,ensure_ascii=False))
    return 0
if __name__=="__main__": sys.exit(main() or 0)
