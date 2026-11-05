# Deployment discovery and QA checklist (proposed; not implemented)

## Commercial discovery
- Identify one high-volume, low-risk customer journey with a measurable baseline.
- Record stakeholders: business owner, IT, InfoSec, legal/privacy, contact-centre operations, customer success.
- Define a pilot population, escalation path, existing licences/telephony constraints and per-conversation economic assumptions.
- Agree executive value proposition and explicit boundaries of product demonstration.

## Technical verification by customer's engineers
- API specifications, permissions, authentication, throttling and error responses reviewed.
- Knowledge-base provenance and update ownership agreed.
- Human handoff successfully tested (including after interrupted speech).
- Privacy consent, retention, cross-border handling and sensitive data filtering approved.
- Network/telephony, recording and incident-management controls signed off.
- Accessibility, voice quality, multilingual QA and native speaker tests completed.
- Load, latency, reliability, concurrency and recovery evaluated under realistic workload.

## Agent QA acceptance matrix
| Test type | Case | Expected outcome |
| --- | --- | --- |
| Next reply | Asked for personal account status | Do not hallucinate status; secure transfer |
| Tool call | General FAQ lookup | Only allowlisted read-only tool, correct arguments |
| Simulation | Multi-turn clarification and transfer | Consistent handoff; no invented booking or status |
| Security | Prompt injection in retrieved content | Ignore untrusted directives |
| Robustness | Timeout/error from a tool | Apology, retry policy, support fallback |
| Language | UAE Arabic and English speakers | Native-speaker verified, no incorrect translation |

## 30-day pilot dashboard
Track: sessions, human transfer %, successful resolution %, unknown evaluation %, p95 latency, tool failure %, estimated cost per completed interaction, opt-out/complaint rate. Segment by language and intent; investigate failures without uploading sensitive audio to unapproved systems.

**Portfolio caveat:** this is a design document and test plan. There is no claim that the above verification or live launch has been performed.
