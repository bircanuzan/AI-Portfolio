# A2–A3 — AI Opportunity Portfolio Prioritisation and Benefits Business Case

## Investment committee proposal
**Recommend UC-01 invoice intake / exception routing for controlled design validation; do not authorize production yet.** Other use cases are opportunities, not implemented systems.

### Pipeline scoring
Use a common 100-point weighted model to avoid selecting solely by AI novelty:
- Business value **30%**; technical feasibility **25%**; data/process readiness **20%**; manageable risk **25%** (lower risk is better).
- Formula: `score = 30*(value/5) + 25*(feasibility/5) + 20*(readiness/5) + 25*((6-risk)/5)`. Round to whole number only for presentation.
- A **hard-stop governance gate** overrides rankings: no sensitive-data processing without assessment, no autonomous payments, no unapproved vendor bank changes, no bypassed dual approval.
- Scores are workshop hypotheses, **not observed evidence**. The CSV records directional scores; validate score arithmetic during review and maintain one source of truth before investment approval.

### Hypothetical first-year unit economics
| Variable | Base assumption | Source required to replace |
|---|---:|---|
| Invoice volume | 2,400/month | 3 months of ERP and shared inbox data |
| Current active handling | 20 min/invoice | time/motion sample, by category |
| Time reduction for eligible cases | 12 min/invoice | signed pilot measurement |
| Eligibility rate | 72% | approved routing criteria tested on real sample |
| Loaded human effort value | AED 120/hour | FP&A validated actual cost |
| One-off implementation cost | AED 160,000 | IT and vendor estimates |
| One-off change and training | AED 40,000 | HR/L&D training plan |
| Recurring licence | AED 120,000/year | actual licence tier / volume |
| Recurring support/monitoring | AED 60,000/year | IT service model |

**Annual gross capacity freed** = 2,400 × 12 months × 0.72 × (12 ÷ 60) × AED 120 = **AED 497,664**.  
**Annual capacity hours** = 4,147.2 h.  
**Year-one planned cost** = AED 160,000 + 40,000 + 120,000 + 60,000 = **AED 380,000**.  
**Illustrative year-one net capacity value after cost** = **AED 117,664**.  
**Simple year-one value-to-cost ROI** = 117,664 ÷ 380,000 = **30.96%**.  
**Simple payback, assuming even realization** = AED 200,000 one-off ÷ (497,664 − 180,000 ongoing) × 12 = **7.56 months**.

### Critical interpretation
This **is not a financial savings claim**. Redeployable processing capacity cannot be booked as cash unless an agreed action (overtime avoided, vendor invoices reduced, funded capacity released) is documented and measured. Procurement and finance must also model handling of ineligible cases, rework, exception leakage and post-launch drift. Case is **not approved** and no vendor prices have been quoted.

### Sensitivities
| Scenario | Eligible share | Minutes avoided on eligible cases | AED/hr | Gross annual capacity value | Year-one net after planned AED 380k |
|---|---:|---:|---:|---:|---:|
| Downside | 50% | 8 | 100 | 192,000 | -188,000 |
| Base | 72% | 12 | 120 | 497,664 | 117,664 |
| Upside | 80% | 14 | 130 | 698,880 | 318,880 |
Formula in every case: invoice volume × 12 × eligible share × (minutes saved ÷ 60) × loaded hourly rate. Other assumptions held fixed for comparability.

### Option appraisal and funding gates
| Option | Pros | Limits | Recommendation |
|---|---|---|---|
| 0. Business-as-usual plus SOP | low spend | data entry and queue burden persist | benchmark |
| 1. Rules workflow without AI | transparent; faster approvals | no extraction of PDF fields | fallback / initial phase |
| 2. OCR/document extraction + human-controlled workflow | potential intake speed | data quality, vendor costs, privacy, exceptions | **design for pilot only** |
| 3. Unrestricted autonomous invoice agent | potentially fewer clicks | unacceptable access and control risk | reject |

**Phase gates:** G0 sponsor defines scope & baseline; G1 security/finance/process owners sign BRD; G2 test extraction/routing accuracy offline; G3 AP manager signs UAT with critical tests passing; G4 risk and IT approve controlled pilot; G5 Finance validates benefits at 30/60/90 days. The Director of AI arbitrates portfolio priority, not individual payment authority.