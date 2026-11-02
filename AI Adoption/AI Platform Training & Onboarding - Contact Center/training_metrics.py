"""Calculate a fictional onboarding cohort training report; Python standard library only."""
from pathlib import Path
import csv
from statistics import mean

with Path(__file__).with_name("synthetic_training_tracker.csv").open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
done = [r for r in rows if r["completed"] == "1"]
weights = {"navigation_score": .15, "prompt_score": .20, "visual_score": .20,
           "privacy_score": .20, "troubleshooting_score": .15, "communication_score": .10}
def weighted(r):
    return sum(float(r[k]) * w for k, w in weights.items())
ready = [r for r in done if weighted(r) >= 3 and float(r["privacy_score"]) >= 3]
blockers = [r["blocker"] for r in rows if r["blocker"].strip()]
feedback = [float(r["feedback_1to5"]) for r in done if r["feedback_1to5"].strip()]
print("DEMO DATA ONLY — not Concentrix or real agent scores")
print(f"Completion: {len(done)} of {len(rows)} ({len(done)/len(rows):.0%})")
print(f"Ready for supervised release: {len(ready)} of {len(done)} ({len(ready)/len(done):.0%})")
print(f"Average feedback 1–5: {mean(feedback):.2f}" if feedback else "No feedback")
print("Open blockers:", "; ".join(blockers) if blockers else "none")
for r in done:
    computed = weighted(r)
    print(f"{r['agent_id']}: {computed:.2f}/4, {'READY' if r in ready else 'REMEDIATION REQUIRED'}")
