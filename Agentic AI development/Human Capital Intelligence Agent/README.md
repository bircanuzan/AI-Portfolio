# Human Capital Intelligence Agent | Agentic AI Development

**Author:** HumanEvoX independent engineering and HR transformation portfolio  
**Agent version:** 0.1.0 (prototype) | **Role requirements reference:** G42 Human Capital Intelligence Agent (AI Agents Only)  
**Status: runnable read-only agent and API prototype using fictional aggregate data. NOT production deployed, NOT G42-qualified, NOT submitted.**

## What this agent does
This is a **bounded, auditable multi-tool Human Capital intelligence service** that executes specialised analytic actions and assembles an executive brief, with access controls and audit trail, without letting an LLM approve HR decisions or invoke arbitrary tools.

| Domain | Implemented tool | Structured output |
|---|---|---|
| Talent Acquisition | talent_acquisition | Funnel, conversion, source mix, cost per hire |
| Employer Brand | employer_brand | CTR, application conversion, mention share and attributed acquisition cost |
| HC Operations | human_capital_operations | Onboarding and employee service SLA, exceptions |
| Talent Management | talent_management | Review coverage, skill gaps, succession readiness and learning completion |
| Total Rewards | total_rewards | Minimum-cohort aggregate grade ratios to **invented** comparator data |
| Organisation & Workforce Intelligence | workforce_intelligence | Position control, vacancies, contingent workforce, annual people budget/cost |
| Executive coordination | executive_brief | **Six-tool orchestration** with provenance, human-review flags and no side effects |

**Demonstration company:** Cedar Gulf Enterprise (invented); 3 entities, 102 approved seats, 89 occupied seats, 13 vacancies and 18 contingent workers. All workforce and pay data are fictional aggregates. No names, IDs or other individual records are included.

## Repository navigation
- [Agent résumé](AGENT_RESUME.md) — agent functionality, roles, technology and restrictions.
- [Developer profile](DEVELOPER_PROFILE.md) — truthful authorship/experience, not a traditional candidate CV presented as an agent.
- [System architecture](docs/ARCHITECTURE.md) — API, bounded planner, analytics, optional sovereign model, trust boundaries and deployment patterns.
- [Security / Responsible AI](docs/SECURITY_RESPONSIBLE_AI.md) — role and entity scoping, personal-data controls, audit, review responsibilities and threats.
- [Integration contract](docs/INTEGRATION_SPEC.md) — read-only mock-tested HTTPS adapter for HRIS, ATS, payroll, talent and workforce systems.
- [Production requirements](docs/PRODUCTION_READINESS.md) — explicit blockers to G42 eligibility and a staging/probation plan.
- [Evaluation](docs/EVALUATION_AND_METRICS.md) — authored scenario tests, latency benchmark methodology, reliability and failure register.
- [Video demonstration plan](docs/WATCH_THE_AGENT_WORK.md) — exact scenes/commands for recording real operation; **no finished video claimed**.
- [Submission evidence checklist](docs/SUBMISSION_CHECKLIST.md) and [version history](docs/VERSION_HISTORY.md).
- [Code](src/hcia/) and [tests](tests/); [benchmark script](scripts/benchmark.py).

## Run offline (zero paid tools / keys)
Requires Python 3.11+.

    cd "Agentic AI development/Human Capital Intelligence Agent"
    python cli.py executive_brief --entity ALL
    python cli.py total_rewards --entity CORP
    python -m unittest discover -s tests -v
    python scripts/benchmark.py

## Run the guarded API (development environment only)
    python -m pip install -r requirements.txt
    # Set HCIA_TOKENS_JSON, HCIA_AUDIT_HMAC_KEY and HCIA_AUDIT_DB in your shell.
    # See .env.example; it is a template, NOT an automatically loaded file.
    uvicorn src.hcia.service:app --host 127.0.0.1 --port 8080

Example request, with your configured token:

    curl -H "Authorization: Bearer YOUR_CONFIGURED_SECRET"       -H "Content-Type: application/json"       -d '{"capability":"executive_brief","entity":"ALL"}'       http://127.0.0.1:8080/v1/agent/run

The API refuses unauthenticated calls, wrong roles and entities, unexpected JSON fields, unsupported tools and operation without audit storage. It never modifies an employer system.

## Model integration
The domain tools **work without an LLM**. An optional summariser supports an operator-approved OpenAI-compatible HTTPS chat-completions endpoint, which can be placed behind an authorised sovereign model gateway. Only aggregate synthetic results are sent in this demo. Configure endpoint, allowlisted hostname, model and credential via environment variables; no credentials or G42 endpoint supplied and **no live sovereign model invocation performed**. Model text is not authoritative, cannot decide HR outcomes or execute tools.

## Important distinction
The job posting explicitly rejects prototypes and demands **enterprise production references, empirical benchmarks, security review, demonstration video and controlled probation**. This repository provides the first technical foundation and reproducible **local** evidence, not those qualifications. It would be misleading to submit this as a deployed agent today.

**Different from earlier portfolio agents:** the Enterprise Workflow Agent handles documents and case handoffs; the HR Policy Evaluation Agent tests policy answers; this project delivers a restricted **multi-domain aggregate intelligence interface** with access-scoped tool planning, traceable analytics and a sovereign-compatible narrative adapter.
