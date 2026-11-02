# Fictional X-Industry HR Service Desk Standard
Version: 0.1 | Synthetic data | Technical demo, not company policy

For an HR policy question, search version-controlled approved sources, cite the relevant document and refuse to guess when coverage is missing. Case-status questions may be resolved through an operator-authorized read-only HTTPS case API, using a CASE-123 style identifier.

High-impact requests (create, submit, approve, grant, change, send, delete) require explicit human approval before any mutation. The local prototype only records the approval decision inside a demo SQLite file. It does not update HRIS or send communications.

Log event IDs and operational status; never publish candidate, salary or employee records in GitHub evidence.
