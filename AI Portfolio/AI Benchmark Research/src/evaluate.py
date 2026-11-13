#!/usr/bin/env python3
"""Offline benchmark authoring QA and synthetic/live run scoring.

Standard library only. The evaluator scores *final answers* and authorized
observable tool/citation records; it cannot inspect private reasoning.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import urlsplit, urlunsplit


ABSTENTIONS = {
    "", "i don't know", "i do not know", "unknown", "not attempted",
    "cannot determine", "unable to determine", "no answer",
}


def normalize_answer(value: object) -> str:
    """Normalize presentation only; do not invent semantic equivalences."""
    text = unicodedata.normalize("NFKC", str(value if value is not None else ""))
    return re.sub(r"\s+", " ", text).strip().casefold()


def canonical_url(url: str) -> str:
    """Normalize scheme/host/cosmetic suffix, without changing a URL's path."""
    parsed = urlsplit(url.strip())
    return urlunsplit(
        (parsed.scheme.lower(), parsed.netloc.lower(),
         parsed.path.rstrip("/"), "", "")
    )


def load_jsonl(path: str | Path) -> list[dict]:
    records = []
    with Path(path).open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: bad JSON: {exc}") from exc
            if not isinstance(item, dict):
                raise ValueError(f"{path}:{line_number}: expected JSON object")
            records.append(item)
    return records


def validate_tasks(tasks: list[dict]) -> None:
    """Reject schema gaps before scoring; research validity requires human review."""
    if not tasks:
        raise ValueError("Benchmark dataset must not be empty")
    seen = set()
    for task in tasks:
        ident = task.get("id")
        if not isinstance(ident, str) or not ident.strip():
            raise ValueError("Every task needs a nonempty string id")
        if ident in seen:
            raise ValueError(f"Duplicate task id: {ident}")
        seen.add(ident)
        if not isinstance(task.get("question"), str) or not task["question"].strip():
            raise ValueError(f"{ident}: missing question")
        if not isinstance(task.get("answer"), str) or not task["answer"].strip():
            raise ValueError(f"{ident}: missing canonical answer")
        accepted = task.get("accepted_answers")
        if not isinstance(accepted, list) or not accepted or not all(
            isinstance(a, str) and a.strip() for a in accepted
        ):
            raise ValueError(f"{ident}: nonempty accepted_answers list required")
        if normalize_answer(task["answer"]) not in {
            normalize_answer(a) for a in accepted
        }:
            raise ValueError(f"{ident}: canonical answer missing from aliases")
        sources = task.get("sources")
        if not isinstance(sources, list) or not sources:
            raise ValueError(f"{ident}: at least one primary/credible source required")
        for source in sources:
            if not isinstance(source, dict) or not isinstance(source.get("url"), str):
                raise ValueError(f"{ident}: invalid source record")
            parsed = urlsplit(source["url"])
            if parsed.scheme != "https" or not parsed.netloc:
                raise ValueError(f"{ident}: source needs absolute HTTPS URL")


def grade_run(task: dict, run: dict) -> dict:
    """Tag answer correctness and observable provenance gaps.

    Failure tags are *heuristic triage*, not proof of a model's internal cause.
    """
    answer = normalize_answer(run.get("prediction", ""))
    aliases = {normalize_answer(x) for x in task["accepted_answers"]}
    if answer in ABSTENTIONS:
        verdict = "not_attempted"
    elif answer in aliases:
        verdict = "correct"
    else:
        verdict = "incorrect"

    official = {canonical_url(s["url"]) for s in task["sources"]}
    cited = {
        canonical_url(u) for u in run.get("sources_used", [])
        if isinstance(u, str)
    }
    events = run.get("events", [])
    if not isinstance(events, list):
        raise ValueError("events must be a list")
    retrieved_official = any(
        isinstance(event, dict)
        and event.get("type") == "retrieve"
        and isinstance(event.get("url"), str)
        and canonical_url(event["url"]) in official
        for event in events
    )
    cited_official = bool(cited & official)

    if verdict == "not_attempted":
        diagnosis = "abstention"
    elif verdict == "correct":
        diagnosis = "no_answer_error"
    elif retrieved_official:
        diagnosis = "reasoning_or_extraction_error"
    elif cited_official:
        diagnosis = "answer_source_mismatch"
    else:
        diagnosis = "missing_primary_source"

    return {
        "run_id": run.get("run_id"),
        "task_id": task["id"],
        "mode": run.get("mode", "unspecified"),
        "verdict": verdict,
        "diagnosis": diagnosis,
        "cited_primary_source": cited_official,
        "retrieved_primary_source": retrieved_official,
        "uncited_correct_answer": verdict == "correct" and not cited_official,
        "review_required": verdict == "incorrect",
    }


def evaluate(tasks: list[dict], runs: list[dict]) -> dict:
    validate_tasks(tasks)
    by_id = {t["id"]: t for t in tasks}
    records = []
    seen_runs = set()
    for run in runs:
        ident = run.get("run_id")
        if not isinstance(ident, str) or not ident or ident in seen_runs:
            raise ValueError("run_id must be present and unique")
        seen_runs.add(ident)
        task_id = run.get("task_id")
        if task_id not in by_id:
            raise ValueError(f"Unknown task_id in run {ident}: {task_id}")
        if run.get("mode") not in {"synthetic", "live"}:
            raise ValueError(f"{ident}: mode must be synthetic or live")
        records.append(grade_run(by_id[task_id], run))

    return {
        "task_count": len(tasks),
        "run_count": len(records),
        "verdict_counts": dict(Counter(r["verdict"] for r in records)),
        "diagnosis_counts": dict(Counter(r["diagnosis"] for r in records)),
        "run_mode_counts": dict(Counter(r["mode"] for r in records)),
        "records": records,
        "disclaimer": (
            "Source/trace tags are heuristic; simulated runs are not live model "
            "measurements. Neither task difficulty nor model failure is established "
            "without independent validity review and controlled testing."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tasks", required=True, help="Verified benchmark JSONL")
    parser.add_argument("--runs", required=True, help="Run record JSONL")
    parser.add_argument("--output", help="Optional JSON output file")
    args = parser.parse_args()
    report = evaluate(load_jsonl(args.tasks), load_jsonl(args.runs))
    payload = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        Path(args.output).write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
