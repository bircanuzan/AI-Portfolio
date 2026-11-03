# Twelve-week HR service platform delivery plan — illustrative

| Workstream | Weeks | Deliverable | Gate / evidence |
|---|---|---|---|
| Mobilise | 1-2 | Sponsor charter, scope, stakeholder RACI, product owner and supplier SOW | Signed plan and escalation |
| Detail requirements | 2-4 | Approved service catalogue, workflow stories, security classification | HR/IT/Legal signoff |
| Configure & integrate | 4-7 | Nonproduction configuration and restricted integration interfaces | Vendor demo, logs, peer review |
| Test & train | 7-10 | UAT scripts, defect remediation, training materials | P0/P1 defects cleared |
| Cutover rehearse | 10-11 | Migration/dry-run, rollback, support rota and comms | Go/no-go evidence |
| Controlled rollout | 12 | Cohort launch, hypercare and incident triage | HR/IT/Compliance approval |

## Scope controls
- Keep Core HR system of record unchanged.
- HR service platform manages requests, case statuses, knowledge and assigned approvals only.
- Payroll and employee master edits remain separate in authorised HRMS/Finance workflows.
- Do not connect an external LLM or sensitive HR repository without a separately signed privacy/security assessment.

## Accountability
| Role | Responsibility |
|---|---|
| HR Product Owner | Prioritises scope and accepts business functionality |
| Project Delivery Lead | RAID, schedule, dependency, change and stakeholder reporting |
| IT Delivery & Security | SSO, permissions, technical environments, audit logging |
| Vendor Engineer | Configuration against accepted requirements and technical documentation |
| HR Service Owners | Test cases, process SOPs, training and business signoff |
| Compliance/Legal | Privacy, employee-facing policy content, contractual applicability |

## Example backlog
Epic E1 Employee service catalogue; E2 secure employee request intake; E3 HR case routing; E4 status notification; E5 report extraction; E6 incident logging and data retention. Every story carries owner, acceptance criterion and dependency.
