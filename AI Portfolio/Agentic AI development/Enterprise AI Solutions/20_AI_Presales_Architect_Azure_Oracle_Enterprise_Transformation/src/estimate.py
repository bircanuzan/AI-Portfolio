"""Illustrative consulting effort estimator; no vendor pricing or customer contract."""
ROLES = {
    "solution_architect": (18, 3500),
    "integration_specialist": (12, 2900),
    "data_architect": (10, 3000),
    "security_reviewer": (5, 3200),
    "delivery_manager": (12, 2600),
}
def estimate(roles=ROLES, contingency=0.15):
    if contingency < 0 or contingency > 1:
        raise ValueError("Invalid contingency")
    if not roles or any(days < 0 or rate < 0 for days, rate in roles.values()):
        raise ValueError("Effort and rates must be non-negative")
    base=sum(days*rate for days, rate in roles.values())
    return {"base_aed":base,"contingency_aed":round(base*contingency,2),
            "total_aed":round(base*(1+contingency),2),
            "excluded":"Azure cloud spend, Oracle/CRM licensing, taxes, live implementation"}
if __name__=="__main__":
    print(estimate())
