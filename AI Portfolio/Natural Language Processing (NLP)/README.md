# Natural Language Processing (NLP) — Text Intelligence & Language Model Evaluation

**Portfolio status:** Reference project blueprint; no unverified client deployment, accuracy number or benchmark result is asserted.

## Business / client requirements
Design and evaluate dependable text-classification, entity-extraction, semantic search and LLM-supported language workflows with multilingual English/Turkish evaluation where applicable, source grounding, privacy protection and human escalation.

## Technical stack and skills
- Python, spaCy, NLTK, scikit-learn, Hugging Face Transformers/Datasets, sentence-transformers, pandas, regex, JSON, SQL
- Tokenization, normalization, lemmatization, TF-IDF, embeddings, named-entity recognition, sentiment/intent classification, semantic similarity, retrieval, RAG evaluation and prompt/response rubric design
- LLM evaluation: factuality, hallucination detection, instruction following, groundedness, adversarial testing, multilingual consistency, PII handling and agent trace review

## Proposed methodology
1. Define use case and language coverage; map risks, sensitive information and acceptable errors.
2. Prepare consented/licensed or synthetic text samples with annotation guidelines and inter-annotator review.
3. Establish rule-based, TF-IDF or embedding baseline before transformer/LLM approaches.
4. Create adversarial cases, ambiguous prompts, multilingual equivalents and difficult negatives.
5. Evaluate on held-out sets with confusion analysis, source checks and human adjudication.
6. Deliver evaluation rubrics, error taxonomy, versioned test set, model card and release gates.

## Metrics / SLAs / KPIs (proposed, not achieved)
| Dimension | Proposed measure |
|---|---|
| Classification / extraction | Macro-F1, precision, recall, per-entity F1, confusion matrix |
| Retrieval | Recall@k, MRR/nDCG, citation support rate |
| Generation / LLM safety | Factuality/groundedness pass rate, hallucination rate, instruction-following and refusal quality |
| Multilingual performance | English-vs-Turkish score gap, terminology consistency and human-review disagreement |
| Operations | p95 latency, review turnaround, PII leakage incidents and escalation resolution |

**Evidence required before claiming results:** annotated test dataset, clear rubric, scripts/notebooks, evaluation outputs and limitations.

## Executable portfolio projects

- **[NLP Corpus Evaluation & Linguistic Dataset Quality Assurance](NLP%20Corpus%20Evaluation%20%26%20Linguistic%20Dataset%20Quality%20Assurance/):** Python standard-library audit of an English/Turkish synthetic corpus; detects duplicates, corrupted encoding, possible PII, entity-offset issues and annotator disagreement, reports Cohen's kappa, and includes regression tests and a formal acceptance rubric. Independently built demo, not a client deployment.

- **[Turkish Language AI Evaluator](Turkish%20Language%20AI%20Evaluator/):** independent Turkish AI-content evaluation demonstration covering message drift, hallucinations, factual grounding, cultural nuance, structured reviewer feedback, synthetic test cases, and Python QA summaries. No company/client affiliation or benchmark performance claimed.
