# 03 — Program Governance and RACI

**R** = executes; **A** = single accountable decision owner; **C** = consulted; **I** = informed.

| Work / approval | TPM | Client PO | Client Tech | Engineering | Product | Security | Operations | Sponsor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Integrated plan / reporting | A/R | C | C | C | C | I | I | I |
| Business requirements and acceptance | R | A | C | C | C | C | I | I |
| Interface contract and data mapping | C | C | A | R | C | C | I | I |
| Engineering sandbox validation | C | I | C | A/R | I | C | R | I |
| New feature priority | R | C | C | C | A | I | I | I |
| Security approval | I | C | C | R | C | A | C | I |
| Business UAT approval | R | A | C | C | C | C | C | I |
| Go/No-Go release decision | R | C | C | C | C | C | C | A |
| Hypercare BAU handoff | C | C | C | R | I | C | A | I |

**Cadence**
- Daily technical issue triage during blocked implementation periods; owner + next action only.
- Twice weekly client working group covering signoffs, dependencies, decisions and acceptance evidence.
- Weekly Engineering/Product feature triage and two-client capacity alignment.
- Weekly executive report with baseline/forecast, variance, risks, blocked requests, resource gap and asks.
- Formal change approval before re-baselining milestone dates or committing new features.

**Decision-log minimum fields:** date, decision ID, alternatives, client approver, impacted milestones, resource impact and communicated decision. The TPM orchestrates decisions but does not claim Security, Product or client authority.
