# Language Data Quality Standard v1.0

## Intake
Required keys: id, text, language, domain, source, annotation_a, annotation_b. Record provenance and consent/licensing for any genuine corpus before importing. Reject secrets, personal identifiers, and unlicensed or sensitive content.

## Checkpoints
- Encoding: read UTF-8 and normalize to Unicode NFC for *comparison only*. Preserve original content for traceability.
- Duplicate audit: casefold and whitespace-fold with language limitations noted; near-duplicates require an approved similarity tool and human review.
- Structural: missing language/domain/source; empty text; malformed rows; invalid annotation label.
- Annotation QA: two independently assigned labels drawn from an agreed taxonomy; report exact agreement and Cohen's kappa, inspect confusion matrix.
- Linguistics: sample morphological constructions, entities, code-switching and dialect cases manually or via validated NLP pipelines.
- Bias/coverage: inspect every language-domain intersection and source distribution; set required target mix before using metrics to claim balance.

## Stratified sampling design
Seeded sample by language x domain x source. Review all rare cohorts (few records), draw random rows from large cohorts, and include deliberately problematic records. Require independent adjudication for policy-sensitive labels. Report selection probability and never generalize from convenience samples alone.

## Acceptance gates (illustrative, not measured on a real corpus)
Zero missing consent/provenance for real inputs; zero missing mandatory metadata; duplicates quarantined; no unresolved invalid UTF-8; reviewed language coverage against documented project targets; kappa threshold decided by use case; all exceptions assigned and logged.

## Corrective action record
record_id | defect | source snapshot | proposed fix | reviewer | approval | change date | recheck outcome
