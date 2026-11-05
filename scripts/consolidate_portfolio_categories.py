"""CHRO + CTO portfolio hierarchy consolidation.

Migrates standalone role/project root folders beneath 15 competency portfolios.
Runs on an isolated runner branch, not as a direct destructive push to main.
Never infers completed client work or rewrites archived git history.

Previous relative Markdown links are re-based based on both source and target
renames, then root README is replaced with a concise functional navigation.
"""
from __future__ import annotations

import os
import posixpath
import re
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit, urlunsplit
import sys

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "bircanuzan/AI-in-HR-Portfolio"
PRIMARY = (
    "AI Adoption", "AI Governance, Risk & Responsible AI Portfolio",
    "AI Model Training & Evaluation Freelancer Project",
    "AI Project & Program Management", "AI Transformation",
    "AI-enabled Recruitment Portfolio", "Agentic AI development",
    "HR Operations & Workflow Automation", "HR Strategy & Planning",
    "HR Technology & Digital Transformation", "Organizational Effectiveness",
    "People Analytics & HR Data", "Talent Assessment", "Talent Development",
    "Workforce Transformation"
)
INFRA = {".github", ".claude", "scripts", "docs"}
EXPLICIT = {
    "02_AI_Enabled_HR_Transformation": "HR Technology & Digital Transformation",
    "06_Workforce_Planning": "Workforce Transformation",
    "08_Talent_Management_Assessment": "Talent Assessment/Legacy Navigation",
    "14_Machine_Learning_Training_and_Model_Evaluation": "AI Model Training & Evaluation Freelancer Project",
    "15_AI_DevOps_Training_CI_CD_and_Kubernetes": "AI Model Training & Evaluation Freelancer Project",
    "16_AI_Voice_Agent_for_Customer_Support": "Agentic AI development/Voice and Customer Agents",
    "17_Voice_AI_Customer_Adoption_and_Analytics": "AI Adoption",
    "19_HR_Workflow_Benchmark_Design_and_AI_Answer_Grading": "AI Model Training & Evaluation Freelancer Project",
    "20_AI_Presales_Architect_Azure_Oracle_Enterprise_Transformation": "Agentic AI development/Enterprise AI Solutions",
    "21_Senior_AI_Business_Analyst_Retail_Process_Reengineering": "AI Transformation/Business Analysis",
    "22_AI_Product_Owner_Agentic_Workflow_and_Product_Delivery": "AI Project & Program Management",
    "23_Strategy_Consultant_SAP_People_Intelligence_Business_Data_Cloud_AI_Driven_People_Analytics": "People Analytics & HR Data",
    "24_Applied_AI_Transformation_Manager_MENA": "AI Transformation",
    "25_People_Operations_AI_Research_Contributor": "AI Model Training & Evaluation Freelancer Project",
    "26_HR_AI_and_Automation_Operations_Lead_Mobility": "HR Operations & Workflow Automation",
    "28_AI_Testing_and_Quality_Review": "AI Model Training & Evaluation Freelancer Project",
    "30_Business_Process_Mapping_Analysis_and_AI_Transformation": "AI Transformation",
    "35_Modern_Workplace_Solutioning": "AI Adoption",
    "36_Human_Data_Operations_Management": "AI Model Training & Evaluation Freelancer Project",
    "38_Assessment_Center_Assessor": "Talent Assessment/Legacy Navigation",
    "39_Human_Data_Operations_Management": "AI Model Training & Evaluation Freelancer Project",
    "42_Human-AI_Workforce_Design_and_Agent_Governance": "Workforce Transformation",
    "45_AI_Lead_Systems_and_Process": "AI Transformation",
    "46_AI_Lead_Enterprise_Invoice_Process_Automation": "Agentic AI development/Enterprise AI Solutions",
    "49_Psychometric_Assessment_and_Talent_Evaluation": "Talent Assessment/Legacy Navigation",
    "50_AI_Agent_Builder_Automation": "Agentic AI development",
    "51_Enterprise_AI_and_Smart_Data_Governance_BI_Analytics": "AI Governance, Risk & Responsible AI Portfolio",
    "53_HR_to_AI_Role_Map_and_Evidence_Lab": "Workforce Transformation",
    "55_AI_Recruitment_Screening_Risk_Assessment": "AI-enabled Recruitment Portfolio/Legacy Navigation",
    "Agentic AI Application Testing & Evaluation for HR Transformation": "AI Model Training & Evaluation Freelancer Project",
    "Agentic AI Automation": "Agentic AI development",
    "Agentic-AI-Engineering-Enterprise-Workflow-Agent": "Agentic AI development",
    "AI in HR & Agentic Automation": "Agentic AI development",
    "AI Integration Engineering": "Agentic AI development",
    "AI Solutions Engineering": "Agentic AI development",
    "AI Strategist": "AI Transformation",
    "AI Strategy & Enablement Lead": "AI Transformation",
    "AI Transformation Project": "AI Transformation",
    "Business Enablement & AI Workflow Automation": "AI Transformation",
    "Change Management": "Organizational Effectiveness",
    "Executive Talent Dashboard in Power BI and Board Presentation": "People Analytics & HR Data",
    "Global_Product_Training_and_Learning_Program_Management": "Talent Development/Legacy Navigation",
    "HR Policy": "HR Operations & Workflow Automation",
    "HR Shared Services": "HR Operations & Workflow Automation",
    "HRIS & HCM Systems": "HR Technology & Digital Transformation",
    "Instructional Design": "Talent Development/Legacy Navigation",
    "Instructional Design and Talent Development": "Talent Development",
    "Instructional-Design-Digital-Learning-service_operations-Portfolio-2026": "Talent Development/Legacy Navigation",
    "Microsoft 365 Copilot Adoption & Enablement": "AI Adoption",
    "Middle East HR Director Project": "HR Strategy & Planning",
    "Oracle Fusion HCM": "HR Technology & Digital Transformation",
    "Organisation Design": "Organizational Effectiveness",
    "Organizational Development": "Organizational Effectiveness",
    "Organizational Transformation Advisory": "Organizational Effectiveness",
    "Pilot Project - Agentic AI Competency Interviews & Talent Intelligence": "AI-enabled Recruitment Portfolio",
    "Prompt Engineering": "AI Model Training & Evaluation Freelancer Project",
    "Responsible AI & AI Governance": "AI Governance, Risk & Responsible AI Portfolio",
}
CLAUDE_PREFIX = "Claude AI in HR - "
TEXT_EXTS = {
    ".md", ".txt", ".py", ".json", ".yaml", ".yml", ".csv", ".html",
    ".js", ".css", ".svg", ".xml", ".sql", ".dax", ".rtf", ".srt", ".example"
}


