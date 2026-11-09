# Rubric: Evaluating AI-Generated Machine Learning Plans and Code

**Purpose:** Grade a model-generated ML engineering solution against the reference task in `docs/problem_spec.md`. This is a review aid, not a substitute for running code.

**Scoring:** For each criterion, 0 = missing/wrong, 1 = partially correct, 2 = correct and evidenced. Maximum 24 points. **Critical failures** below override aggregate score.

| # | Criterion | 2-point evidence expected | Critical? |
|---|---|---|---|
| 1 | Problem and target formulation | Binary SLA failure target and prediction boundary defined before outcome | Yes |
| 2 | Business objective alignment | Recall among 10% highest-risk workflows, not accuracy alone | No |
| 3 | Chronological partitioning | Ordered 60/20/20 and no overlap | Yes |
| 4 | No leakage | Post-outcome retry count, label and holdout-derived fields excluded | Yes |
| 5 | Preprocessing isolation | Scalers/encoders fitted only on training subset | Yes |
| 6 | Model and loss fit task | Valid binary classifier/objective and probability output | No |
| 7 | Baseline and challenger | Non-informative baseline compared with two legitimate models | No |
| 8 | Holdout discipline | Selection on validation, single locked official holdout evaluation | Yes |
| 9 | Correct metrics | Capacity precision/recall, AP, ROC-AUC and Brier with denominators | No |
| 10 | Shift/noise robustness | Temporal slices and training-only label-noise experiment | No |
| 11 | Ablation interpretation | One controlled feature change and qualified conclusion | No |
| 12 | Reproducibility and candor | Seed, environment, runnable tests, synthetic-only disclosure | No |

## Mandatory rejection conditions
Any critical criterion scored 0 means **REJECT / FIX BEFORE ACCEPTING**, even with a total above 20. Also reject if the model fabricates benchmark measurements, claims production deployment without evidence, leaks holdout answers into training or changes the objective after seeing test results.

## Score bands (only after critical checks)
- **21–24:** Strong reference solution; subject to runtime verification.
- **16–20:** Conditional pass requiring targeted fixes.
- **0–15:** Revise substantial aspects.
- **Critical criterion = 0:** Reject irrespective of total.

## Audit process
1. Read the AI-generated plan; locate source evidence or label it missing.
2. Execute with a clean environment; collect errors and artifacts.
3. Check the train/validation/test provenance and actual code paths.
4. Compare the reported numbers with independently re-computed metrics.
5. Inspect whether ablations control for changes other than the stated factor.
6. Write a failure-mode explanation, a **minimal golden patch**, and a re-test.
7. Record final judgment and uncertainty. Never infer deployment readiness from synthetic results.

## Adversarial examples for reviewers
- A model computes target encoding before the time split.
- A pipeline scales the full dataset before partitioning.
- A model cites AUC=0.99 while using a field written after the outcome.
- An author promotes a model because it wins on holdout data.
- A model reports an ablation as causal evidence without replicates, interval estimates or controlled variation.
- A model trains a regression loss for a binary ranking task and claims accuracy is the primary objective.

**Example grading record:** `criterion: 4; score: 0; evidence: post_outcome_retry_count in features; verdict: reject; patch: remove feature and re-run all fits; retest: unit test and metric recomputation`.
