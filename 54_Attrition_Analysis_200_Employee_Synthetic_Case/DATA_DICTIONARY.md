# Data dictionary and reproducibility

All records are **programmatically fabricated**, with IDs SYN001–SYN200. They represent a **fixed roster observed for a fictional 2026-Q3 period**; no additions or transfers during that period are modelled.

| Field | Type / valid values | Business definition |
|---|---|---|
| employee_id | SYN001–SYN200 | Synthetic stable row key |
| cohort | 2026-Q3 | Common fictional observation period |
| department | HR, Technology, Operations, Finance, Customer Services | Fictional functional team |
| tenure_months | integer >=0 | Fictional completed tenure in months |
| engagement_score | 1–5 | Invented survey-style ordinal response; **not validated** |
| manager_support_score | 1–5 | Invented survey-style ordinal response; **not validated** |
| internal_mobility | 0/1 | Fictional internal move indicator |
| work_arrangement | onsite/hybrid/remote | Fictional arrangement |
| exited | 0/1 | Whether person is flagged as departing within invented cohort |
| exit_reason | 5 synthetic categories or blank | Illustrative departure reason; blank for retained |

## Generation mechanism
Five departments of 40 records; other fields are arithmetic functions of row and department indices; exit flag is also programmatically determined. **This induces artificial correlations** and is useful only to test calculations. It is not evidence that engagement or tenure causes turnover.

## Quality checks
200 rows; distinct keys; no invalid exit values; same observation period; departmental counts reconcile with overall rate.

## Formula caveat
Exits / 200 start-cohort employees is a fixed-roster attrition fraction, **not the standard average-headcount turnover rate for a real company with hires, leavers, internal moves, or shifting denominator**. Real dashboards should validate the organizational KPI specification and dates.
