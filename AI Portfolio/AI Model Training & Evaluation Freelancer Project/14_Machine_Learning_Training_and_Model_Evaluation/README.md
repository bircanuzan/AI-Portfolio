# Project 14 | Machine Learning Technical Trainer - portfolio case study

**Scope and integrity:** Original instructional-design portfolio sample with runnable Python code and a lab specification. It is not a commissioned course, published video, commercial client result or proof of production ML deployment.

## Course proposition
Audience: early-career software engineers who can write basic Python. Guided course: three modules, eight six-minute micro-lessons, a 60-minute lab, and model-card assessment.

| Module | Outcomes | Learner deliverables |
| --- | --- | --- |
| Frame and baseline | Explain supervised learning, targets, splits, holdout data and leakage | Problem framing and baseline |
| Train and evaluate | Build scikit-learn Pipeline, compare dummy baseline, cross-validate on train partition, interpret F1 and confusion matrix | Reproducible training log |
| Responsible packaging | Save and reload model, identify monitoring and safety requirements | Model artifact smoke test and model card |

Course build: outcomes and scripts -> technical SME review -> editorial check -> lab-team environment build -> instructor clean-run QA -> recorded demonstrations -> learner feedback and revisions. Production owns editing, animation and publication.

## Files
- src/train_model.py: real scikit-learn example using open Iris data; reproducible split, baseline comparison, training-only CV, held-out evaluation and joblib save/reload.
- tests/test_model.py: smoke and learning acceptance tests.
- lab_and_storyboard.md: detailed hands-on lab build instructions, validation steps, exercise rubric and ~6-minute lesson script.
- requirements.txt: Python dependencies.

## Quick start
Install Python 3.10+, run pip install -r requirements.txt, then python src/train_model.py and python -m unittest discover -s tests.

The dataset is public toy data; no personal information or employment decision data. Saving a model artifact is not the same as production-serving a model. Never unpickle untrusted joblib files.

## Skills illustrated
Learning objectives, curriculum architecture, model-training foundations, reproducibility, holdout evaluation, scikit-learn, metrics, editorial collaboration, lab specifications, test/QA, presentation script and documentation.
