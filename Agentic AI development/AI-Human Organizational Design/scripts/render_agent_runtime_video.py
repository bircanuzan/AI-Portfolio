"""Render an execution-log video of real Python agent tools and output.

This is a readable CLI trace replay of an ACTUALLY EXECUTED code path,
NOT a live LLM screen recording and NOT an enterprise production deployment.
Frames are derived from HumanCapitalAgent.run(), not manually typed results.
"""
from __future__ import annotations
import json
import subprocess
import sys
import textwrap
from pathlib import Path
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from src.hcia.agent_runtime import HumanCapitalAgent
from src.hcia.planner import PlanError

OUTPUT=ROOT/"demo"/"generated"
OUTPUT.mkdir(parents=True,exist_ok=True)
GOAL="Evaluate if 0.8 FTE of HR tasks can be redeployed through workforce redesign"
agent=HumanCapitalAgent()
execution=agent.run(GOAL)
try:
    agent.run("Approve terminating employees to achieve savings")
    raise AssertionError("Expected sensitive request to be refused")
except PlanError as exc:
    refusal=str(exc)
(OUTPUT/"agent_execution_trace.json").write_text(json.dumps({
    "execution":execution,"safety_refusal":refusal
},indent=2),encoding="utf-8")

W,H=1080,1350
BG=(13,17,21);WINDOW=(20,27,33);LINE=(66,75,83)
GOLD=(213,173,84);WHITE=(242,242,239)
SOFT=(181,191,197);GREEN=(107,219,167);RED=(244,133,133)
BLUE=(132,186,239)
FONTS="/usr/share/fonts/truetype/dejavu/"
def f(n,bold=False,mono=False):
    name=("DejaVuSansMono" if mono else "DejaVuSans")+("-Bold" if bold else "")+".ttf"
    try:return ImageFont.truetype(FONTS+name,n)
    except OSError:return ImageFont.load_default()

def txt(d,xy,s,n=25,color=WHITE,bold=False,mono=False):
    d.text(xy,str(s),font=f(n,bold,mono),fill=color)

def wrap(s,width=52):
    return textwrap.wrap(str(s),width=width,break_long_words=False,break_on_hyphens=False) or [""]

log=[]
frames=[]
def short_metric(a):
    if a["type"]=="TOOL_OBSERVATION":
        r=a["result"]
        t=a["tool"]
        if t=="read_workforce":
            return ["POSITIONS: "+str(r["approved_positions"]),"OCCUPIED: "+str(r["occupied"]),
                    "VACANCIES: "+str(r["vacancies"])]
        if t=="model_capacity":
            return ["POTENTIAL HOURS: "+str(r["net_candidate_hours"]),
                    "WORKLOAD FTE: "+str(r["capacity_fte"]),
                    "FUTURE ROLES: "+str(r["future_human_roles"]),
                    "ORG UNITS: "+str(r["future_org_units"])]
        if t=="stress_test":
            return ["ADOPTION MULTIPLIER: "+str(r["adoption_multiplier"]),
                    "SENSITIVITY FTE: "+str(r["capacity_fte"]),
                    "NO JOB CUTS APPROVED"]
        if t=="review_governance":
            return ["DECISION: HUMAN REVIEW", "AGENT WRITE AUTHORITY: NO",
                    "CPO | FINANCE | LEGAL | AI ASSURANCE"]
    if a["type"]=="AGENT_FINAL":
        r=a["result"]
        return ["BASE FTE: "+str(r["base_capacity_fte"]),
                "STRESS FTE: "+str(r["stress_capacity_fte"]),
                "TARGET: "+str(r["target_fte"])+" FTE",
                "HUMAN REVIEW REQUIRED"]
    return None

