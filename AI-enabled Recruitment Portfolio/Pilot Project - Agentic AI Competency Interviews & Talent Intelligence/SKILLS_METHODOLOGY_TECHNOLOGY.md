# Skills, methodologies and technology catalogue

This is a map of the **capabilities required to build and deliver this class of product**, not a claim that every tool is used internally at Humanyse.ai.

## 1. HR, organizational psychology and talent assessment

| Skill area | Techniques, frameworks and tools | Deliverable |
| --- | --- | --- |
| Job analysis | SME interviews, critical incident technique, task decomposition, KSAOs, job-relatedness review | Role requirement specification |
| Competency modeling | Behavioral and technical competency dictionaries, levels, weight justification, gap analysis | Role-calibrated competency matrix |
| Structured interviewing | Consistent core items, job-relevant probing, behavioral event interviewing, STAR / STARR | Interview scripts and protocol |
| Behavioral rating | Behaviorally Anchored Rating Scales (BARS), 1–5 proficiency indicators, review notes | Rated rubric with sourced evidence |
| Technical assessments | Design decisions, debugging, security, reliability, problem solving, system architecture | Technical evidence anchors |
| I-O psychology | Content validity, construct definition, rater training, inter-rater agreement, assessor calibration | Validation study plan |
| Talent intelligence | Strength/skill-gap profiles, evidence coverage, development planning, internal talent mapping | Individual Talent Insights Report |
| Leadership development | Readiness, high-potential and succession discussions with contextual human review | Talent committee briefing |
| Talent acquisition | Candidate experience, standardized screening, recruiter handoff, interview scheduling and workflow | HR operating model |

**Important:** neither BARS nor a "science-backed" marketing description by itself establishes predictive validity. A real selection instrument must be evaluated for the job and applicant population.

## 2. Agentic AI engineering and methodology

- **Agent design:** task decomposition; bounded autonomy; interview state machines; guardrails; tool calling; context windows; turn planning; deterministic vs generative steps; retry/fallback; cost and latency budgets.
- **Prompt engineering:** role/persona constraints, reusable templates, job-grounded prompts, structured JSON schemas, abstention, prompt injection defense, consistent question equivalence.
- **Conversational intelligence:** question sequencing, role-aware technical probes, STAR follow-ups, transcript coverage, ambiguity handling, multilingual and accessibility considerations.
- **LLM evaluation:** scenario-based evaluation datasets, golden answers, hallucination audit, evidence-to-quote verification, consistency, reproducibility, human preference review, regressions.
- **Explainable assessment:** trace interview evidence to competency + question + rating anchor; distinguish observed statements, inference, assessor judgment and unknowns.
- **Human-in-the-loop:** mandatory SME approval of blueprints, trained rater review of responses, overrides and appeals; employment decisions never auto-executed.

## 3. End-to-end data / product architecture (proposed)

```text
JD / Role Intake
  -> [AI-assisted task / KSAO extraction] -> SME approval
  -> [Competency map + five-level BARS anchors]
  -> [Versioned interview blueprint + question bank]
  -> [Consent & candidate session]
  -> [Bounded text or voice conversational agent]
  -> [Transcript + evidence span provenance]
  -> [Human evaluator and calibration]
  -> [Reviewed Talent Insights Report]
  -> [Approved ATS/HRIS export + audit + monitoring]
```

## 4. Technology stack — explicitly distinguish statuses

| Component | Offline pilot actually implemented | Optional production options **not yet implemented** |
| --- | --- | --- |
| Core language | Python, JSON, unittest | TypeScript + Python |
| Job analysis | Human-authored synthetic blueprint | OpenAI Responses API, Azure OpenAI or another approved model with structured output |
| Agent orchestration | Deterministic fixed-order interview steps | LangGraph, Semantic Kernel or custom function-calling orchestrator |
| Speech | None | Speech-to-text + text-to-speech with explicit notice, retention rules and accessibility alternatives |
| Prompt and schemas | Versioned JSON configuration | Pydantic validation; tested prompt/model versions |
| API/backend | Local CLI only | FastAPI/OpenAPI; OAuth2/OIDC |
| Data storage | In-memory synthetic samples only | PostgreSQL, encrypted object storage and retention service |
| Knowledge/role reference | Static role JSON | Access-controlled retrieval; optional pgvector for competency knowledge |
| Workflow/HRIS | None | Secure webhook/JSON interfaces; scoped Workday, Oracle HCM, Greenhouse, Lever or SAP SuccessFactors adapters where vendor APIs permit |
| Assessment analytics | Human-score arithmetic demonstration | Evidence coverage dashboards; Power BI / Metabase; validation analyses |
| Security | Consent gate + quote check | MFA, RBAC, tenant isolation, KMS, audit logs, DLP and secrets management |
| Quality/operations | unittest | pytest, CI/CD GitHub Actions, OpenTelemetry, telemetry redaction, model monitoring |
| Hosting | No deployment | Approved UAE or regional cloud infrastructure, subject to contractual/legal requirements |

**Company-verified integration claim:** Humanyse's website discusses webhook, structured JSON, PDF and CSV outputs compatible with ATS/HRIS. It does **not** disclose the underlying LLM, orchestration framework, cloud, backend or database. Do not attribute our choices to Humanyse.

## 5. Product and implementation skills

B2B HRTech SaaS discovery; product requirements documents; process mapping; human-centered design; backlog and Agile; API contracts; integration patterns; service-level objectives; vendor assessment; change management; training for HR assessors; evaluation design; audit trails; data classification; privacy impact assessment; risk controls; incident response; enterprise procurement and governance.

## 6. CV skills — evidence-aware phrasing

**Designed:** AI conversational interview system architecture; job-related competency frameworks; five-point BARS; STAR interview blueprints; human review and provenance workflows; ATS integration specifications; governance and evaluation methodology.

**Implemented in this folder:** Python/JSON offline interview facilitator, consent boundary, fixed question sequencing, quote validation, manually reviewed scoring summary, unit tests.

**Explored/proposed, not claimed as hands-on integration:** OpenAI/Azure LLM APIs, LangGraph, FastAPI, voice models, databases, live HRIS webhooks, deployment platforms.
