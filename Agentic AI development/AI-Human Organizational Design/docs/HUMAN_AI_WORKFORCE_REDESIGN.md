# Human–AI Workforce Redesign Lab | Architecture-to-Capacity Evidence

**What is implemented:** an executable, synthetic decision lab covering task/activity work analysis, illustrative job families and new skill profiles, human/agent work allocation, *gross vs net* capacity scenarios, a future-state organisation structure and a reinvestment plan subject to explicit human approvals. This module is related to the `#AIHumanWorkforceDesign` field, but **is not evidence of a completed organisational transformation**.

## 1. Business case and baseline
Fictional Cedar Gulf Group People Services pilot, **separate from the organisation-wide workforce dashboard data**. Seven activity groups generate **4,813 baseline work hours annually**, calculated from fictional annual case volume × standard minutes/case. Hours are workloads, not people employed, and the **1,500 productive hours/FTE** assumption is fictional.

The work taxonomy defines each task's present owner, named future human owner, decision authority, exposure, realisation, rework, quality review effort and retained hours. Job evaluation decisions and employee relations/termination remain entirely human-owned.

## 2. Human/agent work allocation
Potentially AI-assisted work is bounded to preapproved task portions; the agent cannot decide hiring, grades, pay or employee rights.

```
baseline task hours = annual units × baseline minutes / 60
assisted units = annual units × eligible share × assumed adoption
gross recoverable hours = baseline hours × eligible share × assumed adoption × (1 − rework share)
review / oversight hours = assisted units × review minutes per unit / 60
net scenario capacity = max(0, gross recoverable hours − oversight hours)
FTE equivalent = net scenario capacity / assumed productive hours per FTE
```

**Baseline hypothetical scenario:** **approximately 1,460.55 hours**, or **0.974 workload FTE equivalents**, could potentially be freed *if the assumptions held*. This is **not** measured productivity, a headcount reduction, redundancy, cash saving or commitment. High-impact employee relations and job grading decisions produce **zero automated decision capacity**. A conservative zero-adoption scenario produces zero capacity release.

## 3. Future job architecture
Eight future-state **illustrative** human roles with defined job family, career stream, skills and decision rights, including the **Human–AI Service Operations Specialist**, **Workforce Intelligence & Data Steward**, **Human–AI Workforce Design Lead**, and **Agent Service Assurance & Governance Lead**.

Illustrative role bands `P3`–`P5` are *not Mercer/Aon grades*, approved HR levels or market benchmark pay. Real grading requires qualified evaluation, comparable roles and independent equity checks.

## 4. Proposed future organisation structure
The *current* fictional structure has fragmented entity service, recruiting, analytics and reward interfaces. The *future proposal* introduces Group OE & Workforce Architecture, People Data & Workforce Intelligence, Human–AI HC Services Operations, Talent & Capability Intelligence, Reward/ER Governance and a matrix Agent Risk & Assurance function. Every unit has a named human accountable officer and a parent reporting line; cycles and orphans are tested.

**No organisational change is approved or implemented by the prototype.** Source-of-truth data, labour law, employee consultation, reward, Finance and CPO committee sign-off are mandatory before real adoption.

## 5. Capacity reinvestment, not invented savings
The scenario redistributes potential workload capacity, proportionally, into:
- 30% human-led service quality and exception resolution
- 25% validated workforce scenarios and data
- 20% reskilling and internal mobility
- 25% AI service assurance, monitoring and governance

Those are **proposed allocation priorities**, not measured gains or commitments. A financially valid business case would model actual employee FTE, cash costs, service risks, implementation costs, redeployment feasibility, milestones, workforce consultation, and measured outcomes with Finance.

## 6. Implementation and governance gates
Independent task baseline validation → skills/role evaluation and human decision rights → IT/security/Responsible AI review → CFO cost verification → CPO/HCC structural decision → employee relations/legal consultation and change support → controlled pilot/quality measurement → verified performance and revised workforce capacity. No production deployment or actual staff impact is claimed.

## Reproduce
From project root:

```bash
python -m src.hcia.workforce_design
python -m unittest discover -s tests -v
```

**Portfolio relationship:** the [Organizational Effectiveness](../../../Organizational%20Effectiveness/) folder develops the Group-level structural governance model. [Workforce Transformation](../../../Workforce%20Transformation/) covers wider Human–AI workforce architecture. This AI-Human Organizational Design module creates a **standalone executable task-to-role-to-structure capacity decision chain** for the short engineering demo.