def mapped_root(oldroot):
    if oldroot in PRIMARY or oldroot in INFRA:
        return oldroot
    if oldroot in EXPLICIT:
        return EXPLICIT[oldroot] + "/" + oldroot
    if oldroot.startswith(CLAUDE_PREFIX):
        return "Agentic AI development/Claude HR Skills/" + oldroot
    raise ValueError("Unclassified root folder: " + oldroot)


def map_file(path):
    first, sep, tail = path.partition("/")
    if not sep:
        return path
    new_root = mapped_root(first)
    return new_root + "/" + tail


def all_files():
    return [
        p.relative_to(ROOT).as_posix()
        for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts
    ]


def dir_index(files):
    dirs = set()
    for p in files:
        parts = p.split("/")
        for i in range(1, len(parts)):
            dirs.add("/".join(parts[:i]))
    return dirs


def rewrite_links(text, old_file, new_file, old_files, old_dirs):
    old_base = posixpath.dirname(old_file)
    new_base = posixpath.dirname(new_file)

    def rewritten(raw):
        if not raw or raw[0] == "#":
            return raw
        # Preserve external references other than own repository permalinks.
        absolute_prefix = None
        if raw.startswith("https://github.com/" + REPOSITORY + "/"):
            # GitHub browser permalink links for main branch
            absolute_prefix = "https://github.com/" + REPOSITORY + "/"
            url = urlsplit(raw)
            pieces = url.path.split("/")
            if len(pieces) < 7 or pieces[3] not in ("blob", "tree") or pieces[4] != "main":
                return raw
            rest = "/".join(pieces[5:])
            target = unquote(rest.rstrip("/"))
            if target not in old_files and target not in old_dirs:
                return raw
            newtarget = map_file(target + "/_")[:-2] if target in old_dirs else map_file(target)
            pieces = pieces[:5] + quote(newtarget, safe="/-_.~!()'").split("/")
            newpath = "/".join(pieces)
            if raw.endswith("/") and not newpath.endswith("/"):
                newpath += "/"
            return urlunsplit((url.scheme, url.netloc, newpath, url.query, url.fragment))
        if raw.startswith(("http:", "https:", "mailto:", "data:", "javascript:", "//")):
            return raw
        if raw.startswith("/") or raw.startswith("<"):
            return raw
        # Preserve fragments and query strings.
        base, hashsep, fragment = raw.partition("#")
        base, qmark, query = base.partition("?")
        if not base or " " in base and not ("%" in base):
            # Some Markdown links include a quoted title; leave them alone.
            pass
        trailing = base.endswith("/")
        try:
            decoded = unquote(base)
        except Exception:
            return raw
        old_target = posixpath.normpath(posixpath.join(old_base, decoded))
        if old_target not in old_files and old_target not in old_dirs:
            return raw
        if old_target in old_files:
            new_target = map_file(old_target)
        else:
            new_target = map_file(old_target + "/_")[:-2]
        rel = posixpath.relpath(new_target, new_base or ".")
        if trailing and not rel.endswith("/"):
            rel += "/"
        rel = quote(rel, safe="/-_.~!()'")
        return rel + (("?" + query) if qmark else "") + (("#" + fragment) if hashsep else "")

    # Standard inline Markdown links / images; preserve link labels and anchor fragments.
    text = re.sub(r"(\]\()([^\n)]*)(\))",
                  lambda m: m.group(1) + rewritten(m.group(2)) + m.group(3), text)
    # Reference-style Markdown links: [id]: relative/path
    text = re.sub(r"(?m)^(\[[^\]]+\]:\s*)(\S+)",
                  lambda m: m.group(1) + rewritten(m.group(2)), text)
    # HTML href or src, including local interactive demos.
    text = re.sub(r"(\b(?:href|src)=['\"])([^'\"]+)(['\"])",
                  lambda m: m.group(1) + rewritten(m.group(2)) + m.group(3), text)
    return text


