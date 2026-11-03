"""Create an authentic, silent LinkedIn-ready video from executable synthetic code.

4:5 (1080x1350), H.264 MP4, 24 FPS with readable on-screen narrative.
All quantities in this video are computed by the checked-in Python engines,
not copied from imaginary production records or engineering screenshots.
"""
from __future__ import annotations

import json
import math
import subprocess
import sys
import textwrap
from pathlib import Path

import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from src.hcia.engine import load_data,execute
from src.hcia.workforce_design import load_design,model_capacity

OUT=ROOT/"demo"/"generated"
OUT.mkdir(parents=True,exist_ok=True)
DATA=load_data()
RESULT=execute(DATA,"workforce_redesign","ALL")
CAP=RESULT["capacity"]
CASE=load_design()
NO_ADOPTION=model_capacity(CASE,0)
HIGH_ADOPTION=model_capacity(CASE,1.2)
HC_BRIEF=execute(DATA,"executive_brief","ALL")
W,H=1080,1350
M=76
BKG=(15,19,24)
PANEL=(26,31,37)
GOLD=(214,174,90)
GOLD_D=(106,88,57)
WHITE=(242,241,236)
MUTED=(170,180,187)
SOFT=(218,207,181)
LINE=(57,64,70)
DURATION=4.4

def font(sz,bold=False):
    file="/usr/share/fonts/truetype/dejavu/DejaVuSans"+("-Bold" if bold else "")+".ttf"
    try:return ImageFont.truetype(file,sz)
    except OSError:return ImageFont.load_default()

def text(d,x,y,message,size=27,color=WHITE,bold=False,spacing=8):
    d.multiline_text((x,y),message,font=font(size,bold),fill=color,spacing=spacing)

def wrapped(d,x,y,message,width=46,size=27,color=WHITE,bold=False,gap=9):
    lines=textwrap.wrap(message,width=width,break_long_words=False,break_on_hyphens=False)
    text(d,x,y,"\n".join(lines),size,color,bold,gap)
    return y+(size+gap)*len(lines)

def card(d,x,y,w,h,title,value="",detail="",accent=GOLD):
    d.rounded_rectangle((x,y,x+w,y+h),radius=19,fill=PANEL,outline=LINE,width=2)
    d.rectangle((x+22,y+24,x+29,y+h-24),fill=accent)
    text(d,x+52,y+23,title.upper(),20,MUTED,True)
    if value:
        text(d,x+52,y+66,str(value),43,WHITE,True)
    if detail:
        wrapped(d,x+52,y+(128 if value else 71),detail,width=int(w/21),size=22,color=SOFT)

def tag(d,x,y,value,color=GOLD):
    f=font(20,True);bb=d.textbbox((0,0),value,font=f);size=bb[2]-bb[0]+34
    d.rounded_rectangle((x,y,x+size,y+42),radius=14,fill=(42,39,32),outline=GOLD_D)
    text(d,x+18,y+7,value,20,color,True)
    return size

def frame(index,section,title,subtitle=""):
    im=Image.new("RGB",(W,H),BKG)
    d=ImageDraw.Draw(im)
    d.rectangle((0,0,W,13),fill=GOLD)
    text(d,M,64,"HUMANEVOX  /  HUMAN CAPITAL AI LAB",23,GOLD,True)
    text(d,M,124,section.upper(),23,MUTED,True)
    title_lines=textwrap.wrap(title,width=26,break_long_words=False)
    text(d,M,173,"\n".join(title_lines),51,WHITE,True,spacing=10)
    fy=173+67*len(title_lines)
    if subtitle:wrapped(d,M,fy+12,subtitle,44,26,SOFT)
    d.line((M,1193,W-M,1193),fill=LINE,width=2)
    text(d,M,1211,"SYNTHETIC WORKFORCE DESIGN • NO PRODUCTION DEPLOYMENT",18,GOLD,True)
    text(d,M,1254,"Human approvals preserved. No job cuts or cash savings claimed.",19,MUTED)
    text(d,W-140,1300,f"{index:02d}/13",21,MUTED,True)
    return im,d

slides=[]
def make(index,section,title,subtitle,draw_func,caption):
    im,d=frame(index,section,title,subtitle)
    draw_func(d)
    slides.append((im,caption))

make(1,"The engineering question","From HR analytics to Human–AI workforce design",
     "A simulated, explainable path from tasks to roles, capacity and future operating structures.",
     lambda d: (
       card(d,M,515,928,195,"The design problem","WHAT WORK?","Identify activity demand before suggesting automation"),
       card(d,M,730,928,195,"The accountability question","WHO DECIDES?","Separate analytical assistance from human authority"),
       card(d,M,945,928,166,"The decision boundary","","Proposed structures require CPO, Finance, Legal and workforce consultation")
     ),
     "An executable fictional case connects tasks, roles, capacity scenarios and a proposed organisation structure.")

