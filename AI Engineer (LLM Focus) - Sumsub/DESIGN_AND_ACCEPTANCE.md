# Multi-Turn Compliance Copilot — Engineering Design and Acceptance

## Goals
Implement a stateful AI assistant for **fictional** compliance work that responds to follow-up questions, retrieves allowlisted case information, cites permitted evidence, and escalates inconclusive or high-impact decisions. This is a **design specification**, not a claim of live production implementation.

## System design
**Gateway → session/auth → LangGraph agent → policy router → approved tools/MCP → retrieval → answer validation → tracing/evaluation.**

- A typed conversation state persists only for an authorized thread; strict TTL, redaction and access boundaries are required.
- The graph has explicit planning, tool execution, verification, escalation and END nodes, with a hard per-request step budget.
- Tools declare JSON-schema contracts, allowlisted arguments and permission scopes. A tool error is classified as transient, permanent, unsafe or unauthorized.
- Transient errors trigger finite retries with exponential backoff and jitter; permanent errors trigger a transparent user-facing fallback, not repeated tool calls.
- Every external action must be separately authorized; prototype tools are read-only and synthetic.
- Unknown/unsupported facts result in abstention, provenance labels, or human review rather than invented KYC/AML recommendations.
- RAG evaluates retrieval recall, groundedness, citation coverage and potentially conflicting source versions.
- Observability captures trace IDs, tool-call count, duration, token/cost budgets, failure classes and human-escalation triggers, subject to PII minimization.
- Offline evaluation uses fixed adversarial and regression cases; A/B tests compare outcome quality, latency and cost with predefined stopping rules.

## Production-readiness checklist (not yet claimed completed)
- [ ] Multi-turn conversation restoration across processes with an approved persistent store.
- [ ] All tools: schema validation, authz, timeout, retry limit and idempotency tests.
- [ ] Loop-stopping tests for cyclic prompts, repeated failing tools and token budget exhaustion.
- [ ] Isolation of users/tenants; redaction; audit trail; retention policy.
- [ ] Multi-model API integration, RAG index, reference answer dataset and grounding verification.
- [ ] Model/agent tracing and regression tests recorded in CI.
- [ ] Containerized service integration with Java/Dropwizard and GCP/AWS Kubernetes, verified in a staging environment.
- [ ] Human review and incident response, including stop conditions for misclassification.
- [ ] Actual deployment/SLI evidence before stating that it is production-shipped.

## Connection to existing implemented examples
- [LangGraph human approval](../Agentic%20AI%20Orchestration/01-LangGraph-Human-Approval-Workflow/README.md) implements basic deterministic graph routing (not multi-turn/tool-calling).
- [MCP skills tools](../Agentic%20AI%20Orchestration/02-MCP-Skill-Inventory-Tools/README.md) exposes read-only synthetic data (not a KYC API).
- [LangSmith example](../Agent%20tracing%20and%20testing/01-LangSmith-Agent-Decision-Traces/README.md) demonstrates tracing for a local rule (not a deployed LLM observability pipeline).
- [RAG assessment](../RAG%20evaluation/README.md) provides distinct groundedness/response-quality prototypes.

## Interview evidence rule
Explain what was actually authored, what was prototype-only, what is a design proposal, and what is production-validated. Never imply that a design checkpoint or demonstration equals a shipped commercial AI copilot.
