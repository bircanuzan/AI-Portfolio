# Modern Workplace Solutioning Lead

**Project 35 | Executive consulting and outcome-based managed workplace services design**

**Role context:** [DXC Technology — Modern Workplace Solutioning Lead, Dubai](https://ae.linkedin.com/jobs/view/modern-workplace-solutioning-lead-at-dxc-technology-4455183080)

## What this project does
Create a complete, fictional **Modern Workplace managed services proposition** for a multi-country client: executive discovery, outcome-driven service architecture, ITSM/service desk, DEX, device lifecycle, DaaS, identity and security, M365 collaboration, AVD vs Windows 365, asset/field services, automation, Copilot and workplace outsourcing. Define service delivery, governance, SLA/XLA, transparent commercials, T&T and continual improvement.

**Core difference from [Project 34 — Copilot adoption](../34_Business_Oriented_Microsoft_365_Copilot_Adoption_and_Enablement_Consultant/):** Project 34 focuses on employee enablement and learning. **Project 35 designs an entire outsourced/managed workplace service** and its executive business case; Copilot is only one component.

## Fictional case
Northbridge Holdings has **4,500 employees in the UAE, UK and India**, mixed laptops and shared devices, separate regional service desks, fragmented asset records, uneven onboarding and little objective employee-experience monitoring. The client CIO, CHRO and CFO are evaluating a three-year workplace transformation and managed service.

**All sizes, prices, incidents, scores and service improvements in this case are fictional assumptions, not a real DXC opportunity, customer delivery or won deal.**

## Review the deliverables

| Read | Key deliverable | Job requirement |
|---|---|---|
| [01 — Executive discovery and business objectives](01_Executive_Discovery_Business_Case_and_Value_Story.md) | CIO/CFO/CHRO workshop, priorities, current-state mapping | C-suite consultative engagement |
| [02 — Full workplace capability & solution reference model](02_End_to_End_Modern_Workplace_Solution_Blueprint.md) | 14 capability towers, ownership, dependencies, options | Portfolio-wide solutioning |
| [03 — Managed services operating model, SLA, XLA & reporting](03_Managed_Services_Operating_Model_SLA_XLA_KPI.md) | ITSM governance, experience measures and escalation | Services architecture / operating model |
| [04 — Commercial options and business case](04_Commercials_TCO_and_Proposal.md) | Per-seat, consumption, outcome/hybrid constructs, assumptions, risk | Commercial solutioning |
| [05 — Transition and transformation roadmap](05_Transition_Transformation_Adoption_and_Governance.md) | Discovery, due diligence, service migration and stabilization gates | T&T delivery alignment |
| [06 — RFP response and executive narrative](06_RFP_Response_Executive_Deck_and_Pursuit.md) | RFP compliance matrix, eight-slide storyline, proactive pursuits | Strategic presales |
| [07 — Copilot, AI ops, DEX, automation and self-service](07_AI_Digital_Employee_Experience_and_Copilot.md) | Business outcome positioning and governance | Modern workplace innovation |
| [08 — Competitive differentiation & capability checklist](08_Options_Tradeoffs_and_Architecture_Decisions.md) | AVD vs Windows 365, service tradeoffs, vendor evaluation | Solution feasibility |
| [Sample inputs](data/synthetic_service_towers.csv) and [business case calculator](src/workplace_commercials.py) | Auditable scenario assumptions, sensitivity analysis | Quantified business value |
| [Calculator tests](tests/test_workplace_commercials.py) | Tests of math, invalid values and sensitivity | Quality / reusable method |

## Consultative solution logic

~~~mermaid
flowchart LR
  A[CIO / CHRO / CFO outcomes] --> B[Workplace discovery + employee journeys]
  B --> C[Service catalogue and option design]
  C --> D[Service desk / ITSM / DEX / devices / identity]
  D --> E[M365 / AVD-W365 / automation and Copilot]
  E --> F[SLA + XLA + governance]
  F --> G[Commercial options and transition]
  G --> H[Benefits tracking and continual improvement]
~~~

## Run the synthetic commercial model
Python 3.10+; no third-party packages or credentials:

~~~bash
python src/workplace_commercials.py
python -m unittest discover -s tests -v
~~~

The calculator produces **illustrative costs and scenario comparisons**, never a supplier quote. Actual vendor licensing, security, regulations and delivery rates require validation.

## Sources and competence boundaries
Microsoft Intune, Windows 365 and AVD differ in architecture and operational implications, which must be confirmed per client requirements; see [Microsoft Learn](https://learn.microsoft.com/en-us/training/paths/deliver-cloud-hosted-desktops/). ServiceNow provides DEX workflows and user support capabilities, but use requires client licensing and technical assessment: [ServiceNow Digital End-user Experience](https://www.servicenow.com/products/digital-user-experience.html).

**This is an original role-aligned design case, not proof of personally delivering IT outsourcing, device management, enterprise AVD migrations, ServiceNow implementations, production endpoint security or a won strategic DXC bid.** It demonstrates business-side solutioning, commercial thinking, stakeholder engagement and structured delivery planning.
