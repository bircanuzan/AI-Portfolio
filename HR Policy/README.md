# HR Policy | Multinational Aviation Policy, Employment Documentation & Change Governance

**HumanEvoX independent portfolio project — fictional global airline case.** Designed against the capabilities in an Etihad Airways HR Policy job description; **not** commissioned by, endorsed by, implemented at, or based on internal information from Etihad. No actual HR, legal, payroll or airline data is used.

## Executive brief
**Scenario:** Aurora Aviation Group (invented) has 4,800 synthetic employees across six illustrative markets (UAE, Saudi Arabia, United Kingdom, Germany, India and Singapore). Policies evolved country-by-country, with inconsistent templates, unclear ownership, weak version control and HRIS/payroll change risks. A proposed centralized HR Policy Office must standardize enterprise principles **without** assuming a single rule overrides each market's law, collective arrangements or employment contracts.

**Mandate:** create a traceable system from legal trigger → policy impact assessment → locally reviewed drafting → contract/handbook alignment → executive approval → HRIS/payroll configuration → communications → monitored effectiveness.

## Evidence-led workstreams
| Deliverable | What it demonstrates |
|---|---|
| [01 — Policy governance & RACI](01_GOVERNANCE_AND_APPROVALS.md) | Policy ownership, Legal sign-off, materiality, exception routing and review controls |
| [02 — Illustrative global policy](02_SAMPLE_POLICY_FLEXIBLE_WORKING.md) | Clear, employee-facing drafting, local addenda, approvals and exception process |
| [03 — Contract & handbook templates](03_EMPLOYMENT_DOCUMENT_TEMPLATES.md) | Variable fields, review gates, precedence, notice/acknowledgment and redline control |
| [04 — Country compliance matrix](04_COUNTRY_COMPLIANCE_MATRIX.csv) | Multi-jurisdiction issue spotting and research/evidence/action tracking (**not** legal conclusions) |
| [05 — Change rollout, HRIS & payroll UAT](05_CHANGE_MANAGEMENT_AND_UAT.md) | Dependency mapping, stakeholder briefings, cutover and test scripts |
| [06 — Evaluation & cost model](06_POLICY_ANALYTICS_AND_BUSINESS_CASE.md) | Quantified scenarios, leading/lagging indicators, feedback and economics |
| [07 — Safe AI drafting](07_AI_ASSISTED_DRAFTING_PROTOCOL.md) | Human accountability, prompt and evidence safeguards |
| [08 — Interview decision case](08_HIRING_MANAGER_CASE_AND_90_DAY_PLAN.md) | Board-ready recommendation and 30/60/90-day plan |
| [Requirements traceability](REQUIREMENTS_TRACEABILITY.md) | Each job accountability mapped to a deliverable |
| [Synthetic policy register](data/synthetic_policy_register.json) | Machine-readable effective dates, versions, sign-offs and release gates |
| [Offline assurance script](src/policy_assurance.py) / [tests](tests/test_policy_assurance.py) | Deterministic release readiness and illustration of cost calculations |

## Operating architecture
1. **Detect** — log legal/regulatory updates, union/works-council implications, complaints and emerging workforce issues. Record exact authority, effective date, market and verification owner.
2. **Assess** — classify materiality; map impacts on contract terms, handbook, collective agreements, payroll, HRIS, benefits, cost, employee relations and operational continuity.
3. **Draft** — write concise global policy principles and locally counsel-reviewed addenda. Use structured redlines and a source-of-truth document register.
4. **Authorize** — obtain Legal, Payroll, HRBP, Reward/Finance, Data Privacy and policy owner reviews where relevant, then a delegated final approval.
5. **Implement** — migrate approved versions; complete country UAT, employee communications, manager briefings and receipt/acknowledgment processes.
6. **Evaluate** — monitor risk, exceptions, adoption, service tickets, payroll corrections, employee sentiment, operational disruption and verified savings; re-open a policy when triggers hit.

## Sample decision rights
**HR Policy** designs and curates; **Country Legal / qualified local counsel** confirms enforceability and hierarchy; **Payroll/Reward** validates pay implications; **HRIS** implements configuration; **HRBPs & Employee Relations** communicate and capture effects; **authorized sponsor** approves release. No AI assistant or standalone script can supply legal sign-off.

## How to run the demonstration
From the repository root (Python standard library only):
```bash
python "HR Policy/src/policy_assurance.py" "HR Policy/data/synthetic_policy_register.json"
python -m unittest discover -s "HR Policy/tests" -v
```
The script reports release readiness and sample cost arithmetic; it **does not** determine legal compliance, validate employment contracts, or push to HRIS/payroll.

## Portfolio distinction & evidence limits
This project is **policy drafting, jurisdictional control and adoption governance**, distinct from the existing [HR policy AI-agent portfolio](../Agentic%20AI%20Application%20Testing%20%26%20Evaluation%20for%20HR%20Transformation/) and [HRIS architecture portfolio](../HRIS%20%26%20HCM%20Systems/). All organizations, records, scores, dates and costs are invented demonstration inputs. Jurisdiction rows are **research tasks awaiting lawyer review**, not statements of current law. Do not use the sample terms or templates for actual employment without qualified local advice.

**Positioning:** Demonstrates a structured, analytically grounded approach to multinational HR policy governance, writing, controls, organizational change, HRIS readiness and responsible AI-assisted drafting. It does **not** assert 5–8 years of dedicated employment-law practice, an Etihad engagement, legal qualification, actual country-law validation, verified ROI or live system deployment.
