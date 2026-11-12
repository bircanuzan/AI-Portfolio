# 05 — Data, AI and MLOps architecture + executive governance

## Data reference design
Extract only authorized Oracle/CRM fields using supported interfaces. Register catalog classifications and contracts. Ingest permitted data through Data Factory to ADLS Gen2; apply validation, deduplication and pseudonymization; curate a semantic KPI layer. Power BI consumption uses appropriate row-level and workspace security.

## AI solution choices
1. **Rules and automation first** for deterministic approvals or reconciliation.
2. **RAG / knowledge assistance** only for approved, permission-filtered documents, with Azure AI Search and an approved language-model endpoint, citations and abstention.
3. **Predictive ML** only where labels, ownership and real business performance justify Azure Machine Learning lifecycle. Define train/validation/test splits, feature/data governance, registry, monitored predictions, drift and retraining approval.
4. **Human-in-the-loop** for HR, finance and any consequential decision; agents cannot authorise their own transactions.

## Architecture governance
TOGAF-inspired business/application/data/technology views, capability map, ADRs and reviews. Not a TOGAF certification claim.

## Security and risk
Microsoft Entra ID, least-privilege RBAC, private networking when supported, managed identity, Key Vault, secure API gateway, tenant boundaries, Purview-style lineage, Azure Monitor and incident runbooks. Validate data residency with legal and provider constraints; do not presume a particular Azure region makes every dataset compliant.

## Success measures
Data reconciliation pass rate, source-to-report latency, API error/timeout rate, dashboard adoption, p95 response latency, protected data access violations, AI answer grounding quality, operational cost per transaction and stakeholder acceptance. Baselines and targets require real customer validation.

## ADR 001
**Decision:** Use durable queues for long-running Oracle-to-portal updates rather than synchronous two-phase writes. **Reason:** safer failure isolation and retries. **Trade-off:** eventual consistency and idempotency overhead. **Open dependency:** API rate limits and transaction semantics.

## ADR 002
**Decision:** Prefer managed PaaS to AKS for first PoV unless workload/NFRs justify Kubernetes. **Reason:** smaller operations surface. **Trade-off:** less low-level control. **Open dependency:** security and runtime compatibility.

## ADR 003
**Decision:** Avoid production LLM tool execution until security review, scoped tool credentials, evaluation and human override are approved. **Reason:** consequence and privacy risk.
