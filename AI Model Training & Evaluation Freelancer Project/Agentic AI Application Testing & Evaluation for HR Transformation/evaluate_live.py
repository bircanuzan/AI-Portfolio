"""Run real OpenAI LLM evaluations only when invoked explicitly; API usage may cost money."""
from __future__ import annotations
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from evaluate import CASES
from live_llm_agent import run_live

def main():
    parser = argparse.ArgumentParser(description="Real LLM evaluation: each model case can incur API costs")
    parser.add_argument("--limit", type=int, default=4, help="Number of first cases (default 4, max 16)")
    parser.add_argument("--all", action="store_true", help="Run all 16 synthetic cases")
    args = parser.parse_args()
    if args.limit <= 0:
        parser.error("--limit must be positive")
    cases = CASES if args.all else CASES[:min(args.limit, len(CASES))]
    rows = []
    for cid, question, expected, policy_id in cases:
        try:
            record = run_live(question)
            passed = (record.outcome == expected and (policy_id is None or policy_id in record.policy_ids))
            rows.append({"case_id": cid, "expected_outcome": expected, "expected_policy_id": policy_id,
                         "passed": passed, "actual": record.to_dict()})
            print(f"{cid}: {'PASS' if passed else 'FAIL'} / {record.outcome} / model_called={record.model_called}")
        except Exception as exc:
            rows.append({"case_id": cid, "expected_outcome": expected, "passed": False,
                         "error_type": type(exc).__name__, "error": str(exc)})
            print(f"{cid}: ERROR ({type(exc).__name__})")
            if isinstance(exc, (RuntimeError, ImportError)):
                break
    total = len(rows)
    payload = {"timestamp_utc": datetime.now(timezone.utc).isoformat(),
               "mode": "LIVE_OPENAI_API_OR_PREFLIGHT", "synthetic_data": True,
               "model_backed_cases": sum(bool(row.get("actual", {}).get("model_called")) for row in rows),
               "evaluated_cases": total, "passed": sum(row["passed"] for row in rows), "cases": rows}
    out = Path(__file__).resolve().parent / "evidence" / "live_evaluation_results.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Saved {out} — {payload['passed']}/{total} passed")
    raise SystemExit(0 if total == len(cases) and payload["passed"] == total else 1)

if __name__ == "__main__":
    main()
