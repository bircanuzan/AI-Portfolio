# 08 | Modern workplace solution options and tradeoffs

## Windows 365 vs Azure Virtual Desktop
| Decision input | Windows 365 | Azure Virtual Desktop |
|---|---|---|
| Primary positioning | Per-user Cloud PC model, more standardized end-user provisioning | Flexible Azure desktop/app virtualization and host pool operations |
| Operational owner | Intune management and approved Cloud PC governance | AVD platform owner plus Intune where supported; image, host, session and scaling management |
| Cost | Licence and service package, confirm actual tiers | Azure compute/storage/network + eligible licensing + platform support |
| Fit | Common persistent Cloud PC personas, simple assignment needs | Varying app delivery, shared/multi-session or flexible host pool cases |
| Risk | Incorrect licence/user sizing or unmanaged entitlements | Higher specialist configuration and operational complexity |
| Decision | Validate persona and tenant requirements | Validate concurrency, workloads and operational capability |

Neither option is always better. Validate local region, access, application compatibility, network, resilience and licensing with Microsoft/technical specialists.

## Managed support alternatives
- Regional desks retained with common knowledge and reporting vs consolidated global desk.
- Full DaaS vs customer-owned fleet with lifecycle support only.
- Field partner subcontracting vs retained on-site staff.
- Single ITSM platform vs federated systems with SIAM-style ownership.
- SLA-only service pricing vs hybrid XLA and outcome-focused incentive overlay.

## Architecture decision records
**ADR-01: service desk** — start with a unified catalogue and common severity model before forcing a full ITSM migration. Avoid losing local service continuity.
**ADR-02: device telemetry** — collect only approved security/DEX metrics; no unsanctioned employee productivity surveillance.
**ADR-03: automation** — prioritize deterministic password/account/support workflow with identity checks over unrestricted LLM actions.
**ADR-04: virtual desktops** — compare Windows 365 and AVD by persona, cost and operations, not by vendor popularity.
**ADR-05: experience measures** — SLAs track process, XLAs track user impact; use a balanced and auditable approach.

## Vendor capability diligence
ServiceNow integration and ITSM, Endpoint/UEM, DEX, DaaS, field service logistics, M365 and Azure engineering must be evaluated with verified partner capability and tool access. This repository is *not* a set of implementation credentials.
