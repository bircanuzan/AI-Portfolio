# Explainable role matcher and gap analysis

## Inputs
The [example profile](config/sample_profile.json) records skill evidence levels:
- **0**: no evidence claimed.
- **1**: demonstrative portfolio artefact, introductory exposure or limited tool familiarity.
- **2**: professional experience in the stated capability (must be independently verified).

The [role requirements](config/role_requirements.json) define capability minimums and weights totaling 100 **per role**.

## Computation
For each skill, coverage = min(profile evidence level / role required level, 1). Score = sum(coverage x role weight). Output includes skill-level gaps and useful repository project references. It is **neither an ATS algorithm nor a scientific employability estimate**. A role with perfect generic skills can still be ineligible for a particular vacancy.

## Non-negotiable eligibility check
Before a role is shortlisted, manually rule out specific JDs requiring:
- Location or work eligibility not met (target UAE only).
- Mandatory Arabic fluency not possessed or evidenced.
- New-business acquisition, cold sales or quota-led revenue ownership.
- Frequent frontline classroom instruction when seeking non-training work.
- Required licensure, degrees, direct production engineering experience, or long tenure in a specific role not met.

## Decision workflow
1. Confirm official vacancy is open and location fits.
2. Mark mandatory credentials and disqualifiers.
3. Update evidence levels from verifiable CV experience and actual artefacts.
4. Run the **explainable score**; use gaps to decide whether to proceed, not to fabricate expertise.
5. Map at most three relevant artefacts to that vacancy with accurate maturity labels.
6. Revisit every draft CV claim against supporting evidence.

**Example:** A policy-routing Python prototype is useful proof of an offline experiment; it is not proof of an enterprise Copilot Studio production deployment.

~~~
python scripts/role_matcher.py
~~~
