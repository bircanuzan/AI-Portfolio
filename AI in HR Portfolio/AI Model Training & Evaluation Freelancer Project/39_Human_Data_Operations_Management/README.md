## NEW — LILT remote UAE | Project Manager, Applied AI JD extension (2 November 2026)

[**Open LILT skills and experience-gap map, multilingual data-ops operating model, QA gates and handoff runbook**](docs/05_LILT_Applied_AI_Project_Manager_JD_Mapping.md).

Added an independent **synthetic multilingual LLM-preference evaluation batch** with Python + in-memory SQLite reporting for exact reviewer agreement, gold-set accuracy, throughput, cost per task, language splits and human-adjudication HOLD thresholds:
- [Synthetic review labels](data/lilt_synthetic_preference_batch.json)
- [Executable SQL-backed evaluation](src/lilt_batch_eval.py)
- [Local regression tests](tests/test_lilt_batch_eval.py)

Run: `python src/lilt_batch_eval.py` and `python -m unittest tests.test_lilt_batch_eval -v` from this folder. These are simulated preference labels, **not production RLHF/SFT, a live LLM evaluation, real annotator activity or a LILT project**. The source vacancy asks for 3–5+ years of AI/ML data-operations project management: this independent demonstration does not confer that prior tenure.

---

# Human Data Operations Management | AI Training Data Quality & Delivery
**Project 39 · Role-aligned simulated operations case · Updated October 2026**

## Business scenario
A fictional multi-region enterprise uses human-labelled support/HR requests to train or evaluate an AI routing model. The programme must deliver accurate, traceable training examples while controlling operational throughput, reviewer disagreements, hand-off delays, and privacy risks.

**This is a synthetic portfolio demonstration, not a client engagement, paid annotation operation, or a deployed AI model.** The inputs, annotators, times and gold labels are invented. The calculations are reproducible from included CSV data.

## What this demonstrates (mapped to Human Data Operations Manager JD)
| Responsibility | Evidence |
|---|---|
| Design, build, manage annotation/collection/processing workflows | [Operating model](docs/01_Operating_Model_and_SOP.md) and data schema |
| Set / monitor actionable operational KPIs | [Metrics and reporting framework](docs/03_KPI_Dictionary_and_Weekly_Report.md), executable audit |
| Analyse datasets, identify improvements | [Root-cause and improvement plan](docs/04_Improvement_Backlog_and_Business_Recommendations.md) |
| Create reporting and governance frameworks | JSON reporting, decision gates, owner matrix |
| Cross-functional data alignment | [RACI, escalation and security](docs/02_Governance_RACI_and_Data_Integrity.md) |
| Improve scale, data integrity, validation and quality | Two independent labels, agreement and Cohen's kappa, simulated gold labels, privacy checks, unit tests |
| Own operational issues | Human adjudication queue and release-blocking decision logic |

## Operating path
`Request & business objective -> schema/source intake -> privacy/completeness gate -> sample & batch -> two independent labels -> disagreement review -> human adjudication -> release decision -> reporting -> improvement backlog`

## Included assets
- `data/cases.csv`: 48 fictional tasks, source IDs, timestamps, gold labels, risk tier.
- `data/reviews.csv`: two fictional independent passes, synthetic effort minutes, exception notes.
- `src/pipeline.py`: schema/data checks, agreement, Cohen's kappa, gold-accuracy estimates, conflict rate, productivity and quality gates.
- `tests/test_pipeline.py`: repeatable validation and failure-path tests.
- `docs/*`: SOP; governance & RACI; metric definitions and weekly reporting; ranked backlog.

## Reproduce the assessment
From this folder, with Python 3.10+ (standard library only):

```bash
python src/pipeline.py
python -m unittest discover -s tests -v
```

The Python command creates `reports/quality_report.json`. **Exit code 2 and a HOLD decision are expected**, because deliberately imperfect human reviews do not satisfy the illustrative 90% agreement / 95% reviewer-B gold-accuracy / 10% conflict-rate release thresholds. Investigate the adjudication queue, calibrate, then re-run rather than implying a release passed.

## Technical solution and tools
**Python 3**, CSV schema/provenance and validation, descriptive analytics, Cohen's kappa, JSON report, `unittest`. Production design can use **SQL, Excel/Power Query, Power BI, annotation platforms, workflow management tools and versioned object storage**; those are recommendations, not deployed components of this sample.

## Relationship to earlier project
[Project 36 — Human Data Operations Management](../36_Human_Data_Operations_Management/) illustrates the annotator/QC method with 18 HR scenarios. **This project focuses on the manager layer**: ownership, operational performance, release gates, cross-functional decisions, and a prioritized plan for scaling.
