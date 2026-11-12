"""Evidence-oriented repository structural audit; never infer production claims."""
import argparse
import ast
import json
import os
import subprocess
from collections import Counter
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
REPOSITORY = PROJECT.parent
EXCLUDE = {".git", ".venv", "node_modules", "__pycache__", ".pytest_cache"}


def git_commit():
    try:
        result = subprocess.run(["git", "-C", str(REPOSITORY), "rev-parse", "HEAD"],
                                check=True, capture_output=True, text=True, timeout=5)
        return result.stdout.strip()
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return None


def audit():
    extensions = Counter()
    file_count = 0
    for base, directories, files in os.walk(REPOSITORY):
        directories[:] = [name for name in directories if name not in EXCLUDE]
        for name in files:
            file_count += 1
            extensions[Path(name).suffix or "<none>"] += 1

    modules = {}
    for path in sorted((PROJECT / "src").glob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        imports = sorted({node.module for node in ast.walk(tree)
                          if isinstance(node, ast.ImportFrom) and node.module})
        functions = sorted(node.name for node in ast.walk(tree)
                           if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)))
        modules[str(path.relative_to(PROJECT))] = {
            "imports": imports,
            "functions": functions,
        }

    workflow = REPOSITORY / ".github" / "workflows" / "applied-engineer-evaluations.yml"
    return {
        "scope": "observed repository structure; not evidence of production deployments",
        "git_head_sha": git_commit(),
        "repository_file_count": file_count,
        "file_extensions": dict(sorted(extensions.items())),
        "project_import_and_function_inventory": modules,
        "ci_workflow_present": workflow.is_file(),
        "project_test_files": sorted(p.name for p in (PROJECT / "tests").glob("test_*.py")),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="artifacts/repository-audit.json")
    args = parser.parse_args()
    destination = (PROJECT / args.out).resolve()
    if not destination.is_relative_to(PROJECT):
        raise ValueError("artifact must be written inside project")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(audit(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Repository audit written: {destination}")


if __name__ == "__main__":
    main()
