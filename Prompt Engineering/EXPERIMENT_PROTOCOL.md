# Real prompt experiments — pending

**Do not misrepresent** manually authored `demo_responses.json` as actual model transcripts.

For each case record: UTC timestamp; model/provider/version; prompt version and Git SHA; complete sanitized input and retrieved context; exact raw output; parsed decision; latency; tokens; tool calls; reviewer decision; error category; evidence link.

Run v1 and v2 on exactly the same test cases and model parameters. Calculate pass rates by category and identify regressions. Independent reviewers check truthfulness and policy grounding; lexical keyword checks alone are insufficient. Incident-level blocking for private data leaks, unsafe tool actions and fabricated policy. Add held-out real-world (consented, redacted) examples once available.

Failure labels: hallucinated policy; missing citation; privacy; tool authorization; escalation; formatting; injection; tone. Store observed failures as fixtures without rewriting the ground truth to increase scores.

| Case | Version | Model / run date | Expected | Exact actual response | Grade | Defect | Evidence |
|---|---|---|---|---|---|---|---|
| E01 | v1 | not run | answer with source | pending | pending | pending | pending |
