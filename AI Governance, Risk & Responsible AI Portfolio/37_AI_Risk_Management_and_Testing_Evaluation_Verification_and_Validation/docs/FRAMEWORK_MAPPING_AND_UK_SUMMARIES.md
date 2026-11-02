# Reference Mapping — NIST AI RMF & Two UK Government Publications

## NIST AI RMF 1.0 — what we operationalise
NIST AI RMF 1.0 is voluntary guidance with four functions; its Playbook suggestions are *not a mandatory checklist*.

| Function | NIST theme | Portfolio evidence | Status |
|---|---|---|---|
| GOVERN | Governance, policies, accountability and third parties | Project charter, decision rights, controls, vendor review | Design |
| MAP | Context, affected parties, intended use and risk | AI impact assessment, model inventory, risks and source dependencies | Documented |
| MEASURE | Fit-for-purpose testing, evaluation, verification, validation, metrics and documentation | Deterministic checks, synthetic version/evidence/answer tests, scorecard | Runnable toy prototype |
| MANAGE | Risk prioritisation, incident response, monitoring and change decisions | Exception log, release HOLD, retest triggers and escalation | Mock gate and design |

In NIST's Playbook MEASURE 1.1, organisations should select context-appropriate metrics, set acceptable limits, monitor post-deployment outcomes, and document risks that are not measured. This sample **explicitly does not measure fairness**.

**TEVV:** Testing = run cases; Evaluation = interpret quality outcomes; Verification = check declared requirements/control behaviour; Validation = determine fitness for intended use. Only the first three are **partially demonstrated on toy data**; real-world fitness has **not** been established.

### GenAI risks and implementation status
- Hallucinations / unsupported answers: mock fixture and source-evidence check.
- Prompt injection: one scripted refusal case **does not prove resistance**.
- Data leakage: one scripted refusal case **does not prove security**.
- Harmful or unsafe output: risk controls outlined, not comprehensively tested.
- Human oversight and agent misuse: architecture and gate documented; no production system built.

## UK 2025: Trusted Third-Party AI Assurance Roadmap
Published **3 September 2025**, UK Department for Science, Innovation and Technology.

**Purpose:** strengthen a trusted independent AI assurance market that can verify AI trustworthiness for adopters who cannot do this internally. Three key proposed commitments are a multi-stakeholder consortium to develop the assurance profession, a skills and competencies framework, and an AI Assurance Innovation Fund.

**Career relevance:** governance assurance draws on strategic, leadership, regulatory and sector understanding, whereas technical assessment needs deeper model expertise. The roadmap discusses quality and trust, not universal AI certification.

**Read:** https://www.gov.uk/government/publications/trusted-third-party-ai-assurance-roadmap/trusted-third-party-ai-assurance-roadmap

## UK 2026: AI Risk Management Toolkit
Published **8 September 2026**, same department.

**Purpose:** help teams that *design, operate, buy or deliver* AI products identify, assess, own, treat and monitor AI risks across the lifecycle. Includes risk-identification prompts, a workbook and monitoring guidance. Risk appetite should be defined for the organisation. Example assessment uses impact 1–5, likelihood 1–5 and risk score = impact × likelihood. Risk treatment categories include avoidance, limitation, transference and acceptance.

**Project application:** the synthetic risk register follows the 1–5 scoring concept; control owners, exceptions and retest gates demonstrate operational governance. It is **not a completed UK government workbook or a regulatory approval**.

**Read:** https://www.gov.uk/government/publications/ai-risk-management-toolkit/ai-risk-management-toolkit-guidance

## Adjacent standards
- **ISO/IEC 42001:** AI management systems; referenced in the role requirements but no ISO conformity test was performed.
- **ISO/IEC 23894:** AI risk management guidance; reference only. No ISO certification or audit is claimed.

## Primary reading
- NIST AI RMF: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- NIST Playbook: https://airc.nist.gov/airmf-resources/playbook/
- NIST Generative AI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
