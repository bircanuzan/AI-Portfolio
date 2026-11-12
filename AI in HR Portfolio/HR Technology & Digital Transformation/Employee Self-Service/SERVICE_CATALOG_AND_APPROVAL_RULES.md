# Employee self-service catalogue and authority design

| Request type | Allowed form input | Human route | Do not auto-decide |
|---|---|---|---|
| Employment certificate | Synthetic ID / basic request note | HR Services | Whether request is eligible or signed |
| Policy question | Synthetic ID / general non-sensitive topic | HR Policy Owner | Binding interpretation of employment law |
| Leave enquiry | Synthetic ID / general question | HR Operations | Leave balance, personal/medical circumstances |
| Onboarding support | Synthetic ID / non-sensitive onboarding issue | HR Onboarding | Employment verification or identity provisioning |
| Payroll enquiry | Synthetic ID / generic concern, **no bank/salary detail** | Payroll/HR specialist | Pay amounts, correction, final settlement |
| Employee relations concern | No sensitive narrative in demo; route to human | Employee Relations | Case resolution or disciplinary decision |

## Architecture — demonstration versus future product
**Current prototype:** Static HTML + JS in-memory list of fictional ticket references. No identity/authentication, persistence, server or notifications. No sensitive data.

**Future enterprise design (not built):** SSO + RBAC, audit logging, ticketing API, secure database, data retention controls, scoped notifications, HRMS read-only context where authorised, accessibility audit, incident handling and encryption. HR/IT/Legal must review before real deployment.

## Workflow
Select category -> enter fictional case label -> validate -> assign provisional *human* service owner -> show local request reference -> display 'Awaiting HR Review'. There is intentionally no 'Approve', 'Pay', 'Terminate' or legal-entitlement function.

## Nonfunctional user stories
- Form errors are explained with text and associated to inputs.
- Keyboard users can navigate and submit without pointing device.
- A human-contact alternative is visible.
- A request will not include an actual name, ID number, bank information, health detail or grievance narrative.
