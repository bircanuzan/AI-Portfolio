# 07 — Adoption KPIs & Benefits Dashboard

## What counts as success?
**Not:** how many people saw an announcement, opened a portal once, or attended training.
**Instead:** employees use the correct channel safely, requests are resolved with clear ownership, managers act within approved authority, and service quality is maintained.

| KPI | Numerator / denominator | Collection | Interpretation |
|---|---|---|---|
| Eligible-employee activation | Unique eligible employees who completed at least one approved ESS action / all eligible employees | Privacy-approved portal usage | First-step adoption, not sustained habit |
| Channel-switch rate | In-scope requests submitted through ESS / all in-scope requests across ESS and legacy channels | HR service logs | Requires stable request taxonomy |
| Transaction success rate | Completed without reopened errors / completed ESS requests | QA sample + tickets | Do not confuse case creation with successful resolution |
| Approval timeliness | Manager approvals completed within approved timeframe / approvals due | Workflow data | Depend on policy and capacity |
| Help/exception rate | Cases escalated to human support / all ESS attempts | Service desk | May initially rise when reporting becomes easier |
| Sustained-use rate | Users completing a qualifying ESS action in ≥2 separate weeks / eligible active users | Privacy-minimised telemetry | Use for repeat-use activities only; letters may be infrequent |
| Employee trust | Survey respondents agreeing they know how to reach a human adviser / all valid responses | Voluntary pulse | Report response and sample bias |
| Service cycle time | Median elapsed time by request class | Ticket timestamp comparison | Compare similar case mix and definition |

## Synthetic example calculations
See [data/synthetic_ess_adoption_metrics.csv](data/synthetic_ess_adoption_metrics.csv).

**Week 12, fictional pilot:**
- Eligible employees: 300.
- 219 employees completed at least one qualifying action in the reported week -> **73% weekly activation** (219 / 300).
- In-scope requests via ESS: 660; legacy channel: 95 -> **87.4% channel-switch share** (660 / 755).
- Successful completed ESS requests: 641 of 660 -> **97.1% first-pass completion** (641 / 660).
- These values are invented to illustrate formulas and can **never** be represented as client results or a forecast.

## Value measurement
1. Record pre-change baseline by service category, location and user group.
2. Compare like-for-like case mix and quality, not total volume alone.
3. Account for implementation cost, additional support, process rework and exceptions.
4. Any estimated **time capacity** release must be signed off by HR Operations; **cash savings** require separate finance validation.
5. Track whether vulnerable/access-constrained staff are being excluded or are using an approved alternative; low portal adoption may be appropriate in those cases.

## Executive dashboard mock-up (text)
| Dimension | Sample RAG | Decision question |
|---|---|---|
| Adoption | Amber | Are employees choosing the approved route because it works? |
| Readiness | Amber | Can managers approve correctly without workarounds? |
| Service quality | Green *illustration only* | Are requests accurate, timely and escalated safely? |
| Privacy and accessibility | Conditional | Have hard gates been signed off? |
| Sustainment | Amber | Is HR Ops ready to take operational ownership? |

**Caution:** A sample high completion rate is insufficient to prove readiness if security or accessibility approvals are missing.

## Data minimisation
Use aggregated counts where possible; do not export identifiable employee-level data into GitHub or public dashboards. Real data would require lawful access, retention rules, appropriate HR/Privacy approval and restricted reporting.

No analytics system was integrated and no observed metrics were collected.
