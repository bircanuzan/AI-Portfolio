# SAP Employee Central replication and engineering specification

## Fictional adapter input (not an SAP API payload)
```json
{"source":"SAP_SUCCESSFACTORS_EC","event_id":"SAP-001","person_id_external":"SYN-200","event":"TRANSFER","effective_start_date":"2026-11-03","company":"UAE_DEMO_01","approved":true,"version":1}
```

## Mapping decisions
| Fictional field | Normalized event | Control |
|---|---|---|
| `person_id_external` | `worker_key` | Not a real employee number; scope by legal entity |
| `event` | `event_type` | Explicit HIRE, TRANSFER or EXIT |
| `effective_start_date` | `effective_date` | Validate ISO date before process |
| `company` | `legal_entity` | Map to approved legal-entity reference |
| `approved` | `approved` | Must be boolean true to accept into downstream staging |
| `version` | `version` | Positive integer for idempotent replay handling |
| `event_id` | `event_id` | Nonblank correlation key |

## Replication runbook
1. Confirm source API is OData or CompoundEmployee based on real target needs.
2. Collect the authoritative SAP documentation applicable to the licensed release.
3. Establish integration user/RBP/permission audit, minimal field set and delta checkpoint.
4. Handle paging, retries, error codes, rate limits and restartability; never assume exactly-once delivery from upstream.
5. Compare received, accepted, quarantined and replay-suppressed event counts.
6. Preserve a safe audit trail and route mapping or approval failures to qualified HRIS stewards.
7. Maintain privacy, lawful transfer and retention controls across legal entities.

## Failure scenarios
- Wrong/expired delta checkpoint
- Overlapping effective-dated employee changes
- Missing permission to a required EC field
- Termination with unsettled downstream request
- Duplicate API replay after timeout
- Rejected legal entity or approval evidence
- Data deletion/retention request requiring specialist handling

The **shared integration lab** demonstrates only a custom canonical mapping. It does not parse real CompoundEmployee SOAP XML nor guarantee compatibility with SuccessFactors APIs.
