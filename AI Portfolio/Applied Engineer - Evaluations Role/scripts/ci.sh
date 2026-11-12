#!/usr/bin/env bash
# Can be run locally or in GitHub Actions. Does not install external dependencies.
set -euo pipefail
cd "$(dirname "$0")/.."
echo "1/4: Compile Python"
python -m compileall -q src tests benchmark.py scripts/repository_audit.py
echo "2/4: Run unittest regression suite"
python -m unittest discover -s tests -p 'test_*.py' -v
echo "3/4: Benchmark trusted synthetic candidate patches"
python benchmark.py --out artifacts/benchmark-results.json
echo "4/4: Audit Git checkout and repository structure"
python scripts/repository_audit.py --out artifacts/repository-audit.json
python -m json.tool artifacts/benchmark-results.json > /dev/null
python -m json.tool artifacts/repository-audit.json > /dev/null
echo "Verification complete"