make(2,"01 / task analysis","Build the activity baseline",
     "Annual work demand is modelled before considering any AI assistance.",
     lambda d: (
       card(d,M,440,928,188,"Fictional pilot work demand",f"{CAP['baseline_hours']:,.0f} hours","Annual baseline across seven activity groups"),
       card(d,M,650,445,195,"Activities modelled",len(CAP["activities"]),"Volume × handling time"),
       card(d,M+466,650,462,195,"Productive hours / FTE",f"{CASE['meta']['productive_hours_per_fte']:,}","Planning assumption, not actual staffing"),
       card(d,M,878,928,205,"Examples","","Policy case triage  •  Interview scheduling  •  Workforce scenario preparation")
     ),
     "The synthetic activity model contains seven work groups, totalling 4,813 annual workload hours.")

def work_allocation(d):
    selected=[next(a for a in CAP["activities"] if a["task_id"]==k) for k in ("A1","A2","A5","A6")]
    top=466
    max_h=max(r["baseline_hours"] for r in selected)
    for i,r in enumerate(selected):
        y=top+i*151
        wrapped(d,M,y,r["work"],width=46,size=22,bold=True)
        d.rounded_rectangle((M,y+48,M+830,y+72),radius=9,fill=(55,62,67))
        bar=int(830*r["net_redeployable_hours_hypothesis"]/max_h)
        if bar>0:d.rounded_rectangle((M,y+48,M+bar,y+72),radius=9,fill=GOLD)
        text(d,M,y+83,f"Baseline {r['baseline_hours']:,.0f}h   /   Scenario released {r['net_redeployable_hours_hypothesis']:,.0f}h",20,MUTED)
    tag(d,M,1091,"RESERVED DECISIONS → 0 AI APPROVALS")
make(3,"02 / allocation","Choose human and agent work",
     "Task suitability does not equal permission to automate people decisions.",
     work_allocation,
     "Illustrative capacity exposure is task-specific. Job evaluation and employee relations decisions remain human owned.")

def job_roles(d):
    jobs=RESULT["job_architecture"]
    ids=(0,2,7)
    for i,idx in enumerate(ids):
        role=jobs[idx]
        y=437+i*220
        card(d,M,y,928,196,role["family"],"",role["role"])
        text(d,M+53,y+130,"Skills: "+", ".join(role["skills"][:2]),19,GOLD)
    tag(d,M,1120,f"{len(jobs)} FUTURE HUMAN ROLE PROFILES / PROPOSED")
make(4,"03 / job architecture","Redesign roles and capabilities",
     "Job family, skills, decision authority and work ownership are linked.",
     job_roles,
     "Eight fictional future role profiles include human AI service operations, workforce intelligence and agent assurance.")

def decisions(d):
    items=[
      ("GRADE AND JOB EVALUATION","Reward panel or qualified human evaluator"),
      ("EMPLOYEE RELATIONS","Legal / ER specialist retains final authority"),
      ("HIRING AND COMPENSATION","Named leaders retain authorisation")
    ]
    for i,(head,sub) in enumerate(items):
        y=460+i*211
        d.rounded_rectangle((M,y,W-M,y+182),radius=19,fill=PANEL,outline=LINE,width=2)
        tag(d,M+24,y+24,"HUMAN ONLY")
        text(d,M+28,y+80,head,25,WHITE,True)
        text(d,M+28,y+129,sub,22,MUTED)
    text(d,M,1118,"AI may prepare evidence; it cannot sign a people decision.",22,GOLD,True)
make(5,"04 / decision authority","Keep sensitive decisions human-owned",
     "Automation exposure is deliberately set to zero for reserved HR determinations.",
     decisions,
     "The design reserves job grading, employee relations, hiring and pay approval to accountable people.")

