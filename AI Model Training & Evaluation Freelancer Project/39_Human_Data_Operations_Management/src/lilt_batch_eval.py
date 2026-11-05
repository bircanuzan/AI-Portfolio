"""Local SQL-based metrics for fictional multilingual preference labels; not model training."""
import json
import sqlite3
from pathlib import Path

LABELS = {"A", "B", "TIE"}
LANGUAGES = {"en", "tr", "fr"}

def summarize(records):
    if not isinstance(records, list) or not records:
        raise ValueError("nonempty list required")
    seen = set()
    for r in records:
        if not isinstance(r, dict) or not isinstance(r.get("id"), str) or not r["id"].strip():
            raise ValueError("invalid item id")
        if r["id"] in seen:
            raise ValueError("duplicate id")
        seen.add(r["id"])
        if r.get("language") not in LANGUAGES or r.get("modality") != "text":
            raise ValueError("unsupported synthetic locale or modality")
        if any(r.get(k) not in LABELS for k in ("reviewer_a", "reviewer_b", "gold")):
            raise ValueError("invalid preference label")
        if any(type(r.get(k)) not in (int, float) or r[k] <= 0 for k in ("minutes", "cost_usd")):
            raise ValueError("invalid time or cost")
    db = sqlite3.connect(":memory:")
    try:
        db.execute("CREATE TABLE reviews (id TEXT PRIMARY KEY, language TEXT, a TEXT, b TEXT, gold TEXT, minutes REAL, cost REAL)")
        db.executemany("INSERT INTO reviews VALUES (?,?,?,?,?,?,?)",
                       [(r["id"], r["language"], r["reviewer_a"], r["reviewer_b"],
                         r["gold"], r["minutes"], r["cost_usd"]) for r in records])
        n, paired, ag, bg, mins, cost = db.execute(
            "SELECT COUNT(*), SUM(a=b), SUM(a=gold), SUM(b=gold), SUM(minutes), SUM(cost) FROM reviews").fetchone()
        locales = {lang: {"tasks": nlang, "agreement": round(agree / nlang, 3)}
                   for lang, nlang, agree in db.execute(
                       "SELECT language, COUNT(*), SUM(a=b) FROM reviews GROUP BY language ORDER BY language")}
        quality = {"paired_agreement": round(paired/n, 3),
                   "reviewer_a_gold_accuracy": round(ag/n, 3),
                   "reviewer_b_gold_accuracy": round(bg/n, 3)}
        report = {"source": "synthetic_not_LILT", "total_tasks": n, "metrics": quality,
                  "throughput_tasks_per_hour": round(n/(mins/60), 2),
                  "average_cost_usd_per_task": round(cost/n, 2),
                  "by_language": locales, "decision": "PASS" if min(quality.values()) >= 0.9 else "HOLD"}
        # Operational gate: independent 80% IAA and 90% reviewer gold; no external release.
        report["decision"] = ("PASS" if quality["paired_agreement"] >= .8 and
            quality["reviewer_a_gold_accuracy"] >= .9 and
            quality["reviewer_b_gold_accuracy"] >= .9 else "HOLD")
        return report
    finally:
        db.close()

if __name__ == "__main__":
    path = Path(__file__).resolve().parents[1]/"data"/"lilt_synthetic_preference_batch.json"
    print(json.dumps(summarize(json.loads(path.read_text(encoding="utf-8"))), indent=2))
