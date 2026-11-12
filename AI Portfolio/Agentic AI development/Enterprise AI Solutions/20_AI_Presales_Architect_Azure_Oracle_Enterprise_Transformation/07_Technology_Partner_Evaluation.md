# 07 — AI technology and partner evaluation framework
## GulfConnect Utilities — hypothetical presales partner ecosystem exercise

**Evidence classification:** Original procurement/solution-shaping **simulation**. No vendors were contacted or scored through a real PoC; there is no Presight partnership, endorsement, reseller authorization or confirmed commercial price. Technology names are *candidate options for due diligence*, not statements that they meet this customer's requirements.

### Business requirement
The fictional GulfConnect Utilities division wants permission-aware retrieval of approved service policies, authoritative CIS/outage/CRM status, human approval for customer communications and management reporting. No single model vendor can replace systems of record, data governance, implementation capability or regulated approvals.

### Build/buy/partner options
| Option | Candidate stack or category | Why examine it | Key feasibility question |
|---|---|---|---|
| A — Azure-led | Azure API Management/Logic Apps, Azure AI Search, approved model endpoint, Power BI | Fits the separate Project 20 Azure reference design | Tenant, supported models/regions, authorization trimming, enterprise integrations, actual consumption cost |
| B — Oracle integration-led | Supported Oracle application interfaces and Oracle integration services with approved AI/search components | May reduce change where Oracle is system of record | Available licenses, integration contracts, supported connectors, end-to-end security ownership |
| C — AWS-led AI | AWS Bedrock plus appropriate search, integration, analytics and IAM services | Alternative enterprise architecture option | Suitability for local residency, access control, retrieval evaluation, operations and total cost |
| D — Google Cloud-led AI | Google Cloud Vertex AI plus approved data/search/integration services | Alternative enterprise architecture option | Region, connector, data-handling, governance and support fit |
| E — Specialist implementation partner | Security-vetted system integrator with utility/CIS experience | May supply industry process and delivery capacity | Proven referenceable integration expertise, local support, security practices and subcontracting boundaries |

**Important:** Products are examples, not an equivalence claim. Verify current features, model availability, hosting/residency, data processing agreements, price and permitted interfaces directly with each provider before a real proposal. Do not assume vendors are authorized Presight partners.

### Weighted partner selection model (100 points)
Use the same validated scoring evidence for every shortlisted option. Weights total **100**; each criterion is scored **0–5**, where 0 = fails/unsupported and 5 = demonstrated fit in an authorized test. Weighted contribution = weight × (score / 5).

| Criterion | Weight | How to substantiate |
|---|---:|---|
| Business workflow fit | 20 | Demonstrated policy retrieval, status lookup and human escalation |
| Data integration and interoperability | 15 | Supported CIS/Oracle/CRM APIs, retries, event contracts and source control |
| Security, privacy and residency | 20 | Provider evidence, tenancy, encryption, roles, data processing and local legal review |
| AI quality, evaluation and safeguards | 15 | Reproducible grounding, refusal, prompt-injection and data-access tests |
| Operational resilience and support | 10 | Support tiers, failover, observability, RTO/RPO proposal and SLA terms |
| Commercial TCO and contract flexibility | 10 | Written pricing, usage curves, exit costs and procurement restrictions |
| Implementation partner and skills capacity | 5 | Relevant references, staffing, accountability and delivery coverage |
| Roadmap, maintainability and exit | 5 | Version policy, portability, lock-in, change and termination plan |
| **Total** | **100** | |

**Scorecard — intentionally unscored until verified evidence exists**

| Option | Workflow 20 | Integration 15 | Security 20 | AI 15 | Resilience 10 | Commercial 10 | Partner 5 | Exit 5 | Decision |
|---|---|---|---|---|---|---|---|---|---|
| A — Azure-led | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | Due diligence |
| B — Oracle-led | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | Due diligence |
| C — AWS-led | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | Due diligence |
| D — Google Cloud-led | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | Due diligence |
| E — Specialist SI | Scope-dependent | Scope-dependent | TBD | Scope-dependent | TBD | TBD | TBD | TBD | Partner qualification |

