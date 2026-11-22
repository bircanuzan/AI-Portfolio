"""Offline synthetic structured-output evaluation; no model or API calls."""
import json
import sqlite3
from pathlib import Path


def score(expected, output):
    try:
        value = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return {"valid_schema": False, "correct_intent": False}
    valid = (isinstance(value, dict) and set(value) == {"intent"}
             and value["intent"] in {"billing", "technical", "unknown"})
    return {"valid_schema": valid,
            "correct_intent": valid and value["intent"] == expected}


def check_splits(rows):
    seen_ids, seen_text = set(), {}
    for row in rows:
        if row["id"] in seen_ids:
            raise ValueError("Duplicate ID")
        seen_ids.add(row["id"])
        text = " ".join(row["text"].casefold().split())
        if not text:
            raise ValueError("Empty text")
        if text in seen_text and seen_text[text] != row["split"]:
            raise ValueError("Exact normalized text leakage across splits")
        seen_text[text] = row["split"]


def run(rows):
    check_splits(rows)
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE scores (id TEXT, valid INTEGER, correct INTEGER)")
    for row in rows:
        if row["split"] == "test":
            result = score(row["expected"], row["output"])
            db.execute("INSERT INTO scores VALUES (?, ?, ?)",
                       (row["id"], int(result["valid_schema"]),
                        int(result["correct_intent"])))
    count, valid, accuracy = db.execute(
        "SELECT COUNT(*), AVG(valid), AVG(correct) FROM scores").fetchone()
    db.close()
    if not count:
        raise ValueError("No held-out test rows")
    return {"status": "synthetic_fixture_only", "test_cases": count,
            "schema_validity": valid, "intent_accuracy": accuracy}


if __name__ == "__main__":
    rows = [json.loads(line) for line in
            Path(__file__).with_name("cases.jsonl").read_text().splitlines()]
    print(json.dumps(run(rows), indent=2))
