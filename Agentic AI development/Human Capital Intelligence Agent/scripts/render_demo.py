"""Render a REAL run of the local, fictional agent as a narrated-slide demo MP4.

Source values come from live execution of engine.execute during rendering.
This is not a terminal screencast or G42 production environment capture.
Requires Pillow and ffmpeg executable; no keys or internet inference needed.
"""
from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from src.hcia.engine import execute,load_data

OUT=ROOT/"demo"/"generated"
OUT.mkdir(parents=True,exist_ok=True)
data=load_data()
r={tool:execute(data,tool,"ALL")["metrics"] for tool in
   ("talent_acquisition","employer_brand","human_capital_operations",
    "talent_management","total_rewards","workforce_intelligence")}
brief=execute(data,"executive_brief","ALL")

def font(size,bold=False):
    suffix="DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    path="/usr/share/fonts/truetype/dejavu/"+suffix
    try:
        return ImageFont.truetype(path,size)
    except OSError:
        return ImageFont.load_default()

C_BG=(15,18,22);C_GOLD=(205,169,79);C_WHITE=(244,244,241);C_GRAY=(173,180,184)
slides=[
 ("HUMAN CAPITAL INTELLIGENCE AGENT",[
   "Six Human Capital analytics tools + executive orchestration",
   "Version 0.1.0  |  Fictional Cedar Gulf Enterprise",
   "Real code execution / synthetic aggregate data",
   "No HRIS writes, personnel decisions or enterprise deployment"
 ]),
 ("01 / TALENT ACQUISITION",[
   "Applications: "+str(r["talent_acquisition"]["applicants"]),
   "Hires: "+str(r["talent_acquisition"]["hires"]),
   "Applicant-to-hire rate: "+str(r["talent_acquisition"]["applicant_to_hire_pct"])+"%",
   "Cost per hire: AED "+str(r["talent_acquisition"]["cost_per_hire_aed"]),
   "No candidate screening or selection"
 ]),
 ("02 / EMPLOYER BRAND",[
   "Impressions: "+str(r["employer_brand"]["impressions"]),
   "Click-through rate: "+str(r["employer_brand"]["ctr_pct"])+"%",
   "Click-to-application rate: "+str(r["employer_brand"]["click_to_application_pct"])+"%",
   "Campaign figures are invented test records"
 ]),
 ("03 / HC OPERATIONS",[
   "Lifecycle service cases: "+str(r["human_capital_operations"]["cases"]),
   "Within SLA: "+str(r["human_capital_operations"]["within_sla"]),
   "SLA performance: "+str(r["human_capital_operations"]["sla_pct"])+"%",
   "Flagged exceptions require authorised human ownership"
 ]),
 ("04 / TALENT & TOTAL REWARDS",[
   "Critical roles: "+str(r["talent_management"]["critical_roles"]),
   "Ready successors: "+str(r["talent_management"]["successors_ready"]),
   "Rewards cohorts disclosed: "+str(len(r["total_rewards"]["cohorts"])),
   "Compensation comparators are fictional, not salary surveys"
 ]),
 ("05 / WORKFORCE INTELLIGENCE",[
   "Approved positions: "+str(r["workforce_intelligence"]["approved_positions"]),
   "Occupied positions: "+str(r["workforce_intelligence"]["filled_positions"]),
   "Vacancies: "+str(r["workforce_intelligence"]["vacancies"]),
   "Annual budget headroom: AED "+f'{r["workforce_intelligence"]["headroom_aed"]:,.0f}',
   "All figures are fictional planning data"
 ]),
 ("06 / BOUNDED AGENT ORCHESTRATION",[
   "Tool steps executed: "+str(len(brief["plan"])),
   "Automatic write actions: "+str(brief["write_actions_executed"]),
   "Each tool returns provenance and a human-review requirement",
   "RBAC and HMAC audit are testable via the local API",
   "Optional LLM summarisation: not configured or invoked here"
 ]),
 ("WHAT THIS DEMONSTRATION PROVES",[
   "Actual outputs of the local Python intelligence tools",
   "Reproducible synthetic metrics, testable policy boundaries",
   "NOT a cloud deployment, client reference or G42 integration",
   "Production approval, genuine pilot and independent tests remain"
 ])
]
paths=[]
for i,(title,items) in enumerate(slides):
    img=Image.new("RGB",(1280,720),C_BG)
    d=ImageDraw.Draw(img)
    d.rectangle((0,0,1280,13),fill=C_GOLD)
    d.text((84,58),"HUMANEVOX  /  AGENT ENGINEERING LAB",fill=C_GOLD,font=font(19,True))
    d.text((84,137),title,fill=C_WHITE,font=font(37,True))
    d.line((84,210,1190,210),fill=C_GOLD,width=2)
    for j,item in enumerate(items):
        d.ellipse((87,261+j*63,102,276+j*63),fill=C_GOLD)
        d.text((129,252+j*63),item,fill=C_WHITE,font=font(23))
    d.rectangle((0,643,1280,720),fill=(42,38,29))
    d.text((84,657),"SYNTHETIC LOCAL DEMO — NOT PRODUCTION / NOT ELIGIBLE AS DEPLOYED AGENT",
           fill=C_GOLD,font=font(18,True))
    d.text((1060,657),str(i+1)+" / "+str(len(slides)),fill=C_GRAY,font=font(18))
    p=OUT/("slide_%02d.png"%i)
    img.save(p)
    paths.append(p)
listing=OUT/"concat.txt"
listing.write_text("\n".join(
    [s for p in paths for s in ("file '"+str(p)+"'","duration 3.5")]
    +["file '"+str(paths[-1])+"'"])+"\n",encoding="utf-8")
video=OUT/"human_capital_intelligence_agent_synthetic_demo.mp4"
subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-y",
                "-f","concat","-safe","0","-i",str(listing),
                "-vf","fps=20,format=yuv420p","-c:v","libx264",
                "-movflags","+faststart",str(video)],check=True)
print(json.dumps({"video":str(video),"slides":len(slides),"tool_steps":len(brief["plan"]),
                  "source":"actual local Python execution on synthetic data","production":False},indent=2))
