# Enterprise AI Assurance — Project Charter & Delivery Plan

## Purpose
Operationalise responsible AI governance for a fictional HR policy-answering assistant. Trigger re-evaluation on policy/source changes; produce evidence to support **approve / conditional approve / hold / retire** decisions.

## Stakeholders and decision rights
| Role | Responsibility | Decision right |
|---|---|---|
| Business sponsor / HR policy owner | Intended use, service value, approved policy meaning | Approves business requirements |
| AI Governance Lead | Controls, model inventory, risk register and assurance pack | Recommends release gate |
| Legal / regulatory SME | Authenticity, applicability, policy effective dates | Validates legal sources (real deployment only) |
| Security / privacy | Data retention, prompt injection, sensitive data, third parties | Can block deployment |
| AI/ML architect | Retrieval, agent permissions, logging, evaluation automation | Owns technical implementation |
| Independent assurance reviewer | Challenge evidence and sign off open findings | Issues independent assessment |
| Risk committee | Risk appetite, residual-risk acceptance, escalation | Final release / halt decision |

## Design-and-delivery phases
1. **Discovery / use-case intake:** define users, context, affected parties, data sensitivity, alternatives to AI, success measures.
2. **MAP:** identify systems, source dependencies, third parties, impact and risks; register owners.
3. **GOVERN:** set policies, decision rights, controls, risk appetite and AI oversight forum.
4. **MEASURE / TEVV:** define test oracle, versioned reference policy, scenarios, metrics, exceptions and benchmark baselines.
5. **MANAGE:** assign incidents; retest changes; require committee approval; monitor post-release.
6. **Engineering handoff:** translate policy requirements into source connectors, RBAC, prompt-injection defenses, immutable audit trail and CI/CD release gates.

## Role / JD traceability
| JD requirement | Evidence in this portfolio | Implementation status |
|---|---|---|
| AI governance framework, policies and oversight forum | This brief, risk/control registers | Documented design |
| Risk taxonomy and AI impact assessment | Impact assessment and risk CSV | Documented design |
| Fairness, transparency, explainability, auditability, human oversight | Vendor assurance questions; control register | Evidence requirements defined; no fairness audit performed |
| Use-case intake, AI inventory, approval workflow | Intake template, inventory, stage gates | Documented + sample data |
| AI Factory / regulated sectors / sovereign AI | Architecture note and deployment restrictions | Context only, no sovereign deployment |
| Agentic Control Plane | Source-triggered agent workflow and permission boundaries | Design-only |
| Policy intent translated to technical guardrails | Rules, Python evaluation, escalation and gate | Partial runnable prototype |
| GenAI hallucination / prompt injection / leakage / unsafe output | Risk taxonomy, controlled test fixtures and control plan | Small synthetic tests only |
| NIST AI RMF, ISO/IEC 42001 and ISO/IEC 23894 | Mappings with accurate scope qualification | NIST-aligned; not certified or audited |

## Governance forum cadence (illustrative)
- **Use-case review:** before procurement / development.
- **Release gate:** whenever model, prompt, retrieval dataset, tool permissions or source policy changes materially.
- **Monthly operational review:** risks, exception trends, evidence gaps, retest coverage and third-party changes.
- **Incident forum:** immediately for severe misinformation, breach or tool misuse.

## Sample acceptance criteria
- Every policy-bearing answer has a traceable approved version and effective date.
- No critical test fails for a release candidate.
- All source changes generate an owned re-evaluation task.
- Risk owners and approvals are recorded.
- Formal thresholds are agreed by the risk committee; sample numeric dashboard rates **do not constitute production thresholds**.

## Deliverables / outcomes
This portfolio **delivers** artifacts, a runnable Python evaluator and a reproducible illustrative scorecard. It **does not deliver** a live agent platform, legal advisory system, deployment to an enterprise, certified audit or vendor fairness determination.
