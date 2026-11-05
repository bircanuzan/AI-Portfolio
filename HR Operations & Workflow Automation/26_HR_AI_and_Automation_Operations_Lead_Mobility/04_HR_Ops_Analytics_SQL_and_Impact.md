# 04 — HR Mobility Ops analytics and value realization

## Synthetic operations dashboard
The CSV contains fictional mobility cases with country, request category, status, touches, cycle hours, SLA adherence and case-sensitivity flag; it contains no names or passport data.

Run: python src/kpi_dashboard.py.

| KPI | Definition | Quality / use |
|---|---|---|
| Median end-to-end cycle | Median elapsed hours per closed case | Segment by jurisdiction and category |
| SLA attainment | On-time first responses / eligible cases | Explicitly define population |
| Human-review rate | Specialist-handled cases / eligible cases | Higher may be appropriate for regulated cases |
| Manual touch effort | Sum documented reviewer minutes | Must not be converted to cash savings automatically |
| Duplicate / rework | Cases reopened or identified duplicate / all cases | Control quality |
| Safe automation rate | Low-risk cases processed without exception / eligible low-risk cases | Excludes regulated decisions |
| Compliance escapes | Confirmed unauthorized or missing approved decisions | Gate metric; target zero |
| Product adoption | Consented users submitting via approved channel / eligible users | Obtain baseline |

## SQL deliverable
[Open SQL scorecard](sql/operations_metrics.sql). This is ANSI-like analytic SQL for a hypothetical staging table, **not executed in Tableau, Sigma, an HRIS or a production warehouse**. A production deployment needs consent, privacy filtering, role access and a data dictionary.

## Financial value formula
Eligible low-risk volume × verified manual minutes removed per case × validated unit cost — (automation infrastructure + review + correction + training + compliance effort). Do not claim savings from a synthetic dataset. Audit correctness, service quality and worker outcomes alongside time.

## Executive review
Monthly DRI report: approved automation scope, demand trend, SLA and exception shifts, blocked high-risk workflows, customer feedback, incident actions, change adoption, validated benefits and decision requests. Use best/worst-case sensitivity, not single-point ROI certainty.
