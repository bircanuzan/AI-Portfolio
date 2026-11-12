"""Synthetic retail returns process improvement sensitivity calculator."""
def roi(monthly_returns=1000,as_is_min=23,to_be_min=13,labour_aed_hour=65,
        project_aed=75000,ops_aed_month=2000):
    vals=[monthly_returns,as_is_min,to_be_min,labour_aed_hour,project_aed,ops_aed_month]
    if any(x<0 for x in vals) or to_be_min>as_is_min:
        raise ValueError("Nonnegative inputs and no negative time-saving assumption required")
    hours=monthly_returns*(as_is_min-to_be_min)/60
    gross=hours*labour_aed_hour
    net=gross-ops_aed_month
    return {"hours_released_month":round(hours,2),"gross_capacity_value_aed":round(gross,2),
            "net_monthly_hypothesis_aed":round(net,2),
            "simple_payback_months":round(project_aed/net,2) if net>0 else None,
            "note":"Capacity is not automatically cash savings; validate with finance."}
if __name__=="__main__":print(roi())
