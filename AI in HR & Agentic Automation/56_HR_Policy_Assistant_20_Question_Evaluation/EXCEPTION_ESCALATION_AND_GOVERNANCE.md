# Human–AI operating model and approval boundaries

~~~mermaid
flowchart TD
 A[Employee submits fictional question] --> B{Privacy / escalation flags?}
 B -->|Third-party private data| C[REFUSE and refer to HR]
 B -->|Grievance / exception / personal entitlement| D[ESCALATE to verified human HR channel]
 B -->|Routine| E{Approved fictional source match?}
 E -->|Match| F[ANSWER with policy ID and version]
 E -->|No match| G[UNKNOWN and HR help route]
 F --> H[Optional anonymous quality feedback]
 C --> H
 D --> I[Human HR owns resolution]
 G --> I
~~~

## Roles and controls (design, not implemented production workflow)
- **HR policy owner:** owns versioned source, approvals and factual corrections.
- **Privacy / security officer:** reviews minimum access, PII, logging, retention, incident response.
- **HR services lead:** owns exception, grievance and appeal SLA and case outcomes.
- **AI / QA owner:** owns prompt set, test evidence, error taxonomy and release gate.
- **Employee:** receives navigation only; no unauthenticated individualized decision or irreversible action.

## Minimal proposed operational KPIs
Answer-source accuracy by category; escalations answered by human; privacy failures; unknown / fallback fraction; deflection only where safe; per-language issue rate; drift after policy revision; time to correct stale content.

## No invented achievements
The repo demonstrates a local Python router and evaluation suite. It **does not** send messages to a human, access an actual HR portal, authenticate anyone, process employee records, or perform live actions.
