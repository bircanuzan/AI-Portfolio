# 05 — AI Portfolio KPIs, ROI & Executive Reporting

## KPI dictionary
| KPI | Formula / definition | Cadence |
|---|---|---|
| Activated-seat utilisation | Active users / licensed seats | Monthly |
| Estimated spend per active user | Monthly invoice-equivalent spend / monthly active users | Monthly |
| Total AI tool spend | Sum of all tool spend, including applicable usage and subscription charges | Monthly |
| Approval compliance | Approved tools with required reviews / total in-scope tools | Monthly |
| Renewal risk | Number of tools with renewal/notice date inside 90 days and missing decision | Weekly |
| Support health | Incident count by severity, time to acknowledge, age, vendor SLA adherence | Weekly/monthly |
| Onboarding completion | Trained users / targeted pilot users | Weekly |
| Pilot acceptance | Passed UAT cases / total planned cases | Per release |
| Active repeat use | Users with repeated business-relevant interactions / total entitled users | Monthly |
| Hypothetical gross value | Active users × assumed hours saved per user × assumed fully loaded hourly value | Scenario only |
| Hypothetical net value | Hypothetical gross value minus tool spend | Scenario only |
| Hypothetical ROI | Hypothetical net value / tool spend | Scenario only |

**Do not equate estimated time savings with realised financial savings.** Finance must validate the baseline, causality, utilisation assumptions, fully loaded cost, transition/training cost, change in output quality, existing process substitution, and double-counting risk before ROI can be reported as realised.

## Data model
- Tool register: product, vendor, entity owner, use case, data classification, risk/approval flags, renewal date, unit price and licence cap.
- Monthly usage: tool ID, month, licences, active accounts, spend, assumed hours saved and assumed hourly value.
- Service metrics: incident logs, SLA incidents and escalation resolution.
- Training: invitations, completions, attendance, champion feedback and post-training active use.
- Finance: approved budget, PO/contract, invoices, departmental allocations and verified benefits.

## Executive D&T monthly report
1. Portfolio status: active, pilot, retiring, blocked pending review.
2. Financials: licence/consumption spend vs budget, unutilised seats, renewals due, vendor concentration.
3. Adoption: activated users and retention by tool/business unit; training completion.
4. Operational risks: vendor outages, adverse events, unapproved data flows and open security findings.
5. Value: validated business benefits **separately** from scenario estimates.
6. Decision requests: fund/stop/scale, negotiate, remediate, reassess.

## Synthetic scenario input
The included sample four-platform dataset is invented to demonstrate arithmetic, not production use and not real vendor pricing. The Python script reads CSV inputs, rejects malformed/invalid seat arithmetic and creates a Markdown management report.

### Example calculation (synthetic, October 2026)
Across four fictional product subscriptions: **97 seats licensed**, **63 active**, **64.9% utilisation**; **$3,430** assumed spend; **$4,081.50** hypothetical gross productivity proxy; **$651.50** hypothetical net value; **19.0%** hypothetical ROI before implementation/training/overhead. **These are not measured savings.**

## Sensitivity / decision rules
- Downside scenario: 50% of estimated hours savings materialise; include implementation and enablement labour.
- Base scenario: explicit operating assumptions and monthly use records.
- Upside scenario: capped by observed task volumes and quality review; no infinite extrapolation.
- Renewal trigger: compare real seat use, cost, support performance, responsible AI review and benefit evidence.
- Exception: unapproved platform may not be scaled regardless of low cost or optimistic ROI.

## Reproducibility
```bash
python "AI Portfolio/AI Solutions Management/scripts/portfolio_report.py"
```
Default output prints to terminal; optional --output saves Markdown. Script reports totals and compliance flags from the supplied CSV data only.
