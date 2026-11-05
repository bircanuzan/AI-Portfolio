# HumanEvoX private HR agent web app — deployment status

**As of 2026-11-02: deployable code, not a verified public deployment.** This project contains a browser chat interface, authenticated FastAPI backend, live-model adapters for OpenAI Agents SDK or a separately running local Qwen server, and regression tests. No production HRIS, real client records, or active hosted URL is claimed.

## Real model execution

1. The user enters a private pilot access token in the browser, retained only in memory.
2. The server verifies a secret, restricts request frequency, screens for obvious personal identifiers, and retrieves synthetic policy content.
3. Sensitive, unknown, or approval-bound questions are routed by deterministic safety controls.
4. For standard supported questions, an actual model is invoked: OpenAI Agents SDK with a server-side API key, or a self-hosted llama.cpp chat-completions endpoint.
5. Raw LLM drafts are NOT published as verified HR policy facts; the response uses the approved policy text. No HR action is executed.
6. Logs record request ID, decision category and policy ID, not question transcripts.

This is currently a guarded LLM-assisted FAQ pilot, not an autonomous production HR workflow engine. In particular, the GitHub Actions Qwen model runs temporarily and is not an always-on model endpoint.

## Run locally

Install requirements-service.txt, set a long private HUMANEVOX_APP_TOKEN and HUMANEVOX_MODEL_PROVIDER=openai plus a private server-side OPENAI_API_KEY, and start from the project directory:

    python -m pip install -r requirements-service.txt
    python -m unittest discover -s tests -v
    uvicorn service.api:app --host 127.0.0.1 --port 8000

The browser interface will be available at http://127.0.0.1:8000, provided the agent and credentials are configured.

## Hosting

Repository-root render.yaml is an optional Render blueprint for this project. It specifies a free-plan web service that may sleep when idle, not guaranteed continuous uptime. The hosting account owner must authorize provider connections and securely configure any model credentials; ChatGPT cannot create user-owned API keys or approve billing. A 24/7 production service will generally need appropriate paid infrastructure.

## Before handling real employee or client data

Replace the shared pilot token with individual SSO/OIDC identities and role-based permissions. Add authorized policy ingestion, versioned retrieval, access-controlled storage, a true approval queue, encryption, retention and deletion controls, UAE-law and contractual privacy assessment, distributed rate limiting, security review, reliability monitoring, independent factual accuracy testing, and an incident response plan.

Do not use this synthetic pilot to make employment decisions or advertise it as a compliant production HR system.