Do **not** publish vendor rankings or "winner" claims from untested assumptions. A pass on data residency and high-risk access controls is a **non-negotiable gate**, not something high commercial scores can offset.

### Detailed due-diligence questions
**Data & API**
- Is the CIS/outage system accessible only through vendor-supported read-only interfaces? Who signs the data contract?
- Can retrieval permissions enforce identity, tenant, document classification and policy version?
- Are events replayable and status timestamps reliable? What happens if an outage feed becomes stale?

**AI assurance**
- Can the system present document provenance and abstain on unsupported questions?
- What evaluation datasets, model/version logs, security test results and audit evidence can be provided?
- Are model tools restricted to an allow-list, with no direct billing, switching or reconnect operations?

**Compliance**
- Where do prompts, context, logs, embeddings, backups and support copies reside and transit? Who are subprocessors?
- What UAE data protection, critical infrastructure and sector obligations apply, subject to qualified local legal review?
- What retention/deletion, incident notification, DPA and transfer controls are contractually supported?

**Commercial and delivery**
- What is fixed vs metered (tokens, retrieval, storage, egress, API traffic, human review, support)?
- What are RTO/RPO and availability commitments, limitations, credits, escalation and termination rights?
- Can a delivery partner show relevant utility/customer-service references and approved access to documentation?
- What is the exit/migration strategy for prompts, embeddings, logs and integrations?

### Reference partner-ecosystem funnel — no real outreach
1. **Identify:** capability gap, industry references, integration constraints and procurement eligibility.
2. **Qualify:** NDA, licensing and reseller rights; security questionnaire; conflicts of interest; support coverage.
3. **Validate:** technical architecture workshop, limited authorized PoV, performance and red-team testing.
4. **Commercialize:** transparent RFP, subcontracting responsibilities, price and change-control assumptions.
5. **Govern:** partner SLA/KPI, vulnerability patch obligations, integration change notice, quarterly review and exit plan.

### Solution options / architecture decision record
**ADR-P07-01 (proposed):** Prefer a non-invasive integration layer above the existing CIS/CRM and Oracle estate, leaving authoritative systems unchanged.  
**Reason:** minimizes uncontrolled writes, protects source ownership and supports phased testing.  
**Trade-off:** depends on supported interfaces and may require partner integration effort.  
**Alternative:** direct migration/replacement. Not selected without a documented business case, technical assessment and procurement approval.  
**Decision state:** *Pending customer architecture, vendor and security validation.*

### Example competitive intelligence record (template only)
| Field | Evidence standard |
|---|---|
| Vendor and product | Exact SKU/version and provider URL |
| Evaluation date | Date reviewed and reviewer |
| Relevant capability | Direct documentation + authorized PoV finding |
| Constraints | DPA, region, integration, security, licenses |
| Commercial evidence | Written quote, date, caveats |
| Buyer relevance | Use-case match, risks, switching cost |
| Product feedback to internal team | Reproducible need, priority, proposed enhancement |
| Decision | Shortlist / reject / re-test with signed owner |

### Roles and controls
- **Solutions consultant:** business requirements, vendor-market research, evaluation rubric and presentation; does not claim administrator/engineering access.
- **Engineering/architect:** technical proof, API architecture, operations and performance validation.
- **Security/privacy/legal:** data and vendor assurance, terms and applicable regulatory obligations.
- **Procurement/finance:** competitive fairness, tender rules, quote and TCO approval.
- **Product/partnership lead:** relationship, roadmap, reseller and integration arrangements.

### CV-safe statement
"Authored a fictional utilities-sector AI solution-partner evaluation framework, including an evidence-gated 100-point scorecard, architecture choices, vendor due-diligence questions and cross-functional procurement governance." This is **not** evidence of managing actual Presight partners or implementing the named platforms.
