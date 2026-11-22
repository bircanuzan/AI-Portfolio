"""Synthetic training-data audit: label QA, duplicates, split leakage, privacy markers."""
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

rows = [json.loads(s) for s in Path(__file__).with_name("cases.jsonl").read_text().splitlines() if s.strip()]
valid_labels = {"billing", "technical", "unknown"}
by_id = defaultdict(list)
by_text = defaultdict(list)
flags = []
for r in rows:
    rid, split, label, msg = (r[k] for k in ("id","split","label","message"))
    if not all(isinstance(x, str) and x.strip() for x in (rid, split, label, msg)):
        flags.append({"id": str(rid), "issue": "invalid field"})
        continue
    by_id[rid].append(split)
    by_text[" ".join(msg.casefold().split())].append((rid, split))
    if label not in valid_labels:
        flags.append({"id": rid, "issue": "invalid label"})
    if split not in ("train", "validation", "test"):
        flags.append({"id": rid, "issue": "invalid split"})
    if re.search(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b", msg):
        flags.append({"id": rid, "issue": "possible email address; requires privacy review"})
for rid, splits in by_id.items():
    if len(splits) > 1:
        flags.append({"id": rid, "issue": "duplicate identifier"})
for norm, instances in by_text.items():
    if len(instances) > 1:
        issue = "cross-split exact text leakage" if len({split for _,split in instances}) > 1 else "duplicate text"
        flags.append({"id": ",".join(rid for rid,_ in instances), "issue": issue})
print(json.dumps({"source": "synthetic QA fixtures (intentional defects)",
                  "row_count": len(rows), "label_distribution": dict(Counter(r["label"] for r in rows)),
                  "quarantine_review_queue": flags,
                  "note": "Heuristic only, not complete PII detection"}, indent=2))
