# Responsible Agentic AI ISO/IEC 42001 as per UAE Laws
**HumanEvoX Talent Consultancy | Original practical governance and assurance lab | 2 November 2026**

> **Evidence boundary:** This is a reproducible, locally executed **deterministic Python governance gate** using 12 fictional recruitment/HR scenarios. It does **not** connect to a live LLM, recruiter ATS, candidate database, UAE regulator or client system. It is **not** a compliant/certified AI management system, proof of ISO/IEC 42001 conformity, PECB qualification or paid client implementation. Use real records only after a legally reviewed security/data-protection deployment.

## The business problem
Agentic recruiting assistants may read HR policies, draft candidate communications, rank applicants, or attempt to export data. Such systems need a defined management system, controlled tools, human decision rights, verifiable sources, transfer safeguards, incident handling and audit evidence. This lab demonstrates the governance layer instead of making unverified claims about AI model accuracy.

## What was actually built and tested
- A Python 3 **standard-library-only** rule-based tool-authorization and escalation gate: `src/governance_gate.py`.
- **12 fictional decision cases**: `data/synthetic_scenarios.json`.
- **9 executed unit tests**, including injection, unlawful processing, stale policy, consequential ranking, cross-border export and rule precedence: `tests/test_governance_gate.py`.
- On **2026-11-02**, local evaluation produced **12/12 matching expected decisions, 0 failed**, and **9/9 passing unit tests**; see `evidence/EXECUTION_NOTE.md`. Those are tests of **our authored rules**, not empirical agent/model performance.
- A HumanEvoX-oriented **AIMS implementation plan**, UAE legal/guidance applicability matrix, AI risk register, owner/control matrix, incident and policy procedures, sample audit package and blank project-hours log.

## NEW — Evidence-backed Responsible AI assessment and actual career-entry bridge

The **governance gate in this folder remains a deterministic simulation**. Separately, the repository's [working HR-policy LLM experiment](../../AI%20Model%20Training%20%26%20Evaluation%20Freelancer%20Project/Agentic%20AI%20Application%20Testing%20%26%20Evaluation%20for%20HR%20Transformation/README.md) preserves **three genuine Qwen model outputs** from a 2026-11-02 GitHub Actions run (plus three other host-controlled scenarios). Those actual responses revealed omitted annual-leave facts, missing manager-approval conditions, and unsupported onboarding details. All three generated drafts were kept separate from source-backed served answers.

- **[Real LLM assurance and CAPA case study](docs/REAL_LLM_ASSURANCE_CASE_STUDY.md)** — 6 evidence-linked case findings, observed model failures, preliminary impact review, proposed controls, open corrective actions and independent-audit questions. It is an original portfolio *assessment* of observed output, not a client audit or ISO conformity claim.
- **[Responsible AI entry roadmap and HumanEvoX paid-pilot scope](docs/RESPONSIBLE_AI_CAREER_ENTRY_AND_PAID_PILOT.md)** — four-week work-based learning plan, entry-level governance/assurance roles, client pilot acceptance criteria, honest CV phrasing and certification decision gates.

**Proof boundary:** A model was actually called in the *companion* project, but no HumanEvoX customer pilot, independent audit, enterprise deployment or management-system certification has been performed. No CAPA is marked closed.

## Repository map
| Path | Purpose |
|---|---|
| [src/governance_gate.py](src/governance_gate.py) | Executable guardrails: allow-demo-only, deny, human escalation |
| [data/synthetic_scenarios.json](data/synthetic_scenarios.json) | 12 fake HR agent tool-use situations and expected decisions |
| [tests/test_governance_gate.py](tests/test_governance_gate.py) | Regression tests |
| [data/risk_register.csv](data/risk_register.csv) | Risks, inherent scores, mitigations, responsible role, evidence |
| [docs/UAE_LEGAL_APPLICABILITY.md](docs/UAE_LEGAL_APPLICABILITY.md) | Laws versus nonbinding UAE guidance versus ISO standard; federal/DIFC/ADGM distinctions |
| [docs/AIMS_IMPLEMENTATION_ROADMAP.md](docs/AIMS_IMPLEMENTATION_ROADMAP.md) | ISO/IEC 42001-aligned plan/do/check/act workstream with deliverables |
| [docs/GOVERNANCE_POLICY_AND_CONTROLS.md](docs/GOVERNANCE_POLICY_AND_CONTROLS.md) | Governance policy, tool boundaries, human oversight, RACI and sample controls |
| [docs/ASSURANCE_AND_AUDIT_EVIDENCE.md](docs/ASSURANCE_AND_AUDIT_EVIDENCE.md) | Evidence matrix, limitations, internal audit questions, treatment and improvement |
| [docs/PECB_AND_WORK_LOG_GUIDE.md](docs/PECB_AND_WORK_LOG_GUIDE.md) | Provisional vs. full credential; integrity of experience/hours |
| [evidence/EXECUTION_NOTE.md](evidence/EXECUTION_NOTE.md) | Transparent local results and repeat instructions |
| [evidence/real_project_hours_log.csv](evidence/real_project_hours_log.csv) | Empty log for future verified personal/client implementation work |

## Run
From *this project folder* using Python 3.9+:
```bash
python src/governance_gate.py
python -m unittest discover -s tests -v
```
The engine prints machine-readable JSON. **ALLOW_DEMO_ONLY never performs the requested tool operation.** The code has no API keys, network calls, external dependencies or personal/candidate records.

## Illustrative decision rules
1. Prompt-injection attempts, unsupported tools, missing lawful-basis review or inadequate export safeguards -> **DENY**.
2. Candidate ranking, external data export even after basic safeguards review, unapproved sends/deletes/status updates or stale policy sources -> **ESCALATE_HUMAN**.
3. Only scoped synthetic read/draft requests that satisfy example checks -> **ALLOW_DEMO_ONLY** (never production permission).
4. The most restrictive result wins; every result identifies control IDs and reasoning.

## Responsible deployment path (not yet achieved)
Identify the real legal entity/jurisdiction and AI use case; designate owners and data controller/processor roles; purchase/consult the licensed ISO/IEC 42001 standard; complete legal/privacy and AI impact assessments; document risk appetite and Statement of Applicability; obtain supplier and retention reviews; test a *real* LLM with a versioned test set; collect genuine records and human sign-offs; audit/monitor corrective actions; obtain independent advice and certification as appropriate.

**Original-work relationships:** [AI Governance parent](../README.md) · [UAE/GLOBAL policies companion](../Responsible%20AI%20and%20AI%20Governance%3A%20Standards%20%26%20Policies%20as%20per%20UAE%20laws%20and%20Global%20Standards./README.md) · [Project 37 assurance](../37_AI_Risk_Management_and_Testing_Evaluation_Verification_and_Validation/) · [Project 44 ethics](../44_AI_Ethics_Responsible_AI_and_AI_Governance/).

**Reference baseline:** [ISO official standard](https://www.iso.org/standard/42001) · [UAE federal data-protection overview](https://u.ae/en/about-the-uae/digital-uae/data/data-protection-laws) · [UAE AI Ethics self-assessment](https://ai.gov.ae/aiethics-self-assessment/) · [PECB credentials](https://pecb.com/en/education-and-certification-for-individuals/iso-iec-42001/iso-iec-42001-lead-implementer).
