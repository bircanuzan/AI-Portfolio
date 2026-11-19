# Model Usage Ledger & Budget Guardrails

**New independent demonstration | locally runnable | Python standard library only**

## Decision problem
Enterprise buyers need to distinguish AI-token spend, cost per verified successful request, departmental budgets and hypothetical optimization scenarios before claiming return on investment.

## Implemented
- Synthetic usage ledger by department and example model tier.
- Token spend calculated from *illustrative* USD-per-million-token input/output rates.
- Budget thresholds, spending variance and cost per successful request; zero-success handling.
- Defensive validation of usage counts and pricing; machine-readable JSON output and unit tests.

## Run (from this project directory)
```bash
python src/usage_ledger.py --input data/fictional_usage.csv --budgets data/fictional_budgets.json --output cost_report.json
python -m unittest discover -s tests -v
```

## Interpretation & governance
Costs are **modelled example expenses**, not invoices. Rates do not quote or represent real provider pricing. A cheaper model, lower output cap, prompt compression, cache or local inference must also pass quality, governance, privacy and latency gates before a real-world routing decision. License consolidation is covered separately in the [existing enterprise AI discovery case](../Licence_and_Subscription_Review/).

**Production extensions (not built):** Azure/AWS/GCP billing feeds, actual token logs, provider usage APIs, tenant-level license reconciliation, FinOps alerts, prompt caching experiments and tested model-routing policies. No live account, API access, savings or production cost optimisation is claimed.
