# NLP Corpus Evaluation & Linguistic Dataset Quality Assurance

**Independent, runnable, synthetic demonstration — aligned to the closed Agile 4UX Senior Natural Language Corpus Evaluation Specialist job description (UAE remote).** No employment relationship or client delivery is implied.

## Client requirements mapped to this project
- QA large-scale mono/multilingual, domain-specific language corpora (prototype: English and Turkish)
- Establish dataset acceptance criteria and quality rubric for grammar, semantic relevance, metadata, annotation and representativeness
- Detect duplicate text, text normalization / encoding issues, corrupted inputs and schema inconsistencies
- Examine named-entity span validity, source metadata and inter-annotator consistency
- Screen for potential privacy risks and bias; human review required for complex linguistic and fairness judgments
- Track corpus distribution across languages, domains and registers
- Design repeatable statistical sampling, quality reports, issue taxonomy and remediation gates

## Technical skills demonstrated
Python 3 standard library, JSONL validation, Unicode NFKC normalization, duplicate detection, regex privacy screening, entity-offset validation, label consistency, two-rater Cohen's kappa, deterministic language-stratified sampling, transparent error taxonomy, JSON reporting and Python unittest.

**Not claimed:** production-scale corpus processing, trained NER/POS/dependency models, automated semantic understanding, or independently verified demographic fairness. Those require licensed corpora, a linguist-annotated gold set and dedicated models/tools (spaCy, pandas, Hugging Face, etc.).

## Project structure
- [corpus_quality.py](corpus_quality.py) — executable text corpus audit and evaluation summary
- [data/synthetic_corpus.jsonl](data/synthetic_corpus.jsonl) — synthetic English/Turkish HR and support text, including deliberate quality defects
- [tests/test_corpus_quality.py](tests/test_corpus_quality.py) — regression tests
- [QUALITY_RUBRIC.md](QUALITY_RUBRIC.md) — checks, methodology, proposed KPIs, release process

## Reproduce
Python 3.10+; **no dependencies or external services**.

```bash
cd "AI Portfolio/Natural Language Processing (NLP)/NLP Corpus Evaluation & Linguistic Dataset Quality Assurance"
python corpus_quality.py --output reports/quality_report.json
python -m unittest discover -s tests -v
```

The synthetic fixture deliberately includes a duplicate, inter-annotator disagreement, possible contact information and replacement-character corruption. A HOLD_FOR_REVIEW decision is therefore expected, **not** a performance failure.

## Methodology
1. Define data contract, label taxonomy, language/domain/register targets and acceptance gates.
2. Document corpus provenance, privacy and version; use only consented or synthetic text.
3. Run structural, Unicode, duplication, annotation and sensitive-text heuristics.
4. Use deterministic language-stratified samples for human audit; compute agreement and adjudicate disagreements.
5. Document semantic and grammatical issues with linguists, and evaluate representation against an approved reference distribution.
6. Export JSON report, review critical defects, record remediation and rerun before release.

## Evidence
Source code + tests + synthetic fixture are inspectable; **numeric outcomes are only local synthetic-fixture checks**. Thresholds in the rubric are proposals, not achieved client SLAs.
