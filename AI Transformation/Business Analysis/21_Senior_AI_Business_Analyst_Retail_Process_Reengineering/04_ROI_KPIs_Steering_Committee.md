# 04 — Business case, benefits realization and steering committee

## Example ROI calculation (synthetic)
1,000 returns/month × 10 minutes time reduction = 166.7 staff-hours saved/month. At AED 65/hour, gross labour *capacity* value ≈ AED 10,833/month. Less illustrative monthly operations cost AED 2,000 = AED 8,833/month before other adjustment factors. One-time delivery assumption AED 75,000 yields simple payback ≈ 8.5 months if capacity converts into **genuine avoidable costs**. It does not automatically mean headcount savings.

The Python demo performs the calculation from stated assumptions. Avoidable rework reduction from 8% to 3% is separately tracked to avoid double counting.

## KPI scorecard
| KPI | Formula | Evidence source | Accountable owner |
|---|---|---|---|
| Median minutes per return | Median end-to-end handling minutes | POS/store logs | Retail Ops |
| Return error rate | Incorrect or reworked cases / total returns | QA and refunds | Finance |
| Stock match % | Correct cycle counts / total counts | WMS inventory | Supply Chain |
| Promo error % | Incorrect promo prices / promo transactions | POS/promo logs | Merchandising |
| Cost-to-serve | Verified attributable operating costs / cases | Finance ledger | CFO |
| Automation containment | Safely completed cases without manual handling / eligible cases | Workflow logs | Process Owner |
| AI quality | Grounded correct summaries / reviewed summaries | Human QA | AI Risk |

## RACI
Sponsor COO (A); Business Analyst/process consultant (R for discovery/design); Store Operations (R for process acceptance); Finance (A for refund accounting); IT Integration (R for engineering feasibility); Security/Legal (A for approval in their domains); Analytics (R for KPI instrumentation).

## Steering committee
**Cadence:** fortnightly during design, monthly during rollout. **Decision pack:** baseline evidence, proposed change, 2–3 architecture options, financial sensitivity, defects/risks, deployment readiness and owner/action log.

## Go/no-go
No critical security or payment handling defects; evidence of correct refund paths; controlled pilot with store training; reconciled test transactions; named operational support; finance baseline signoff and approval to expand. **No observed business savings are claimed in this case study.**
