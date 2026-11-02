# Power Automate solution design — public overview

**Status:** proposed configuration. This document is not an importable flow package or evidence of a working integration. Detailed operational templates and tenant configuration are not published.

## Microsoft 365 components

| Component | Proposed role |
|---|---|
| Microsoft Forms | Organisation-only request intake |
| SharePoint list | Controlled request and status register |
| Power Automate cloud flow | Validation, routing, approval and notifications |
| Approvals | Authorised HR decision with an outcome record |
| Outlook | Private acknowledgement and status email |
| Teams | Restricted HR operational alerts containing request reference only |
| Copilot in Power Automate | Optional maker assistance during design and explanation |

Tenant availability, service permissions, connector policies and applicable licences must be checked before implementation. Copilot availability is not assumed. The flow can be configured manually if it is unavailable.

## Proposed flows

### A. Automated intake and approval
**Trigger:** a new response is submitted in the designated Microsoft Form.

**Action sequence:** retrieve response details; create or identify the request by unique intake reference; validate service type and mandatory fields; look up the authorised HR approver; acknowledge receipt; start approval; record outcome; notify the appropriate person.

For the standard service, propose an Approve/Reject approval assigned to the HR approver. A rejection closes with a recorded explanation. Approval moves the request to **Ready for preparation**, not Completed. Unresolved routing moves it to **Exception**.

### B. Scheduled follow-up
**Trigger:** recurrence during the pilot's agreed service hours.

Check pending requests and alert the HR owner when a configured due date is passed. Reminders must not approve requests, create duplicate approvals or silently alter the original due date. For the pilot, use an illustrative two-business-day target and document the business calendar before configuration.

### C. Controlled closure
**Trigger:** an authorised HR officer records that the letter was checked and delivered.

Confirm approval exists and record delivery evidence before changing status to **Completed**. Any optional completion email must avoid attaching confidential records to an unverified address.

## Proposed record and status model
The request register needs a request ID, intake reference, requester identifier, service type, created timestamp, HR owner, approval ID, approval outcome/timestamp, status, due date, completion timestamp and exception reference. Avoid storing unnecessary personal detail in notifications or logs.

**States:** Received; Needs clarification; Pending approval; Ready for preparation; In preparation; Completed; Rejected; Exception; Cancelled.

**Key gate:** Completed requires both a valid approval and delivery confirmation. Recovery from Exception returns to the last verified state after human review.

## Reliability and access decisions
- Enforce uniqueness of the intake reference in the request store; a retry should resume or flag the existing request rather than send another approval.
- Keep flow triggers narrow. An update made by the workflow must not continually retrigger itself.
- Record approval outcome before sending downstream success notices. Handle failed/timed-out actions through an exception branch and owner alert.
- During recovery, check stored approval and delivery references before retrying actions that could duplicate messages or work.
- Limit access to HR and the relevant approver. A filtered SharePoint view alone is not access control; validate actual item/list permissions.
- Use an approved ownership arrangement with a backup owner; review connection access when staff change.
- Retention, access and connector policies require organisational agreement before using employee data.

## Build readiness
Implementation requires a test tenant, fictional requests, approved connections, the configured list and form, authorised approver identity and a service owner. Collect screenshots and sanitised run references only after the flow exists and tests have actually run.


© 2026 Bircan Uzan — All Rights Reserved.
