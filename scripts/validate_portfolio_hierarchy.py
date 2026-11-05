"""Repository-wide portfolio taxonomy and Markdown navigation diagnostic.

Runs with GitHub Actions after moving capability projects. It checks the root
taxonomy and internal links but does not mutate content or claim that a local
link scan covers external URLs, rendered HTML or Git history.
"""
from __future__ import annotations

from pathlib import Path
from urllib.parse import unquote, urlsplit
import posixpath
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CATEGORY_NAMES = {
    "AI Adoption", "AI Governance, Risk & Responsible AI Portfolio",
    "AI Model Training & Evaluation Freelancer Project",
    "AI Project & Program Management", "AI Transformation",
    "AI-enabled Recruitment Portfolio", "Agentic AI development",
    "HR Operations & Workflow Automation", "HR Strategy & Planning",
    "HR Technology & Digital Transformation", "Organizational Effectiveness",
    "People Analytics & HR Data", "Talent Assessment", "Talent Development",
    "Workforce Transformation",
}
INFRA = {".github", ".claude", "scripts", "docs"}


def list_paths():
    files = sorted(
        p.relative_to(ROOT).as_posix()
        for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts
    )
    dirs = set()
    for path in files:
        parts = path.split("/")
        for i in range(1, len(parts)):
            dirs.add("/".join(parts[:i]))
    return files, dirs


def validate_links(files, dirs):
    all_files = set(files)
    errors = []
    nchecked = 0
    own_prefix = "https://github.com/bircanuzan/AI-in-HR-Portfolio/"
    for file in files:
        if not file.lower().endswith(".md"):
            continue
        text = (ROOT / file).read_text(encoding="utf-8", errors="replace")
        values = []
        # Markdown permits balanced parentheses in relative links. A simple
        # [^)]+ expression misidentifies valid directory names as bad links.
        for opening in re.finditer(r"\]\(", text):
            start = opening.end()
            depth = 1
            offset = start
            while offset < len(text):
                ch = text[offset]
                if ch == "\\" and offset + 1 < len(text):
                    offset += 2
                    continue
                if ch == "(":
                    depth += 1
                elif ch == ")":
                    depth -= 1
                    if depth == 0:
                        values.append(text[start:offset])
                        break
                offset += 1
        values.extend(m.group(1) for m in re.finditer(r"(?m)^\[[^\]]+\]:\s*(\S+)", text))
        base = posixpath.dirname(file)
        for raw in values:
            raw = raw.strip()
            if not raw or raw.startswith(("#", "mailto:", "data:")):
                continue
            if raw.startswith(own_prefix):
                u = urlsplit(raw)
                parts = u.path.split("/")
                if len(parts) >= 6 and parts[3] in {"tree", "blob"} and parts[4] == "main":
                    target = unquote("/".join(parts[5:]).rstrip("/"))
                else:
                    continue
            elif re.match(r"^[a-z][a-z0-9+.-]*:", raw, flags=re.I) or raw.startswith(("//", "/")):
                continue
            else:
                # Markdown title syntax or raw HTML inside link isn't a file link.
                if " \"" in raw or " '" in raw or raw.startswith("<"):
                    continue
                target = posixpath.normpath(posixpath.join(base, unquote(raw.split("#", 1)[0].split("?", 1)[0]).rstrip("/")))
            if not target:
                continue
            nchecked += 1
            if target not in all_files and target not in dirs:
                errors.append((file, raw, target))
    return nchecked, errors


def main():
    files, dirs = list_paths()
    current_roots = {p.split("/")[0] for p in files if "/" in p}
    missing = sorted(CATEGORY_NAMES - current_roots)
    extra = sorted(current_roots - CATEGORY_NAMES - INFRA)
    missing_readme = sorted(c for c in CATEGORY_NAMES if c + "/README.md" not in files)
    checked, broken = validate_links(files, dirs)
    print(f"Portfolio hierarchy: {len(CATEGORY_NAMES)} capability roots, {len(files)} files, {checked} resolvable-style links checked")
    print("MISSING_CATEGORIES", missing)
    print("EXTRA_ROOTS", extra)
    print("MISSING_CATEGORY_READMES", missing_readme)
    print("BROKEN_INTERNAL_LINKS", len(broken))
    for source, link, target in broken[:140]:
        print("BROKEN", source, "->", link, "->", target)
    if missing or extra or missing_readme:
        print("STATUS: FATAL CATEGORY STRUCTURE DEFECT")
        return 1
    if broken:
        print("STATUS: LINK REVIEW REQUIRED (diagnostic run, nonfatal for legacy links)")
    else:
        print("STATUS: TAXONOMY AND LINK AUDIT PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
