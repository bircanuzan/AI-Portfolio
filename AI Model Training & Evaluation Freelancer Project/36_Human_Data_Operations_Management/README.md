# Human Data Operations Management

**Project 36 — Human annotation, data collection, processing, quality assurance and AI-training data operations**

## Plain-English purpose
Demonstrate how an AI-data operations lead would run a **human-in-the-loop annotation program**: define a task, control its data, write annotation guidance, coordinate annotators, resolve disagreements, validate a labeled dataset, measure annotation quality and operational efficiency, and prepare a decision-ready reporting pack.

### Fictional business challenge
A multinational HR service organization needs reliable human-labeled examples to **evaluate and potentially improve** an AI-powered case routing assistant. Human workers categorize synthetic questions into six queues (policy, payroll, mobility, recruiting, benefits, other). The team needs reproducible labels, privacy protections, quality gates and performance reporting.

The case uses **18 synthetic queries, two fictional annotator passes, gold-adjudicated labels and simulated operational metrics**. It illustrates process design and evaluation; it is not a real AI training pipeline, deployed model or client dataset.

## Folder contents

| Open | Deliverable | What it demonstrates |
| --- | --- | --- |
| [01 — Data-ops workflow design](01_Data_Collection_Annotation_Processing_and_Scaling_Workflow.md) | Intake -> validation -> assignment -> QA -> adjudication -> release | End-to-end operational ownership |
| [02 — Annotation rules and edge cases](02_Annotation_Guidelines_and_Annotator_Training.md) | Taxonomy, privacy, precedence and examples | Consistent and teachable human labeling |
| [03 — QA, gold standard and release gates](03_Quality_Assurance_Agreement_and_Adjudication.md) | Dual-label QC, conflicts, review, sampling, kappa | Data integrity and measurement |
| [04 — KPI reporting and improvement plan](04_Operations_KPIs_Dashboard_and_Continuous_Improvement.md) | Operational scorecard, issue categorization, stakeholder actions | Business-oriented data analysis |
| [05 — RACI and stakeholder governance](05_RACI_Security_Reporting_and_Governance.md) | Owner mapping, retention, data minimization, escalation | Cross-functional alignment |
| [Input and labels](data/) | Fictional task data, annotations, gold and work events | Realistic evaluation dataset |
| [Python QA and inter-rater calculation](src/audit_annotations.py) | Schema, label, completeness, agreement and kappa checks | Reproducible data-quality analysis |
| [Python operational report](src/report_ops.py) | Completion %, cycle time and rework rate | Efficiency reporting |
| [Executable tests](tests/) | Happy path, bad label, duplicate, missing and metric tests | Workflow validation |

## Run locally
Python 3.10+ and standard library only, from repository root:

~~~bash
python src/audit_annotations.py
python src/report_ops.py
python -m unittest discover -s tests -v
~~~

**Important outcome:** The synthetic rater agreement is *deliberately below* the illustrative 80% calibration target. The report is therefore a **retrain/adjudicate** example, not a falsely successful quality release. Human subject-matter review is needed before any dataset release.

## Responsibilities demonstrated
- **Annotation & collection:** schema, sampling, task cards, source provenance and documented labeling rules.
- **Quality checks:** completeness, taxonomy, inter-rater agreement, independent gold reference, ambiguity queue and human adjudication.
- **Analysis & reporting:** descriptive KPIs, cycle time, acceptance/error rates, trend drill-down and leadership recommendations.
- **Scaling:** assign/review separation, workload balancing, tooling requirements, reviewer calibration, change control and audit records.
- **Operational improvement:** identify disagreement themes, revise guidance, retest, measure sustainable improvements and track ownership.

## Integrity and limitations
All data and operations are **fictional and AI-assisted portfolio materials**. There are no actual annotators, personally identifiable employee records, paid projects, vendor assignments, model training runs or verified production results. The Python checks are designed for this illustrative structured dataset; real projects require data security approvals and more robust annotation tooling.
