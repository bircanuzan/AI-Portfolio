# 04 — Stakeholder Communications

## Audience and schedule
| Audience | Frequency | Artifact |
| --- | --- | --- |
| Integration Engineering / client tech | Daily while P1 active | Blocker list, evidence and engineering owner |
| Client Product Owner | Twice weekly | Requirements and acceptance decisions |
| Product + Engineering managers | Weekly + escalation for P1 | Feature intake and resource trade-offs |
| Client PMO and sponsor | Weekly + immediate for material changes | RAG, root cause, owner, recovery date |
| Launch authority | Per gated milestone | Signed go/no-go and rollback evidence |

## Fictional client email — Atlas
**Subject:** Atlas integration | Data mapping approval affects critical path

The 23 October signoff for device/timestamp field mapping is still open. Engineering has completed the work that does not depend on the final mapping, but schema-dependent testing cannot be accepted. Could the Client Product Owner approve the field mapping by 30 October, or nominate a decision-maker for a short working session? I will circulate the revised sequencing and any release-date impact after that decision. We will not silently change the project baseline.

## Fictional escalation — Beacon
**Subject:** Beacon sandbox status RED | P1 webhook duplicate alerts

Beacon's 28 October sandbox milestone is blocked by a duplicate-event processing defect in this illustrative client scenario. Engineering is testing idempotency and replay, and the client technical lead must verify the negative-path evidence. We are holding readiness signoff until a passing rerun and formal acceptance are recorded. I will issue an owner/date update and any requested Product decision before the next steering meeting.

## Rule
Executive updates distinguish **evidence**, **interpretation**, and **requested decision**. Never report an untested fix, unapproved mapping or verbal launch promise as completed acceptance.
