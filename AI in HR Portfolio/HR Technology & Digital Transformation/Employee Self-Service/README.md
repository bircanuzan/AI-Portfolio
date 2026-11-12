# Employee Self-Service | Transactional HR Request Portal Prototype

**Independent HumanEvoX front-end concept | In-browser prototype | Synthetic requests only**

## Unique purpose
Build the employee-facing **transactional** experience for requesting routine HR support and tracking a case. The scope is form validation, clear status, permission boundaries and human escalation—not employee-experience discovery, vendor selection, program delivery, HCM master data or AI assistants.

## What was built
- [Offline HTML/JavaScript prototype](prototype/index.html) with selectable HR request types, in-memory case creation, transparent reference IDs and status messaging.
- [Catalogue and rules](SERVICE_CATALOG_AND_APPROVAL_RULES.md) specifying which HR team owns each case and which requests need human review.
- [Privacy, accessibility and UAT scenarios](PRIVACY_ACCESSIBILITY_AND_UAT.md) including clearly marked unexecuted tests.
- [Acceptance worksheet](TEST_SCENARIOS.csv) for reproducible manual testing.

## Tools and methods
HTML, CSS, vanilla JavaScript, client-side validation, service catalogue, user stories, accessible form controls, secure product-design boundaries, human-in-the-loop routing, incident escalation and operational KPIs.

## Running the prototype
Open `prototype/index.html` locally in a browser. No npm, backend, authentication, payment details, APIs, persistence or employee information is required. Requests exist only in that browser page's memory and disappear on refresh.

**Do not use with genuine employee information.** This is a local interaction mock-up, not a production secure HR platform. It is not an AI agent and does not grant leave or calculate entitlements.
