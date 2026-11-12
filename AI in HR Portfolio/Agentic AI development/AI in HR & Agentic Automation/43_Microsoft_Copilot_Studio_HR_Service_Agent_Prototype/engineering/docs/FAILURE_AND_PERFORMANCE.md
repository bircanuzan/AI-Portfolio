# Hardening backlog and non-functional validation

## Priority gaps
1. **Semantic quality:** local hashed lexical vectors are not neural embeddings; test OpenAI embedding and LangChain model calls with strict source/answer adjudication, negative and adversarial holdout examples.
2. **Scale:** benchmark retrieval with 10k+ synthetic policies, p50/p95 latencies, query throughput, SQLite contention and index construction cost. Move to managed vector/hybrid search only if measured demand warrants.
3. **Pipeline robustness:** persistent quarantine, records removed from source, schema drift, duplicate source IDs across feeds, one authoritative timezone, watermark/CDC, replay and rollback.
4. **Data protection:** TLS + Entra/OAuth, RBAC/ABAC, retention, encryption, permission-aware retrieval, prompt-injection against connectors, safe logging and incident playbooks.
5. **Process correctness:** verify asynchronous human approval/denial, timeout handling, idempotent case creation and no action on failed approval with real n8n/Teams/Power Automate execution history.
6. **Model operations:** per-version evaluation, agent config hashes, token usage, drift, trace IDs, spend caps, model rollback, independent reviewer sampling.
7. **DevOps:** container scan/SBOM, version pinning, CI run attestations, staged promotion, service-level monitoring, exception alerts and recovery drills.

## Acceptance before calling this a deployment
Never call a source-code stub a hosted integration. For each tool claim, supply configuration ID, request/response trace, cost/identity/region, failed-case trace, independent signoff and a screen recording of the actual system — all with PII removed.
