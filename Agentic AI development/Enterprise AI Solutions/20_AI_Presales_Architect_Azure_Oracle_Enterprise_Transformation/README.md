# Project 20 — AI Pre-Sales Architect | Azure, Oracle & Enterprise Transformation

**Independent, role-aligned original solution-design simulations.** The core GulfConnect Group Azure/Oracle case was authored in relation to an AI presales architect vacancy; an added **fictional GulfConnect Utilities division** case addresses the publicly provided Presight Manager – Solutions requirements. These are not real client deliveries, Presight engagements, won bids, executed demos, verified vendor tests, production deployments or Azure/TOGAF certifications.

## Fictional customer
GulfConnect Group operates Oracle HCM/ERP SaaS, a separate CRM, legacy .NET/Java portal and disconnected spreadsheets. Its CIO wants governed integration, modern applications, Azure analytics and carefully approved AI use cases.

## Presales deliverables
1. [Executive discovery and workshop](01_Discovery_and_Executive_Workshop.md): decision-makers, questions, capability mapping, business and non-functional requirements.
2. [Reference solution architecture](02_Azure_Oracle_Integration_Architecture.md): Azure PaaS, serverless, event-driven integrations, APIs, modernization, security and data architecture.
3. [Modernization and migration decisions](03_Modernization_Migration_Roadmap.md): six Rs, Kubernetes trade-offs and phased delivery.
4. [RFP response and Statement of Work](04_RFP_SOW_and_Estimate.md): scope, acceptance, assumptions, estimates and executive value narrative.
5. [Enterprise architecture controls](05_Data_AI_MLOps_Governance.md): data lake, MLOps, analytics, responsible AI and TOGAF-informed governance.
6. [Example API contract](api/employee_metrics.openapi.yaml) and [Python proposal estimate](src/estimate.py), with [unit tests](tests/test_estimate.py).
7. [AI solution discovery and executive demo](06_AI_Solution_Discovery_and_Executive_Demo.md): fictional UAE utilities customer, business storyline, scripted interface behaviours, pilot evaluation and value hypotheses.
8. [Technology and partner evaluation](07_Technology_Partner_Evaluation.md): candidate-vendor due diligence, evidence-gated weighted scorecard, integration fit and partner qualification.
9. [Technical RFP and delivery handover](08_Technical_RFP_and_Delivery_Handover.md): requirements compliance matrix, proposed architecture, technical validation ownership, UAT cases, security/BCP and deployment gates.

### Reference architecture — decision-first, not a diagram alone
Oracle HCM/ERP and CRM remain systems of record. A governed API layer using Azure API Management plus Functions / Logic Apps validates requests. Durable workflow messages use Service Bus; pub/sub updates may use Event Grid. Curated inputs land through Data Factory into ADLS Gen2, are transformed in a fit-for-purpose service such as Databricks, and power Power BI. Sensitive AI use cases require retrieval permissions, evaluation and human approval.

**Azure App Service / Container Apps vs. AKS:** prefer managed PaaS unless workload constraints justify the complexity and operational ownership of Kubernetes. **MLOps:** only if real model retraining and operational evaluation are warranted; a retrieval prototype does not automatically require ML model training.

### Run
Python 3.10+: `python src/estimate.py` and `python -m unittest discover -s tests -v`. Example estimates are *assumptions*, not a vendor price quote.

### Covers job-description keywords
Client discovery, executive workshops, solution shaping, enterprise architecture, TOGAF concepts, Oracle SaaS/ERP/CRM, Azure PaaS/serverless, API/microservices, Kubernetes and containers, event-driven design, data lakes/MLOps, security, RFP, SOW, budget assumptions, roadmap and delivery gates.

**What it does not prove:** Azure production deployment, successful bid awards, Kubernetes operations or TOGAF/Azure certifications.

JD: https://ae.linkedin.com/jobs/view/ai-pre-sales-architect-at-kaidon-ai-4476581295


## Presight Manager – Solutions skills coverage (portfolio exercise)
| Vacancy capability | Portfolio artifact | Evidence limitation |
|---|---|---|
| Customer discovery, solution storytelling, executive presentation | [06](06_AI_Solution_Discovery_and_Executive_Demo.md) | Workshop and demo are scripted, not delivered to a live customer |
| Business value, pilot prioritization and ROI discussion | [06](06_AI_Solution_Discovery_and_Executive_Demo.md) | Volumes and time-saved assumptions are hypothetical; no verified ROI |
| Ecosystem partners, technology fit and market intelligence | [07](07_Technology_Partner_Evaluation.md) | Vendor scorecard unscored; no endorsements, verified bids or actual partner outreach |
| Technical RFI/RFP, architecture and business-to-engineering handover | [08](08_Technical_RFP_and_Delivery_Handover.md) | Design-only; no implementation or technical sign-off |
| Governance, privacy, QHSE/safety and continuity | [05](05_Data_AI_MLOps_Governance.md), [08](08_Technical_RFP_and_Delivery_Handover.md) | Proposed controls; regulatory/legal assessment and production evidence outstanding |

**Scenario boundary:** The utilities pilot is a *fictional industry extension* of the original fictional GulfConnect Group; it is not an actual Presight customer and does not imply that Presight provides the depicted products or services. The demo examples are *scripted expected outcomes*, **not real LLM responses**. Named cloud products are reference options subject to current provider verification, licensing, jurisdictional review and engineering feasibility. Professional software, hardware and networking implementation skills must be separately demonstrated.

**Presight role reference (public job description supplied for this portfolio exercise):** https://www.linkedin.com/jobs/view/4483436443/