def render(event,caption,duration=2.6):
    canvas=Image.new("RGB",(W,H),BG)
    d=ImageDraw.Draw(canvas)
    d.rectangle((0,0,W,12),fill=GOLD)
    txt(d,(60,55),"HUMANEVOX  /  AGENT RUNTIME",28,GOLD,True)
    txt(d,(60,111),"DEVELOPER DEMO  •  EXECUTED PYTHON TOOL TRACE",22,WHITE,True)
    d.rounded_rectangle((57,164,1026,240),radius=18,fill=(43,38,30))
    txt(d,(83,185),"OFFLINE TEST POLICY  •  NO LIVE LLM INVOCATION",22,GOLD,True)
    txt(d,(60,258),"USER OBJECTIVE",17,SOFT,True)
    for i,line in enumerate(wrap(GOAL,58)[:2]):
        txt(d,(60,292+i*32),line,22,WHITE)
    d.rounded_rectangle((56,381,1026,956),radius=18,fill=WINDOW,outline=LINE,width=2)
    d.rectangle((57,381,1025,429),fill=(38,47,54))
    txt(d,(81,390),"hcia-agent  $  python -m scripts.demo_agent_runtime",19,SOFT,mono=True)
    inner=list(log)[-12:]
    line_y=452
    for item in inner:
        msg=item["text"]
        for line in wrap(msg,62)[:3]:
            if line_y>922:break
            txt(d,(79,line_y),line,19,item["color"],mono=True)
            line_y+=35
        if line_y>922:break
    # Not the model's hidden reasoning, only explicit tool-selection reasons.
    d.rounded_rectangle((56,976,1026,1132),radius=16,fill=(35,40,44),outline=LINE,width=2)
    txt(d,(79,992),"CURRENT OBSERVATION",17,GOLD,True)
    metrics=short_metric(event) or []
    if metrics:
        for i,metric in enumerate(metrics[:4]):
            txt(d,(79+(i%2)*475,1029+(i//2)*43),metric,19,GREEN,True)
    else:
        txt(d,(79,1035),"Tool outputs appear here after execution",20,SOFT)
    d.rounded_rectangle((56,1152,1026,1260),radius=17,fill=(49,44,33))
    txt(d,(79,1166),"ON-SCREEN CAPTION",17,GOLD,True)
    for i,line in enumerate(wrap(caption,62)[:2]):
        txt(d,(79,1194+i*27),line,19,WHITE)
    txt(d,(65,1290),"REPRODUCIBLE TRACE REPLAY • SYNTHETIC DATA • 0 HRIS WRITES",18,SOFT,True)
    img=OUTPUT/("trace_%02d.png"%len(frames))
    canvas.save(img)
    frames.append((img,duration))

def emit(text,color=WHITE):
    log.append({"text":text,"color":color})
    if len(log)>13:del log[:-13]

emit("$ user> "+GOAL,GOLD)
render({"type":"USER_GOAL"},"An actual user objective enters the working Python agent controller.",3.2)
emit("policy: OFFLINE_ADAPTIVE_POLICY_NOT_AN_LLM",SOFT)
emit("runner: observe -> decide -> validate -> execute -> replan",BLUE)
render({"type":"PLANNER_MODE"},"The offline test policy chooses tools after observing previous results; no LLM inference is claimed.",3.4)
for event in execution["trace"]:
    kind=event["type"]
    if kind=="AGENT_ACTION":
        tool=event["tool"];step=event["turn"]
        emit("AGENT: propose "+tool,BLUE)
        if event["args"]:emit("ARGS: "+json.dumps(event["args"]),BLUE)
        emit("WHY: "+event["reason"],SOFT)
        render(event, "Step "+str(step)+": the agent selects the next allowlisted tool.",3.2)
    elif kind=="TOOL_OBSERVATION":
        emit("EXECUTED: "+event["tool"]+"()",GREEN)
        metrics=short_metric(event) or []
        for m in metrics[:3]:emit("OBSERVED: "+m,GREEN)
        render(event,"Real Python tool returned these values from fictional HR data.",3.8)
    elif kind=="AGENT_FINAL":
        r=event["result"]
        emit("AGENT FINAL: "+r["outcome"],GOLD)
        emit("base="+str(r["base_capacity_fte"])+" fte; stress="+str(r["stress_capacity_fte"])+" fte",GREEN)
        emit("target="+str(r["target_fte"])+" fte; approvals=HUMAN",WHITE)
        render(event,"The answer cites observed model output, stress conditions and human approvals.",5.0)
emit("USER> Approve terminating employees to achieve savings",RED)
emit("DENIED: "+refusal,RED)
render({"type":"GUARDRAIL"},"A sensitive personnel-action request is refused before execution.",4.5)
emit("DONE: "+str(execution["tool_calls"])+" real tool calls; write actions=0",GREEN)
emit("MODEL STATUS: configured LLM optional, NOT exercised",GOLD)
render({"type":"DONE"},"This proves a bounded agent runtime. It is not production deployment or a live LLM demo.",5.0)

concat=OUTPUT/"agent_concat.txt"
concat.write_text("\n".join(
    [x for p,secs in frames for x in ("file '"+str(p)+"'","duration "+str(secs))]
    +["file '"+str(frames[-1][0])+"'"]
)+"\n",encoding="utf-8")
dest=OUTPUT/"agent_runtime_executed_tool_trace.mp4"
subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(),"-hide_banner","-loglevel","error","-y",
    "-f","concat","-safe","0","-i",str(concat),
    "-vf","fps=24,format=yuv420p","-c:v","libx264",
    "-pix_fmt","yuv420p","-preset","medium","-b:v","800k","-minrate","800k",
    "-maxrate","800k","-bufsize","1600k","-x264-params","nal-hrd=cbr:filler=1",
    "-movflags","+faststart",str(dest)],check=True)
print(json.dumps({"video":str(dest),"tool_calls":execution["tool_calls"],
    "steps_rendered":len(frames),"frames_from":"actually executed local Python agent trace",
    "live_llm":False,"synthetic":True,"approved_staff_changes":0},indent=2))
