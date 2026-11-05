# Workstream 01 — Synthetic motor-claims triage: actual local demonstration

## Use case
A fictional UAE motor-insurance claims operations team wants to identify claims that should be reviewed by a trained employee. **No automated approvals/denials or fraud findings.** Train a simple reproducible predictive baseline using only simulated, non-personal tabular records.

## Input fields
claim_id, claim_amount_aed, policy_tenure_months, prior_claim_count, missing_doc_count, anomaly_indicator, submission_channel, manual_review_required.

The last field is a **simulated label**, produced by a stated random formula, not an observation from real claims. Its relationship with model features is deliberately artificial.

## Execution and evidence
Run the script with --output-dir to generate:
- synthetic_claims.csv — invented data, deterministic seed;
- data_quality.json — checks for expected fields, missing/duplicate IDs, nonnegative amounts, valid categories, allowed fields;
- summary.json — actual holdout metrics; test split, cutoff and package versions;
- review_queue_sample.csv — score, example synthetic ground truth and proposed review routing, **not** insurance decisions.

Versioned execution evidence is in the parent evidence/ directory. Metrics do **not** estimate real model accuracy, fairness, financial benefit or generalizability. The synthetic generator makes the target, so real-world predictive validity has not been assessed.

## Business test cases
| ID | Given | Expected |
|---|---|---|
| UAT-01 | schema-valid synthetic data | data quality gate passes |
| UAT-02 | repeated claim_id | validation fails before training |
| UAT-03 | new column named email | unexpected personal field is blocked |
| UAT-04 | negative claim amount | validation fails |
| UAT-05 | classifier above chosen score threshold | suggested route = human_review, not claim denial |
| UAT-06 | any classifier score | model provides probability + human routing; no autonomous adverse decision |
| UAT-07 | unavailable true outcomes or insufficient live evidence | do not deploy; escalate to insurer model-risk committee |

## Why this does not prove production AI engineering
No real data, endpoint, event pipeline, Azure ML run, data mesh or production MLOps stack is used. This supports the conversation about **model validation and accountable decision workflows**, not a claim of 12 years in AI/data science.
