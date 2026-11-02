# Regulatory screening, sovereign AI and AI Factory governance
**Purpose:** close cross-role knowledge requirements in Capgemini, byteSpark and Al-Futtaim; original design only.

## Framework vs legal obligation
| Instrument | Nature | Action in a UAE enterprise |
|---|---|---|
| ISO/IEC 42001:2023 | AI management-system international standard | Develop documented AIMS scope, leadership, governance, monitoring and improvement. No certification asserted. |
| ISO/IEC 23894:2023 | AI risk-management guidance | Contextual risks, impact likelihood, treatment, monitoring and stakeholder involvement. |
| NIST AI RMF 1.0 | Voluntary risk framework | GOVERN, MAP, MEASURE, MANAGE; prioritise actions by organisational context. |
| NIST AI 600-1 | GenAI-specific profile | Address confabulation, information integrity, data privacy and other GenAI risks. |
| OECD AI Principles | International principles | People-centred governance and transparency; not automatically binding law. |
| EU AI Act | EU legal regime with scope-dependent obligations | Identify provider/deployer role, geography, high-risk uses, exclusions, dates, obligations; external counsel review. |
| GDPR / UAE PDPL / DIFC / ADGM | Potentially binding privacy regimes with different scopes | Assess controller, processing, geography, transfers, individuals' rights; don't conflate regimes. |
| CCPA/CPRA | California privacy laws | Screen only when data, business and territorial conditions apply; not blanket worldwide. |

## Sovereign AI questions and controls
*Sovereign AI* can mean multiple things—local compute/data jurisdiction, operational independence, national security requirements or governance autonomy. Define the client's actual objective before choosing architecture:
- Data source, region and cross-border processing: document actual cloud geography and access paths.
- Model weight and supplier dependence: identify vendor control, export rights, availability, update and exit risk.
- Local supervision: are incident response, escalation, audit logs and legal authorities accessible?
- National / sector obligations: consult governing authority and procurement contracts; do not claim UAE-only hosting is universal.
- Risks of over-restriction: insufficient testing populations, resilience and availability; assess trade-offs.

## AI Factory / AI CoE intake-control map
**Intake** registered use-case + sponsor -> **Triage** purpose/impact/risk/data -> **Build/purchase** model and vendor assurance -> **Independent QA** safety/fairness/UAT/privacy checks -> **Go/no-go** assigned decision rights -> **Operations** telemetry, audit, data stewardship and incident response -> **Retirement** deletion and access revocation.

Control-plane implementation choices are context-sensitive and might involve Microsoft Purview, Power Platform, ServiceNow AI/GRC/SPM, Azure AI Foundry, MLOps pipelines, observability tools, SIEM and identity/access management. **No such enterprise systems were configured in this project.**

## External assurance and regulator engagement
An external meeting pack should include documented system scope, risk tier and basis, model/system card, known limitations, privacy assessment, independent test evidence, incident records, human appeal mechanism and signed accountability matrix. Only authorised counsel/legal relations can represent the organisation; a public case study does not imply experience engaging actual regulators.
