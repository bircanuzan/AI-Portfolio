# 04 — Example RFP response, SOW and estimate

**All prices and scope figures are illustrative commercial assumptions, not actual Kaidon.ai fees, vendor quotes or won proposals.**

## RFP compliance matrix
| Request | Proposed response | Evidence |
|---|---|---|
| Azure enterprise architecture | Governed cloud PaaS architecture with secure integration | 02 architecture |
| Oracle SaaS + CRM integration | Supported APIs, canonical data contract and event reliability | 02 / OpenAPI |
| Containerization, microservices, Kubernetes | App assessment and PaaS-vs-AKS decision; no forced Kubernetes | 03 roadmap |
| Data lakes, AI and MLOps | ADLS, optional ML lifecycle, governance and evaluation | 05 data/AI |
| Security and privacy | Identity, RBAC, encryption, source restrictions, audit controls | 05 / risks |
| Delivery assurance | Discovery workshops, testable PoV, phased gates and handover | 01 / 03 |
| Commercial offer | Itemized illustrative effort/cost assumptions | estimator |

## Statement of Work — phase 0 (12 weeks)
**In scope:** discovery interviews, application landscape, TOGAF-informed architecture views, conceptual Azure/Oracle integrations, synthetic PoV (not production deployment), security/risk review, estimates and phase 1 roadmap.

**Out of scope:** actual production ERP/CRM migration, full implementation, tenant licensing, vendor fees, ongoing support, on-call SRE, security accreditation and unrestricted employee data access.

**Deliverables:** discovery requirements, diagrams, API draft, integration decision record, initial threat model, synthetic PoV acceptance test, indicative TCO, business-case assumptions, RACI/risks and phase 1 SoW.

**Acceptance:** client and engineering owners validate completeness, realistic security constraints, reproducible synthetic PoV and signed decision log. Defer all live production rollout until explicit technical and security approval.

## Estimation assumptions
Roles: presales solution architect, integration SME, data architect, security reviewer, delivery manager. Effort uses person-days multiplied by synthetic AED daily-rate assumptions; a 15% contingency is added to estimated labour. Azure usage, Oracle licences, vendor costs and taxes are excluded.

Run `python src/estimate.py` for a defensible example calculation, then refine after discovery. Never present illustrative price as a quoted contract.
