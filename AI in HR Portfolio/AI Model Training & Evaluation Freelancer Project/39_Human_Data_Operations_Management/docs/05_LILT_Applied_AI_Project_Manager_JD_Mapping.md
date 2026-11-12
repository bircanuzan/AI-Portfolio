# LILT — Project Manager, Applied AI | Multilingual LLM Data Operations extension

**Source:** https://jobs.ashbyhq.com/lilt-production/61cb6b83-e9c2-41c8-9097-c8246b40b81f
**Location/employment:** remote United Arab Emirates; contract (checked 2 November 2026).
**Published requirement:** 3–5+ years of project management **specifically within AI/ML data operations**, plus strong LLM data/evaluation knowledge, Excel/Sheets, SQL, Agile methods and documentation quality. This portfolio example does **not** substitute for that work experience.
**Integrity:** fabricated preference labels, fictional annotators and synthetic quality data. No LILT dataset, client program, Scale AI/SuperAnnotate integration or real LLM calls.

## Direct JD-to-artifact traceability

| JD responsibility / tool | Artifact and skill | Current evidence level |
| --- | --- | --- |
| Scope multilingual AI data projects | Existing operating model + synthetic batch spec | Operating-model exercise |
| Build and monitor text/audio/image data pipelines | Batch intake schema, modality, language, provenance/consent and validation checkpoints | Synthetic text-preference sample; audio and image future |
| RLHF / SFT / ranking / safety testing | Label taxonomy, synthetic preference annotation and red-team exceptions; note pre-training vs SFT vs RLHF conceptual distinction | **No actual model training or fine-tuning** |
| Quality: inter-annotator agreement and gold-set performance | `src/lilt_batch_eval.py`, `data/lilt_synthetic_preference_batch.json` and tests | Reproducible deterministic evaluation |
| Throughput and cost per task | SQL-backed batch calculation in `src/lilt_batch_eval.py` | Demonstration of SQL analytics on synthetic data |
| QA loops/root-cause/corrective training | Release HOLD gate, disagreement analysis and adjudication SOP | Written controls and test fixtures |
| Dashboards and bottlenecks | JSON KPIs, by-language breakdown, optional Excel/Power BI visualization | No connected BI dashboard claimed |
| Annotator operations and SLA | RACI, task ownership, calibration, decision clock | Planned operating control |
| Cross-functional engineering collaboration | Escalation to technical operations, QA sign-off, change-control loop | Proposed cadence, not a real team |
| Jira, Scale AI, SuperAnnotate | Desirable third-party tools | Not used or claimed |
| SQL and Excel/Sheets | SQLite aggregation queries and data export-friendly JSON | Local SQL demo; spreadsheet-ready schema |
| Multilingual guidance | English/Turkish plus French synthetic cases; language-specific review policy | User's languages apply to communication; not translation credential |
| Agile/Scrum/Kanban | Weekly planning, WIP limits, delivery review, retrospectives | Operating-model template |

## Task and annotation schema
Each synthetic record contains `id`, `language`, `modality`, `reviewer_a`, `reviewer_b`, `gold`, `minutes`, `cost_usd`. Labels are `A`, `B`, or `TIE`: preference judgments between two imaginary outputs. These fields are **not** production RLHF rewards and cannot be used to infer a model improved.

## Quality gates & escalation (proposed)
1. Reject missing IDs, invalid labels, repeated identifiers, negative duration/cost and unknown languages.
2. Track exact pairwise agreement, gold agreement per reviewer, tasks/hour, cost/task and language-level coverage.
3. Illustrative HOLD threshold: IAA < 80%, reviewer gold accuracy < 90%, missing privacy consent or unexplained cross-language drift.
4. Route disagreements to independent adjudicator; inspect source context, issue type and reviewer instructions before relabel.
5. After guidelines are revised, run a **new** blinded calibration batch; never silently overwrite previous reviewer evidence.
6. Share weekly report containing deliverables, rejected items, blockers, reviewer questions, budget/throughput, root causes and due owners.

## Local reproduction
From this folder:

```bash
python src/lilt_batch_eval.py
python -m unittest tests.test_lilt_batch_eval -v
```

The script executes SQLite-based SQL aggregation against an in-memory synthetic dataset, prints a labeled JSON report and returns a HOLD gate on deliberately imperfect agreement. A passing **unit test is not a quality-release PASS**.

## Suggested Jira-style issue example — hypothetical, not observed
Issue LILT-EX-01; Type: annotation disagreement; severity: medium; Language: TR; Modality: text; Batch: synthetic; Expected: both reviewers apply preference rubric; Actual: not yet observed; Reproduce: load case, compare reviewer_a/reviewer_b/gold; Proposed action: adjudicator review + guideline clarification + re-calibration; Status: DEMO / NOT A PRODUCTION INCIDENT.

## CV/interview presentation
Use wording like: "Created an independent, synthetic multilingual AI annotation operations project demonstrating gold comparison, reviewer agreement, human adjudication and SQL quality reporting." Do not claim to have managed real RLHF programs, production crowdworkers, model fine-tuning, LILT customers or paid AI data contracts.
