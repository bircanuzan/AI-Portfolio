# Oracle-specific solution-engineering handoff

## Fictional source event
The following is a **custom synthetic adapter input**, not an Oracle REST, HDL, Extract or Atom payload:

```json
{"source":"ORACLE_FUSION_HCM","event_id":"ORC-001","person_number":"SYN-100","action":"HIRE","effective_date":"2026-11-03","legal_entity":"UAE_DEMO_01","approved":true,"version":1}
```

## Source-to-canonical mapping
| Adapter field | Canonical field | Business validation |
|---|---|---|
| `source` | `source_system` | Known supported simulator only |
| `event_id` | `event_id` | Nonblank; unique per source, legal entity and version |
| `person_number` | `worker_key` | Pseudonymous test value |
| `action` | `event_type` | Approved event type (HIRE/TRANSFER/EXIT) |
| `effective_date` | `effective_date` | Strict ISO calendar date |
| `legal_entity` | `legal_entity` | Approved reference-data mapping |
| `approved` | `approved` | Explicit `true` boolean before outbound publishing |
| `version` | `version` | Positive integer, replay-sensitive |

## Engineer-ready checklist
1. Agree source objects, person/assignment identifier semantics and legal entity mapping with HRIS owner.
2. Validate actual Oracle endpoint/feed/extract support and permissions with IT and the vendor.
3. Document transport/authentication, secrets, retries, idempotency, schema evolution and redaction.
4. Write mapping specification and tests: missing key, duplicate event, retroactive date, unsupported action, wrong entity, unapproved request, invalid payload.
5. Send only approved canonical records to controlled **staging**, not to payroll or live systems.
6. Reconcile `source_received = accepted + rejected` at batch level. Investigate pending/failed delivery separately.
7. Obtain HRIS, HR Ops, Security and downstream consumer sign-off before deployment.

## Build/test evidence
The [offline adapter lab](../04_HRIS_HCM_Integration_Solution_Engineering_Lab/README.md) implements this schema with standard-library Python and synthetic data. It does not authenticate to Oracle or invoke any vendor API.
