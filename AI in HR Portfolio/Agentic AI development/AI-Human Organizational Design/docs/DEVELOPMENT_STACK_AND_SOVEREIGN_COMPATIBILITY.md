# Recommended engineering stack and G42 ecosystem alignment

## Recommendation

**Python 3.11+ and FastAPI** remain the implementation foundation. Keep the existing native Responses-style function-calling agent and deterministic workforce calculators. **LangGraph** is the preferred future orchestration layer *if* checkpointed multi-agent workflow complexity justifies it; benchmark it against the current bounded runtime.

For enterprise delivery, target **Azure AI Foundry (Azure Agent Foundry)**, signed identity (Entra ID), protected secrets (Key Vault), audit/observability and container deployments.

For G42 compatibility, prioritize **Core42 Compass** model APIs and documented **OpenAI Agents SDK** support. This is a *planned adapter*, not an actual connection. **Inception42 Catalyst** is G42's sovereign agent operating system; external developer/partner access and compatibility must be verified before using it.

| Layer | Choice | Evidence status |
|---|---|---|
| Analytics and capacity | Python deterministic tools | Locally executable on fictional cases |
| Model tool calling | Existing native Responses implementation | Offline scripted-provider tests; real hosted model not yet verified |
| Agent orchestration | LangGraph | Planned; must be evaluated |
| Model provider | Core42 Compass model APIs | G42-aligned published documentation; no tenant or API key connected |
| Enterprise agent platform | Azure AI Foundry | Inception42 job posting confirms used technology; no deployment |
| Agent operating system | Inception42 Catalyst | Partner access not verified |
| App/API | FastAPI + container | Local prototype; no production hosting |
| Retrieval/data | Approved RAG, SQL/graph, vector stores | Planned; cannot use live HR data without authorization |
| HR systems | Oracle Fusion, Workday, SAP, ATS/LMS | Read-only contract patterns; not connected |
| Governance | Human approvals, RBAC, audit, red teaming, evals | Synthetic safeguards; independent assurance pending |

## Verified ecosystem signals

- Inception42's **7 November 2026** Data Engineer vacancy names Azure Agent Foundry, OpenAI, LangChain, n8n, RAG, knowledge graphs, Azure Databricks and Fabric: https://jobs.g42.ai/Inception42/job/Abu-Dhabi-Data-Engineer-Abu/733373322/
- Inception42 states Catalyst agents are served through Compass and surface into Microsoft 365 Copilot: https://www.inception42.ai/news/Inception42-Microsoft-AgenticAI
- Core42 officially documents OpenAI Agents SDK integration with Compass: https://www.core42.ai/compass/documentation/agents-sdk
- Core42 offers REST and region-specific Responses APIs: https://www.core42.ai/compass/documentation/response-api-reference
- G42 requires live deployment and empirical validation: https://github.com/G42-Careers/Agent-Jobs/blob/main/AGENTS.md

**Not verified:** identities or selected toolchains of the external agent developers admitted by G42. An internal team job posting is not evidence that all G42 submissions use that stack.
