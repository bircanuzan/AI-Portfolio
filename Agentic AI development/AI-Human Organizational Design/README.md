# AI-Human Organizational Design | Agentic AI Development

**HumanEvoX | AI-Human Organizational Design**

**Status: synthetic engineering prototype, not a deployed enterprise agent.**

This renamed product preserves previous Human Capital Intelligence Agent engineering and evidence. Its Python import namespace remains `src.hcia` for compatibility. New product capabilities are added under the new directory; historical tests and demos remain labelled synthetic.


**[NEW: Human–AI Workforce Design Architect with native LLM tool-calling runtime](WORKFORCE_ARCHITECT_AGENT.md)** — implements an OpenAI Responses API plan→function call→observation→replan→submit loop, 7-task work design, scenario stress tests and future organization role validation. **GitHub Actions uses an explicitly scripted model stub, not real LLM inference.** Live model invocation is available only with operator-provided API credentials; no live result claimed.

**Author:** HumanEvoX independent engineering and HR transformation portfolio  
**Agent version:** 0.2.0 (synthetic engineering prototype) | **Role requirements reference:** ai_enterprise AI-Human Organizational Design (AI Agents Only)  
**Status: runnable read-only agent and API prototype using fictional aggregate data. NOT production deployed, NOT ai_enterprise-qualified, NOT submitted.**

## Working agent-runtime developer demonstration (separate from analytics slide demo)

**[Watch the executed agent tool trace (MP4)](demo/Agent_Runtime_Executed_Tool_Trace.mp4)** · **[Inspect the exact Python execution trace (JSON)](demo/Agent_Runtime_Execution_Trace.json)** · **[Review architecture and reproducibility](docs/DEVELOPER_AGENT_RUNTIME.md)**

This new developer demo executes the actual `HumanCapitalAgent` in `src/hcia/agent_runtime.py` and documents its **observation-dependent action selection**, real Python tool invocations, scenario recalculation, human-only decision gates and rejection of unsafe employment-action requests. The captioned video is a **replay of executed logs** rather than the earlier animated analytics presentation. Verification: 76 passing automated tests in [GitHub Actions](https://github.com/bircanuzan/AI-in-HR-Portfolio/actions/runs/41678692510).

**Scope of proof:** actual deterministic offline **test policy**, **not** a live LLM / production agent. An optional HTTPS model action selector has been implemented but **not configured or live-tested**.

```bash
python -m scripts.demo_agent_runtime
python -m unittest discover -s tests -v
```

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
| Human–AI Workforce Redesign | workforce_redesign | Task analysis, proposed job architecture, net-capacity scenario, reinvestment and illustrative future organisational structure |
| Executive coordination | executive_brief | **Six-tool orchestration** with provenance, human-review flags and no side effects |
| Goal-based read-only orchestration | bounded planner | Offline goal-to-tool routing and optional LLM-proposed, validated 1–3 tool plans; no HR actions |

**Demonstration company:** Cedar Gulf Enterprise (invented); 3 entities, 102 approved seats, 89 occupied seats, 13 vacancies and 18 contingent workers. All workforce and pay data are fictional aggregates. A separate **fictional Group People Services workforce redesign pilot** models seven activity groups, eight future roles, a seven-unit proposed structure and potential capacity reinvestment; do not confuse its workload-equivalent FTE with real employee headcount. No names, IDs or other individual records are included.

## Repository navigation
- [Agent résumé](AGENT_RESUME.md) — agent functionality, roles, technology and restrictions.
- [Developer profile](DEVELOPER_PROFILE.md) — truthful authorship/experience, not a traditional candidate CV presented as an agent.
- [System architecture](docs/ARCHITECTURE.md) — API, bounded planner, analytics, optional sovereign model, trust boundaries and deployment patterns.
- [Security / Responsible AI](docs/SECURITY_RESPONSIBLE_AI.md) — role and entity scoping, personal-data controls, audit, review responsibilities and threats.
- [Integration contract](docs/INTEGRATION_SPEC.md) — read-only mock-tested HTTPS adapter for HRIS, ATS, payroll, talent and workforce systems.
- [Human–AI Workforce Redesign case, methods and safeguards](docs/HUMAN_AI_WORKFORCE_REDESIGN.md) — actual runnable task-to-job-to-future-structure scenario with illustrative role profiles, capacity reallocation and governance.
- [Production requirements](docs/PRODUCTION_READINESS.md) — explicit blockers to ai_enterprise eligibility and a staging/probation plan.
- [Evaluation](docs/EVALUATION_AND_METRICS.md) and [verified execution evidence](evidence/EXECUTION_EVIDENCE.md) — 67 automated tests and 12/12 original numeric benchmark scenarios verified in GitHub Actions; local latency figures reflect only in-process runs.
- [Watch the Agent Work — committed MP4](https://github.com/bircanuzan/AI-in-HR-Portfolio/blob/main/Agentic%20AI%20development/AI-Human%20Organizational%20Design/demo/Human_Capital_Intelligence_Agent_Synthetic_Demo.mp4) — a new 1080×1350 portrait video generated from actual execution of the HR intelligence and workforce redesign simulation, saved in this GitHub folder. **Not a production screencast.** [Recording plan](docs/WATCH_THE_AGENT_WORK.md).
- [Submission evidence checklist](docs/SUBMISSION_CHECKLIST.md) and [version history](docs/VERSION_HISTORY.md).
- [Code](src/hcia/) and [tests](tests/); [benchmark script](scripts/benchmark.py).

## Run offline (zero paid tools / keys)
Requires Python 3.11+.

    cd "Agentic AI development/AI-Human Organizational Design"
    python cli.py executive_brief --entity ALL
    python cli.py total_rewards --entity CORP
    python cli.py workforce_redesign --entity ALL
    python -m src.hcia.workforce_design
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

## Goal-directed agent planning

The authenticated API exposes `workforce_redesign` for group-scoped synthetic scenarios and also POST `/v1/agent/orchestrate` for an authorised people leader. A safe aggregate question such as `Review recruiting and headcount` selects the Talent Acquisition and Workforce Intelligence tools, executes them locally and returns a source-grounded plan and audit reference. Unsafe, identifying and state-changing prompts are refused. See `src/hcia/planner.py` and `tests/test_orchestrator_api.py`.

## Model integration
The analytics engine runs offline without an LLM. An optional operator-approved OpenAI-compatible/sovereign HTTPS endpoint may propose a strictly allowlisted **1–3 step tool plan** and/or summarise synthetic aggregate results. The model never executes a tool directly, cannot edit computed numbers or approve HR outcomes, and outputs require independent validation. No ai_enterprise sovereign endpoint or live model inference has been used in this demonstration.

## Important distinction
The job posting explicitly rejects prototypes and demands **enterprise production references, empirical benchmarks, security review, demonstration video and controlled probation**. This repository provides the first technical foundation and reproducible **local** evidence, not those qualifications. It would be misleading to submit this as a deployed agent today.

**Different from earlier portfolio agents:** the Enterprise Workflow Agent handles documents and case handoffs; the HR Policy Evaluation Agent tests policy answers; this project delivers a restricted **multi-domain aggregate intelligence interface** with access-scoped tool planning, traceable analytics and a sovereign-compatible narrative adapter.
