# 05 | Control-Group Measurement and CEO-Ready Scorecard

## Primary causal question
Does the AI-assisted response workflow improve **qualified viewing bookings per eligible inquiry** compared with business-as-usual routing?

## Experimental design
- Randomise **agency teams or agents** (cluster assignment) rather than individual leads when process spillover likely.
- Pre-register primary endpoint, baseline, minimum detectable effect, sample-size method, stop rules and observation window.
- Balance baseline cohorts on channel, response capacity, lead volume, region and listing inventory.
- Use intention-to-treat on *eligible* leads; do not exclude non-adopters after assignment.
- Report uncertainty intervals and cluster-robust analysis; involve Analytics to size the experiment.
- Account for delayed conversion, repeat inquiries, seasonality, marketing changes and conflicting lead attribution.

## KPI scorecard
| Dimension | Metric | Numerator / denominator or calculation |
| --- | --- | --- |
| Business outcome (primary) | Qualified booking rate | Qualified booked viewings / eligible inquiries |
| Service (leading) | Median response time | Median minutes received -> first valid response |
| Operational | SLA attainment | Responses <=5 minutes / eligible answered leads |
| Adoption | Weekly active-agent share | Agents using approved draft >=1 / eligible agents |
| Quality | Human edit / rejection rate | Edited or rejected proposals / surfaced drafts |
| Safety | Consent violations | Outbound events without valid consent (target 0) |
| Economics | Net contribution hypothesis | Attributable incremental margin - fully loaded costs |
| Reliability | Draft uptime and fallback | Requests successfully handled or visibly handed to human |

## SQL artifact
[lead_response_kpis.sql](sql/lead_response_kpis.sql) demonstrates cohort metrics over a hypothetical PostgreSQL lead-events table. Columns align with [synthetic_leads.csv](data/synthetic_leads.csv); a real CRM would require a staging mapping and verified timestamp semantics.

## Executive storyline (template — no fabricated outcomes)
1. **Decision required:** pause, continue, redesign or scale.
2. **What changed:** observed primary outcome and uncertainty versus control.
3. **What did not change:** customer complaints, agent workload, conversion mix.
4. **Economic bridge:** measured incremental opportunity, conservative attribution, implementation and run costs.
5. **Risk:** fact errors, consent violations, support load and localization issues.
6. **Next 30 days:** action owners, milestones and commercialization handoff.

**Important:** The synthetic CSV and local script have no randomized treatment assignment; they are sample instrumentation only and cannot establish treatment impact.
