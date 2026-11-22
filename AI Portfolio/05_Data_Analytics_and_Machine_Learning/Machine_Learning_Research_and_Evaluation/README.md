# Machine Learning Research & Evaluation — Reproducible Baseline Lab

**Type:** Independently authored portfolio demonstration using synthetic data. **Status:** Educational research prototype; not evidence of prior paid ML research employment, production deployment, GPU training, or published research.

## Research question
How do preprocessing choices, training-data quality and class imbalance affect classifier generalisation, calibration and subgroup performance?

## Business / research requirement
An AI team needs a transparent baseline for a binary classification workflow, with model selection that considers more than headline accuracy and a repeatable evidence trail before deployment.

## Methodology
1. Generate an entirely synthetic binary dataset (no client or personal records).
2. Split into training/test sets with stratification; fit preprocessing **only** on training data to avoid leakage.
3. Train a dummy majority-class baseline and a logistic-regression baseline using a reproducible random seed.
4. Evaluate accuracy, precision, recall, F1, ROC-AUC and Brier score; compare against the naive baseline.
5. Calculate per-group confusion-derived measures and flag performance differences for investigation—not as proof of fairness.
6. Persist structured JSON metrics and experiment parameters for review.

## Technology
Python 3, NumPy, pandas, scikit-learn; JSON; pytest (optional). The executable baseline uses scikit-learn rather than asserting deep-learning framework proficiency. Possible **future extensions**, not implemented: PyTorch training loop, experiment tracking with MLflow/W&B, CPU/GPU profiling, hyperparameter search, drift monitoring and ML model-card automation.

## Run
```bash
python -m pip install numpy pandas scikit-learn
python run_experiment.py
```
The script writes `metrics.json` in the current directory. Exact numerical results depend on package versions. **No measured KPIs are claimed here until an execution record is attached.**

## Deliverables and quality controls
- Reproducible synthetic dataset generation and train/test isolation
- Baseline comparison and multidimensional classification metrics
- Subgroup diagnostic reporting; small support counts require caution
- Machine-readable experiment output and explicit scope/limitations

## Relevance to ML researcher applications
Demonstrates a concrete *baseline evaluation workflow* relevant to research methodology, numerical metrics, model quality, Python scripting and experiment reproducibility. It does **not** substantiate advanced model architecture research, distributed training or low-level training/inference optimization.

## Portfolio evidence policy
This is an original illustrative sample, not a client case study. No fabricated client names, ROI claims, benchmark victories or published-paper contributions are implied.
