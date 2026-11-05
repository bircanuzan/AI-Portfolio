# People KPI dictionary and capability assessment

| KPI | Defined formula | Interpretation / caveat | Accountable owner |
|---|---|---|---|
| Opening / closing headcount | Active eligible employees at period boundaries | Document assignment and country rules | HR Operations |
| Avg period headcount | (opening + closing) / 2 | Approximation; daily-weighted average may be needed | People Analytics |
| Monthly attrition | exits / average headcount | Classify voluntary/involuntary only with good source data | CHRO |
| Vacancy-pressure proxy | approved open requisitions / (closing HC + approved open requisitions) | This is a design proxy, not universal statutory/industry KPI | TA + Finance |
| Learning reach | unique staff trained / eligible staff | Do not use duplicated course enrolments | L&D |
| Skills confidence | verified and current skill records / eligible staff | Separate self-reported vs validated data | Talent |
| Internal mobility | qualified moves / eligible staff | Effective date and eligibility required | HRBP |

## Capability maturity score
Rate 0-4 for each: executive sponsorship, ownership and quality of source data, KPI governance, analytical platforms, visualization, statistical literacy, privacy safeguards, manager enablement and benefits measurement. Every score requires documentary evidence, accountable owner and action. "Unknown" is not scored as zero.

## Decision example
Business question: "Where can we redeploy skills before making additional hires?" -> determine workforce and verified skills coverage -> govern definitions -> permitted SAP source products -> People Intelligence/SAC story design -> action owner -> impact follow-up.

## Python demonstration
Input data: synthetic business-unit monthly workforce records. Checks closing HC = opening HC + hires - exits; then computes attrition, vacancy-pressure proxy and training reach. Automated tests check arithmetic and bad input. This demonstrates calculations, not SAP report deployment.

## Safety
For small workforce cohorts, aggregate and suppress to avoid exposing identities. Document jurisdiction-specific privacy, manager access, retention, consent and fairness. Dashboard guidance is decision support, not an automated employment decision.
