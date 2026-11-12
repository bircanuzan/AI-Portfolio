# Ability Cooldown and Input State

**Evidence classification:** Independently developed portfolio demonstration based on a **simulated** client/producer inquiry, not commissioned commercial work, a shipped game, or a paid SLA. Acceptance KPIs are targets unless explicitly labeled as measured. Godot editor/visual playtesting has not been verified.

## Client Inquiry
Simulated designer inquiry: prevent a player ability from spamming while a cooldown is active, without losing clear on-screen status.

## Our Methodology / Tech Used
Use Godot 4, GDScript, a frame-delta cooldown counter, Input.is_action_just_pressed and a Status Label. Document ready/cooldown transitions and reproducible hold/rapid-press scenarios.

**Technical components:** Godot 4 | GDScript | Input API | frame delta | Label.

## Result (KPI / SLA / Metrics)
Acceptance KPI targets: 2.0-second cooldown after activation; 0 additional activations while cooling down; a second activation accepted only when timer returns to zero. Engine execution remains pending. Proposed QA SLA: same-business-day defect report after test execution; not a delivered client SLA.

## Evidence and Delivery Status
Published GDScript ability.gd and reviewer test instructions. No independently verified frame-time benchmark or engine recording is claimed.

## Reproduction / Evaluation
Follow the source files and task acceptance guide in this folder. Capture the input sequence, actual on-screen state, screenshot or screen recording, severity, and pass/fail rationale. Escalate any discrepancy; do not mark simulated targets as achieved.

## Related portfolio
[Game Developer project collection](https://github.com/bircanuzan/AI-in-HR-Portfolio/tree/main/Game%20Developer).
