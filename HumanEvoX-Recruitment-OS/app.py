"""HumanEvoX Recruitment OS — local-first, human-controlled pilot (Streamlit)."""
from __future__ import annotations

import json
import os
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import streamlit as st

from humanevox.documents import extract_document
from humanevox.engine import RUBRIC, analyze, assess_competencies, requirements
from humanevox.storage import (add_candidate, add_role, add_task, audit, complete_task, connect,
                               csv_bytes, delete_candidate, initialize, rows, save_assessment, update_candidate)
from humanevox.templates import STAGES, conversation_guide, invitation_ics, outreach_draft

st.set_page_config(page_title="HumanEvoX | Talent Workspace", page_icon="✦", layout="wide")
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"], [data-testid="stAppViewContainer"] {font-family: Inter, sans-serif;}
h1,h2,h3 {letter-spacing:-0.025em;}
[data-testid="stMetricValue"] {color:#C6A052;}
.stButton button[kind="primary"] {background:#C6A052;color:#000;border:0;font-weight:700;}
small {color:#BBB;}
</style>""", unsafe_allow_html=True)

DB_PATH = os.environ.get("HUMANEVOX_DB", str(Path.home() / ".humanevox_recruitment_os" / "workspace.sqlite3"))
with connect(DB_PATH) as db:
    initialize(db)


def query(sql, params=()):
    with connect(DB_PATH) as db:
        return rows(db, sql, params)


def mutate(fn, *args):
    with connect(DB_PATH) as db:
        return fn(db, *args)


def role_options():
    return query("SELECT * FROM roles ORDER BY id DESC")


def candidate_options():
    return query("""SELECT c.*, r.title AS role_title FROM candidates c
        JOIN roles r ON r.id=c.role_id ORDER BY c.updated_at DESC""")


def display_role(r):
    return f"#{r['id']} — {r['title']}"


def display_candidate(c):
    return f"#{c['id']} — {c['full_name']} ({c['role_title']})"


st.title("HumanEvoX · Talent Workspace")
st.caption("Engineered for the AI Era · Local-first recruitment operations pilot · No automated calls or hiring decisions")
st.warning("PILOT: Run locally with synthetic data until proper authentication, authorization, encryption, retention, lawful-basis checks and a deployment security review are completed. Do not deploy this app publicly with real candidate data.", icon="🔒")

tabs = st.tabs(["Overview", "Roles & CV screening", "Candidate assessment", "Pipeline & tasks", "Outreach & scheduling", "Reporting & privacy"])

with tabs[0]:
    roles = role_options()
    candidates = candidate_options()
    stage_counts = Counter(c["stage"] for c in candidates)
    tasks_open = query("SELECT * FROM tasks WHERE completed=0")
    a, b, c, d = st.columns(4)
    a.metric("Open roles", len(roles))
    b.metric("Candidate records", len(candidates))
    c.metric("In review", stage_counts["Review"] + stage_counts["Client review"])
    d.metric("Open tasks", len(tasks_open))
    st.subheader("How this workspace works")
    st.markdown("""
    1. Create a role and define essential/preferred skills.
    2. Extract an applicant's PDF, DOCX or TXT résumé **locally**; view matched text and gaps.
    3. Record independent recruiter assessments against 0–4 evidence-based competencies.
    4. Advance the pipeline manually, create follow-up tasks and draft messages/interview invitations.
    5. Export controlled reports or erase records. Every write creates an audit entry.

    **Text matching is not verification of capability.** The coverage metric is a document evidence indicator, never an automated suitability or hiring score.
    """)
    if candidates:
        st.subheader("Pipeline snapshot")
        st.bar_chart([{"stage": s, "count": stage_counts[s]} for s in STAGES if stage_counts[s]], x="stage", y="count")

with tabs[1]:
    st.subheader("Set up a recruitment assignment")
    with st.form("new_role", clear_on_submit=True):
        name = st.text_input("Role title", placeholder="AI-enabled Talent Intelligence Consultant")
        dept = st.text_input("Client team / department (internal label)")
        req = st.text_area("Essential skills (comma-separated)", placeholder="recruitment, excel, stakeholder management")
        pref = st.text_area("Preferred skills (comma-separated)", placeholder="power bi, workday, python")
        create = st.form_submit_button("Create role", type="primary")
    if create:
        try:
            mutate(add_role, name, dept, req, pref)
            st.success("Role created; you can now screen a document.")
        except ValueError as e:
            st.error(str(e))
    roles = role_options()
    if roles:
        st.divider()
        st.subheader("Screen résumé against an existing role")
        role = st.selectbox("Recruitment assignment", roles, format_func=display_role, key="screen_role")
        with st.form("intake_form", clear_on_submit=False):
            cname = st.text_input("Candidate display name", placeholder="Aisha Example")
            email = st.text_input("Candidate email (for duplicate detection)", placeholder="aisha@example.test")
            source = st.text_input("Source", placeholder="Example: inbound application")
            uploaded = st.file_uploader("CV (PDF/DOCX/TXT, maximum 8MB)", type=["pdf", "docx", "txt"])
            consent = st.checkbox("I confirm a documented lawful basis/permission to process this CV")
            create_candidate = st.form_submit_button("Extract, evaluate and save", type="primary")
        if create_candidate:
            if not uploaded:
                st.error("Upload a résumé to continue.")
            else:
                try:
                    raw = extract_document(uploaded.name, uploaded.getvalue())
                    evidence = analyze(raw, role["required"], role["preferred"])
                    cid = mutate(add_candidate, role["id"], cname, email, source, uploaded.name, evidence, consent)
                    st.session_state["last_analysis"] = (cid, evidence)
                    st.success(f"Candidate #{cid} saved. Raw résumé text was not stored.")
                except Exception as e:
                    import sqlite3
                    if isinstance(e, sqlite3.IntegrityError):
                        st.error("Duplicate candidate email for this role; existing record was preserved.")
                    elif isinstance(e, (ValueError, TypeError)):
                        st.error(str(e))
                    else:
                        st.error("Document extraction failed. Try a text-based PDF, DOCX or TXT.")
        if "last_analysis" in st.session_state:
            cid, evidence = st.session_state["last_analysis"]
            st.metric("Evidence keyword coverage", f"{evidence['summary']['coverage_percent']}%")
            st.caption("Not a hiring recommendation; no automatic ranking or rejection.")
            st.write("**Required-skills evidence**")
            st.dataframe(evidence["required"], use_container_width=True, hide_index=True)
            st.write("**Preferred-skills evidence**")
            st.dataframe(evidence["preferred"], use_container_width=True, hide_index=True)
            st.write("Missing document mentions:", evidence["summary"]["missing_required"])

with tabs[2]:
    st.subheader("Human-led structured assessment")
    candidates = candidate_options()
    if not candidates:
        st.info("Add a candidate from the screening tab first.")
    else:
        cand = st.selectbox("Candidate", candidates, format_func=display_candidate, key="assess_candidate")
        evidence = json.loads(cand["evidence"])
        st.caption("Document keyword coverage is separate from human-evaluated competence.")
        st.metric("Document keyword coverage", f"{cand['coverage']}%")
        st.write("**Source evidence / gaps**")
        st.dataframe(evidence["required"] + evidence["preferred"], use_container_width=True, hide_index=True)
        st.write("**Rating anchors**")
        st.table([{"Score": k, "Definition": v} for k, v in RUBRIC.items()])
        with st.form("assessment"):
            competency = st.text_input("Competency", placeholder="Stakeholder management")
            score = st.select_slider("Human rating (0–4)", options=list(RUBRIC), value=2)
            explanation = st.text_area("Specific observed evidence and gaps", placeholder="Cite interview example, practical task or verified reference")
            assessor = st.text_input("Assessor name")
            save = st.form_submit_button("Save human assessment", type="primary")
        if save:
            try:
                mutate(save_assessment, cand["id"], competency, score, explanation, assessor)
                st.success("Assessment saved. Pipeline stage was not changed.")
            except ValueError as e:
                st.error(str(e))
        history = query("SELECT competency,score,evidence,assessor,created_at FROM assessments WHERE candidate_id=? ORDER BY id DESC", (cand["id"],))
        if history:
            st.write("**Recorded assessments**")
            st.dataframe(history, use_container_width=True, hide_index=True)
            summary = assess_competencies({str(i): a["score"] for i, a in enumerate(history)})
            st.caption(f"Unweighted human rating average: {summary['average']} / 4 ({summary['rated']} recorded assessments). Verify evidence before use.")

with tabs[3]:
    st.subheader("Recruitment pipeline and follow-up tasks")
    candidates = candidate_options()
    if candidates:
        st.dataframe([{"id": c["id"], "candidate": c["full_name"], "role": c["role_title"], "stage": c["stage"], "updated_at": c["updated_at"]} for c in candidates], use_container_width=True, hide_index=True)
        cand = st.selectbox("Update candidate", candidates, format_func=display_candidate, key="pipeline_candidate")
        with st.form("stage_form"):
            stage = st.selectbox("Stage", STAGES, index=STAGES.index(cand["stage"]))
            notes = st.text_area("Recruiter notes", value=cand["recruiter_notes"])
            save = st.form_submit_button("Save stage and notes", type="primary")
        if save:
            mutate(update_candidate, cand["id"], stage, notes)
            st.success("Updated and recorded in audit log.")
            st.rerun()
        with st.form("task_form", clear_on_submit=True):
            title = st.text_input("Follow-up task", placeholder="Request role-specific work sample")
            due = st.date_input("Due date", value=datetime.now(ZoneInfo("Asia/Dubai")).date() + timedelta(days=2))
            add = st.form_submit_button("Add task")
        if add:
            try:
                mutate(add_task, cand["id"], title, due.isoformat())
                st.success("Task created (no automated message sent).")
            except ValueError as e:
                st.error(str(e))
    tasks = query("""SELECT t.id,t.title,t.due_at,c.full_name FROM tasks t
                    JOIN candidates c ON c.id=t.candidate_id WHERE t.completed=0 ORDER BY t.due_at""")
    if tasks:
        st.write("**Open follow-ups**")
        for task in tasks:
            x, y = st.columns([4, 1])
            x.write(f"#{task['id']} · {task['full_name']} · {task['title']} · due {task['due_at']}")
            if y.button("Complete", key=f"complete_{task['id']}"):
                mutate(complete_task, task["id"])
                st.rerun()

with tabs[4]:
    st.subheader("Human-approved communications and interview preparation")
    st.caption("Creates drafts and calendar files only. No emails, AI calls or invitations are sent.")
    candidates = candidate_options()
    if candidates:
        cand = st.selectbox("Candidate", candidates, format_func=display_candidate, key="outreach_candidate")
        kind = st.radio("Message type", ["invitation", "follow-up", "interview"], horizontal=True)
        subject, body = outreach_draft(cand["full_name"], cand["role_title"], kind=kind)
        st.text_input("Draft subject", value=subject)
        st.text_area("Draft content (edit and copy manually)", value=body, height=220)
        st.download_button("Download email draft", data=f"Subject: {subject}\nTo: {cand['email']}\n\n{body}", file_name=f"draft_{cand['id']}.txt")
        st.divider()
        st.write("**Interview calendar file (tentative)**")
        dt = st.date_input("Proposed date", key="interview_date")
        tm = st.time_input("Proposed Dubai time", key="interview_time")
        dur = st.selectbox("Duration (minutes)", [15, 30, 45, 60, 90], index=1)
        start = datetime.combine(dt, tm).replace(tzinfo=ZoneInfo("Asia/Dubai"))
        ics = invitation_ics(f"Interview — {cand['role_title']}", start, dur, description=f"HumanEvoX candidate #{cand['id']}. Confirm time and invitees manually.")
        st.download_button("Download tentative .ics", data=ics, file_name=f"interview_{cand['id']}.ics", mime="text/calendar")
        with st.expander("Optional conversation guide (NO automated calling)"):
            st.text_area("Human-controlled guide", value=conversation_guide(cand["role_title"]), height=250)
            st.info("Live phone calls, voice bots, diallers, recording and speech analysis are not connected.")
    else:
        st.info("Add a candidate to prepare messages and interviews.")

with tabs[5]:
    st.subheader("Reporting, audit and deletion")
    candidates = candidate_options()
    by_stage = Counter(c["stage"] for c in candidates)
    st.dataframe([{"stage": stage, "candidates": by_stage[stage]} for stage in STAGES], use_container_width=True, hide_index=True)
    st.write("**Controlled CSV exports**")
    st.caption("Contains identifiable candidate information; keep exports in access-controlled storage.")
    export = [{"candidate_id": c["id"], "name": c["full_name"], "email": c["email"], "role": c["role_title"],
               "stage": c["stage"], "document_coverage_pct": c["coverage"], "created_at": c["created_at"]} for c in candidates]
    st.download_button("Export pipeline CSV", csv_bytes(export), "humanevox_pipeline.csv", mime="text/csv", disabled=not export)
    audit_log = query("SELECT entity,entity_id,action,detail,created_at FROM activity ORDER BY id DESC LIMIT 500")
    st.download_button("Export latest 500 audit events CSV", csv_bytes(audit_log), "humanevox_audit.csv", mime="text/csv", disabled=not audit_log)
    with st.expander("Audit activity (latest 100)"):
        st.dataframe(audit_log[:100], use_container_width=True, hide_index=True)
    st.divider()
    st.write("**Candidate right-to-erasure workflow**")
    st.caption("Deletes the candidate, attached structured assessment and tasks from the active database. Existing backups/exports require separate deletion.")
    if candidates:
        cand = st.selectbox("Candidate to erase", candidates, format_func=display_candidate, key="delete_candidate")
        confirmed = st.checkbox("I confirm that this candidate's record should be erased")
        if st.button("Permanently erase candidate record", disabled=not confirmed):
            mutate(delete_candidate, cand["id"])
            st.success("Candidate erased from active database. Handle any exported copies separately.")
            st.rerun()
    st.caption("Local database path: " + DB_PATH)