def main():
    paths = all_files()
    old_dirs = dir_index(paths)
    old_files = set(paths)
    roots = sorted({p.split("/")[0] for p in paths if "/" in p})
    unknown = [r for r in roots if r not in PRIMARY and r not in INFRA
               and r not in EXPLICIT and not r.startswith(CLAUDE_PREFIX)]
    if unknown:
        raise RuntimeError("Unknown roots, refusing partial move: " + str(unknown))
    mapping = {old: map_file(old) for old in paths}
    targets = list(mapping.values())
    if len(set(targets)) != len(targets):
        raise RuntimeError("Destination name conflict detected")
    if any(target in old_files and mapping.get(target) == target and target != old
           for old, target in mapping.items()):
        raise RuntimeError("Collision with retained source file")

    old_root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    source_text = {}
    for old in paths:
        p = ROOT / old
        if p.suffix.casefold() in TEXT_EXTS and p.stat().st_size < 6_000_000:
            source_text[old] = p.read_text(encoding="utf-8", errors="replace")

    moved = 0
    for old, target in mapping.items():
        if old == target:
            continue
        dest = ROOT / target
        dest.parent.mkdir(parents=True, exist_ok=True)
        (ROOT / old).rename(dest)
        moved += 1
    updated = 0
    for old, orig in source_text.items():
        if old.startswith(".github/workflows/"):
            # Workflow configuration is updated separately via authenticated
            # connector due restricted GitHub Actions token permissions.
            continue
        new_file = mapping[old]
        revised = rewrite_links(orig, old, new_file, old_files, old_dirs)
        if revised != orig:
            (ROOT / new_file).write_text(revised, encoding="utf-8")
            updated += 1

    # Full legacy index remains accessible; its links are re-based from root.
    legacy = ROOT / "docs" / "LEGACY_DETAILED_PROJECT_INDEX.md"
    legacy.parent.mkdir(exist_ok=True)
    legacy.write_text(
        "# Detailed Project Index (Archived Navigation)\n\n"
        + "For the executive portfolio taxonomy, see [the main README](../README.md).\n\n"
        + rewrite_links(old_root_readme, "README.md", "docs/LEGACY_DETAILED_PROJECT_INDEX.md", old_files, old_dirs),
        encoding="utf-8",
    )
    overview = [
        ("Workforce Transformation", "Human–AI workforce architecture, capacity, agent decision rights and workforce economics."),
        ("HR Strategy & Planning", "People strategy, cross-border workforce planning, leadership scorecards and executive HR direction."),
        ("Organizational Effectiveness", "Organization design, restructuring, operating models, job architecture and change governance."),
        ("Talent Development", "Skills frameworks, leadership pipelines, succession, instructional design and L&D measurement."),
        ("Talent Assessment", "Assessment centers, psychometrics and evidence-led talent decisions."),
        ("AI-enabled Recruitment Portfolio", "Recruitment intelligence, talent mapping, hiring controls and AI-assisted selection assurance."),
        ("People Analytics & HR Data", "Headcount/cost MIS, executive dashboards, analytics models and reliable workforce evidence."),
        ("HR Operations & Workflow Automation", "Employee services, shared services, payroll-facing controls and HR policy operations."),
        ("HR Technology & Digital Transformation", "HRIS/HCM technology, enterprise HR platforms, UAT and systems change."),
        ("AI Transformation", "Enterprise AI strategy, business process redesign, operational AI implementation and adoption value."),
        ("AI Adoption", "Digital workplace, Copilot enablement, AI fluency and adoption governance."),
        ("Agentic AI development", "AI agents, HR service automation, integration engineering, orchestration and human approvals."),
        ("AI Governance, Risk & Responsible AI Portfolio", "Responsible AI, ethics, safety evaluations, assurance and governance control planes."),
        ("AI Model Training & Evaluation Freelancer Project", "AI/LLM quality assurance, evaluation, benchmarking, ML and dataset operations."),
        ("AI Project & Program Management", "AI portfolio/PMO delivery, prioritization, roadmaps, agile product ownership and risk control."),
    ]
    doc = [
        "# Human–AI Workforce, HR & Enterprise AI Portfolio",
        "",
        "**Independent professional evidence portfolio | 15 capability domains**",
        "",
        "This repository contains a mix of actual career experience summaries and independently built",
        "synthetic or proposed demonstrations. **An interview-aligned case does not imply work for",
        "a named employer or a commissioned client deployment.** Read each project for its evidence limits.",
        "",
        "## Executive navigation — CHRO and CTO perspectives",
        "",
        "| Main portfolio | Decision capability and technical evidence |",
        "|---|---|",
    ]
    for domain, description in overview:
        doc.append(f"| [{domain}]({quote(domain, safe='/')}/) | {description} |")
    doc += [
        "",
        "## How to assess the work",
        "",
        "- **CHRO lens:** business outcomes, workforce economics, leadership capability, fairness, national workforce planning, human decision rights and governance.",
        "- **CTO lens:** architecture, testable Python prototypes, data lineage, access control, evaluation, CI/CD, traceable assumptions and operational readiness.",
        "- **Evidence maturity:** distinguish actual delivery, independent prototype, design-only concept and simulated results. No production deployment should be inferred from a README or sample output.",
        "- **Reproducibility:** run only the local demos with published synthetic inputs. Verify each project's README, dependencies, safety constraints and unit tests.",
        "",
        "## Research and archive",
        "",
        "- [Detailed previous project navigation](docs/LEGACY_DETAILED_PROJECT_INDEX.md) — historical text retained with relative links rewritten.",
        "- [Portfolio hierarchy decision record](docs/PORTFOLIO_ARCHITECTURE.md) — taxonomy, ownership, migration rules and technical checks.",
        "- [Automated portfolio identity audit](scripts/portfolio_identity_audit.py) — guards against employer/client identifiers in current published files.",
        "",
        "© Independent professional portfolio. No client, employer or university affiliation is implied for synthetic projects.",
        "",
    ]
    (ROOT / "README.md").write_text("\n".join(doc), encoding="utf-8")
    notes = [
        "# Portfolio architecture | CHRO × CTO decision record",
        "",
        "## Strategic intent",
        "Unify a formerly fragmented portfolio into **15 competency-based main categories**.",
        "Role titles and one-off interview demonstrations are subprojects, not top-level categories.",
        "Model, dataset, README, test and control artifacts stay inside their respective project subtrees.",
        "",
        "## CHRO content boundaries",
        "- Corporate HR strategy / job architecture / transformation: distinct from talent acquisition and talent development.",
        "- People Analytics owns workforce evidence; HR Technology owns HR systems and integration.",
        "- HR Operations owns delivery controls and policy mechanics.",
        "- Workforce Transformation owns Human–AI capacity, organization design interfaces and agent workforce governance.",
        "",
        "## CTO technical boundaries",
        "- Agentic AI development owns runnable agent/integration patterns; AI Adoption owns human rollout.",
        "- Model Training & Evaluation owns data quality and evaluation; Responsible AI owns risk controls and assurance.",
        "- AI Transformation owns business value and process change; AI PMO owns project execution.",
        "- Preserve relative imports/data paths, repository test workflows and project-level READMEs.",
        "",
        "## Navigation / migration",
        f"- Migrated **{moved} files** from legacy top-level project folders into competency portfolios.",
        f"- Updated links in **{updated} text files** based on their original source and destination paths.",
        "- Retained all original project bytes unless a source file's relative documentation links needed correction.",
        "- Legacy one-page relocation pointers are preserved under functional category Legacy Navigation folders.",
        "- Previous externally shared direct GitHub folder URLs may need replacement; GitHub does not automatically redirect directory moves.",
        "- CI workflows need a deliberate review of changed working-directory and test paths before promotion.",
        "",
        "## Quality gates",
        "- Run privacy/identity scan, existing CI suites and broken-link checks on the proposed branch.",
        "- Require clean project inventory and no unresolved path collisions before merging.",
        "- A green smoke test does not guarantee production readiness or real client deployment.",
        "",
    ]
    (ROOT / "docs" / "PORTFOLIO_ARCHITECTURE.md").write_text("\n".join(notes), encoding="utf-8")
    # Files moved successfully; remove now-empty source directories (Git does not track empty dirs).
    for directory in sorted(
        (p for p in ROOT.rglob("*") if p.is_dir() and ".git" not in p.parts),
        key=lambda p: len(p.parts),
        reverse=True,
    ):
        if directory.name in {".github", ".claude", "scripts", "docs"} or directory.parent == ROOT and directory.name in PRIMARY:
            continue
        try:
            directory.rmdir()
        except OSError:
            pass
    # Git tracks files, not empty directories. Count only roots containing file artifacts.
    final_roots = sorted({
        p.relative_to(ROOT).parts[0]
        for p in ROOT.rglob("*")
        if p.is_file() and ".git" not in p.parts and len(p.relative_to(ROOT).parts) > 1
    })
    if set(final_roots) != set(PRIMARY) | INFRA:
        raise RuntimeError("Unexpected root taxonomy: " + str(final_roots))
    print("MOVED_FILES", moved)
    print("UPDATED_TEXT_LINKS", updated)
    print("TOP_LEVEL_PROJECT_DOMAINS", len(PRIMARY))
    print("TOP_LEVEL_ROOTS_INCLUDING_INFRA", len(final_roots))
    print("MAIN_CATEGORIES", " | ".join(PRIMARY))
    return 0


if __name__ == "__main__":
    sys.exit(main())
