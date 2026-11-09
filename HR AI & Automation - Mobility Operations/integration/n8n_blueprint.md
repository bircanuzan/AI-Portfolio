# n8n / API / webhook integration blueprint (design, not deployed)

## Recommended topology
```text
HRIS change feed -- webhook gateway -+
Case mgmt events -- signed webhooks -+--> n8n intake workflow
Support portal ---- queue connector -+       |
                                        validate tenant + purpose
                                        assign idempotency key
                                        fetch minimally needed facts
                                                 |
                                       Python agent/checker service
                                                 |
                                      policy decision / human queue
                                                 |
                                       create case draft or hold
                                                 |
                                  event log + operational SQL model
```

## Workflow graph
1. **Webhook Trigger:** receive `mobility.case.created` or `hris.employee.changed` event, validate signature and UTC timestamps.
2. **Schema Validator:** allowlist fields, tenant-scoped keys, field-size limits; reject documents and secrets.
3. **Deduplicate Event:** transactional key `tenant_id:event_id` and case version. Replayed events return canonical status.
4. **Fetch Context:** REST GET approved HRIS and case metadata via OAuth2 least-privilege credentials; no indiscriminate employee profile fetch.
5. **Privacy Gate:** classify field sensitivity; send personal documents to protected human-only queue.
6. **Propose & Check:** invoke Python service returning `proposed_action`, `checker_pass`, `requires_human`, `reason_code`.
7. **Switch:** low-risk => create draft/case route; regulated => approval queue; unsupported => exception queue.
8. **Approval Wait:** reviewer decision signed with identity, role and timestamp; no generic LLM approval.
9. **Commit Action:** only allowlist actions; re-check authorization and idempotency at executor.
10. **Audit & Metric Event:** append minimized structured outcome, alert on repeated failures or denied operations.

## API contract examples
**Request**
```json
{
  "event_id": "evt-demo-010",
  "case_id": "MOB-101",
  "tenant_id": "sandbox",
  "case_type": "payroll_mismatch",
  "jurisdiction": "AE",
  "source": "case_management",
  "contains_sensitive_data": false,
  "metadata": {"effective_date_mismatch": true}
}
```
**Response**
```json
{
  "trace_id": "redacted-audit-ref",
  "case_id": "MOB-101",
  "proposed_action": "create_discrepancy_ticket",
  "disposition": "human_approval_required",
  "checker_passed": true,
  "policy_version": "v0.1"
}
```

## Production readiness dependencies
Connector authentication and authorization, endpoint SLAs, privacy basis, residency constraints, approved knowledge sources, secret rotation, alerting, retries, reconciliation, integration tests and human-review UI must be implemented and proven before deployment. n8n/Make/Zapier/Retool are potential orchestration technologies here; this design does not claim a live workflow in any platform.
