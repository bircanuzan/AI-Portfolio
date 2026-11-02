# 05 — Feature Requests, Product Escalation and Change Control

Each request is logged in [feature_requests.csv](../data/feature_requests.csv) with a business outcome, impact, owner, status, due date and blocking dependency.

## Status transitions
New -> Triaged -> In Progress -> Testing -> Done. Alternative dispositions are Deferred or Rejected with written rationale. Blocked work requires a clear unblock owner.

## Worked request: BE-F01
1. Client reports duplicated alerts after webhook retries.
2. Engineering captures reproducible *synthetic* replay behavior and expected event-id semantics.
3. TPM marks the milestone blocked; Product and Engineering assess if correction is defect repair or contract change.
4. Product accepts priority; Engineering owns the solution; Security reviews audit effects.
5. Client technical lead signs negative-path and duplicate suppression test evidence.
6. TPM updates critical-path dates and executive status; no unapproved launch commitment.

## Formal scope change
Record rationale, expected value, acceptance criteria, interface/security impact, engineering estimate, resource conflicts across both clients, schedule impact, commercial effect if any and named Product/client approval. Re-baseline after decision, never before it.

**Metrics:** triage lead time, request aging, blocked items, reopened defects, accepted versus deferred backlog, schedule and capacity impact.
