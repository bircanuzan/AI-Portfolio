# 01 | CEO/COO Engagement Charter and Discovery Pack

## Engagement objective
Turn a costly client operating problem into a verifiable AI-enabled improvement, jointly sponsored by the agency CEO/COO and product/engineering leadership. Scope includes discovery, prototype, pilot, adoption, measurement, handover and a decision on product scaling.

### North-star outcome
Increase **qualified lead-to-viewing conversion**, with median first-human-response time as leading indicator. Avoid optimising the number of AI-written messages without evidence of bookings or service quality.

## Discovery interviews
| Executive/stakeholder | Questions | Evidence requested |
| --- | --- | --- |
| CEO/COO | What moves revenue, agent productivity and retention? What would justify renewal? | Unit economics, segment P&L, conversion funnel |
| Sales director | How are inquiries assigned and followed up? Where are leads dropped? | Response-time distribution, coverage hours, handover rules |
| Marketing lead | Are paid leads or listing quality driving changes? | Channel mix, spend, listing completeness |
| Agents/team leads | Where do prompts help or slow you? Who approves customer messages? | Workflow shadowing, objections, language preferences |
| Data/IT/CRM owner | Where are event timestamps, consent and opportunity state held? | Schema map, API constraints, access policy |
| Legal/privacy | What customer data may be processed and retained? | Lawful basis, retention, cross-border access review |

## Baseline acceptance
Before engineering begins, agree on source-of-truth definitions: received_at, first_valid_response_at, agent assignment, eligible lead, booked viewing, attended viewing, won transaction. Segment by shift, channel, agency and agent capacity. Document missing values rather than inferring timestamps.

## Executive governance
- **Client CEO/COO:** business sponsor, priority and investment decision, go/no-go.
- **AI Strategist:** accountable for use-case value, scope, backlog, client relationship, adoption and executive narrative.
- **Engineer A:** data mapping, CRM connector, API access and logging.
- **Engineer B:** retrieved listing facts, suggested reply, approval screen and fallback.
- **Analytics partner:** experimental design, data validation and impact estimation.
- **Legal/security/CRM owner:** approve data handling and release gates; may block launch.

## Checkpoints
Week 2: discovery sign-off and baseline; week 4: approved design and estimated effort; week 7: internal UAT; week 9: controlled pilot; week 12: executive readout. Any date is illustrative, not an actual delivery milestone.

## Decision memo
**Pilot only when** lawful processing, auditability, quality evaluation, rollback ownership and reliable event data are confirmed. Otherwise improve non-AI routing/CRM hygiene first.
