# 05 — DRI ownership, scout-to-scale roadmap, RACI and adoption

## Scout -> prototype -> pilot -> scale
**0–2 weeks:** inventory mobility case categories, interviews with operations/payroll/country legal specialists, current process maps, identify safe routine tasks, establish baselines and privacy decision record.
**3–4 weeks:** create small synthetic prototype (Python + n8n sandbox), evaluate negative scenarios, review integration contracts and required security controls.
**5–8 weeks:** *proposed* controlled pilot with named process owner and sandbox-approved source data. No unsupervised status or employment changes.
**9–12 weeks:** optimize based on observed KPIs and agent-run failures, refine runbooks and enablement, and seek signed permission for additional cases/countries.
**Ongoing:** CoE/reusable patterns, vendor/tool monitoring, periodic role access review and benefit realization checks.

## RACI
| Deliverable | Accountable | Responsible | Consult |
|---|---|---|---|
| Workflow and adoption | Senior Manager Mobility | Automation Ops DRI | HR Ops/Employee Experience |
| Data access and integrations | IT platform lead | Integration engineers | Privacy and process owners |
| Immigration eligibility | Country/legal owner | Approved specialist | Mobility Ops |
| Payroll events | Payroll owner | Payroll integrations | HRIS, Legal, Security |
| Agent evaluation / guardrails | AI governance owner | Automation DRI + QA | Engineering and Security |
| Benefit realization | Operations sponsor | Operations analytics | Finance |
| Ongoing support and incidents | Operations service owner | Platform/automation support | Risk and HR |

## Enablement workshop
30-minute live case triage training: what automation does, when to override, human transfer, correcting mistakes, personal data restrictions, interpreting tool errors and reporting safety concerns.

## DRI trade-offs
Do not scale a brittle workflow simply because it saves minutes. Prioritize a reliable, low-risk request first. Stop any initiative with unsupported regulatory decisions, unacceptable data leakage or no independent service owner.

## Executive sponsor update
Outcome hypothesis, what the prototype proved, what it did not prove, unresolved data/privacy dependencies, actual measured baselines required, prioritized next steps and decision log.
