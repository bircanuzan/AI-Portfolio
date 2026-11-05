# 03 — Application modernization and capability roadmap

## Workload decisions (illustrative)
| Workload | Candidate 6R | Rationale | Validation |
|---|---|---|---|
| Oracle HCM/ERP | Retain / integrate | SaaS authoritative core; avoid needless replacement | Supported API permissions and data contracts |
| Legacy employee portal | Rehost then refactor / replatform | API-first modernization without immediate rewrite | Latency, test coverage, authentication |
| Custom workflow backend | Replatform to App Service/Container Apps | Less ops than managing AKS for modest use | Dependency and runtime PoV |
| Unused legacy reports | Retire | Duplicated KPIs create confusion | Owner sign-off and audit retention |
| Manual file-based analytics | Replace / replatform to governed lake | Lineage and trusted metric definitions | Reconciliation against approved sample |

## Staged roadmap
- **Weeks 1–2 discovery:** inventory, 6R assessment, nonfunctional requirements, source owners, test cases, cost assumptions.
- **Weeks 3–4 architecture:** solution views, data ownership, privacy threat model, API contracts, agreed PoV use case.
- **Weeks 5–8 bounded PoV:** synthetic API, sample ETL, dashboard KPI, safety and integration failure exercise; no production cutover.
- **Weeks 9–10 business UAT:** validate operational workflows, security control reviews, exceptions and estimate update.
- **Weeks 11–12 executive decision:** architecture decision records, risks, deployment plan, delivery-phase SoW and go/no-go.

## Value hypotheses — must verify baseline
Manual reconciliation time, failed interface events, reporting turnaround, rework, onboarding case completion and customer/employee experience. Never claim percentage savings until customer measurements exist.

## Migration operational gates
Dependency map complete; zero unresolved critical data access risks; rollback rehearsal; disaster recovery target agreement; integration load tests; SLAs; environment segregation; written operations handover and CIO/security approval.
