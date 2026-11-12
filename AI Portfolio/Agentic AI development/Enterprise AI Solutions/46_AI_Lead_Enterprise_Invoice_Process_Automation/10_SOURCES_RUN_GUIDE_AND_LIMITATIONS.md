# Reproduce the Prototype — Source Notes and Claim Boundaries

## Primary role reference
[Azizi Developments — AI Lead Systems and Process, LinkedIn posting](https://www.linkedin.com/jobs/view/4477076564/) (accessed 29 October 2026). Responsibilities were used to shape the four portfolio sections; no association with Azizi is claimed.

## Learning references to explore when building an enterprise pilot
- [Microsoft Learn — Power Automate documentation](https://learn.microsoft.com/en-us/power-automate/)
- [Microsoft Learn — AI Builder documentation](https://learn.microsoft.com/en-us/ai-builder/)
- [Microsoft Learn — Business process flows](https://learn.microsoft.com/en-us/power-automate/business-process-flows-overview)
- [OMG — BPMN](https://www.omg.org/spec/BPMN/)
- [Microsoft Learn — Power BI documentation](https://learn.microsoft.com/en-us/power-bi/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
These are design references, not endorsements, integration tests or professional certification claims.

## Reproduction
Requires **Node.js 18+**, standard library only:
```bash
cd 45_AI_Lead_Systems_Process_Enterprise_Automation
node routing_demo.js synthetic_invoices.json
node test_routing_demo.js
```
The first command emits a JSON object per invoice with a route and reason; the second runs synthetic expected-outcome tests, control precedence and boundary checks. See `demonstration_evidence.json` for a scripted offline demonstration result created during authoring. No API key or cloud service is required.

## Evidence taxonomy
| Label | Meaning |
|---|---|
| DOCUMENTED DESIGN | proposed enterprise architecture, process maps, work instructions, source references |
| SYNTHETIC DATA | fabricated invoices and hypothetical operating/financial assumptions |
| LOCAL RULE EXECUTION | actual deterministic branching on synthetic input; not OCR/AI |
| UNIT ASSERTION | scripts check what was coded, not real-world extraction quality |
| NOT EXECUTED | enterprise UAT, security review, deployed cloud workflow, user training or cost realization |

## Limitations and next steps
- Supplier samples are entirely invented. No Azizi internal facts or public job applicant information was accessed.
- No AI model has been trained, called or evaluated. `field_confidence`, `po_match` and anomaly flags are synthetic stand-ins for upstream results, not measured OCR/model scores.
- Rules are illustrative, not a UAE tax, legal, accounting, privacy or authority-of-approval determination.
- Any production flow requires human approval, legal/privacy review, ERP interface mapping, delegated limits, validated exception and fraud detection and signed UAT.
- Operational ROI is a hypothetical **capacity** model; no verified savings or actual benefits are claimed.
- Before using this as professional experience, represent it as an **independent portfolio project**, not a previous client engagement.

## Suggested evidence to collect in a genuine follow-on pilot
Anonymized process captures with owner approval; BPMN diagram exports; mocked API schemas; real UAT defect log signed by test owners; extraction field provenance; approved delegated authority; user-training attendance; incident/run-history samples; KPI definitions and baseline-vs-pilot reconciliation; business sign-offs and Finance-reconciled benefits.