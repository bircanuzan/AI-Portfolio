# 02 — Controlled Human–AI Workflow Pilot

**Practical question:** How can an internal AI-assistant workflow support employees while maintaining knowledge ownership, least-privilege access, human review and incident escalation?

The Python demonstration is an **executed-on-demand local rules engine**, NOT an LLM or externally connected agent. All examples are synthetic and contain no personal employee information.

## Architecture
User request -> identify role and source -> validate source approval -> enforce RBAC information class -> select allowable task -> create draft **for review only** -> hold release for authorized human -> append minimized audit decision. Block unsupported external actions; record no sensitive source text.

[Architecture and control matrix](ARCHITECTURE_AND_CONTROL_MAP.md) | [Python prototype](src/controlled_workflow.py) | [Unit tests](tests/test_controlled_workflow.py) | [Synthetic test requests](data/synthetic_requests.json)

## Skills and tech
Workflow orchestration, process mapping, JSON data contracts, role-based access control, privacy, information classification, human-in-the-loop approval, error/exception handling, audit event design, negative testing, UAT and deployment handover.

**Proposed, not claimed as implemented:** Microsoft Copilot Studio + SharePoint/Entra ID permissions + Power Automate approval flow; alternative managed enterprise LLM + retrieval and an integration adapter with explicit policy enforcement, telemetry, encrypted secrets and human approval. Any real tenant connection requires customer approvals and independent security tests.

## Evidence / limits
No LLM inference; no external side effects; no emails, HR actions, CRM mutations or personal-data retrieval. A human approval status does not automatically trigger release. The prototype demonstrates *decision routing*, not enterprise identity enforcement or certified security.
