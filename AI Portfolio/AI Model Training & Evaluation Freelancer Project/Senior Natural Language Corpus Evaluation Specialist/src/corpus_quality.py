"""Lightweight, offline NLP dataset hygiene checks; not full linguistic analysis."""
from collections import Counter
import json
import sys
import unicodedata

REQUIRED=("id","text","language","domain","source","annotation_a","annotation_b")

def normalize(text):
    return " ".join(unicodedata.normalize("NFC",text).casefold().split())

def kappa(left,right):
    if len(left)!=len(right) or not left:raise ValueError("aligned nonempty labels required")
    n=len(left); observed=sum(a==b for a,b in zip(left,right))/n
    ca=Counter(left);cb=Counter(right)
    chance=sum(ca[x]*cb[x] for x in set(ca)|set(cb))/(n*n)
    return round((observed-chance)/(1-chance),4) if chance < 1 else (1.0 if observed==1 else 0.0)

def audit(records):
    if not isinstance(records,list):raise ValueError("expected list")
    seen=set();dups=[];missing=[];empty=[];langs=Counter();domains=Counter();a=[];b=[]
    for i,r in enumerate(records):
        ident=r.get("id",f"row-{i}")
        for k in REQUIRED:
            if not isinstance(r.get(k),str) or not r[k].strip():missing.append((ident,k))
        text=r.get("text","")
        if not isinstance(text,str) or not text.strip():
            empty.append(ident)
        else:
            norm=normalize(text)
            if norm in seen:dups.append(ident)
            seen.add(norm)
        if r.get("language"):langs[r["language"]]+=1
        if r.get("domain"):domains[r["domain"]]+=1
        if r.get("annotation_a") and r.get("annotation_b"):
            a.append(r["annotation_a"]);b.append(r["annotation_b"])
    return {"rows":len(records),"duplicate_ids":dups,
       "empty_text_ids":empty,"missing_fields":missing,
       "language_counts":dict(langs),"domain_counts":dict(domains),
       "annotation_pairs":len(a),"cohens_kappa":kappa(a,b) if a else None}

if __name__=="__main__":
    with open(sys.argv[1],encoding="utf-8") as f: rows=json.load(f)
    print(json.dumps(audit(rows),ensure_ascii=False,indent=2))
