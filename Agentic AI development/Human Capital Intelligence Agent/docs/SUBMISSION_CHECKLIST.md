# AI-Agent-only application pack | Status and provenance

| Submission artefact | File / evidence | Status |
|---|---|---|
| Agent profile / specialisation | AGENT_RESUME.md | Written, prototype-qualified |
| Agent and developer resumes | AGENT_RESUME.md; DEVELOPER_PROFILE.md | Drafted, verify details before external use |
| Technical architecture / model / boundaries | docs/ARCHITECTURE.md | Documented; sovereign model not connected |
| Features and differentiators | README.md; AGENT_RESUME.md | Implemented locally with synthetic data |
| Security and responsible AI | docs/SECURITY_RESPONSIBLE_AI.md | Scope controls; full independent audit missing |
| Structured HC analytics | src/hcia/engine.py | Implemented on synthetic data |
| HRIS/ATS/payroll integration | src/hcia/integrations.py | Mock tested only, not enterprise-connected |
| Benchmarks and stress results | tests/; scripts/benchmark.py | Local scenario and latency testing, no load test or enterprise outcome |
| Deployment status | docs/PRODUCTION_READINESS.md | **NOT DEPLOYED** |
| Client references / testimonials | None | **NOT AVAILABLE** |
| Video recording | docs/WATCH_THE_AGENT_WORK.md | Script available; **NO RECORDED VIDEO** |
| Sovereign LLM operation | src/hcia/llm.py | Optional adapter, **NO CONNECTED MODEL** |
| Productivity gains / savings | None | **NOT MEASURED** |
| Controlled probation | None | **NOT PERFORMED** |

**Submission recommendation:** do not represent the agent as eligible for a live-production-only application at present. First create genuine enterprise usage, evidence and security maturity.
