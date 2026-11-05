# 02 | End-to-end Modern Workplace portfolio solution blueprint

## Capability towers and handoffs

| Tower | Proposed managed-service design | Integration / dependency | Acceptance |
|---|---|---|---|
| 1. Service desk & end-user support | Omnichannel L0-L3 intake, knowledge, dispatch, multilingual *coverage evaluated by vendor* | ITSM, identity, asset registry | SLA, reopens, escalation |
| 2. DEX | Proactive endpoint/app health and employee sentiment | Approved telemetry, privacy and consent | Experience change vs baseline |
| 3. Device management | Standard enrollment, patching, app distribution, compliance | Intune or approved UEM, identity | Compliant managed fleet |
| 4. Device lifecycle | Procure, image, provision, repair, redeploy, wipe, recycle | HR joiners, supplier, inventory | Asset chain of custody |
| 5. DaaS | Per-device lifecycle and support bundle | Financial / security / device ownership | Unit price and service conditions |
| 6. Identity & workplace security | Entra ID design, MFA, conditional access, least privilege | CISO policy, IAM and ITSM | Access reviews, exception tests |
| 7. Microsoft 365 & collaboration | Service catalogue for M365, Teams, Outlook, OneDrive, SharePoint | Licence, change and information governance | Collaboration quality and adoption |
| 8. AVD / Windows 365 | Persona-driven virtual desktop feasibility, not a forced solution | Azure landing zone, license, network, Intune | User acceptance and cost feasibility |
| 9. Asset management | Software/hardware inventory, CMDB and lifecycle status | Procurement, ITSM, finance | Inventory reconciliation |
| 10. Field services | Dispatch, site hands-and-eyes, device swap, incident escalation | Partner locations, region coverage | Site response and visit quality |
| 11. Automation & self-service | FAQ, password-reset routing, joiner/mover/leaver tasks | ServiceNow, identity, approved APIs | Safe containment and audit |
| 12. Copilot & AI-enabled workplace | Use-case discovery, training, responsible-AI review | Licensed M365 tenant and permissioned data | Correct task quality / adoption |
| 13. ServiceNow & ITSM | Incident/request/change/problem/knowledge/CMDB processes | ServiceNow configuration SME and integration | Ticket lifecycle integrity |
| 14. Managed services / T&T | Outcomes, transition, runbook, continuous service improvement | Incumbent handover, vendors, internal IT | Signed readiness and support |

## Persona-led reference architecture

~~~mermaid
flowchart TD
  EMP[Employee devices and collaboration] --> ACCESS[Identity, MFA & device posture]
  EMP --> SERVICE[Digital service portal / omni-channel desk]
  ACCESS --> UEM[UEM / device lifecycle / AVD / Cloud PCs]
  SERVICE --> ITSM[ITSM workflow / ServiceNow]
  ITSM --> DEX[DEX, endpoint health and feedback]
  ITSM --> AUTOM[Self-service + approved workflow automation]
  AUTOM --> HR[HRIS joiner/mover/leaver events]
  ITSM --> ASSET[CMDB + asset / field services]
  DEX --> GOV[SLA / XLA / KPI governance]
  UEM --> GOV
  ASSET --> GOV
  AI[Copilot and safe knowledge assistance] --> SERVICE
  AI --> GOV
~~~

## Design principles
1. Business outcomes and experience-led service catalogues.
2. Preserve systems of record and supported integration contracts.
3. Security/identity, data minimization, privacy and retention by design.
4. Accessibility and hybrid/remote user coverage.
5. Automation for bounded low-risk workflows; human review for regulated actions.
6. Explicit scope, SLAs, experience measures, governance and service credits.
7. Deliverable run model and realistic partner dependencies.

## Sample end-to-end journey: new employee
Approved HRIS event -> identity provisioning with approval -> secure device request -> enrollment/compliance -> M365 entitlement -> application readiness -> employee experience check -> service request if needed -> verified close. **No automatic sensitive employment decision or live provisioning occurs here.**

This reference model is for commercial/consulting discussion; device/security/ITSM implementation would be owned and tested by qualified technical specialists.
