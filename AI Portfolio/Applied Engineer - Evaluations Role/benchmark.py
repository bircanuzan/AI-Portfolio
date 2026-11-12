"""CLI: python benchmark.py --out artifacts/benchmark-results.json"""
import argparse
import json
from pathlib import Path
from src.candidate_agents import CANDIDATES
from src.eval_engine import run_benchmark

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="artifacts/benchmark-results.json")
    args = parser.parse_args()
    cases = json.loads((ROOT / "evaluation_cases.json").read_text(encoding="utf-8"))
    rubric = json.loads((ROOT / "rubric.json").read_text(encoding="utf-8"))
    results = run_benchmark(CANDIDATES, cases, rubric)
    payload = {"project": "Applied Engineer - Evaluations Role",
               "kind": "synthetic-executable-candidate-benchmark",
               "disclaimer": "No third-party or frontier LLM models were evaluated.",
               "rubric_id": rubric["rubric_id"], "results": results}
    destination = (ROOT / args.out).resolve()
    if not destination.is_relative_to(ROOT):
        raise ValueError("output file must be inside project directory")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for result in results:
        print(f'{result["candidate"]}: {result["passed"]}/{result["total"]} cases, weighted score {result["score"]}/100')
    baseline = next(result for result in results if result["candidate"] == "synthetic-reference-patch")
    if baseline["passed"] != baseline["total"]:
        raise SystemExit("Reference patch regression detected")


if __name__ == "__main__":
    main()
