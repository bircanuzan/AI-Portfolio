"""Structural/syntax checks for 20 independent AI engineering portfolio examples.

This checker uses only Python's standard library. It does NOT install frameworks,
invoke model APIs, evaluate model quality, or demonstrate deployment.
"""
import ast
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "AI_ENGINEERING_TOOL_PROJECTS_INDEX.md"
ROWS = re.compile(r"^\| ([^|]+) \| \[[^\]]+\]\(([^)]+/README\.md)\) \| ([^|]+) \|$", re.M)

def main() -> None:
    text = INDEX.read_text(encoding="utf-8")
    entries = ROWS.findall(text)
    assert len(entries) == 20, f"Expected 20 tool projects; found {len(entries)}"
    seen = set()
    for technology, href, category in entries:
        path = Path(unquote(href))
        assert path.parent not in seen, f"Duplicate project: {path.parent}"
        seen.add(path.parent)
        assert (ROOT / path).is_file(), f"Missing project README: {path}"
        source = ROOT / path.parent / "main.py"
        assert source.is_file(), f"Missing Python example: {source}"
        assert (ROOT / path.parent / "requirements.txt").is_file(), f"Missing dependencies: {source.parent}"
        ast.parse(source.read_text(encoding="utf-8"), filename=str(source))
        category_readme = ROOT / category.strip() / "README.md"
        assert category_readme.is_file(), f"Missing category index: {category_readme}"
        print(f"PASS {technology.strip():28} {path.parent}")
    assert len({str(p.parent) for p in seen}) == 9, "Expected nine category folders"
    print("PASS: 20 projects; nine category indexes; Python syntax parsed.")

if __name__ == "__main__":
    main()
