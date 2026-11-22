"""Synthetic People Operations headcount and compensation reference + rubric.
No live LLM, HRIS, employment decisions, real pay data or customer integration.
"""
import argparse
import json
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

DATA=Path(__file__).resolve().parents[1]/"data"/"scenario.json"
CENT=Decimal("0.01")

def amt(v):
    return Decimal(str(v)).quantize(CENT,rounding=ROUND_HALF_UP)

def load(path=DATA):
    with Path(path).open(encoding="utf-8") as f:
        return json.load(f)

def reference(data=None):
    d=data if data is not None else load()
    if d.get("data_type")!="synthetic":
        raise ValueError("Only synthetic data supported")
    months=d["months"]
    if not months or len(set(months))!=len(months) or months!=sorted(months):
        raise ValueError("Invalid month order")
    load_pct=Decimal(d["benefits_load"])
    if not 0<=load_pct<=1:
        raise ValueError("Invalid benefits load")
    roles={}
    for role in d["roles"]:
        rid=role["id"]
        if not rid or rid in roles:
            raise ValueError("Duplicate role")
        salary=amt(role["salary"])
        if not amt(role["salary_min"])<=salary<=amt(role["salary_max"]):
            raise ValueError("Salary outside synthetic salary band")
        if type(role["headcount"]) is not int or role["headcount"]<0:
            raise ValueError("Invalid source headcount")
        roles[rid]=role
    movements={}
    for month,rid,hires,exits in d["movements"]:
        key=(month,rid)
        if key in movements or month not in months or rid not in roles:
            raise ValueError("Invalid or duplicate movement key")
        if type(hires) is not int or type(exits) is not int or min(hires,exits)<0:
            raise ValueError("Invalid hiring movement")
        movements[key]=(hires,exits)
    expected={(m,r) for m in months for r in roles}
    if set(movements)!=expected:
        raise ValueError("Missing movement records")
    budgets={}
    for month,dept,value in d["budgets"]:
        key=(month,dept)
        if key in budgets or amt(value)<0:
            raise ValueError("Invalid budget")
        budgets[key]=amt(value)
    all_depts={r["department"] for r in roles.values()}
    if set(budgets)!={(m,dept) for m in months for dept in all_depts}:
        raise ValueError("Incomplete budget")
    prev={rid:r["headcount"] for rid,r in roles.items()}
    result=[]; agg=defaultdict(lambda:{"hc":0,"cost":Decimal("0")})
    for month in months:
        for rid in sorted(roles):
            role=roles[rid]
            opening=prev[rid]
            hires,exits=movements[(month,rid)]
            closing=opening+hires-exits
            if closing<0:
                raise ValueError("Negative closing headcount")
            salary=amt(role["salary"])
            base=amt(closing*salary)
            loaded=amt(base*(1+load_pct))
            result.append({"month":month,"role_id":rid,
                "department":role["department"],"opening_hc":opening,
                "hires":hires,"exits":exits,"closing_hc":closing,
                "salary_aed":f"{salary:.2f}",
                "base_cost_aed":f"{base:.2f}","loaded_cost_aed":f"{loaded:.2f}"})
            prev[rid]=closing
            g=agg[(month,role["department"])]
            g["hc"]+=closing
            g["cost"]+=loaded
    summary=[]
    for key,g in sorted(agg.items()):
        budget=budgets[key];cost=amt(g["cost"])
        summary.append({"month":key[0],"department":key[1],"closing_hc":g["hc"],
            "loaded_cost_aed":f"{cost:.2f}","budget_aed":f"{budget:.2f}",
            "budget_minus_cost_aed":f"{amt(budget-cost):.2f}"})
    return {"case_id":d["case_id"],"model":"SYNTHETIC_DETERMINISTIC",
            "rows":result,"summary":summary,
            "human_pay_approval_required":True,
            "live_model_used":False,"actual_employment_writes":0}

def grade(candidate,correct=None):
    ref=correct if correct is not None else reference()
    rows=candidate.get("rows")
    summaries=candidate.get("summary")
    if not isinstance(rows,list) or not isinstance(summaries,list):
        raise ValueError("Candidate requires rows and summary lists")
    rkeys=[(x["month"],x["role_id"]) for x in rows]
    skeys=[(x["month"],x["department"]) for x in summaries]
    ref_rows={(x["month"],x["role_id"]):x for x in ref["rows"]}
    ref_sum={(x["month"],x["department"]):x for x in ref["summary"]}
    got_rows=dict(zip(rkeys,rows))
    got_sum=dict(zip(skeys,summaries))
    exact=len(rows)==len(ref_rows)==len(set(rkeys)) and set(got_rows)==set(ref_rows)
    sums_exact=len(summaries)==len(ref_sum)==len(set(skeys)) and set(got_sum)==set(ref_sum)
    def same(fields, actual, truth, complete):
        if not complete:return False
        try:
            return all(all(Decimal(str(actual[k][field]))==Decimal(str(truth[k][field]))
                       for field in fields) for k in truth)
        except (KeyError,ValueError,TypeError,ArithmeticError):
            return False
    checks={
        "POP-01": exact,
        "POP-02": exact and all(got_rows[k].get("department")==ref_rows[k]["department"] for k in ref_rows),
        "POP-03": same(("opening_hc",),got_rows,ref_rows,exact),
        "POP-04": same(("hires","exits"),got_rows,ref_rows,exact),
        "POP-05": same(("closing_hc",),got_rows,ref_rows,exact) and all(
             isinstance(got_rows[k].get("closing_hc"),int) and got_rows[k]["closing_hc"]>=0
             for k in ref_rows) if exact else False,
        "POP-06": same(("salary_aed",),got_rows,ref_rows,exact),
        "POP-07": same(("base_cost_aed","loaded_cost_aed"),got_rows,ref_rows,exact),
        "POP-08": sums_exact and same(("closing_hc","loaded_cost_aed"),got_sum,ref_sum,sums_exact),
        "POP-09": sums_exact and same(("budget_aed","budget_minus_cost_aed"),got_sum,ref_sum,sums_exact)
    }
    criteria=[{"id":k,"result":"YES" if v else "NO"} for k,v in checks.items()]
    criteria.extend({"id":k,"result":"NOT_EVALUATED","reason":"Requires human Excel workbook inspection"}
        for k in ("POP-10","POP-11","POP-12"))
    return {"status":"PASS_NUMERIC_REFERENCE" if all(checks.values()) else "FAIL_NUMERIC_REFERENCE",
        "automated_yes":sum(checks.values()),"automated_total":9,
        "workbook_review_pending":3,"criteria":criteria,
        "live_model_graded":False,"real_hr_writes":0}

if __name__=="__main__":
    cli=argparse.ArgumentParser()
    cli.add_argument("--output",help="Save synthetic reference to JSON")
    cli.add_argument("--grade",help="Path to candidate JSON to grade")
    args=cli.parse_args()
    if args.grade:
        with open(args.grade,encoding="utf-8") as f:
            candidate=json.load(f)
        report=grade(candidate)
    else:
        report=reference()
    output=json.dumps(report,indent=2)
    if args.output:
        Path(args.output).write_text(output+"\n",encoding="utf-8")
    else:
        print(output)
