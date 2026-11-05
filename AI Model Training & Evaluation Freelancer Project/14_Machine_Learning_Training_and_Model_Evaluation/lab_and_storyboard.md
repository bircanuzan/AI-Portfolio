# Machine Learning lab | Engineering handoff, learner assessment and video storyboard

## Prerequisites and lab environment
Python 3.10+, dependencies in requirements.txt; CPU only; no secrets/cloud account. Lab engineering provisions clean workspace and verifies dependencies. Instructor tests solutions end-to-end. Teaching data: sklearn Iris. Estimated hands-on time 50-60 minutes.

## Guided exercise
1. Frame a 3-class classification question and failure costs. Explain which 4 features are inputs.
2. Run script and record a stratified 80/20 split; test partition stays outside training and selection.
3. Inspect DummyClassifier as the baseline and Pipeline(StandardScaler, LogisticRegression).
4. Explain how cross_val_score fits preprocessing only on each training fold.
5. Compare 5-fold macro F1 scores; then review the single holdout F1, report and confusion matrix.
6. Open joblib artifact by **trusted code only**. Reload smoke test is not a deployment.
7. Write a model card: intended use, provenance, error analysis, drift, safety and ownership.
8. Peer-explain why a toy dataset and an artifact do not establish production readiness.

## Acceptance criteria (20 points)
Reproducible data separation (5); baseline and train-only validation (5); evidence-based interpretation (5); limitations and deployment checklist (5). Passing is 16+. Instructor checks fresh environment, unit tests, clarity, screen-reader text and expected errors.

## ~6-minute lesson: "Why a baseline matters"
00:00-00:50 | "Your model is 90% accurate. Is it good? If 90% of real cases belong to one class, a trivial classifier could match that. Today we give our ML model a fair test."
00:50-01:40 | Explain targets, features, train/test split and why leaked data makes impressive-but-misleading metrics.
01:40-02:30 | Show dummy baseline in code. "We only earn extra complexity when it helps."
02:30-03:30 | Narrate pipeline and fold-wise fitting. "Scale within each training fold, not on the final holdout."
03:30-04:30 | Compare macro F1, then show confusion matrix and one mistaken prediction.
04:30-05:20 | Show saved artifact and reload test. "Saving and reloading is not a production deployment."
05:20-06:00 | Challenge learners to justify model selection and document three limitations.

## Editorial QA
Technical reviewer: leakage, metrics, proper API usage. Curriculum editor: plain English, scaffolding, lesson pacing. Lab engineer: requirements reproducible. Production team: video/editing/captions. Revise using review log before publishing.
