# Worked cases - synthetic, manually authored

All companies, figures and candidate responses below are fictional. No live model was evaluated.

## STRAT-001: Revenue growth is not profit

**Prompt:** A service costs AED 1,200 per engagement to deliver. The current price is AED 2,000, with 50 engagements per month. A proposed discounted price of AED 1,600 is forecast to generate 65 engagements. Monthly fixed costs remain AED 20,000. Should the business discount?

**Candidate answer:** Accept the discount because revenue rises from AED 100,000 to AED 104,000, improving profit.

**Reference check:**

- Current contribution: (2,000 - 1,200) × 50 = AED 40,000.
- Current operating result after fixed costs: 40,000 - 20,000 = AED 20,000.
- Discounted contribution: (1,600 - 1,200) × 65 = AED 26,000.
- Discounted operating result: 26,000 - 20,000 = AED 6,000.
- Discounted volume needed to preserve current contribution: 40,000 / 400 = 100 engagements, assuming unchanged unit costs and sufficient capacity.

**Decision:** The candidate confuses revenue with profit. Under these assumptions the proposal reduces the monthly operating result by AED 14,000. Reject the stated rationale; explore willingness to pay, capacity and acquisition costs before proposing another offer.

**Rubric implication:** Numerical correctness = 0. Major reasoning failure requiring correction.

## STRAT-002: Sales target exceeds delivery capacity

**Prompt:** Three consultants each have 120 delivery hours per month. Each engagement requires 30 delivery hours. Management proposes accepting 15 engagements next month without adding delivery resources.

**Candidate answer:** Accept all 15; the team has three consultants and can distribute the work evenly.

**Reference check:**

- Available delivery capacity: 3 × 120 = 360 hours.
- Required effort: 15 × 30 = 450 hours.
- Gap: 90 hours, equivalent to three engagements.
- Maximum supported volume: 360 / 30 = 12 engagements.

**Decision:** Present at least two options: cap commitments at 12, phase delivery, or secure 90 additional qualified delivery hours before acceptance. Revalidate overhead, quality and contingency assumptions. Avoid assuming that unpaid overtime resolves the gap.

**Rubric implication:** Feasibility = 0 because the proposed commitment exceeds stated capacity.

## STRAT-003: Missing demand evidence

**Prompt:** A consultancy has ten positive interviews from existing UAE customers and no research in a proposed new market. Should it enter that market immediately?

**Candidate answer:** Demand is proven. Launch immediately and expect 30% market share in the first year.

**Reference check:** Existing-customer feedback does not establish demand in a different market. There is no source for the market-share estimate.

**Decision:** Recommend staged validation: identify target buyers, test demand and willingness to pay, examine local competitors and delivery constraints, define pilot success criteria, and defer major irreversible spending until evidence supports it. A limited exploratory pilot can be defensible if its budget and stopping conditions are explicit.

**Rubric implication:** Grounding = 0; uncertainty handling = 0. Record the unsupported market-share estimate and the evidence gap separately.

## Validation record

The arithmetic in STRAT-001 and STRAT-002 was independently checked during authoring. STRAT-003 was reviewed for logical consistency with its source facts. This is manual fixture validation, not automated testing, live-model performance or external commercial verification.
