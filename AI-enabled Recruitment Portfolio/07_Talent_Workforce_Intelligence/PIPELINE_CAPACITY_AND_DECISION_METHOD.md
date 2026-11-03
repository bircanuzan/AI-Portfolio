# Talent & Workforce Intelligence | Recruitment capacity and decision support

**Project 07 owns the recruiter and panel *workload* model.** It does not assess individuals, forecast real placements or duplicate Project 01 clinical credential controls.

## Use case
Fictional UAE/KSA hiring portfolio with six requisitions and invented review queues. HR leadership wants to discover where assessor hours are inadequate, where the queue is too small *even before qualification* and whether a hiring-plan assumption needs review.

## Tools / evidence
- [Input data](data/synthetic_recruitment_capacity.csv)
- [Executable Python capacity calculation](src/recruitment_capacity.py)
- [Unit tests](tests/test_recruitment_capacity.py)
- [Versioned synthetic result](evidence/synthetic_capacity_report.json)

```bash
python src/recruitment_capacity.py --out evidence/synthetic_capacity_report.json
python -m unittest discover -s tests -v
```

## Definitions and decision gates
**Review workload hours** = queue × assumed reviewer-hours/profile.
**Capacity deficit hours** = max(0, review workload − available hours).
**Queue coverage** = invented profiles awaiting review / planned roles. It does **not** measure qualified hiring supply, actual time-to-fill, hire conversion, candidate quality, country talent availability or predictive success.

All project outputs are fictional. A legitimate employer would need approved requisitions, verified workflow stages, clear interview owner capacity, disability accessibility, confidentiality review, labour-market and immigration advice where relevant and real historical calibration.

**Executive response:** Consider adjusting interviewer allocation or sourcing effort after human review. No automated screening, scheduling, hiring decision, candidate messaging or real ATS write is implemented.

[Overall workflow](../WORKFLOW_INTELLIGENCE_AND_RELEASE_MODEL.md)
