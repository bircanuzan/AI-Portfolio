# Data dictionary, MDM rules & data quality contract

| Local synthetic field | Type | Control | Real-world treatment |
|---|---|---|---|
| claim_id | string | unique, SIM-00001 style only | tokenize/pseudonymize; never public repo |
| claim_amount_aed | decimal | >=0; currency AED | reconciliation with claims ledger |
| policy_tenure_months | int | >=0 | align contract effective dates |
| prior_claim_count | int | >=0 | avoid look-ahead / label leakage |
| missing_doc_count | int | >=0 | define document completeness from source status |
| anomaly_indicator | int 0/1 | allowed values | not a fraud determination |
| submission_channel | enum | app/broker/branch | accountable channel mapping |
| manual_review_required | int 0/1 | artificial generator label | NEVER use as actual label; actual decisions need trusted adjudications |

## Recommended acceptance thresholds — proposals, not achieved
- **Completeness:** required tier-1 data fields 99.5%+ before pilot (provisional target).
- **Uniqueness:** 100% claim-intake key uniqueness after event-version semantics.
- **Freshness:** SLA defined per batch/event business workflow, with delay alert + manual fallback.
- **Reconciliation:** risk-approved balance totals by source and period; disputed exceptions tracked.
- **Lineage:** every field has steward, source, transformation, consumer and retention rule.
- **Label quality:** independent definition of human-review outcome with time cutoff to prevent leakage.
- **Master Data Management:** match policy/claim/case references using documented keys; customers and claimants must not be incorrectly merged; manual stewardship for conflicts.

## Data privacy / security
Separate personal data from modelling features; do not place personal identifiers, claim narratives or medical documents in portfolio artifacts. Data access and lawful purpose are preconditions for any future real project. Assess need for DPIA, insurer regulatory obligations and restrictions on AI-supported decisions with UAE counsel and compliance.
