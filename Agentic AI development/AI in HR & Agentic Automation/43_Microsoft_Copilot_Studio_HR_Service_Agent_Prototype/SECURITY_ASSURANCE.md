# Threat model and assurance boundaries

## Attacker and data scenarios
Prompt injection, PII fishing, role escalation, employee impersonation, stale policy, fabricated citations, disclosure via source documents, repeated high-volume attempts, and over-reliance on agent replies. Business impact includes privacy breaches and incorrect employment decisions.

## Existing observable controls in local prototype
- Text-rule rejection routes obvious restricted terms and adversarial phrases to a human category.
- Only invented policy text can be returned; no file, network, employee, API or HRIS connectors exist.
- Each response contains decision, rule, source version and a minimal in-memory trace object.
- Browser displays the result; it neither stores server logs nor sends messages. This is **NOT independently verified cybersecurity**.

## Not implemented or demonstrated
Real authentication, RBAC/ABAC, access logging, retention, encryption, per-employee authorisation, connector gating, prompt injection robustness across paraphrases, incident response, monitoring, independent TEVV, bias evaluation, DPIA, UAE legal review, NIST audit, Microsoft cloud deployment, reliable observability, HRMS change prevention under actual privileges.

## Governance implementation checklist
Asset register; data inventory and retention; threat modelling; DLP; least privilege; control mapping to NIST AI RMF Govern/Map/Measure/Manage; red-team evaluation; human sign-off matrix; rollback, override, incident triage; monitoring and revalidation after policy/model changes. No assertion of certifications or conformity.
