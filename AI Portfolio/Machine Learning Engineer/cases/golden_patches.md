# LLM Failure Modes, Golden Patches and Retest Checklist

These are **constructed teaching examples**, not transcripts or measurements from a real client or LLM evaluation campaign.

## Case 1 — Target leakage through post-event data
**Defective model-written code**
```python
X = df.drop(columns=["missed_sla"])
```
**Why it fails:** Includes `post_outcome_retry_count`, a field created *after* knowing the outcome, and potentially `shifted_period` and timestamps. The model may show impressive offline results yet cannot run legitimately at decision time.

**Golden patch**
```python
from src.ml_eval_lab import FEATURES
X = df.loc[:, list(FEATURES)]
```
**Retest:** `test_reject_target_leakage`; ensure all training calls use only allowed features; discard prior scores.

## Case 2 — Temporal contamination
**Defective approach:** Random train/test split of time-dependent workflow failures, or scaling fitted to all rows before splitting.

**Golden patch**
```python
train, valid, test = chronological_split(df.sort_values("event_time"))
model = fit_model("logistic", train)
# The scale transform is fitted inside a pipeline on train only.
```
**Retest:** `test_temporal_order_and_no_overlap`, `test_reject_unsorted_time`. Confirm all data preprocessing happens inside fitted training pipeline.

## Case 3 — Wrong optimization metric
**Defective claim:** "Accuracy of 95% means it catches almost every SLA miss."

**Golden patch:** Evaluate risk ordering with `recall_at_capacity` and `precision_at_capacity` at 10% review capacity; inspect class prevalence and average precision. Track Brier for probabilistic calibration. High accuracy alone is not proof of useful review prioritization.

**Retest:** Compare all candidate validation outputs under the same `CAPACITY`.

## Case 4 — Holdout-driven model selection
**Defective approach:** Run many configurations on the test set and select the highest-scoring one.

**Golden patch:** Select the model solely by validation recall@capacity, break ties with validation AP, freeze its configuration, and score holdout once. The code uses the `candidates_validation_only` section and `selected_on_validation` key to make this visible.

**Retest:** Check code path has no dependency on `test_metrics` prior to `chosen` assignment.

## Case 5 — Misleading ablation
**Defective claim:** "Dropping retrieval confidence lowered AUC, proving this feature causes better outcomes."

**Golden patch:** Hold model class, partitions and seed constant; report the measured change, its uncertainty and alternative explanations. An ablation shows sensitivity within a modeling setup, not causal impact on an external system. A test-only ablation is diagnostic, not an excuse for post-hoc model tuning.

**Retest:** Compare `remove_retrieval_confidence_ablation` with `locked_champion_test`; explicitly qualify claims.

## Case 6 — Label noise / distribution shift
**Defective claim:** "Training convergence shows the model will keep performing as workflows evolve."

**Golden patch:** Perturb only training labels; keep original test truth fixed. Score pre-shift and shifted slices separately. Investigate changes in data distributions, feature validity and ranking utility before considering any rollout.

**Retest:** `test_corrupt_only_copy_of_training_labels`; compare slice metrics, and reject untested generalization claims.

## Evidence ledger template
| ID | Suspected failure | Code location / observation | Severity | Golden patch | Retest | Result |
|---|---|---|---|---|---|---|
| EX-001 | Post-outcome feature | Example 1 | Critical | Strict allowlist | unit test + rerun | Illustrative only |

## Limitations
This project supplies reference patterns and an executable synthetic case. It does not prove reliability on proprietary data, compare true frontier LLMs, or report an externally validated leaderboard.
