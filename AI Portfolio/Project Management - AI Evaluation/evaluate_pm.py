"""Project Management - AI Evaluation: reproducible synthetic benchmark.

No LLM calls, private data, third-party dependencies, or client performance claims.
The script builds a reference from each scenario's *inputs*, then checks two
manually authored candidate answers. Do not report fixture scores as AI quality.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent


def load_cases(path: Path) -> list[dict]:
    rows = []
    seen = set()
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        item = json.loads(line)
        required = {"id", "domain", "method", "requirement", "scenario", "inputs",
                    "reference_explanation", "good_answer", "flawed_answer", "error_tags"}
        if not isinstance(item, dict) or not required.issubset(item):
            raise ValueError(f"Case line {line_number} has missing fields")
        if item["id"] in seen:
            raise ValueError(f"Duplicate id: {item['id']}")
        seen.add(item["id"])
        rows.append(item)
    if not rows:
        raise ValueError("No cases found")
    return rows


def critical_path(tasks: list[dict]) -> dict:
    by_id = {x["id"]: x for x in tasks}
    if len(by_id) != len(tasks):
        raise ValueError("Duplicate task ids")
    finished = {}
    routes = {}
    remaining = set(by_id)
    while remaining:
        progressed = False
        for name in sorted(tuple(remaining)):
            task = by_id[name]
            duration = task["duration_days"]
            deps = task["depends_on"]
            if not isinstance(duration, (int, float)) or duration < 0:
                raise ValueError("Invalid duration")
            if any(d not in by_id for d in deps):
                raise ValueError("Missing dependency")
            if all(d in finished for d in deps):
                parent = max(deps, key=lambda d: (finished[d], d)) if deps else None
                finished[name] = duration + (finished[parent] if parent else 0)
                routes[name] = (routes[parent] if parent else []) + [name]
                remaining.remove(name)
                progressed = True
        if not progressed:
            raise ValueError("Cyclic project dependencies")
    ending = max(finished, key=lambda k: (finished[k], k))
    return {"duration_days": finished[ending], "critical_path": routes[ending]}


def compute_reference(item: dict) -> dict:
    method = item["method"]
    d = item["inputs"]
    if method == "critical_path":
        return critical_path(d["tasks"])
    if method == "earned_value":
        ev, ac, pv, bac = (float(d[k]) for k in ("ev", "ac", "pv", "bac"))
        if ac <= 0 or pv <= 0 or ev <= 0 or bac <= 0:
            raise ValueError("All EVM input denominators must be > 0")
        cpi = ev / ac
        spi = ev / pv
        return {"cpi": cpi, "spi": spi, "eac": bac / cpi,
                "over_budget": cpi < 1, "behind_schedule": spi < 1}
    if method == "resource_capacity":
        available, required = (sum(d[k]) for k in ("available_hours", "planned_hours"))
        if available < 0 or required < 0:
            raise ValueError("Hours must be nonnegative")
        return {"available_hours": available, "required_hours": required,
                "capacity_gap_hours": max(0, required - available),
                "is_feasible": required <= available}
    if method == "expected_monetary_value":
        aggregate = 0.0
        for r in d["risks"]:
            probability = float(r["probability"])
            impact = float(r["impact_aed"])
            if not 0 <= probability <= 1 or impact < 0:
                raise ValueError("Invalid risk probability or impact")
            aggregate += probability * impact
        return {"aggregate_emv_aed": aggregate}
    if method == "sprint_overcommitment":
        velocity, planned = (float(d[k]) for k in ("velocity_points", "planned_points"))
        if velocity < 0 or planned < 0:
            raise ValueError("Velocity and workload must be nonnegative")
        return {"overcommitment_points": max(0, planned - velocity),
                "replan_required": planned > velocity}
    if method == "change_control":
        if d["scope_increase_pct"] <= 0:
            raise ValueError("Example expects a positive scope increase")
        # Do not treat an unapproved change as a new baseline.
        approved = bool(d["approval_granted"])
        return {"log_change_request": True, "impact_assessment_required": True,
                "approve_immediately": False, "update_baseline_now": approved}
    raise ValueError(f"Unsupported method: {method}")


def compare_answer(reference: dict, candidate: dict) -> dict:
    if not isinstance(candidate, dict):
        raise ValueError("Candidate must be a JSON object")
    field_results = {}
    for field, expected in reference.items():
        actual = candidate.get(field)
        if type(expected) is bool:
            good = type(actual) is bool and actual == expected
        elif isinstance(expected, (int, float)):
            good = type(actual) in (int, float) and math.isclose(
                actual, expected, abs_tol=0.0001, rel_tol=1e-8
            )
        else:
            good = actual == expected
        field_results[field] = {"correct": good, "expected": expected, "actual": actual}
    unexpected = sorted(set(candidate) - set(reference))
    correctness = sum(v["correct"] for v in field_results.values())
    return {"correct_fields": correctness, "total_fields": len(reference),
            "field_accuracy": round(correctness / len(reference), 4),
            "strict_schema": not unexpected and set(reference) == set(candidate),
            "field_checks": field_results, "unexpected_fields": unexpected}


def run_evaluation(cases: list[dict]) -> dict:
    scored = []
    for item in cases:
        reference = compute_reference(item)
        scored.append({
            "id": item["id"], "domain": item["domain"], "method": item["method"],
            "reference_from_inputs": reference,
            "authored_good_candidate": compare_answer(reference, item["good_answer"]),
            "authored_flawed_candidate": compare_answer(reference, item["flawed_answer"]),
            "review_rationale": item["reference_explanation"],
            "error_tags": item["error_tags"],
        })
    return {
        "evidence_level": "synthetic fixtures only; not an LLM benchmark run",
        "case_count": len(scored),
        "perfect_good_fixtures": sum(r["authored_good_candidate"]["field_accuracy"] == 1
                                     for r in scored),
        "flawed_fixtures_with_error_detected": sum(r["authored_flawed_candidate"]["field_accuracy"] < 1
                                                    for r in scored),
        "scenarios": scored,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", default=str(ROOT / "data/cases.jsonl"))
    parser.add_argument("--output", default=str(ROOT / "results/synthetic_fixture_report.json"))
    args = parser.parse_args()
    report = run_evaluation(load_cases(Path(args.cases)))
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("Synthetic PM benchmark cases:", report["case_count"])
    print("Gold fixture cases with all expected fields correct:", report["perfect_good_fixtures"])
    print("Deliberately flawed fixtures flagged:", report["flawed_fixtures_with_error_detected"])
    print("Report:", out)
    print("These are fixture unit checks, NOT AI model accuracy metrics.")


if __name__ == "__main__":
    main()
