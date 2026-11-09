# HRIS, ATS, Payroll, Talent and Workforce integration contracts

## Current state
A working **mock-tested generic HTTPS read-only connector** is implemented in src/hcia/integrations.py. It has five allowlisted source labels: hris, ats, payroll, talent and workforce. The operator supplies a full HTTPS endpoint, bearer token and exact hostname allowlist; the API never lets user prompts supply an arbitrary URL.

## Illustrative common payload (fictional)
```json
{
  "schema_version": "1",
  "source_system": "synthetic ATS",
  "entity_id": "CORP",
  "period": "2026-Q3",
  "aggregates": {"applicants": 100, "hires": 6}
}
```

Schema validation requires aggregate scalar values, a period, entity ID and source. Explicit individual/PII identifiers and nested record arrays are rejected. The example uses only fictitious statistics.

## Mapping for intended platforms
| Source type | Possible product / interface | Desired read-only fields | Validation |
|---|---|---|---|
| HCM / HRIS | Oracle Fusion HCM, SAP SuccessFactors, Workday | approved/filled positions, organizational hierarchy and legal entity aggregate | effective date, status, entitlement, cross-entity consistency |
| ATS | Greenhouse, Lever, Workday Recruiting, Oracle Recruiting | stage-level funnel and source mix aggregates | funnel monotonicity, deduplication, period, source IDs |
| Payroll / Total Rewards | authorised payroll or compensation data mart | band/grade aggregates, approved wage budget | small-cell suppression, compensation access and data lineage |
| Talent / L&D | enterprise talent management and LMS exports | completion, gaps, succession-coverage aggregates | data dictionary, denominator and temporal coverage |
| Workforce BI | approved financial and HR reporting system | occupancy and FTE/headcount budget | controlled cost centres, effective dates, auditable snapshots |

## Azure and sovereign interoperability
The agent core has no cloud SDK dependency; integration code uses standard HTTPS, and optional model narrative uses an OpenAI-compatible chat-completions payload. Adapting a real ai_enterprise sovereign endpoint requires documented service contract, approved access, authentication, network policy and test evidence. **No ai_enterprise infrastructure integration is represented or claimed.**

## What remains to integrate safely
Source-system permissions; enterprise OAuth2/service identities rather than simple tokens; policy-driven API routes; signed canonical data contracts; reconciliation between HRIS/payroll/Finance; real data warehouse or data-mart ingest; employee privacy impact assessment; private network connectivity; error retry/idempotency and batch pagination; observability. The current engine deliberately uses only fictional fixtures, not live connector payloads.
