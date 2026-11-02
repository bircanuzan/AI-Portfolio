"""Synthetic HR AI policy assurance dashboard. Python standard library only.

Not a live AI evaluation, real legal source monitor or fairness assessment.
Run from any current working directory: python src/assurance_dashboard.py
"""
from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_csv(filename: str) -> list[dict[str, str]]:
    with (ROOT / "data" / filename).open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def evaluate() -> tuple[list[dict[str, object]], dict[str, object]]:
    """Compare mock answers to the current fictional approved source version."""
    sources = read_csv("source_versions.csv")
    current = {s["source_id"]: s["version"] for s in sources if s["status"] == "active"}
    tests = read_csv("test_cases.csv")
    results = []
    for test in tests:
        active = current.get(test["source_id"])
        current_version = bool(active and test["observed_version"] == active)
        evidence_complete = bool(
            active
            and test["evidence_ref"] == f"{test['source_id']}-{active}"
            and test["source_verified"].lower() == "true"
        )
        correct_answer = test["observed_answer"] == test["expected_answer"]
        passed = current_version and evidence_complete and correct_answer
        results.append({
            "id": test["test_id"],
            "risk": test["risk_theme"],
            "fresh": current_version,
            "evidence": evidence_complete,
            "citation_present": bool(test["evidence_ref"]),
            "answer": correct_answer,
            "pass": passed,
            "critical": test["critical"].lower() == "true",
        })
    count = len(results)
    if not count:
        raise ValueError("No tests; cannot create scorecard.")
    critical_failures = sum(1 for x in results if x["critical"] and not x["pass"])
    failures = sum(1 for x in results if not x["pass"])
    summary = {
        "total": count,
        "fresh": sum(1 for x in results if x["fresh"]),
        "evidence": sum(1 for x in results if x["evidence"]),
        "citation_present": sum(1 for x in results if x["citation_present"]),
        "correct": sum(1 for x in results if x["answer"]),
        "passed": count - failures,
        "failures": failures,
        "critical_failures": critical_failures,
        "decision": "HOLD" if critical_failures else ("REVIEW" if failures else "CANDIDATE_FOR_APPROVAL"),
    }
    return results, summary


def render_dashboard(results: list[dict[str, object]], summary: dict[str, object]) -> str:
    total = int(summary["total"])
    rate = lambda number: f"{100 * int(number) / total:.1f}%"
    lines = [
        "# AI Assurance Evidence Dashboard — Simulated",
        "",
        "> Educational mock responses only. No live LLM, legal content, real assurance audit, or fairness claim.",
        "",
        f"**Release recommendation: {summary['decision']}** (synthetic critical-risk gate; human approval still required).",
        "",
        "| Metric | Mock cases | Share |",
        "|---|---:|---:|",
        f"| Source version current | {summary['fresh']}/{total} | {rate(summary['fresh'])} |",
        f"| Any citation supplied | {summary['citation_present']}/{total} | {rate(summary['citation_present'])} |",
        f"| Verified current-source evidence | {summary['evidence']}/{total} | {rate(summary['evidence'])} |",
        f"| Exact expected-answer match | {summary['correct']}/{total} | {rate(summary['correct'])} |",
        f"| All checks passed | {summary['passed']}/{total} | {rate(summary['passed'])} |",
        f"| Exceptions | {summary['failures']} | — |",
        f"| Critical exceptions | {summary['critical_failures']} | — |",
        "",
        "## Test-by-test record",
        "| Test | Theme | Source fresh? | Evidence? | Answer correct? | Result |",
        "|---|---|---|---|---|---|",
    ]
    for r in results:
        yesno = lambda b: "Yes" if b else "No"
        lines.append(
            f"| {r['id']} | {r['risk']} | {yesno(r['fresh'])} | "
            f"{yesno(r['evidence'])} | {yesno(r['answer'])} | "
            f"{'PASS' if r['pass'] else 'FAIL'} |"
        )
    lines += [
        "",
        "## Interpretation and limitations",
        "- A source notification is not equivalent to approved change implementation.",
        "- A correct-looking answer without current evidence is an exception.",
        "- A small synthetic sample cannot demonstrate real-world accuracy, reliability, demographic fairness, security or regulatory compliance.",
        "- These percentages are descriptive of mock fixtures only. A real release gate needs risk-based thresholds, representative samples, qualified experts and independent review.",
        "- The HOLD recommendation is a demonstration of a proposed governance control, not an automated production blocker.",
        "",
        "Generated using stdlib Python, data/source_versions.csv and data/test_cases.csv.",
        "",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    results, summary = evaluate()
    output = ROOT / "reports" / "dashboard.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_dashboard(results, summary), encoding="utf-8")
    print(f"{summary['decision']}: {summary['passed']}/{summary['total']} mock tests passed; wrote {output}")
