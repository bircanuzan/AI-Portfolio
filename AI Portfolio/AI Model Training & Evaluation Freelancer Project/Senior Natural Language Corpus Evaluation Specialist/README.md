# Senior Natural Language Corpus Evaluation Specialist | NLP Corpus Quality Audit

> **Portfolio status:** Independent, synthetic demonstration. No confidential information, employer/client work, actual model-training delivery or production deployment is claimed. All records and ratings are invented to exercise the methodology.


## Problem and evaluation goals
Language datasets used to train and test AI models require reliable text normalization, metadata, representativeness, annotation consistency and sampling procedures. This project builds a transparent quality assurance protocol and an offline Python validator for a **synthetic multilingual text corpus**.

## JD-aligned workstreams
1. **Quality framework:** measure record validity, duplicates, Unicode/whitespace anomalies, null text, metadata completeness, language/domain distributions and source traceability.
2. **Linguistic review:** document tokenization, normalization, sentence segmentation, annotation taxonomy, named-entity categories, part-of-speech and semantic-label expectations. These advanced linguistic checks are manual/extension points, not claimed implemented by the basic script.
3. **Dataset representativeness:** compare observed language proportions with documented target mixes; identify coverage gaps, register imbalance and underrepresented dialects.
4. **Annotation consistency:** calculate Cohen's kappa for two categorical annotators on aligned records; flag low agreement for adjudication.
5. **Sampling plan:** stratify by language, domain and source, inspect rare categories and high-error cohorts, retain reproducible random seed.
6. **Remediation:** preserve immutable source snapshot, document quarantined records and retest after the cleaning pipeline.

## Sample synthetic corpus
`data/corpus.json` contains English and Turkish records with a deliberate exact duplicate and Unicode/metadata defects for validation. Language values are manually supplied; this script does not perform reliable language identification.

## Evaluation metrics
Duplicate share; empty/invalid text count; missing metadata; observed language and domain proportions; categorical annotator agreement (kappa) where available. Automated checks are a preliminary hygiene gate, not a full linguistic certification.

## Deliverables
- `quality_protocol.md`: standards, metadata contract, stratified QA sampling, inter-rater calibration, remediations.
- `src/corpus_quality.py`: deterministic audit using Python standard library.
- `tests/test_corpus_quality.py`: tests for duplication, kappa and missing text.
- `data/corpus.json`: made-up records, no customer/private data.

## Run
```bash
python -m unittest discover -s "AI Model Training & Evaluation Freelancer Project/Senior Natural Language Corpus Evaluation Specialist/tests"
python "AI Model Training & Evaluation Freelancer Project/Senior Natural Language Corpus Evaluation Specialist/src/corpus_quality.py" "AI Model Training & Evaluation Freelancer Project/Senior Natural Language Corpus Evaluation Specialist/data/corpus.json"
```

## Extension roadmap (not implemented)
Add spaCy/Stanza integration for linguistic annotation audits, language-specific tokenization, NER boundary agreement, statistical confidence intervals and configurable bias thresholds. Report results separately for each language and source.
