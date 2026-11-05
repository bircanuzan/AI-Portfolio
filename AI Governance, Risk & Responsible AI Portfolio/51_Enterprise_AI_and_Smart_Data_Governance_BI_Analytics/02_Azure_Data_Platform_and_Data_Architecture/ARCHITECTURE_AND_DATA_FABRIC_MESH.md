# Azure architecture blueprint — PROPOSED, NOT BUILT OR DEPLOYED

## System boundary
Hypothetical regulated UAE insurer. No access to Azure tenant, live data pipelines, cloud storage, identity, insurer's systems or client architecture; service recommendations below require licensed architects' review.

## Data flow / service responsibilities
1. **Source systems:** policy administration, claims core, broker portals, service/CRM, document stores. Design ingress per data-owner approval and purpose limitation.
2. **Ingestion:** Azure Data Factory for scheduled batch/CDC orchestration; Azure Event Hubs for prospective event streams. Secure private endpoints, managed identities, encryption and monitoring.
3. **Storage zones:** Azure Data Lake Storage Gen2 **raw/quarantined → validated → curated** zones; immutable audit trail and explicit retention. Claim attachments separated from analytics facts. No Emirates ID, phone, name, or free-text case narrative in the local demonstration.
4. **Transforms / features:** proposed Azure Databricks Spark jobs for validation, deduplication, feature engineering and governed derived tables. Use Delta Lake pattern if approved; define schema evolution contracts.
5. **Serving:** Azure Synapse or Azure SQL for curated marts, managed semantics to Power BI; separate governed analyst and executive roles. Exact product choice is subject to organization architecture/cost review.
6. **Model lifecycle:** Azure Machine Learning workspace proposal; registered model lineage, train/validation data snapshots, approval gates, model cards, monitored inference and rollback. Azure AI Services/Document Intelligence only when an OCR/NER use case has a separate PII/redaction and human-quality gate.
7. **Governance:** Microsoft Purview (or existing catalog) for catalog, lineage, owners and classifications; customer master / policy master hierarchy using existing MDM if available.
8. **Operational feedback:** capture human reviewer corrections, escalation timestamps, complaint incidents, schema/feature drift and source freshness for periodic model/rule assessment.

**Delivery evidence:** None of these Azure services were provisioned or executed for this case. Only a local pandas/scikit-learn synthetic demo is executable.

## Data fabric vs data mesh — pragmatic choices
- **Data fabric:** catalog, metadata-driven lineage, interoperability, policy enforcement and consistent discovery across storage and source systems; useful where existing tools are heterogeneous.
- **Data mesh:** data-domain ownership and interoperable data products, e.g. Claims, Policies, Customer (with strict permission controls), plus federated governance and self-service infrastructure.
- **Do not confuse them:** Fabric emphasizes shared metadata/integration capabilities; mesh emphasizes domain-accountable operating ownership. A program can combine both, but neither is a substitute for good data-quality controls.

## Data product contract (example)
- Name: claims_review_queue_v1; owner: Head of Claims; steward: Claims Data Steward.
- Grain: one distinct non-personal claim identifier per intake event, with explicit latest-version semantics.
- Fields: claim_id, event_time_utc, channel, amount_aed, missing_doc_count, triage_score, suggestion, model_version.
- Consumer: approved Claims Operations and Risk/Compliance teams; no open access.
- SLO: freshness target to be negotiated; reconciliation coverage and exception volumes explicitly monitored.
- Availability: primary/fallback to human manual queue on data/model outages.
- Change control: breaking schema changes require producer + consumer approval; retain contract tests.
- Retention/region/residency: legal/privacy decision with UAE insurer; no hard-coded assertion about mandated hosting jurisdiction.

## MLOps and CI/CD proposal (not implemented)
Feature contract → pipeline test → security scan → independent validation → approval to staging → shadow pilot → monitored human-review → rollback. Minimum monitoring: data completeness, drift, calibration, error rates, false-positive review burden, overrides, incident register, cost/latency, and audit-log integrity.

## Non-functional gates
RBAC/least privilege, data isolation, private connectivity, secrets rotation, encryption in transit/at rest, access logs, backups/DR, pen test, third-party assurance, approvals for cross-border transfers, retention/minimization, documented disaster and stop-switch procedures. Applicable UAE rules require counsel/compliance validation in the actual regulated context.
