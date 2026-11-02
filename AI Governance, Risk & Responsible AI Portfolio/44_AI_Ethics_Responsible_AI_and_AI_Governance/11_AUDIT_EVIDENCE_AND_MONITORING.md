# AI audit trail, control assurance and continuous monitoring
**Illustrative architecture only**. No enterprise audit tool or dashboard is connected.

## Evidence repository hierarchy
```
/evidence/<system-id>/<release-version>/
  01-intake-and-inventory/
  02-privacy-and-data-lineage/
  03-ai-impact-and-ethics/
  04-risk-and-control-tests/
  05-model-card-and-vendor/
  06-security-uat-and-independent-qa/
  07-approval-and-human-oversight/
  08-monitoring-change-incident-retirement/
```
Required metadata for every record: evidence ID, date, system ID, artefact and model version, accountable owner, independent reviewer if applicable, checksum, decision ID, approval time, allowed retention period, and current status. Access is controlled; public GitHub must not store private audit logs or applicant personal data.

## Example synthetic control-evidence manifest
| Evidence ID | Control | Required document | Sample status | Owner |
|---|---|---|---|---|
| E-001 | CTRL-01 | AI system inventory | PRESENT (synthetic) | AI Governance Officer |
| E-002 | CTRL-02 | AIA and signed residual risk | DRAFT only | Risk |
| E-003 | CTRL-03 | DPIA / transfer and privacy opinion | MISSING | DPO |
| E-004 | CTRL-05 | lawful fairness test, subgroup outputs and review | MISSING | QA |
| E-005 | CTRL-06 | red-team prompt injection and factuality results | MISSING | Security/QA |
| E-006 | CTRL-08 | HITL authorisation test and action trace | DESIGN only | Engineering |
| E-007 | CTRL-10 | approved alert thresholds and rollback drill | MISSING | Ops |
| E-008 | CTRL-14 | internal audit sample plan | DRAFT only | Internal Audit |

## KPI dictionary — definitions before reporting
| KPI | Definition | Owner | Escalation |
|---|---|---|---|
| Inventory coverage | Known in-scope AI systems registered / discovered AI systems | AI Governance | Below 95% triggers discovery sprint |
| Assessment coverage | Approved current AIA / registered in-scope systems | Risk | High-tier without AIA = HOLD |
| Independent pre-launch review | High-tier launches with QA sign-off / high-tier launches | AI Assurance | Must be 100% |
| Outstanding critical defects | Count open release-blocking issues | Quality | Must be zero for GO |
| Human-review adherence | Consequential decisions with signed human record / sampled decisions | Operations | Any zero-review adverse action triggers incident |
| Vendor evidence freshness | Approved vendors with current reviews / approved AI vendors | Procurement | Stale vendor = re-review |
| Monitoring coverage | Active systems with telemetry and triggers / all active systems | Model Ops | High-tier gap = containment plan |
| Residual-risk acceptance | High residual risks with authorised exceptions / all high residual risks | Risk | Unauthorised risk = HOLD |

**Numerators and denominators are not populated:** project has no live source systems or verified organisational data.

## Incident escalation tabletop (design exercise, not conducted)
If a candidate is rejected based only on an AI ranking: stop automated pathway, preserve audit trail under restricted access, notify Security and DPO if sensitive data affected, open critical finding, identify/notify human decision owner, offer meaningful manual review, conduct root-cause and impact evaluation, document remediations, retest and only then seek independent re-approval.

## Material change policy
Change of model weights/version; retriever corpus; new tool connector; action permissions; sensitive data processing; new geographic processing location; business decision impact; significant performance/drift trigger **mandatory review**. Low-risk cosmetic UI changes may take an abbreviated recorded process.

## Audit testing plan
Quarterly select high-impact systems and sample approvals, review objectivity, verify raw model test artifacts, confirm human decisions, supplier obligations, alert responsiveness, remediation and retirements. Any contradiction between stated evidence and source logs is an adverse finding. Evidence on GitHub here illustrates schema, **not completed controls**.
