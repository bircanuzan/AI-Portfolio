"""Generate editable synthetic consulting DOCX, XLSX and PPTX examples.

Optional libraries: openpyxl, python-docx, python-pptx.
No real client material, validated claims or external data sources.
"""
import argparse
from pathlib import Path
import json

def build(output_dir):
    from docx import Document
    from docx.shared import Inches, Pt, RGBColor
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.utils import get_column_letter
    from pptx import Presentation
    from pptx.util import Inches as PI, Pt as PP
    from pptx.dml.color import RGBColor as PC
    a = json.loads(Path("data/business_case_assumptions.json").read_text(encoding="utf-8"))
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    # Executive memo (editable Word document).
    doc = Document()
    doc.add_heading("Executive Decision Memo — Controlled Workflow Pilot", 0)
    doc.add_paragraph("SYNTHETIC CASE | NOT A REAL CLIENT RECOMMENDATION", style="Subtitle")
    doc.add_heading("Decision requested", 1)
    doc.add_paragraph("Consider a bounded 90-day pilot, subject to verified baseline, access controls, and Risk/CFO approval.")
    doc.add_heading("Options", 1)
    for t in ["Option A — Baseline study only: lowest execution risk, slower learning.",
              "Option B — Manual process redesign: moderate complexity, no AI deployment.",
              "Option C — Governed AI-assist pilot: higher potential learning and stricter safety gates."]:
        doc.add_paragraph(t, style="List Bullet")
    doc.add_heading("Financial illustration", 1)
    doc.add_paragraph(f"Assumptions: upfront investment USD {a['upfront_investment']:,.0f}; annual gross benefit USD {a['annual_gross_benefit_base']:,.0f}; annual opex USD {a['annual_operating_cost_base']:,.0f}; discount {a['discount_rate']:.0%}.")
    doc.add_paragraph("Not verified; measure baseline and conduct a finance review before approving funding.")
    doc.add_heading("Controls and next steps", 1)
    doc.add_paragraph("Human sign-off for exceptions; role-based access; audit logs; day-30 baseline, day-60 risk gate and day-90 stop/go review.")
    doc.save(out / "client_memo.docx")

    # Formula-driven spreadsheet (editable Excel workbook).
    wb = Workbook()
    ws = wb.active
    ws.title = "Investment Case"
    lines = [
        ["NORTHSTAR SERVICES GROUP — SYNTHETIC WORKFLOW CASE"],
        ["ASSUMPTIONS (edit blue input cells)"],
        ["Upfront investment (USD)", a["upfront_investment"]],
        ["Annual gross benefit at full adoption (USD)", a["annual_gross_benefit_base"]],
        ["Annual operating cost (USD)", a["annual_operating_cost_base"]],
        ["Discount rate", a["discount_rate"]],
        ["Adoption factor", 1],
        ["Cost factor", 1],
        ["Years", a["horizon_years"]],
        [],
        ["CASH FLOW", "Year 0", "Year 1", "Year 2", "Year 3"],
        ["Gross benefit", 0, "=$B$4*$B$7", "=$B$4*$B$7", "=$B$4*$B$7"],
        ["Operating cost", 0, "=$B$5*$B$8", "=$B$5*$B$8", "=$B$5*$B$8"],
        ["Net cash flow", "=-$B$3", "=C12-C13", "=D12-D13", "=E12-E13"],
        ["Discount factor", 1, "=1/(1+$B$6)^1", "=1/(1+$B$6)^2", "=1/(1+$B$6)^3"],
        ["Discounted cash flow", "=B14*B15", "=C14*C15", "=D14*D15", "=E14*E15"],
        ["Net present value (USD)", "=SUM(B16:E16)"],
        ["Simple payback (years)", '=IF(C14>0,$B$3/C14,"Not reached")'],
        [],
        ["SENSITIVITY — NPV BY ADOPTION (ROWS) / OPEX MULTIPLIER (COLUMNS)"],
        ["Adoption \\ Opex multiplier", 0.9, 1, 1.2],
    ]
    for row in lines: ws.append(row)
    for adoption in a["adoption_factors"]:
        row_num = ws.max_row+1
        ws.cell(row_num, 1, adoption)
        for col in range(2, 5):
            cost_col = get_column_letter(col)
            formula = f'=-$B$3+SUMPRODUCT((($B$4*$A{row_num}-$B$5*{cost_col}$21)/(1+$B$6)^{{1,2,3}}))'
            # Use three explicit terms to keep formulas compatible with Excel without array CSE.
            annual = f"($B$4*$A{row_num}-$B$5*{cost_col}$21)"
            ws.cell(row_num, col, f"=-$B$3+{annual}/(1+$B$6)+{annual}/(1+$B$6)^2+{annual}/(1+$B$6)^3")
    ws.column_dimensions["A"].width = 49
    for letter in "BCDE": ws.column_dimensions[letter].width = 19
    for row in [1,2,11,20]:
        for c in ws[row][:5]:
            c.fill = PatternFill("solid", fgColor="182838")
            c.font = Font(bold=True, color="FFFFFF")
    for row in range(3,10):
        ws.cell(row,2).font = Font(color="1962A9", bold=True)
    for row in range(22,25):
        for col in range(2,5): ws.cell(row,col).number_format = '"$"#,##0;[Red]("$"#,##0)'
    ws["B6"].number_format="0.0%"
    wb.calculation.fullCalcOnLoad = True
    wb.save(out / "sensitivity_business_case.xlsx")

    # Executive slide deck (editable PowerPoint).
    prs = Presentation()
    prs.slide_width=PI(13.33)
    prs.slide_height=PI(7.5)
    slides=[
      ("Decision: controlled pilot, not rollout", ["Proposed approval: USD 300,000 assumed pilot cap", "90-day learning gates with executive sponsor", "All financial returns are hypothetical"]),
      ("Current challenge: test before scaling", ["Assumed 1,800 monthly service cases", "Five handoffs in the fictional process", "Baseline and capacity effects remain unverified"]),
      ("Options: compare reversibility and control", ["A  Baseline measurement only", "B  Manual process redesign", "C  Governed AI-assist pilot (conditional recommendation)"]),
      ("Economics: use sensitivity, not a point claim", ["Editable Excel workbook computes 3-year NPV and payback", "Benefits depend on adoption; costs vary by scenario", "Finance validation required before approval"]),
      ("Operating safeguards", ["Human approval for exception decisions", "Role access, audit, issue severity and rollback", "Stop if unauthorized disclosure or material control breach"]),
      ("Decision gates and owners", ["Day 30: baseline and sponsor sign-off", "Day 60: Risk/IT and workflow validation", "Day 90: CFO/COO stop-go review"])
    ]
    for title, bullets in slides:
        sl=prs.slides.add_slide(prs.slide_layouts[1])
        sl.shapes.title.text=title
        tf=sl.placeholders[1].text_frame
        tf.clear()
        for i,b in enumerate(bullets):
            p=tf.paragraphs[0] if i==0 else tf.add_paragraph()
            p.text=b; p.level=0; p.font.size=PP(25)
        sl.background.fill.solid()
        sl.background.fill.fore_color.rgb=PC(250,250,249)
    prs.save(out/"steering_committee_deck.pptx")
    print(f"Created 3 editable fictional samples in {out}")

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output-dir",default="generated")
    args=parser.parse_args()
    build(args.output_dir)

