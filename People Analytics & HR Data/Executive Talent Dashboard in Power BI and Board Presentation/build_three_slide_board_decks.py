#!/usr/bin/env python3
"""Generate two editable, three-slide fictional executive talent board decks.
Requires python-pptx. Usage: python build_three_slide_board_decks.py
No employer data, tenant access or licensed platform required.
"""
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches,Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

HERE=Path(__file__).parent
NAVY=(18,33,55);GOLD=(209,171,105);PAPER=(249,250,252);RED=(194,64,83);GREY=(102,116,135);WHITE=(255,255,255)
def color(rgb):return RGBColor(*rgb)
def rect(sl,x,y,w,h,shade):
 s=sl.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,Inches(x),Inches(y),Inches(w),Inches(h))
 s.fill.solid();s.fill.fore_color.rgb=color(shade);s.line.fill.background()
def text(sl,s,x,y,w,h,pt=14,bold=False,shade=NAVY):
 shape=sl.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h));tf=shape.text_frame
 tf.word_wrap=True;tf.margin_left=tf.margin_right=Inches(.02);tf.margin_top=tf.margin_bottom=0
 p=tf.paragraphs[0];p.text=str(s);p.font.size=Pt(pt);p.font.name="Aptos";p.font.bold=bold;p.font.color.rgb=color(shade)
def base(sl,n,kicker,title,sub):
 sl.background.fill.solid();sl.background.fill.fore_color.rgb=color(PAPER)
 rect(sl,0,0,13.33,.11,GOLD);text(sl,kicker,.55,.39,12,.25,10,True,GOLD)
 text(sl,title,.55,.77,12,.6,26,True);text(sl,sub,.55,1.42,12,.35,12,False,GREY)
 text(sl,"FICTIONAL CASE  •  SYNTHETIC DATA  •  NOT INTERNAL COMPANY REPORTING",.55,7.13,11,.22,9,False,GREY)
 text(sl,f"{n:02d}/03",12.18,7.13,.62,.2,9,False,GREY)
def card(sl,x,y,label,val,target,red=True):
 rect(sl,x,y,2.96,1.02,WHITE);text(sl,label,x+.15,y+.11,2.65,.24,10,False,GREY)
 text(sl,val,x+.15,y+.37,2.63,.39,24,True,RED if red else NAVY);text(sl,"TARGET "+target,x+.15,y+.82,2.7,.19,9,False,GREY)
def produce(oracle):
 prs=Presentation();prs.slide_width=Inches(13.33);prs.slide_height=Inches(7.5)
 s=prs.slides.add_slide(prs.slide_layouts[6])
 base(s,1,"ORACLE FUSION HCM / OTBI" if oracle else "POWER BI / CROSS-SYSTEM REPORTING","Talent performance: completion is not capability","FY2025 annual talent operating plan — independent illustrative case")
 metrics=[("Reviews complete","94%","98%",True),("Goal alignment","82%","90%",True),("Talent reviews","90%","100%",True),("Ready-now bench","45%","70%",True)] if oracle else [("Employee count","519","510",False),("Leader pathways","76%","85%",True),("Critical skills","71%","85%",True),("Learning hours","6,850","7,000",True)]
 for i,(l,v,t,r) in enumerate(metrics):card(s,.62+3.17*i,2.02,l,v,t,r)
 rect(s,.62,3.45,7.5,2.3,WHITE);text(s,"EXECUTIVE INTERPRETATION",.85,3.72,7,.26,10,True,GOLD)
 text(s,"Succession coverage is 62% versus 85% plan. Critical capability gaps create delivery exposure, even when headcount expansion is achieved.",.85,4.19,6.94,1.21,19,True)
 rect(s,8.37,3.45,4.32,2.3,NAVY);text(s,"RECOMMENDED CONTROL",8.59,3.74,3.80,.27,10,True,GOLD)
 text(s,"Use management-owned outcome measures, verified skill uplift and exception closure, not activity counts alone.",8.59,4.14,3.80,1.2,17,True,WHITE)
 s=prs.slides.add_slide(prs.slide_layouts[6]);base(s,2,"TALENT RISK / ORACLE TALENT REVIEW" if oracle else "WORKFORCE RISK / CROSS-SYSTEM MODEL","Critical workforce exposure","Material exceptions, owners and 90-day mitigation")
 rows=[("HIGH","Succession readiness","62% vs 85%","CHRO","Seven uncovered critical delivery positions"),("HIGH","Critical skills","71% vs 85%","Talent Development","40 verified proficiency assessments"),("HIGH","Regretted attrition","10.4% vs <=8%","CHRO","Risk diagnostics for scarce capabilities"),("MEDIUM","Performance closeout","94% vs 98%","Business leaders","Manager exception escalation")]
 for i,(sev,name,actual,owner,act) in enumerate(rows):
  y=1.99+1.06*i;rect(s,.63,y,12.04,.88,WHITE)
  text(s,sev,.82,y+.2,.88,.3,11,True,RED if sev=="HIGH" else GOLD);text(s,name,1.87,y+.16,2.47,.39,14,True)
  text(s,actual,4.49,y+.18,1.72,.36,13,True);text(s,owner,6.40,y+.17,2.08,.34,11,True)
  text(s,act,8.58,y+.13,3.82,.54,11)
 text(s,"Governance: eligible cohorts, effective dates, restricted ratings, and signed HRIS-to-PMR KPI definitions.",.72,6.48,11.95,.34,10,False,GREY)
 s=prs.slides.add_slide(prs.slide_layouts[6]);base(s,3,"EXECUTIVE COMMITTEE / GOVERNED PMR","Three decisions. Named owners. Measurable proof.","Incremental asks proposed, not approved — every amount is synthetic")
 rows=[("D01","Approve successor sprint","AED 1.20m","CHRO","Validated deputies for 7 exposed positions"),("D02","Fund skill verification","AED 0.85m","CTO","40 role-calibrated assessments and cohort"),("D03","Mandate manager closure","No new cost","COO","Monthly performance and Talent Review tasks")]
 for i,(code,title,money,owner,proof) in enumerate(rows):
  y=1.94+1.16*i;rect(s,.63,y,12.03,.94,WHITE)
  text(s,code,.90,y+.24,.55,.27,13,True,GOLD);text(s,title,1.58,y+.13,4.10,.44,15,True)
  text(s,money,5.70,y+.23,1.50,.31,15,True);text(s,owner,7.29,y+.23,1.0,.29,11,True)
  text(s,proof,8.52,y+.11,3.8,.58,10,False,GREY)
 rect(s,.66,5.67,12.01,.66,NAVY);text(s,"TOTAL INCREMENTAL REQUEST: AED 2.05m",.96,5.79,10.0,.33,20,True,WHITE)
 text(s,"Oracle OTBI → Analytics Publisher → PMR" if oracle else "Cross-source Power BI reporting optional; underlying PMR software not asserted",.75,6.49,11.9,.27,10,False,GREY)
 out=HERE/("02_Executive_Talent_Dashboard_Oracle_Fusion_HCM" if oracle else "01_Executive_Talent_Dashboard_Power_BI")/"board"
 out.mkdir(parents=True,exist_ok=True)
 file=out/("Oracle_Executive_Talent_Board_Presentation.pptx" if oracle else "PowerBI_Executive_Talent_Board_Presentation.pptx")
 prs.save(file);print(file)
if __name__=="__main__":
 produce(True);produce(False)