def org_structure(d):
    """Reflect the actual parent links in the fictional reporting hierarchy."""
    hierarchy={unit["unit"]:unit for unit in RESULT["future_structure"]}
    def unit(y,key,x=170,w=830,h=80,fsize=24):
        u=hierarchy[key]
        d.rounded_rectangle((x,y,x+w,y+h),radius=13,fill=PANEL,outline=GOLD_D,width=2)
        text(d,x+20,y+10,u["unit"].upper(),fsize,WHITE,True)
        text(d,x+20,y+h-33,u["human_accountability"],18,MUTED)
    unit(417,"Group People Office",x=170,w=830,h=81)
    # CPO is parent of OE, Services, Talent and Reward. They are NOT
    # subordinated to each other; only People Data reports into Group OE.
    d.line((170,460,130,460),fill=GOLD,width=3)
    d.line((130,460,130,993),fill=GOLD,width=3)
    peers=[
      (541,"Group OE & Workforce Architecture"),
      (764,"Human–AI HC Service Operations"),
      (856,"Talent & Capability Intelligence"),
      (948,"Reward & Employee Risk Governance")
    ]
    for y,name in peers:
        d.line((130,y+40,170,y+40),fill=GOLD,width=3)
        unit(y,name,x=170,w=830,h=80,fsize=23)
    # One explicit second-level reporting relationship: Data -> Group OE.
    d.line((224,621,224,660),fill=GOLD,width=2)
    d.line((224,660,255,660),fill=GOLD,width=2)
    unit(658,"People Data & Workforce Intelligence",x=255,w=745,h=76,fsize=21)
    wrapped(d,M,1049,
        "Matrix: Agent Risk & Assurance reports through Group OE, with CIO/CISO risk partnership.",
        width=67,size=21,color=SOFT)
    text(d,M,1128,"ILLUSTRATIVE / UNAPPROVED TARGET STRUCTURE",18,GOLD,True)
make(6,"05 / organisation design","Design the future operating model",
     "Illustrative reporting interfaces, not approved organisational changes.",
     org_structure,
     "A future-state Group structure proposes organisation effectiveness, people analytics, service operations and talent capability governance.")

def capacity(d):
    card(d,M,433,928,155,"Baseline workload",f"{CAP['baseline_hours']:,.0f}h","")
    card(d,M,611,928,155,"Potential net capacity",f"{CAP['net_redeployable_hours_hypothesis']:,.2f}h","")
    card(d,M,790,928,170,"Equivalent productive capacity",f"{CAP['potential_capacity_to_redeploy_fte_equivalent']:.3f} FTE","Workload capacity, not staff reductions")
    wrapped(d,M,1005,"Method: eligible task hours × adoption × (1 − rework) − human oversight.",width=65,size=23,color=SOFT)
    tag(d,M,1106,"0 APPROVED HEADCOUNT CHANGES")
make(7,"06 / scenario modelling","Calculate net capacity responsibly",
     "Gross theoretical hours are reduced by rework and human review effort.",
     capacity,
     "The hypothetical model calculates 1,460.55 net hours of potentially redeployable work, equivalent to about 0.974 FTE of workload, not layoffs.")

def reinvest(d):
    entries=CAP["capacity_reinvestment"]
    y=443
    for r in entries:
        w=round(next(x["weight"] for x in CASE["redistribution_weights"] if x["investment"]==r["investment"])*100)
        wrapped(d,M,y,r["investment"],width=43,size=23,bold=True)
        d.rounded_rectangle((M,y+71,M+905,y+107),radius=10,fill=PANEL)
        d.rounded_rectangle((M,y+71,M+int(905*w/35),y+107),radius=10,fill=GOLD)
        text(d,M,y+117,f"{w}%  •  {r['hours_reinvested']:,.1f} scenario hours",22,MUTED)
        y+=176
make(8,"07 / workforce transition","Reinvest capacity; do not assume cuts",
     "The model redirects potential time toward higher-value human responsibilities.",
     reinvest,
     "Potential capacity is allocated to service quality, workforce modelling, reskilling and agent service assurance.")

def options(d):
    card(d,M,445,928,170,"No agent adoption",f"{NO_ADOPTION['net_redeployable_hours_hypothesis']:,.0f}h","Control scenario; capacity release is zero")
    card(d,M,640,928,170,"Guarded base-case adoption",f"{CAP['net_redeployable_hours_hypothesis']:,.0f}h","Unverified assumptions; review effort included")
    card(d,M,835,928,170,"Higher adoption scenario",f"{HIGH_ADOPTION['net_redeployable_hours_hypothesis']:,.0f}h","Sensitivity only; human-only decisions unchanged")
    tag(d,M,1092,"CFO VALIDATION REQUIRED BEFORE FINANCIAL CLAIMS")
make(9,"08 / scenario comparison","Test assumptions, not optimism",
     "Counterfactuals should challenge projected benefits and surface risks.",
     options,
     "Zero, base and higher adoption scenarios are simulated. No financial benefit or employee impact is verified.")

def safeguards(d):
    items=[
      "Approved source data and service-level baseline",
      "Reward, Legal and employee consultation",
      "Finance and CPO structural approval",
      "AI security, privacy and operating assurance",
      "Observed pilot outcomes and adverse-event review"
    ]
    for i,item in enumerate(items):
        y=445+i*130
        d.rounded_rectangle((M,y,M+928,y+101),radius=16,fill=PANEL,outline=LINE,width=2)
        tag(d,M+20,y+27,"G"+str(i+1))
        wrapped(d,M+105,y+21,item,width=39,size=23,color=WHITE,bold=True)
    tag(d,M,1114,"NO AGENT AUTHORITY OVER EMPLOYEE OUTCOMES")
