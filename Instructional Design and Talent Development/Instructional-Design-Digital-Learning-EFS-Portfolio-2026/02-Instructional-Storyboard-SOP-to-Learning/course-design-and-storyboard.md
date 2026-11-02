# Instructional Design Document & Storyboard
**Project:** Service Request Triage — from raw SOP to performance-ready training  
**Status:** Original 2026 portfolio demonstration, not deployed; hypothetical organizational policies.  
**Authoring method:** AI-assisted content creation with planned SME review.  
**Audience:** facilities coordinators and team supervisors.  
**Estimated duration:** 10 minutes + a printable job aid.

## 1. Performance problem and learner needs (ADDIE — Analyze)
Incoming service tickets vary in completeness; safety-critical reports can be improperly categorized; handoffs may lack confirmed ownership. Audiences include new starters, experienced service coordinators and supervisors with mixed technology literacy. Corporate learners need short scenarios, clear routes, simple language and meaningful decisions.

**Business metrics to establish before rollout:** % tickets containing complete handoff data; % correct first-time triage; escalation response time; errors and repeat tickets.

## 2. Objectives and alignment (ADDIE — Design)
By the end, learners will:
- **Apply:** classify three fictional cases using urgency, safety and type of service (Bloom Apply).
- **Analyze:** justify an escalation route for a safety-critical request, distinguishing facts from assumptions (Analyze).
- **Create:** produce a complete handoff record with at least six essential fields (Create).

**Prerequisites:** site-specific safety orientation; official local escalation policy. This example never substitutes for that policy.

## 3. Content source and SME process
Inputs requested: approved SOP, service categories, escalation matrix, permitted response language, current SLAs, logging tool fields, emergency contacts and accessibility requirements. Workflow: SME kickoff → draft content map → SME review (Accuracy Gate 1) → storyboard approval (Gate 2) → interaction prototype → QA/UAT → pilot → release, sign-off and version log.

## 4. Screen-by-screen storyboard
| ID | Learning objective | On-screen narrative | Visual / audio direction | Interaction / feedback |
|---|---|---|---|---|
| S01 | Orientation | “From incoming request to accountable action.” Three learning outcomes. | Open with simplified intake visual; optional 15-sec VO. | Continue; accessible text equivalent. |
| S02 | Understand model | “Recognise → Route → Record.” Define each with a concrete non-sensitive example. | Three-step motion diagram; captions if animated. | Match field to step. |
| S03 | Identify risk | Chair request vs smoking socket vs paper refill. | Three cards with clear icons and text. | Choose one; corrective explanatory feedback; retry allowed. |
| S04 | Select route | Show safety-critical and routine pathways, explicitly dependent on approved policy. | Two-lane diagram. | Choose route; require evidence from request. |
| S05 | Produce handoff | Include location, observations, received time, action, owner and acknowledgement. | Annotated sample log with callouts. | Drag/choose missing fields. |
| S06 | Assessment Q1 | “Water near exposed wiring. Select initial response.” | Plain text and two safety-neutral visuals. | Correct: approved escalation; no technical diagnosis. |
| S07 | Assessment Q2 | “Which handoff note is actionable?” | Three text cards. | Correct: complete traceable record. |
| S08 | Assessment Q3 | “Routine lightbulb request with no published SLA.” | Short ticket. | Correct: do not fabricate response time. |
| S09 | Results and transfer | Score + practical reminder. | Completion summary, downloadable job aid prompt. | Pass recommendation 2/3 for demo only; revise against business standard. |

## 5. Example narration and script
**VO (S02, approximately 27 seconds):** “When a service request arrives, recognise the issue and separate confirmed facts from assumptions. Route potential safety issues using the approved escalation procedure and send routine requests through the normal workflow. Record the handoff so the next person knows what happened, who owns the next step, and whether they accepted it.”

**On-screen captions:** Exact VO text, with no reliance on sound alone. Avoid color-only urgency signals.

## 6. Assessment blueprint
| Objective | Item | Correct response | Rationale |
|---|---|---|---|
| Classify and route | Near exposed wiring | Approved immediate safety escalation | Potential hazard. |
| Document handoff | Complete record | Location, observed facts, time, action, owner, acknowledgement | Auditability and continuity. |
| Avoid unsupported commitments | Routine lightbulb | Route in normal queue, don't invent SLA | Policy fidelity. |

Assessment type: multiple-choice and scenario-based feedback. Every distractor addresses a realistic misconception. Module is a knowledge demonstration, not field authorization.

## 7. Build, accessibility, publishing
- Build using HTML/CSS/JavaScript prototype or re-author in licensed Storyline/Rise 360 with explicit functionality testing.
- Keyboard-operable interactions, WCAG-minded heading structure, readable text, captions/transcripts, non-color-only feedback and responsive design.
- LMS package: SCORM 1.2/xAPI selection with the LMS administrator; configure completion, attempts and score; validate in target LMS.
- QA checklist: approved SME content, typos, policy references, responsive viewport, keyboard traversal, alt text, quiz logic, tracking and source-version record.

## 8. Sample development controls
**File naming:** YYYYMMDD_topic_vMajor.Minor.ext  
**Release log:** v0.1 prototype → v0.2 SME corrections → v0.3 UAT → v1.0 approved release.  
**Approval roles:** HR/L&D content owner, operational SME, safety/compliance owner, LMS administrator.

## 9. Personal contribution statement
This 2026 portfolio demonstration was created with generative AI assistance to explore storyboard development, scenario writing, instructional alignment and QA specification. It is not an EFS-approved operating procedure, a client-owned deliverable or evidence of prior Articulate production usage.
