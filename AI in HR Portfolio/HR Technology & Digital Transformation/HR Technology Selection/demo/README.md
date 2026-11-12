# Reproducible synthetic vendor selection demo

Run with Python 3.10+ and no external dependencies from this folder:

```bash
python score_options.py
python -m unittest -v test_score_options.py
```

Uses fictional vendor options **Option A/B/C** only. Weighted scoring uses Decimal and a mandatory security/privacy gate; an ineligible option cannot be recommended regardless of its rank.

Fields in `synthetic_vendor_scores.csv` are illustrative, not estimates from real vendors. A positive outcome means **shortlist for procurement review**, not a legal approval or signed vendor contract.
