# 03 — KPI Dictionary, Decision Dashboard and Weekly Reporting
_All figures below are synthetic, derived from the included 48-case demonstration._

| KPI | Definition | Operational decision |
|---|---|---|
| Collection completeness | Records with every required field / intake records | Reject or repair missing-input batch |
| Independent review coverage | Both reviewer labels present / cases collected | Allocate reviewer capacity |
| Reviewer agreement | Matching reviewer A and B labels / dual-reviewed cases | Calibrate taxonomy and examples if below 90% |
| Cohen's kappa | (observed agreement − chance agreement)/(1−chance agreement) | Evaluate consistency beyond raw agreement |
| Gold-label accuracy (A/B) | Reviewer class equals synthetic reference / reviewed cases | Target calibration; not an independent external audit |
| Disagreement/conflict rate | Different reviewer labels / dual-reviewed cases | Human SME adjudication; HOLD above 10% |
| Dual-review effort | Mean(A minutes+B minutes) per case | Identify bottlenecks / unit effort |
| Theoretical daily throughput | 480 minutes / mean dual-review minutes | Capacity planning proxy only; excludes meetings and breaks |
| SLA compliance | Completed before due timestamp / completed tasks | Requires actual completion timestamp, not available here |
| Rework rate | Items returned for correction / reviewed items | Requires rework event log to measure |
| Queue age | Review completion time minus intake time | Requires workflow event logs to measure |

## Weekly management report template
**Week / batch:** fictional October 2026 pilot
**Demand:** 48 synthetic cases across 6 categories; review effort recorded as hypothetical durations.
**Quality:** Python-generated `reports/quality_report.json` gives independently reviewed counts, agreement, kappa, gold accuracy, discrepancy IDs and release gates. The intentional failed gates mean **HOLD**.
**Operational status:** exceptions queued for a human SME; no downstream training/export.
**Decisions required:** approve revised taxonomy examples; assign adjudicator; agree follow-up QA sample and re-test date; obtain ML schema sign-off.
**Not yet measured:** true SLA adherence, queue aging, actual throughput, monetary benefits and production drift.

## Production visualization proposal
Power BI dashboard pages: **Volume & SLA**, **Quality & Disagreements**, **Capacity / Effort**, **Release Readiness & Exceptions**. Slice by batch, source, class, risk tier and time window; show confidence intervals and count bases when volume is small. Document measure owners, refresh schedule and audit trail.
