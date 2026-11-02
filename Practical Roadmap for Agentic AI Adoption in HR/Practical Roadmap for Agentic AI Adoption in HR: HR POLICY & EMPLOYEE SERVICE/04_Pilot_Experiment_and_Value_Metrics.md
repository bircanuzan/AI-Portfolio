# Step 3 — PILOT: Test with real users, limited scope and clear success metrics

**Pilot described here is a PROPOSED experiment, not an executed customer engagement.**

## 1. Pilot sequence (four-week illustrative plan)

- **Weeks 0–1, safety prerequisite:** Organizational readiness approval, synthetic-only sandbox, test cases, security/privacy review, approved ticket taxonomy and instrumented baseline.
- **Week 2, shadow mode:** Recruit 5–8 HR service advisors to compare agent suggestions against normal handling without employee-facing actions. Correct errors; include multilingual/ambiguous/sensitive samples.
- **Weeks 3–4, limited supervised users:** If preproduction safety gate passes, enable to an approved small cohort (illustrative 30–50 employees). Start with 2–3 routine policies and restricted human queue. Human approval required for any consequential route and all external communications.
- **Closeout:** Independent HR policy and security reviewers assess pre-registered metrics and decide HOLD, REWORK, EXTEND or LIMITED EXPANSION.

**Suggested sample plan:** Aim for ≥200 eligible operational cases across varied policies and HR user groups (if demand permits), plus ≥40 independently selected exceptions and ≥30 adversarial/security scenarios in a test environment. These are proposed study design minimums, not statistical proof of safety. If volume is insufficient, extend the pilot rather than declaring success.

## 2. Before/after experimental design

A/B or matched case assignment where ethical/operationally appropriate:
- Manual-only control lane, with the same policy topics and similar complexity;
- Agent-supported lane with human oversight;
- Compare per-case total time from opening to resolution, rework/reopens, correct routing, citations and satisfaction;
- Record manual interventions, approval wait, operating spend, exceptions and incident response;
- Do not cherry-pick only easy cases into the agent lane when reporting effectiveness.

**Attribution limits:** Policy simplification, seasonal caseload, user training and changes in staffing can also reduce time. Disclose these confounders. Preserve baseline and analysis plan before running.

## 3. Pilot value, reliability and risk KPIs

All thresholds below are **proposed acceptance criteria**, subject to human sponsor sign-off and case mix. They are NOT observed results.

| KPI | Formula / denominator | Draft acceptance condition |
|---|---|---|
| Net HR effort per eligible request | Total HR minutes including corrections, reviews, escalations / eligible cases | ≥20% reduction versus matched manual baseline |
| Correct routing | Correctly routed audited requests / audited requests | ≥95% |
| Source-grounded answer accuracy | Human-verified correct answers based on approved policies / audited eligible answers | ≥95%; no critical false policy claims |
| Citation / version presence | Responses with correct approved policy source + version / answers requiring citation | ≥98% |
| High-impact or sensitive escalation recall | Critical/human-required cases correctly routed / all such tested cases | **100% in defined test set** |
| Unauthorized consequential tool writes | Successful unauthorized writes / attempts | **0 observed**; all defined attack attempts blocked |
| Data disclosure/security incidents | Confirmed critical privacy/security events | **0 unresolved**; one critical event triggers HOLD |
| Audit completeness | Eligible tool calls with required correlation/decision fields / eligible calls | 100% for material tool events |
| Human acceptance | HR reviewers rating accepted-without-substantive-correction / audited routine drafts | ≥90%, with reasons logged |
| User satisfaction | Survey 1–5 among pilot responses | Proposed ≥4.0/5, track response bias |
| Operating cost | License + usage + support + training + monitoring | Measured; compare monthly with capacity benefits |
| Tool call/service availability | Successful authorized operations / attempted authorized operations | Proposed ≥99%, with outage definitions |

**Reliability requirement:** Include negative cases (old policy, conflicting sources, missing identity, ambiguous eligibility, abusive inputs, injection, tool timeouts, incomplete audit). Report numerator, denominator, and interval estimates if possible; a 100% pass on a small sample is not proof of zero future failures.

## 4. Calculating *real* value

Collect measured times with the same accounting rules in both lanes.

```
Net labor capacity hours =
  (manual baseline minutes for comparable cases
   - pilot agent-assisted HR minutes incl. review/rework)
  / 60

Gross capacity value AED = net labor hours × fully loaded hourly internal cost

Net pilot value AED =
  gross capacity value + other independently validated benefits
  - platform fees - usage costs - setup/amortization - change management
  - monitoring/security/legal effort - incident/rework costs
```

Interpret saved labor time as freed capacity, **not automatic cash expense reduction**. Report decision quality, employee trust, escalations and fairness along with efficiency.

## 5. Pilot go/no-go

**GO to controlled expansion only if** mandatory security and privacy controls passed, sufficient cases represent actual diversity, acceptance metrics are met, unresolved critical defects are zero, human override and shutdown are demonstrated and an authorized HR/security/legal governance board signs off.

**REWORK/HOLD** if a source-free legal/eligibility answer occurs, sensitive requests are misrouted, an agent action bypasses approval, data is exposed, answer accuracy falls below preregistered criteria or sample sizes are inadequate.

Measurement template: [13_Pilot_Event_Template.csv](13_Pilot_Event_Template.csv).