"""Executive option screening on assumptions. Released capacity is NOT cash savings."""
import argparse,json
from math import isfinite
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]
SOURCE=HERE/"data"/"synthetic_executive_options.json"

def _check_num(v,lower,upper,label):
    if isinstance(v,bool) or not isinstance(v,(int,float)) or not isfinite(v) or not lower<=v<=upper:
        raise ValueError("Invalid "+label)
    return v

def evaluate(case):
    if not isinstance(case,dict) or case.get("classification")!="SYNTHETIC_VALUE_OPTIONS_ONLY":
        raise ValueError("Only explicitly synthetic investment cases")
    volume=_check_num(case.get("annual_requisitions"),1,1000000,"volume")
    if int(volume)!=volume:raise ValueError("Requisition count must be integer")
    minutes=_check_num(case.get("minutes_per_requisition_baseline"),0,1440,"minutes")
    rate=_check_num(case.get("fully_loaded_hr_cost_aed_per_hour"),0,100000,"rate")
    options=case.get("options")
    if not isinstance(options,list) or len(options)<2:raise ValueError("Need comparable options")
    seen=set();results=[]
    for row in options:
        if not isinstance(row,dict) or not isinstance(row.get("id"),str) or not row["id"] or row["id"] in seen:
            raise ValueError("Duplicate or invalid option")
        seen.add(row["id"])
        fraction=_check_num(row.get("fraction_of_minutes_avoided"),0,1,"reduction")
        adoption=_check_num(row.get("eligible_adoption_fraction"),0,1,"adoption")
        oversight=_check_num(row.get("minutes_of_extra_human_oversight_per_requisition"),0,1440,"oversight")
        licence=_check_num(row.get("annual_license_cost_aed"),0,1000000000,"licence")
        assurance=_check_num(row.get("annual_assurance_support_aed"),0,1000000000,"assurance")
        setup=_check_num(row.get("one_time_build_change_cost_aed"),0,1000000000,"setup")
        gross_hours=volume*minutes/60*fraction*adoption
        oversight_hours=volume*oversight/60
        net_hours=gross_hours-oversight_hours
        hypothetical_capacity_value=net_hours*rate
        recurring=licence+assurance
        first_year= hypothetical_capacity_value-recurring-setup
        results.append({
          "option_id":row["id"],"description":row.get("description",""),
          "gross_time_freed_hours":round(gross_hours,2),
          "extra_human_oversight_hours":round(oversight_hours,2),
          "net_capacity_change_hours":round(net_hours,2),
          "hypothetical_capacity_value_aed":round(hypothetical_capacity_value,2),
          "annual_vendor_and_assurance_cost_aed":round(recurring,2),
          "one_time_change_cost_aed":round(setup,2),
          "first_year_capacity_value_less_costs_aed":round(first_year,2),
          "actual_cash_savings_aed":None,
          "production_funding_approved":False
        })
    return {
      "classification":"SYNTHETIC_VALUE_OPTIONS_ONLY",
      "comparison_basis":"One fictional annual demand and cost model; NOT realised financial performance",
      "annual_requisitions":int(volume),"options":results,
      "executive_recommendation":"MEASURE_REAL_BASELINE_AND_PILOT_SIMPLE_PROCESS_FIRST",
      "vendor_or_ai_release":"HOLD",
      "monetization_uncertainty":"Capacity value does not equal cash cost reduction or incremental revenue. No actual HR hours, benefits or AI results measured."
    }
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out",default="")
    args=p.parse_args()
    result=json.dumps(evaluate(json.loads(SOURCE.read_text(encoding="utf-8"))),indent=2)+"\n"
    if args.out:Path(args.out).write_text(result,encoding="utf-8")
    print(result,end="")
if __name__=="__main__":main()
