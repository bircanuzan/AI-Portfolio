# Machine Learning Engineer
## Production ML Reliability Lab: Training, Evaluation, Leakage & Distribution-Shift Auditing

**Portfolio project | Reproducible synthetic-data demonstration | Python + scikit-learn + pandas + Docker**

> This is an original portfolio demonstration using synthetic data. It is **not** a claim of real customer deployment, independently audited model performance, or prior employment as a production ML engineer.

### 1. Client-style problem
An enterprise operates automated work queues and needs to **prioritize workflows likely to miss a service-level agreement (SLA)**. A review team can inspect only 10% of queues. The ML objective is therefore **early detection of SLA failures at a fixed review capacity**, not naive accuracy.

An AI research team also wants reference solutions for grading model-authored training code, evaluation plans and production-readiness claims. The deliverable combines a working ML experiment with a rubric for checking AI-generated solutions.

### 2. What the repository implements
- Reproducible **synthetic data generation** with a defined decision time, six pre-outcome features, noisy-outcome experiment and an intentionally leaky post-outcome field.
- **Chronological train/validation/test partitions**; a late-period distribution shift is reserved for holdout evaluation.
- **Baseline and challenger**: prior-probability classifier, logistic regression and histogram gradient boosting.
- **Metrics aligned to decision constraints**: average precision, ROC-AUC, Brier score, precision and recall in the highest-risk 10% of workflows.
- **Ablation study** that removes a relevant feature to test whether the evidence actually supports its value.
- **Label-noise stress test** that corrupts training labels only; holdout truth remains untouched.
- **Deliberately invalid leakage experiment** to demonstrate how strong offline performance can be deceptive.
- **Slice analysis** comparing late stable-period cases with distribution-shift cases.
- Machine-readable JSON report, review rubric, annotated LLM failure cases and unit tests.

### 3. Role-to-evidence mapping
| Mercor Machine Learning Expert expectation | Evidence in this repository |
|---|---|
| Write a modeling problem with data, objective and constraints | This README + `docs/problem_spec.md` |
| Create a grading reference answer | `rubrics/ml_code_review_rubric.md` + `cases/golden_patches.md` |
| Check code, loss/objective and leakage | `src/ml_eval_lab.py` + leakage unit tests |
| Verify whether an ablation supports a conclusion | Ablation in experiment report; interpretation rules in rubric |
| Identify failure under distribution shift / label noise | Stress tests, time slices and risk notes |
| Explain reasoning clearly | Documented decisions and limitations |

### 4. Project layout
```text
Machine Learning Engineer/
├── README.md
├── requirements.txt
├── Dockerfile
├── Makefile
├── src/
│   ├── __init__.py
│   └── ml_eval_lab.py
├── tests/
│   └── test_ml_eval_lab.py
├── docs/
│   └── problem_spec.md
├── rubrics/
│   └── ml_code_review_rubric.md
└── cases/
    └── golden_patches.md
```

### 5. Run locally
Use Python 3.11+.

```bash
cd "Machine Learning Engineer"
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m src.ml_eval_lab --rows 3000 --seed 42 --output-dir artifacts
```

Or run in Docker:

```bash
docker build -t ml-reliability-lab .
docker run --rm ml-reliability-lab
```

The CLI writes `artifacts/report.json`; `artifacts/` is generated and is not committed. Scores are produced by your own run. **Do not quote illustrative metrics as verified results without running the code.**

### 6. Evaluation contract
**Prediction time:** Before execution outcome is known. **Positive label:** Workflow misses its SLA. **Review capacity:** 10% of workflows, selected by predicted risk per evaluation set. **Model selection:** Validation only. **Final audit:** Test set only. **Primary metric:** Recall among the top-risk 10%; additional precision, average precision, calibration and segment gaps.

An outcome-derived retry count is included *only* to illustrate target leakage and is excluded from valid models. Feature eligibility, temporal order, fixed selection capacity and outcome provenance are explicit review gates.

### 7. What to look for in the report
1. Compare the logistic and gradient-boosted challengers against the non-informative baseline on validation.
2. Confirm the validation-selected model and its locked configuration are the ones reported on test.
3. Compare test metrics across stable and shifted slices without tuning on test.
4. Review results of training-label corruption and retrieval-confidence ablation.
5. Observe the leakage model's misleading offline scores and the explicit invalidity label.
6. Check whether the evidence supports deployment. No single high AUC justifies production release.

### 8. Limitations and next engineering steps
All data is simulated. The demonstration does **not** establish external validity, fairness, user impact, privacy compliance, latency SLAs, operational reliability, or production deployment. Next steps: replace synthetic data with authorized, time-stamped production data; add feature lineage and data contracts; evaluate groups and error costs with business owners; calibrate probabilities; implement model registry, drift monitoring, alerting, human review and staged rollout.

**JD reference:** [Mercor Machine Learning Expert talent network](https://work.mercor.com/jobs/list_AAABoKMjIsiYWQM6KQFCtp1w/machine-learning-expert). The linked role is a standing talent network, not a confirmed active client assignment.
