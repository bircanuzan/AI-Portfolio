# Security, fairness and data-handling notes

**Scope**: local single-operator pilot only. Do not use this prototype as a public SaaS or enter real applicant data before an organizational risk assessment.

- **Lawful processing**: check right to process, purpose, notices, candidate consent where applicable, and retention policy. UI acknowledgement is not a legal consent-management system.
- **Fairness and explainability**: do not process protected attributes for hiring, use opaque job-fit scores, or reject based on missing CV keywords. Text evidence is an imperfect retrieval aid; multilingual/scanned/nonstandard CVs can be underserved.
- **Human oversight**: all evaluations, pipeline changes and communication sends are explicitly human-controlled. No automated calling, recording or decisioning.
- **Data minimization**: only short snippets rather than full text are saved; note that snippets may still contain PII. Masking handles common email and phone patterns, not all forms of PII.
- **Access controls**: the app has no login or tenant isolation. The SQLite file and exports must be protected by the operator's OS controls. Never expose the Streamlit port publicly.
- **Erasure and retention**: delete in-app plus externally downloaded CSVs, backups, attachments and sent emails where legally applicable. The audit trail anonymizes the deleted record's identifier.
- **Threat model**: malicious documents, file decompression, CSV formula injection, untrusted text in drafts, local filesystem access, data exfiltration, cross-client access. Size/page limits and CSV formula hardening provide partial controls only; production needs antivirus/sandbox, stronger file processing and penetration tests.
- **Change gate**: verify access control, data protection, abuse prevention, fairness testing and approval before any live integration or commercial client deployment.
