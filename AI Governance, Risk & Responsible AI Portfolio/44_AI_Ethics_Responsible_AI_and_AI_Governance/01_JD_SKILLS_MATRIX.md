# Job description analysis and consolidated capability matrix
**Source date:** 29 October 2026. Four primary job descriptions + one supplemental RTA vacancy.

| Source vacancy | What the employer explicitly wants | Evidence this project supplies | Experience the portfolio cannot itself confer |
|---|---|---|---|
| **Capgemini Invent — Responsible AI & AI Governance (Dubai)** | AI governance policies, agentic control plane, risk taxonomy, oversight forums, fairness/explainability/human oversight, AI use-case intake and approvals, AI Factory/sovereign AI understanding, architect coordination. **8–12+ years** in governance/risk/compliance/audit/cyber/privacy/consulting. ISO/IEC 42001, NIST AI RMF, ISO 23894, model risk; GenAI hallucination/injection/leakage. | Governance charter, agentic control-plane architecture, risk and controls library, intake and decision gate, mapping standards to artifacts | Cannot prove 8–12 years directly working in AI governance or production control-plane integration |
| **Al-Futtaim / Orient — AI, Data Governance & Privacy Officer (Dubai)** | Enterprise second-line governance; AI/GenAI/agentic AI and model inventory; data stewardship, lineage, classification and catalog; privacy (UAE PDPL, DIFC, GDPR screening), DPIA, transfers, breach procedures; model lifecycle, drift, vendor/LLM due diligence, evidence and reporting. **10+ years** data/privacy/risk/technology governance and **5 years** leading initiatives, preferably regulated industry. | Governance office, data and privacy annex, sample DPIA, inventory, vendor questionnaire, monitoring and audit pack | Does not establish legal DPO qualifications, live enterprise data-catalog implementation or statutory privacy compliance |
| **byteSpark.ai client — Head of AI Ethics & Responsible AI (Dubai, hybrid)** | Enterprise Responsible AI strategy, bias and explainability, ethical audits, model-risk management, C-suite reporting, cross-functional change, regulatory engagement, EU AI Act/GDPR/CCPA and NIST. **7+ years** senior governance/compliance/tech policy/data ethics with substantial AI/ML exposure. Privacy credentials, advanced degrees and ML-cycle familiarity desirable. | Ethics principles, governance board pack, fairness protocol, model assurance, regulatory applicability register and change/adoption plan | Does not demonstrate years of AI audit experience, regulator engagement, advanced technical degree or privacy certification |
| **Q-REF — AI Governance / AI Ethics Specialist (Abu Dhabi)** | Governance policies, ethical lifecycle and approvals, human oversight, AI risk/impact assessment, governance-maturity KPIs, internal/external audit evidence, senior briefings, AI/ML/GenAI literacy, privacy/tech risk, cross-functional collaboration and policies. Bachelor's and relevant prior experience. | Charter, risk register, assessed use case, RACI, go/no-go workflow, metrics and board pack | Does not substitute for prior professional AI compliance experience |
| **Supplemental: RTA — Manager, AI Solutions Quality Assurance (Dubai)** | AI solution quality gates across design→retirement, risk-based requirements, independent assurance, model validation, fairness reviews, UAT, drift/incident thresholds, model change triggers, supplier audit rights, pre-launch go/no-go, governance training. Technical degree and **12+ years with master's / 14+ with bachelor's** progressive experience. | Formal TEVV plan, change-management triggers, sample go/no-go evidence, unit tests, supplier audit checklist | Does not establish technical degree, long-term AI model QA leadership or actual performance/drift testing |

## Unified competencies: depth and evidence
| Competency | Required knowledge/skill | Tool, methodology or artifact in this repo | Capability type |
|---|---|---|---|
| Responsible AI strategy | Ethical principles; harms to individuals and groups; accountability | Charter, fairness and contestability policy | Governance |
| AI management system | Policy ownership, committee, decision rights, internal audit, continual improvement | ISO 42001-informed governance design | Governance |
| AI risk management | Risk identification, likelihood/impact, residual risk, risk acceptance | ISO 23894-informed risk register; NIST MAP/MANAGE | Governance |
| AI risk assessment | Use-case intake, impact, criticality, autonomy, human rights and operational harms | Impact assessment + synthetic risk tiers | Governance |
| AI control engineering | Translate policy to validation, approvals, permissions and logs | Agentic control-plane spec + gate.py | Technical interface |
| AI model assurance | Acceptance criteria, fairness, explanatory evidence, robustness, data drift | TEVV protocol, model card, monitoring plan | Technical assurance |
| GenAI-specific safety | Hallucination, prompt injection, sensitive data leakage, unsafe recommendations | Red-team scenarios, source-checks, allowlists | Technical assurance |
| Data governance | Lineage, quality, catalog, classification, access, retention | Model/data inventory and steward template | Data |
| Data privacy | Lawful basis, DPIA, DSR, cross-border transfers, vendor processor contracts | Privacy annex and DPIA screening | Legal/privacy interface |
| Third-party AI | Supplier due diligence, foundation-model terms, audit rights, update notice | Vendor review and assurance clauses | Third-party risk |
| Agentic AI oversight | Human-in-the-loop, least privilege, transaction limits, tool monitoring | Agentic control-plane and HITL design | Agent governance |
| QA and independent audit | Evidence manifest, UAT, change-triggered re-review, incidents | Gate statuses, unit tests, audit plan | QA |
| Executive communication | Board risk appetite, escalation and metrics, decision memos | Executive pack | Leadership |
| Capability development | Staff policies, stakeholder training, awareness, change management | Role-skills roadmap and training plan | Adoption |

### Interpreting the tool stack accurately
**Used in deliverables:** Markdown; CSV/JSON; Python standard library; synthetic RACI, scoring, impact and audit templates.

**Reference methods but not production tool deployments:** ISO/IEC 42001; NIST AI RMF; ISO/IEC 23894; NIST AI 600-1; Microsoft Purview; ServiceNow GRC/SPM; Power Automate; Microsoft Fabric; Python pandas/scikit-learn/Fairlearn/SHAP; Evidently; MLflow; Azure AI Content Safety; cloud/LLM observability. These are logical implementation choices, **not employer-specific requirements or tools already operated in this case.**

See SOURCES_AND_LIMITATIONS.md for job-post links and differentiation between normative frameworks, binding law and internal governance.
