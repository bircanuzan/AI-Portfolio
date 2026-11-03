# Pilot Project — Agentic AI Competency Interviews & Talent Intelligence

**Keywords:** Agentic AI | AI job analysis | Job-description parsing | Competency mapping | Structured interviews | Voice-led conversational agents | Behavioral and technical assessments | STAR | BARS | Interview evidence | Explainable scoring | Talent intelligence | Leadership potential | Succession planning | Human-in-the-loop | HRTech integration | Responsible AI

**HumanEvoX | Independent portfolio pilot | November 2026**

> **Evidence statement:** This is an independently designed educational pilot inspired by a publicly described market category exemplified by Humanyse.ai. It is NOT Humanyse.ai's proprietary source, an affiliated project, a deployed client system, a validated psychometric test, or evidence of actual model/voice/ATS integration. The runnable sample is **offline deterministic Python with synthetic role and answers**, not an autonomous LLM interviewer. Future tools are identified separately.

## Business problem and niche

High-volume CV screening often fails to capture evidence about applied problem-solving, role-specific technical capability, actual project decisions and observable behavioral competencies. The niche: a role-calibrated AI interview system that translates a job brief into a standardized competency blueprint, runs structured conversations, organizes answer evidence, and presents an auditable report to a human decision maker.

**Humanyse.ai publicly markets:** AI JD analysis; behavioral/technical competency derivation; role-calibrated agents; structured AI-led interviews (including voice-led interviews described by its leadership); a Conversational Blueprint with five-level anchors, evidence/technical/risk indicators; per-person Talent Insights Reports; hiring and internal talent decisions, such as succession and leadership program intake; consent, data minimization, human decision ownership and JSON/webhook exports. These are public claims, not independently validated performance or a confirmed vendor-specific software stack.

Sources: https://humanyse.ai/ ; https://humanyse.ai/pricing ; https://www.linkedin.com/company/humanyse-ai/ (accessed November 2026).

## Functional pipeline

1. **Job analysis:** parse role, purpose, seniority, tasks, mandatory qualifications and criteria; HR/SME review.
2. **Competency framework:** derive prioritized behavioral, technical and role-specific capabilities with explicit evidence and risk indicators.
3. **Conversational Blueprint:** five behaviorally anchored levels per competency; consistent question plan and probes.
4. **Agentic structured interview:** candidate notice/consent; structured conversation, consistent coverage and role-calibrated follow-ups.
5. **Evidence interpretation:** link findings to exact candidate responses; distinguish missing evidence from low capability.
6. **Talent Insights Report:** present reviewed capabilities, strengths, gaps, rationale, confidence/limitations and suggested human follow-up.
7. **Human decision:** recruiters, hiring managers or talent panels own final shortlisting, development and promotion decisions.
8. **Enterprise enablement:** audit, privacy, versioning, reporting and proposed integrations with ATS/HRIS.

## Independent pilot assets

- [Skills, Methodologies & Technology Stack](SKILLS_METHODOLOGY_TECHNOLOGY.md): skill dictionary; selection science; agent workflows; technical architecture; specific implemented vs proposed technologies.
- [Blueprint & Product Workflows](BLUEPRINT_AND_WORKFLOWS.md): role-calibrated interview blueprint, question bank, scoring anchors, traceability and outputs.
- [Governance & Delivery Roadmap](GOVERNANCE_AND_DELIVERY.md): privacy, fairness, job-relatedness, threat model, quality gates and implementation phases.
- [Synthetic role configuration](blueprint.json), [Python offline prototype](pilot.py), and [automated tests](tests/test_pilot.py).

## Run this demonstrator

From this folder with **Python 3.10+** (no API key or pip install required):

```bash
python pilot.py --demo
python -m unittest discover -s tests -v
```

The demo enforces consent, presents fixed questions, captures synthetic answer evidence and requires human-provided ratings/quotes/rationales for any weighted calculation. It DOES NOT assess or rank real applicants. In actual hiring, ratings, methodology, accommodation and selection use require professional validation, lawful processing and oversight.

## Portfolio distinction

This project is a **conversational AI product / HRTech system-design and software pilot**, distinct from the separate **Talent Assessment** portfolio, which documents human-assessor practices and established assessment methods. No projects are moved or merged.

**Related, not merged:** [Talent Assessment](../Talent%20Assessment/) | [AI-enabled Recruitment](../AI-enabled%20Recruitment%20Portfolio/) | [AI Governance](../AI%20Governance%2C%20Risk%20%26%20Responsible%20AI%20Portfolio/).
