# Game Developer — Gameplay Implementation, Debugging & Test Design

**Evidence classification:** Independently developed portfolio demonstration based on a **simulated** client/producer inquiry, not commissioned commercial work, a shipped game, or a paid SLA. Acceptance KPIs are targets unless explicitly labeled as measured. Godot editor/visual playtesting has not been verified.

This collection contains **five distinct independent work samples**. Each case study uses the same structure as the CV: **Client Inquiry / Our Methodology & Tech Used / Result (KPIs, SLAs and metrics)**. Where a metric is a test target rather than measured outcome, it is identified as such. The Python regression harness is the only example with recorded local automated-test results as of 6 November 2026.

| Project | Work sample | Validation status |
|---|---|---|
| 1 | [Gameplay Input Bug and Reference Fix](https://github.com/bircanuzan/AI-in-HR-Portfolio/tree/main/Game%20Developer) | Godot playtest pending |
| 2 | [Ability Cooldown and Input State](https://github.com/bircanuzan/AI-in-HR-Portfolio/tree/main/Game%20Developer/02-Ability-Cooldown) | Godot playtest pending |
| 3 | [Inventory and Quest State Logic](https://github.com/bircanuzan/AI-in-HR-Portfolio/tree/main/Game%20Developer/03-Inventory-Quest-Logic) | Godot playtest pending |
| 4 | [2D Movement and World Boundaries](https://github.com/bircanuzan/AI-in-HR-Portfolio/tree/main/Game%20Developer/04-Movement-Boundaries) | Godot playtest pending |
| 5 | [Gameplay Regression Test Harness](https://github.com/bircanuzan/AI-in-HR-Portfolio/tree/main/Game%20Developer/05-Gameplay-Regression-Harness) | 3/3 Python tests passed locally |

---

# Gameplay Input Bug and Reference Fix

**Evidence classification:** Independently developed portfolio demonstration based on a **simulated** client/producer inquiry, not commissioned commercial work, a shipped game, or a paid SLA. Acceptance KPIs are targets unless explicitly labeled as measured. Godot editor/visual playtesting has not been verified.

## Client Inquiry
Simulated producer brief: a held Space key must not collect multiple tokens or falsely finish the objective.

## Our Methodology / Tech Used
Create a Godot 4 2D scene (main.tscn), an intentionally defective GDScript reference (broken_main.gd), and a corrected script (main.gd) using Input.is_action_just_pressed, a capped token counter, terminal-state lock and on-screen Label feedback. Specify reproduction and acceptance steps.

**Technical components:** Godot 4 | GDScript | Godot 2D scene (.tscn) | Node2D | Input.is_action_just_pressed | Label UI.

## Result (KPI / SLA / Metrics)
Acceptance KPI targets: exactly 1 token per deliberate keypress; win state at exactly 3 unique presses; 0 extra increments after completion. Godot visual/engine playtest remains unverified. Proposed QA SLA: log expected/actual outcome with video or screenshot within 1 business day after execution; not a measured service commitment.

## Evidence and Delivery Status
A reproducible project template, faulty script, reference fix and written acceptance checklist are published; no shipped game or end-to-end engine test is claimed.

## Reproduction / Evaluation
Follow the source files and task acceptance guide in this folder. Capture the input sequence, actual on-screen state, screenshot or screen recording, severity, and pass/fail rationale. Escalate any discrepancy; do not mark simulated targets as achieved.

## Related portfolio
[Game Developer project collection](https://github.com/bircanuzan/AI-in-HR-Portfolio/tree/main/Game%20Developer).
