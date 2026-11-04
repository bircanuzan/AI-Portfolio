# 03 | Solution Architecture, APIs, Data Model and Responsible AI

## Logical system flow
Marketplace lead webhook -> authenticated ingestion API -> consent and deduplication -> CRM event store -> approved listing-data retrieval -> optional LLM draft generator -> factuality/policy checks -> human agent approval -> CRM write-back -> event telemetry -> analytics / executive scorecard.

**No live vendor integration is implemented here.** This is a deployment-ready specification and a local deterministic demonstration.

## Data contract (example, JSON fields)
| Field | Type | Rule |
| --- | --- | --- |
| lead_id | string | Pseudonymous unique ID, required |
| agency_id | string | Allowed agency tenancy scope |
| received_at | UTC timestamp | Immutable source event |
| response_at | UTC timestamp / null | First valid human-approved response |
| consent_to_contact | bool | Explicit gate; false -> no draft or contact |
| listing_id | string | Only approved listing facts accessible |
| language | enum | Use supported language only; fallback to agent |
| booked_viewing | bool | Outcome recorded by CRM, not guessed |
| response_actor | enum | human / human_approved_assist; audit provenance |
| approval_event_id | string | Required for any assisted outbound message |

## Engineering conversation checklist
- API availability, webhook retry behaviour, idempotency keys and per-agency tenant isolation.
- CRM data contracts, field-level access, event ordering, deduplication and late-arriving events.
- Retrieval freshness and citation of listing availability/fees; no hallucinated claims.
- Provider latency/price, rate limits, outage fallback and language-specific evaluation.
- Human approval, edit/override reasons, audit logs and retention schedule.
- Post-release drift, prompt injection in free-text lead content, PII minimisation and incident shutdown.

## LLM contract — conceptual only
**Input:** approved non-sensitive listing attributes, customer inquiry with personal identifiers removed, contact preference, language, CRM-approved policy snippets.
**Output:** proposed agent-facing draft, provenance references, detected uncertainty, escalation reason and a no-draft status.
**Reject if:** customer consent missing, unsupported property claim, missing listing facts, prompt injection, prohibited sensitive inference or unsupported language. Agent sees citations and may edit/reject.

## Security and responsible-AI controls
Role-based tenancy, secrets management, encrypted transport/storage, region-appropriate retention, data subject request process, security review of LLM provider, no automated high-impact decisions and preproduction red-team/UAT. Applicable law and vendor contracts require legal review; this case study is not a legal compliance certification.

## Failure modes
- CRM or model unavailable -> manual triage, no silent queues.
- Conflicting listing price/availability -> abstain and request confirmation.
- Consent false -> hold; no text generation for outbound delivery.
- Timestamp missing -> exclude from SLA calculation, alert data owner.
- Unauthorized cross-tenant retrieval -> critical incident, freeze rollout.
