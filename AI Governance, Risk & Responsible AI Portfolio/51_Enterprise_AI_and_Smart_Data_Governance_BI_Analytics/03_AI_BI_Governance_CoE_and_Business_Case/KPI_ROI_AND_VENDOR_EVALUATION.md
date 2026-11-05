# KPI, ROI and vendor evaluation pack — PROPOSAL, NOT OBSERVED RESULTS

## KPI catalogue
| KPI | Definition | Owner / baseline evidence |
|---|---|---|
| Queue time | median and P90 time from intake to first human review | Claims Ops / claims event logs |
| Review workload | human-review cases and minutes per case | Claims Ops / time study |
| Data quality | exceptions, schema violations, source freshness, reconciliation | Data Steward / DQ logs |
| Model quality | temporal validation ROC-AUC, calibration, FN/FP & reviewer override | Model Risk / independently labelled claims |
| AI adoption | eligible case suggestions reviewed and overrides explained | Claims Owner / audit trail |
| Complaints / harm | customer complaints and verified incident rate, by authorized analysis groups | Compliance / incidents |
| Reliability | pipeline freshness, uptime, inference latency, fallback availability | Platform / observability |
| Financial impact | incremental validated net benefit, with controls and human cost | Finance / signed baseline |

## Example *hypothesis only* for benefit sensitivity (AED)
Assume 20,000 claims per year, 35% of them could see 6 minutes less clerical handling time **if** a validated human-assisted workflow changes operations, cost at AED 110 per hour:
- Annual time saved = 20,000 × 0.35 × 6 ÷ 60 = **700 hours**
- Gross capacity value = 700 × AED 110 = **AED 77,000**
- If annual run cost is AED 150,000, initial **net value = -AED 73,000**, before implementation, security, human override, retraining, licensing and compliance costs.
- This *negative* indicative value is deliberate: the business case cannot be declared successful without a verified baseline, realistic cost/benefit sensitivity and safeguards.
- No workforce reduction is assumed. Capacity value is not cash saving unless finance validates actual cost avoidance.
- Decision: **do not fund production on this illustrative arithmetic**; require source-data validation and scenario analysis.

## Prospective InsurTech / AI vendor evaluation
Score only after due diligence, not from marketing claims:
- Security, cloud residency/transfer terms, PII controls, audit rights and exit (30%)
- Fit with claims/core-policy systems and data product interfaces (20%)
- Explainability, independent validation, human override, monitoring (20%)
- Vendor financial / operational resilience and support SLAs (10%)
- Pricing, lock-in, integration effort, total cost over 3 years (10%)
- Accessibility, adoption effort and change management (10%)

Threshold: no vendor may proceed if mandatory privacy, security or legal gates fail, even if the weighted score is high. Vendor shortlist **not performed**; no specific InsurTech is endorsed.
