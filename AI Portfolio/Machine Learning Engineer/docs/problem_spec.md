# Machine Learning Task Specification and Reference Answer Contract

## Scenario
An enterprise AI workflow orchestration service processes tasks with varying queue depth, step count, tool errors and estimated latency. Human quality reviewers can inspect **only 10%** of queued workflows. A model should rank cases by probability of missing a service-level agreement (SLA).

**Data classification:** Entirely synthetic. No employee, customer, client or proprietary dataset is used.

## Formal problem statement
For pre-execution feature vector `x_i`, estimate `p(y_i=1 | x_i)`, where `y_i=1` means the workflow missed its SLA. Return a ranking of the **highest-risk 10%** of each evaluation cohort, and report the proportion of all missed-SLA cases captured by that group.

- **Prediction boundary:** Before an actual SLA miss and outcome-related retries.
- **Permitted:** step count, queue depth, retrieval confidence, tool error rate observed so far, estimated latency and recent handoffs.
- **Forbidden:** labels, event timestamp as a predictive shortcut, shifted-period/test-slice flag, and `post_outcome_retry_count`.
- **Primary model-selection metric:** Validation recall@10%-capacity.
- **Secondary:** Average precision, precision@capacity, ROC-AUC and Brier.
- **Splits:** Oldest 60% train, next 20% validation, latest 20% locked holdout.
- **Shift:** Data-generating process changes in the last 15% of cases.
- **Model-selection protocol:** Compare baseline, logistic and histogram gradient boosting on validation; only selected model gets an official holdout score.
- **Stress tests:** Flip 10% of training labels; remove retrieval confidence; inspect shifted test slice. Separate invalid leakage demo is never promoted.

## Reference workflow
1. Verify timestamps and label availability at the prediction boundary.
2. Define loss/training target versus operational decision metric explicitly.
3. Fit all preprocessing on training data only. Logistic regression uses a fitted standardization pipeline.
4. Split by event time before fitting or tuning models.
5. Compare candidates on validation under a fixed review-capacity rule.
6. Freeze selection and assess once on test, including changed-distribution slices.
7. Use controlled label-noise and feature-ablation experiments to test robustness.
8. Diagnose any gap before proposing a rollout, and never consider post-outcome fields valid.
9. Report limitations, calibration, operational cost, privacy, business review and monitoring requirements.

## Common analytical traps
- High classification accuracy with rare positive events can be operationally useless.
- Low log loss or Brier is not identical to maximizing recall given review capacity.
- Random train/test splits can overstate generalization for time-dependent processes.
- Feature leakage can improve offline scores but be impossible in live inference.
- A test-only ablation is exploratory: do not tune or change the chosen model based on the test result.
- An ablation's observed metric change alone does not imply causal value without experimental controls.
- Refit, threshold changes, repeated holdout inspection or redefining slices after results can invalidate evidence.

## Definition of done
Provide source code, dependency pins/ranges, deterministic data construction, a single reproducible command, unit-test evidence, machine-readable metrics, feature-lineage constraints, honest failure analysis, and an explicit production-readiness decision. Production approval is **not** in scope for this synthetic lab.
