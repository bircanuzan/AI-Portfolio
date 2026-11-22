# AI Automation — Agentic Reference Architecture

## High-level process

```text
Inbound intake (form / API / webhook / batch)
  -> identity and schema checks
  -> classify request, sensitivity and ownership
  -> policy gates (RBAC / allowlisted tools / PII restrictions)
     -> BLOCK: audit + reviewer queue
     -> HUMAN REVIEW: secure approval queue, never execute without authorization
     -> LOW RISK: draft answer / propose action only
  -> evaluate content (groundedness, completeness, hallucinations, policy adherence)
  -> publish only after required approvals
  -> structured trace, cost/latency logs, KPI dashboard
```

## Suggested implementation modules

1. API gateway: FastAPI/REST, OAuth2 or managed identity, per-request correlation IDs, JSON Schema validation.
2. Orchestrator: n8n, Power Automate or LangGraph for durable workflow states, retries, idempotency and human approval.
3. LLM/agent: Azure AI Foundry and approved LLM APIs for narrowly scoped classification/summarization; constrained structured outputs.
4. Retrieval: approved knowledge base indexed for RAG with citations; no unrestricted customer record access.
5. MCP/tool integration: tool registry with permissions, dry-run mode and allowlists; run actions only with valid authorization.
6. Evaluation: golden test sets, rubrics, prompt-injection/adversarial tests, execution traces; human feedback.
7. Analytics: SQL event store, Python/pandas aggregation, Power Query/Power BI or Tableau dashboards, MLflow/W&B where applicable.
8. Operations: GitHub CI, secrets manager, error monitoring, audit retention policy and formal UAT/rollback.

## Human-in-the-loop boundaries

- No automated hiring or rejection decisions, account/bank detail changes, payment/refund execution, broad record exports or changes to salary.
- Each sensitive request requires authenticated reviewer approval and records actor, scope and decision.
- Prompt injection, policy conflicts and absent source evidence route to review or block.
- The local demo implements only a subset of these boundaries; do not treat the architecture description as deployed controls.

## Build phases (proposed, not claimed delivered)

- Phase 1: synthetic process simulation and local tests (in repo).
- Phase 2: connected sandbox agent and read-only APIs; golden datasets and trace capture.
- Phase 3: human-reviewed pilot and privacy/security checks.
- Phase 4: monitored deployment with audit, cost and operational SLAs.
