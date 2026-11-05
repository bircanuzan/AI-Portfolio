# 02 | Use-Case Register and Investment Logic

## Prioritisation (illustrative, scored 1–5; higher is better)
| Use case | Value | Feasibility | Data readiness | Risk manageability | Decision |
| --- | ---: | ---: | ---: | ---: | --- |
| Consent-aware first-response drafting | 5 | 4 | 4 | 4 | **Pilot first** |
| Missing-listing-field quality assistant | 4 | 4 | 4 | 4 | Parallel prototype |
| Marketing-spend recommendations | 5 | 2 | 2 | 2 | Defer pending causal evidence |
| Agent follow-up reminder orchestration | 3 | 5 | 5 | 5 | Baseline automation |
| Autonomous lead qualification/rejection | 3 | 3 | 2 | 1 | Excluded |

## Illustrative customer economics — not employer revenue or forecast
Assumptions for a single **hypothetical agency**:
- 4,000 eligible inquiries/month, held constant for the sensitivity case.
- Baseline qualified viewing booking conversion: 5.0%.
- Pilot hypothesis: +1.0 percentage point absolute (to 6.0%).
- 25% of incremental viewings hypothetically progress to a closed transaction.
- Average agency gross contribution margin per incremental transaction: AED 12,000.
- Annualized operating and change costs: AED 300,000; exclude one-off integration costs pending estimation.

**Calculation:** 4,000 x 0.01 = 40 additional viewings/month; 40 x 0.25 = 10 additional transactions/month; 10 x AED 12,000 = AED 120,000 monthly *agency* contribution; annual gross = AED 1,440,000; illustrative contribution after annual operating costs = AED 1,140,000 **before** implementation costs, selection effects, attribution uncertainty and cannibalization. **These are scenario assumptions, not predictions or observed results.**

## Sensitivity (other assumptions held fixed)
| Absolute uplift | Incremental viewings/month | Potential gross contribution/month |
| --- | ---: | ---: |
| 0.0 pp | 0 | AED 0 |
| 0.5 pp | 20 | AED 60,000 |
| 1.0 pp | 40 | AED 120,000 |
| 1.5 pp | 60 | AED 180,000 |

## Separate agency value from marketplace value
An agency's incremental contribution does **not** equal marketplace/platform revenue. Commercial expansion belongs to the existing account team. AI Strategist supplies a measured value hypothesis and adoption narrative; do not book uplift as sector_organization revenue without an agreed causal commercial model.

## Investment gates
- Before kickoff: baseline completeness >=95%, technical integration estimate reviewed by both engineers, privacy/security approvals.
- Before pilot: 100% of outbound messages human-approved; retrieval citation / listing-field check passed; fallback and incident owner in place.
- Before scaling: statistically and operationally meaningful funnel improvement with acceptable support load, complaint rates, agent adoption and unit costs.
