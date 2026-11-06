# 2D Movement and World Boundaries

**Evidence classification:** Independently developed portfolio demonstration based on a **simulated** client/producer inquiry, not commissioned commercial work, a shipped game, or a paid SLA. Acceptance KPIs are targets unless explicitly labeled as measured. Godot editor/visual playtesting has not been verified.

## Client Inquiry
Simulated QA inquiry: player movement should be predictable at different frame rates and never exceed defined scene boundaries.

## Our Methodology / Tech Used
Use Godot's Input.get_vector, normalized directional input, delta-scaled Node2D position, and clampf limits; specify corner, edge and diagonal movement checks.

**Technical components:** Godot 4 | GDScript | Node2D | Input.get_vector | clampf.

## Result (KPI / SLA / Metrics)
Acceptance KPI targets: 100% of positions inside x=[0,800] and y=[0,450]; no diagonal movement speed advantage; delta-scaled movement. No frame-rate, engine execution or performance result has been measured. Proposed QA SLA: record visual boundary evidence within 1 business day after playtest.

## Evidence and Delivery Status
player.gd and acceptance specification are committed as a learning sample; not a published or shipped gameplay implementation.

## Reproduction / Evaluation
Follow the source files and task acceptance guide in this folder. Capture the input sequence, actual on-screen state, screenshot or screen recording, severity, and pass/fail rationale. Escalate any discrepancy; do not mark simulated targets as achieved.

## Related portfolio
[Game Developer project collection](https://github.com/bircanuzan/AI-in-HR-Portfolio/tree/main/Game%20Developer).
