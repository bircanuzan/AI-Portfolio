# Model card, AI system card and third-party assurance
**Synthetic example AI-003: HR Policy Helpdesk Agent**. Supplier and technical stack are not selected, so unverified capabilities are explicitly 'unknown'.

## System card — draft
| Field | Sample record |
|---|---|
| System name / version | AI-003 HR Policy Helpdesk Agent / concept v0.1 |
| Intended users / use | authenticated employees; read and explain approved HR policies |
| Prohibited uses | employment decisions, legal advice, payroll change, bank-data changes, employee profiling |
| Model | third-party general-purpose LLM **TBD**; model weights and training corpus unknown |
| Data inputs | employee question, allowlisted policy retrieval results |
| Output / actions | sourced policy answer, disclaimer, escalation link; no autonomous writes |
| Data stewardship | HR Policy Owner; Security and DPO review pending |
| Fairness and accessibility | no live results, testing required across user language/needs |
| Reliability / hallucination | no tested performance metrics |
| Human fallback | HR Service Desk for exceptions and conflicting policies |
| Version control | source policy revision, prompts, retrieval config, model and tools tracked |
| Monitoring | unsupported-answer rate, escalations, safety incidents, source age |
| Risk tier | internal T2 (could increase if agent acquires consequential action permissions) |
| Approval status | HOLD pending supplier and independent evaluation |

## Supplier / cloud / foundation-model due diligence
Score each as **Provided / Partial / Missing / Not Applicable**, with evidence URL, owner and expiry:
1. Corporate information, applicable security attestations and breach-response contacts.
2. Data processing contract, subprocessors, training-use opt-out, deletion assurance and region of processing.
3. Lawful basis, transfer mechanisms where relevant, data-subject-rights cooperation.
4. Training provenance summary and known limitations (as disclosed).
5. Model/version release notes, rollback options, material-change notice SLA.
6. Content safety, injection boundaries, tool-call and data-exfiltration protections.
7. Evaluation results on intended languages, factuality, robustness and meaningful fairness dimensions.
8. Audit rights, incident notification, liability allocation, IP and confidentiality terms.
9. Retention of prompts/outputs/telemetry, log access, tenant isolation and encryption.
10. Exit plan, portability, deletion evidence and replacement vendor strategy.

**Gate:** Missing DPA, security evidence, permission boundaries or model/version change transparency → HOLD or NO_GO according to severity. Contract and audit-right review belongs to qualified legal and procurement stakeholders.

## Sample contract control clauses (drafting topics, not legal wording)
- Provide audit logs and independent assurance access for customer-owned data.
- Notify material model, subprocessor, region, tool or data-use changes.
- Support suspension, incident investigation, rollback and deletion within agreed timelines.
- Prohibit training on customer-provided data unless specifically contracted and lawful.
- Evidence of compliance with agreed retention, access and change-management controls.