make(10,"09 / governance","Make every structural decision auditable",
     "Decision support only: accountable people retain authority at every gate.",
     safeguards,
     "Employment, reward, budget, security and organisational decisions require human approval, consultation and validation.")

def technical(d):
    card(d,M,440,928,166,"Original HC intelligence system","6 specialist tools","Recruitment, brand, operations, talent, rewards and workforce")
    card(d,M,629,928,166,"New engineering component","Workforce redesign lab","Task analysis → role architecture → capacity → org structure")
    card(d,M,817,928,167,"Security and traceability","Bounded + audited","Role/entity RBAC, source provenance, zero write operations")
    wrapped(d,M,1046,"Optional sovereign-compatible LLM interface is not a live sovereign deployment.",width=67,size=22,color=SOFT)
make(11,"10 / system architecture","Agentic capability with explicit boundaries",
     "Working code and tests, with optional model-based planning—not autonomous HR decisions.",
     technical,
     "The prototype combines six intelligence tools with an executable workforce design simulation and human-centred decision controls.")

def last(d):
    card(d,M,457,928,232,"What is demonstrable","Executable simulation","Synthetic task demand, job profiles, target organisation and scenario calculations")
    card(d,M,710,928,232,"What is not evidenced","Enterprise deployment","No live HRIS, client pilot, validated workforce savings or approved restructuring")
    tag(d,M,1009,"SOURCE CODE + METHODS IN GITHUB")
    wrapped(d,M,1071,"github.com/bircanuzan/AI-in-HR-Portfolio",width=63,size=24,color=GOLD,bold=True)
make(12,"Proof and limitations","Engineering evidence, not deployment theatre",
     "Human–AI design should connect work, skills, authority and real outcomes.",
     last,
     "This is an independent synthetic engineering demonstration, not a production agent or completed workforce transformation.")

make(13,"Closing perspective","Design the workforce, not only the workflow",
     "Human expertise + bounded AI capability + governed accountability.",
     lambda d: (
        card(d,M,490,928,220,"Strategic focus","TASK → ROLE → STRUCTURE","Workforce capacity, skills, controls and executive governance"),
        card(d,M,760,928,217,"Design principle","HUMAN DECISION AUTHORITY","Every high-impact employment outcome requires accountable approval"),
        tag(d,M,1056,"HUMANEVOX  /  INDEPENDENT PORTFOLIO")
     ),
     "The next frontier is accountable Human AI workforce design. See the open source prototype and methods in GitHub.")

def timestamp(t):
    ms=round(t*1000)
    hh,ms=divmod(ms,3600000);mm,ms=divmod(ms,60000);ss,ms=divmod(ms,1000)
    return f"{hh:02}:{mm:02}:{ss:02},{ms:03}"

paths=[]
captions=[]
for i,(im,caption) in enumerate(slides):
    filename=OUT/f"slide_{i:02d}.png"
    im.save(filename)
    paths.append(filename)
    captions.append(f"{i+1}\n{timestamp(i*DURATION)} --> {timestamp((i+1)*DURATION)}\n{caption}\n")
(OUT/"linkedin_captions.srt").write_text("\n".join(captions),encoding="utf-8")

concat=OUT/"concat.txt"
concat.write_text("\n".join(
    [v for p in paths for v in ("file '"+str(p)+"'",f"duration {DURATION}")]
    +["file '"+str(paths[-1])+"'"]
)+"\n",encoding="utf-8")
dest=OUT/"human_capital_intelligence_agent_synthetic_demo.mp4"
subprocess.run([
    imageio_ffmpeg.get_ffmpeg_exe(),"-hide_banner","-loglevel","error","-y",
    "-f","concat","-safe","0","-i",str(concat),
    "-vf","fps=24,format=yuv420p","-c:v","libx264","-pix_fmt","yuv420p",
    "-preset","medium","-b:v","650k","-minrate","650k","-maxrate","650k",
    "-bufsize","1300k","-x264-params","nal-hrd=cbr:filler=1",
    "-movflags","+faststart",str(dest)
],check=True)
print(json.dumps({
    "video":str(dest),"dimensions":[W,H],"duration_approx_sec":round(len(slides)*DURATION,1),
    "slides":len(slides),"baseline_hours":CAP["baseline_hours"],
    "net_capacity_hours":CAP["net_redeployable_hours_hypothesis"],
    "job_roles":len(RESULT["job_architecture"]),
    "future_organisational_units":len(RESULT["future_structure"]),
    "approved_headcount_changes":CAP["authorized_headcount_changes"],
    "source":"actual execution on fictional data","production":False
},indent=2))
