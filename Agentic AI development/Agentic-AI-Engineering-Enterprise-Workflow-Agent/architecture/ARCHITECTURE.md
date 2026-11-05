# Architecture, tasks and trust boundaries

~~~mermaid
flowchart TD
  A[User or n8n webhook] --> B[FastAPI run endpoint]
  B --> C{Requested action?}
  C -->|Yes| D[SQLite pending request]
  D --> E[Human approver with separate secret]
  E --> F[Record local approval or rejection]
  C -->|No| G{Case ID present?}
  G -->|Yes| H[Configured HTTPS read-only Case API]
  G -->|No| I[Retrieve versioned local Markdown]
  I --> J{LLM key configured?}
  J -->|Yes| K[LLM with bounded policy context]
  J -->|No| L[Evidence-only offline preview]
  H --> M[Status and safe error handling]
  K --> M
  L --> M
  F --> N[No external write performed]
~~~

## Human vs deterministic vs AI

| Work | Owner |
|---|---|
| Authorize sensitive changes, policy exceptions, employment decisions | Human only |
| ID validation, routing, local persistence, HTTPS client, timeouts | Deterministic Python |
| Natural-language answer from retrieved context | LLM only when API credentials supplied |
| Orchestrate intake and backend handoff | n8n |
| Source approval and version control | Human policy owner |

## Guardrails and deployment gaps
- Read-only access is separated from approvals. The approval endpoint writes to a local SQLite demo table only, and does not invoke downstream services.
- Run endpoint is NOT authenticated or rate-limited; do not host publicly until OAuth/OIDC, user identity, audit controls, CORS restrictions, secrets management, rate limiting, data retention, and access reviews are implemented.
- Allowlist the exact LLM and case API hosts via infrastructure/network policy, not prompt text.
- Prompt injections inside retrieved documents are mitigated by role separation but not conclusively solved; add hostile-document tests.
- SQLite is a local demonstration store, not appropriate for high-volume distributed services.
- Never send personal or regulated information to external model endpoints without documented enterprise approval and data protections.
