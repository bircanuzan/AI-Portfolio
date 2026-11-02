"""Reproduce the Project 56 20-case deterministic HR policy evaluation."""
import argparse
import json
from pathlib import Path

from policy_assistant import respond

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "20_question_benchmark.json"

def evaluate(cases):
    output = []
    for case in cases:
        answer = respond(case["prompt"])
        ok = (answer["route"] == case["expected_route"]
              and answer["policy_id"] == case["expected_policy"])
        output.append({
            "case_id": case["id"], "exact_prompt": case["prompt"],
            "expected_route": case["expected_route"],
            "expected_policy": case["expected_policy"],
            "actual_route": answer["route"],
            "actual_policy": answer["policy_id"],
            "actual_answer": answer["answer"], "citation": answer["citation"],
            "needs_human": answer["needs_human"], "pass": ok
        })
    return {
        "case_count": len(output), "passed": sum(c["pass"] for c in output),
        "failed": sum(not c["pass"] for c in output),
        "pass_rate_percent": round(100 * sum(c["pass"] for c in output) / len(output), 1) if output else None,
        "limitations": "Fictional offline rules. Not LLM accuracy or actual HR policy compliance.",
        "cases": output
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="", help="Write evaluation JSON to file")
    args = parser.parse_args()
    cases = json.loads(DATA.read_text(encoding="utf-8"))["cases"]
    result = evaluate(cases)
    print(f"Matched {result['passed']}/{result['case_count']} "
          f"({result['pass_rate_percent']}%). Known gaps are retained.")
    for case in result["cases"]:
        print(f"{case['case_id']}: {'PASS' if case['pass'] else 'FAIL'} "
              f"expected={case['expected_route']}/{case['expected_policy']} "
              f"actual={case['actual_route']}/{case['actual_policy']}")
    if args.out:
        Path(args.out).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
