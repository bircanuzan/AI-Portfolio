# AI Agent Résumé — Human Capital Intelligence Agent

**Agent identifier:** HCIA-DEV-001 | **Version:** 0.1.0 | **Current eligibility:** prototype, **not** production-qualified  
**Developer/portfolio author:** HumanEvoX (see developer profile)  
**Mission:** Governed, explainable, read-only cross-functional Human Capital intelligence for a multi-entity enterprise.

## Core capabilities and specialisation
- Talent Acquisition — source and hiring-funnel efficiency; conversion and aggregate cost-per-hire; no automatic candidate selection.
- Employer Branding — campaign visibility, engagement and synthetic mention-share metrics; no inference about people.
- Human Capital Operations — onboarding and employee-service SLAs, exception rates, control flags.
- Talent Management — review completion, workforce skills gaps, readiness for critical-role succession.
- Total Rewards — group/grade aggregate compensation index relative to **invented** comparator fixtures; minimum cohort suppression; no salary advice or equality determination.
- Organisation/Workforce — approved/occupied positions, vacancies, contingent mix, cost vs planned budgets.
- Executive Brief — orchestrates the six allowlisted tools and returns provenance, warnings and human-review requirements.

## Agent architecture
- **Compute:** Python 3.11, bounded deterministic tool planner and analytics functions.
- **Service:** guarded FastAPI HTTP endpoint; JSON schema validation; entity/role scoping.
- **Language model:** not required for tool execution. Optional operator-supplied OpenAI-compatible/sovereign model for *narrative-only* summarisation; no model run evidenced.
- **Persistence:** local SQLite HMAC-chained *demo* audit events, without storing queries, identity details or salary rows.
- **Inputs:** fictional aggregate JSON for local operation; separate HTTPS read-only mock-tested integration adapter.
- **Execution rights:** read-only analytics; no payroll/HRIS write capability; no personnel decisions, no self-authorisation.
- **Cloud deployment:** platform-neutral container recipe; Azure/Kubernetes deployment topology *designed*, not deployed.

## Differentiators
1. **Tool boundary:** model cannot select unknown tools or edit their calculations.
2. **Role/entity boundary:** roles independently limit domain access; analysts cannot access reward calculations unless assigned.
3. **Provenance:** each result identifies synthetic source section, data limitations and decision owner.
4. **Audit integrity:** HMAC chaining detects modifications to local event records in test conditions, without implying immutable enterprise storage.
5. **Sensitive-workforce guardrail:** rewards outputs are group-only and smaller cohorts are suppressed.
6. **Failure-by-default:** no API token, missing audit store or unallowlisted tool causes rejection or operational unavailability.

## Empirical evidence
See evaluation plan and executed CI/test artifacts when available. Tests evaluate synthetic fixtures; benchmark timing measures **in-process Python execution only**. No measured HR productivity/time saving, external LLM reliability, production SLA, G42 trial or bias evaluation across real employee groups has occurred.

## Deployment and references
**Production deployments:** none claimed. **Client organisations:** none claimed. **Enterprise integrations:** mock-tested contract only. **Testimonials:** none supplied. **Video demo:** storyboard/script available; finished video not recorded.

## Known failure modes
Unreconciled/missing HRIS data; nonrepresentative hiring and employer-brand samples; small pay cohorts; inconsistent aggregate definitions; role/identity misuse; audit database outage; external model latency or invented summary; unsafe HR impact extrapolation. Mitigations: validation, provenance, suppression, fail-closed access, human approval, explicit model fallback and real deployment gates.

**Do not submit this agent as meeting a production-only invitation until all evidence and deployment requirements are genuinely satisfied.**
