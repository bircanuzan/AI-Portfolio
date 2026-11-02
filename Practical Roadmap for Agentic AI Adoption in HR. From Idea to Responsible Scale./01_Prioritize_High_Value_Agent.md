# Step 1 — PRIORITIZE: Choose a high-value use case with manageable risk

## 1. Define the business pain instead of choosing technology first

For a fictional UAE company, assume HR is receiving recurrent questions about leave, policy eligibility, travel administration, onboarding documents and service requests. Requests arrive through email or Teams, are manually categorized, passed to the wrong owner, answered using outdated policies, or repeated when a case lacks details.

**Evidence to request before choosing anything:** 4–6 weeks of HR service-ticket metadata (without exporting unnecessary PII), categories, monthly volumes, touch time, transfer/reopen rate, SLA misses, source-policy update frequency, language mix and employee feedback. Interview HR operations, privacy, security and representative users. Assess whether good search/FAQ or deterministic workflow would solve the issue more simply.

## 2. Compare four candidates, not a predetermined winner

**Illustrative screening rubric:** For each dimension, score 1 = weakest and 5 = strongest. Higher scores always favor selection; the "manageable risk" column assigns 5 to LOWEST controllable risk.

| Criterion | Weight | HR policy triage | Onboarding task coordinator | Candidate screening/ranking | Payroll change executor |
|---|---:|---:|---:|---:|---:|
| Volume and time-saving potential | 25% | 5 | 4 | 4 | 3 |
| Suitability for bounded multi-step agent | 20% | 5 | 4 | 4 | 3 |
| Quality/readiness of approved data | 15% | 4 | 3 | 3 | 2 |
| Feasibility of safe integration | 15% | 4 | 3 | 3 | 2 |
| Manageability of risk | 15% | 4 | 3 | 1 | 1 |
| Ease of measuring outcomes | 10% | 5 | 4 | 3 | 4 |
| **Illustrative total (/100)** | **100%** | **91** | **71** | **63** | **50** |

**Formula:** Total = Σ(weight percentage × score / 5), rounded if needed. Numbers above reflect **analyst assumptions**, not measured UAE market statistics. Re-score with company evidence, sponsor input and legal/privacy review.

## 3. Why the HR Policy & Service Request Triage Agent wins *provisionally*

**Demand:** Routine recurring HR questions are good candidates for triage, while case types can be counted and benchmarked.

**Agentic requirement:** Unlike FAQ search alone, a bounded agent can select relevant approved policy, request missing information, decide whether a draft response is safe, route an exceptional query to a specific authorized queue, and create a restricted test ticket. It uses multiple tool decisions while staying inside a fixed authority envelope.

**Control feasibility:** Read-only sources and restricted queue creation, human review for exceptions, versioned policies and blocked HRIS/payroll write access reduce blast radius. The model never grants itself permissions.

**Observability:** Time from arrival to correct owner, reopens, factual answer rates, handoffs and staff correction effort are measurable.

**Deliberately excluded:** Automated hiring/rejection, compensation, employee-relations conclusions, disciplinary advice, legal interpretation, medical information and sensitive employee records. These require other workflows and stricter authorization.

## 4. Falsifiable value hypothesis

**Illustrative—not real baseline:** 1,200 monthly HR inquiries, 55% in pilot-eligible routine categories, 9 minutes of baseline human work per eligible inquiry, 3 minutes remaining with review of agent-supported output.

Eligible inquiries: 1,200 × 55% = 660/month.  
Net saved per eligible inquiry: 9 − 3 = 6 minutes.  
**Gross illustrative recovered capacity:** 660 × 6 / 60 = **66 hours/month**.  
If internally valued at AED 100/hour, **AED 6,600/month equivalent capacity** BEFORE agent licensing, run costs, operations, supervision, training, failures and opportunity cost. This is *not* cash saved, guaranteed efficiency or headcount reduction.

Calculate **net** benefit from observed case-level handling time, including review, corrections, escalations, audit costs and ongoing support. Report avoided rework and queue backlog separately; do not count equivalent capacity as booked financial savings.

## 5. Selection / rejection gate

Select only after: (a) real baseline confirms significant repeat demand; (b) policy sources are controlled; (c) legal/privacy say a restricted pilot is permissible; (d) team cannot achieve comparable value with lower-complexity FAQ/workflow; (e) security owners confirm permission isolation; (f) human operations sponsor accepts ownership.

**Stop / redesign if:** eligibility is low, policies are too contradictory, integrations are unsafe, human handoffs dominate, or a simpler search tool produces equal outcomes at lower risk/cost.

**Artifact:** [Alternative scoring CSV](09_Use_Case_Prioritization.csv).