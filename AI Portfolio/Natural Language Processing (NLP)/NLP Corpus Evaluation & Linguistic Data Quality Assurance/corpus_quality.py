"""Synthetic multilingual corpus QA demo (Python standard library only)."""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
import json
import random
import re
import unicodedata
from pathlib import Path

REQUIRED = ("id", "language", "domain", "register", "source", "text", "annotations", "entities")
EMAIL = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
PHONE = re.compile(r"(?<!\d)(?:\+?\d[ -]?){9,15}(?!\d)")
ALLOWED_LANGUAGES = {"en", "tr"}

def normalized_text(value: str) -> str:
    """Normalize compatibility characters and whitespace for duplicate detection."""
    return " ".join(unicodedata.normalize("NFKC", value).casefold().split())

def cohen_kappa(pairs: list[tuple[str, str]]) -> float | None:
    """Return two-rater nominal Cohen's kappa; None for empty/undefined data."""
    if not pairs:
        return None
    n = len(pairs)
    observed = sum(a == b for a, b in pairs) / n
    counts_a, counts_b = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    expected = sum((counts_a[label] / n) * (counts_b[label] / n)
                   for label in counts_a.keys() | counts_b.keys())
    return round((observed - expected) / (1 - expected), 4) if expected < 1 else (1.0 if observed == 1 else None)

def inspect_corpus(rows: list[dict]) -> dict:
    issues, seen, language_counts, domain_counts, register_counts, pairs = [], {}, Counter(), Counter(), Counter(), []
    def flag(record_id: str, severity: str, code: str, detail: str):
        issues.append({"record_id": record_id, "severity": severity, "code": code, "detail": detail})
    for index, row in enumerate(rows):
        rid = str(row.get("id", f"row-{index+1}"))
        for key in REQUIRED:
            if key not in row:
                flag(rid, "blocker", "missing_field", f"Missing required field: {key}")
        text = row.get("text", "")
        if not isinstance(text, str) or not text.strip():
            flag(rid, "blocker", "empty_text", "Text missing or empty")
            text = ""
        language = row.get("language", "unspecified")
        language_counts[str(language)] += 1
        domain_counts[str(row.get("domain", "unspecified"))] += 1
        register_counts[str(row.get("register", "unspecified"))] += 1
        if language not in ALLOWED_LANGUAGES:
            flag(rid, "review", "unrecognized_language", "Language outside declared English/Turkish scope")
        if "\ufffd" in text or any(ord(ch) < 32 and ch not in "\t\n\r" for ch in text):
            flag(rid, "blocker", "encoding_or_control_character", "Unicode replacement or control character present")
        key = normalized_text(text)
        if key and key in seen:
            flag(rid, "review", "duplicate_text", f"Same normalized text as {seen[key]}")
        elif key:
            seen[key] = rid
        if EMAIL.search(text) or PHONE.search(text):
            flag(rid, "review", "potential_personal_data", "Potential contact information; requires privacy review")
        ann = row.get("annotations")
        if isinstance(ann, dict) and isinstance(ann.get("a"), str) and isinstance(ann.get("b"), str):
            pairs.append((ann["a"], ann["b"]))
            if ann["a"] != ann["b"]:
                flag(rid, "review", "annotator_disagreement", "Rater labels disagree; adjudication required")
        else:
            flag(rid, "blocker", "invalid_annotation", "Two nonempty string rater labels required")
        entities = row.get("entities", [])
        if not isinstance(entities, list):
            flag(rid, "blocker", "invalid_entities", "Entities must be a list")
        else:
            for j, entity in enumerate(entities):
                if not isinstance(entity, dict) or not isinstance(entity.get("start"), int) or not isinstance(entity.get("end"), int) or not isinstance(entity.get("label"), str) or not 0 <= entity["start"] < entity["end"] <= len(text):
                    flag(rid, "blocker", "invalid_entity_offset", f"Entity {j}: offset/label invalid")
    blockers = {x["record_id"] for x in issues if x["severity"] == "blocker"}
    flagged = {x["record_id"] for x in issues}
    counts = Counter(x["code"] for x in issues)
    return {
        "dataset_type": "synthetic demonstration",
        "records": len(rows),
        "languages": dict(language_counts),
        "domains": dict(domain_counts),
        "registers": dict(register_counts),
        "qa_clean_record_rate": round((len(rows) - len(flagged)) / len(rows), 4) if rows else None,
        "blocking_record_rate": round(len(blockers) / len(rows), 4) if rows else None,
        "inter_annotator_agreement": round(sum(a == b for a, b in pairs) / len(pairs), 4) if pairs else None,
        "cohen_kappa": cohen_kappa(pairs),
        "issues_by_code": dict(counts),
        "issues": issues,
        "release_decision": "HOLD_FOR_REVIEW" if issues else "PASS_AUTOMATED_QA",
        "note": "Automated checks are illustrative. Human linguists must adjudicate semantics, fairness and representativeness."
    }

def stratified_sample(rows: list[dict], per_language: int = 2, seed: int = 42) -> list[dict]:
    """Deterministic quota sampling; exploratory, not population-representative."""
    if per_language < 1:
        raise ValueError("per_language must be >= 1")
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get("language", "unspecified"))].append(row)
    rng = random.Random(seed)
    return [item for lang in sorted(grouped) for item in rng.sample(grouped[lang], min(per_language, len(grouped[lang])))]

def main() -> None:
    parser = argparse.ArgumentParser(description="Multilingual synthetic corpus QA")
    parser.add_argument("--input", default=str(Path(__file__).resolve().parent / "data" / "synthetic_corpus.jsonl"))
    parser.add_argument("--output", default="")
    parser.add_argument("--sample-per-language", type=int, default=2)
    args = parser.parse_args()
    with open(args.input, encoding="utf-8") as stream:
        rows = [json.loads(line) for line in stream if line.strip()]
    result = inspect_corpus(rows)
    result["sampling"] = {"strategy": "deterministic per-language quota; not representative",
                           "seed": 42, "sampled_ids": [x["id"] for x in stratified_sample(rows, args.sample_per_language)]}
    report = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        Path(args.output).write_text(report, encoding="utf-8")
    else:
        print(report, end="")

if __name__ == "__main__":
    main()
