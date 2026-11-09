"""Synthetic bank transformation portfolio: explainable prioritisation, not investment advice."""
import csv
import sys
from pathlib import Path

WEIGHTS = {"strategy": 25, "benefits_evidence": 25, "feasibility": 20, "controls": 20, "adoption": 10}

def score(item):
    """Calculate weighted 0-100 readiness score from five 0-5 criteria."""
    values = {key: int(item[key]) for key in WEIGHTS}
    if any(v < 0 or v > 5 for v in values.values()):
        raise ValueError("Each criterion must be in the range 0..5")
    return round(sum(values[k] * WEIGHTS[k] / 5 for k in WEIGHTS), 1)

def recommendation(item):
    if int(item['controls']) < 3:
        return 'HOLD - CONTROL REVIEW'
    if score(item) >= 75:
        return 'PRIORITISE - SUBJECT TO APPROVAL'
    return 'SHAPE / RESEQUENCE'

def load(path):
    with Path(path).open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def main(path):
    initiatives = sorted(load(path), key=score, reverse=True)
    print('SYNTHETIC UAE BANK AI/CHANGE PORTFOLIO (NO REAL BANK DATA)')
    print(f"{'ID':<8} {'SCORE':>6} {'FTE MONTHS':>10}  {'DECISION':<32}  INITIATIVE")
    for item in initiatives:
        print(f"{item['id']:<8} {score(item):>6.1f} {int(item['effort_fte_months']):>10}  {recommendation(item):<32}  {item['initiative']}")
    print('Ranking requires ExCo approval, risk gates, funding and resource/dependency review.')
    print('Total indicative demand:', sum(int(x['effort_fte_months']) for x in initiatives), 'FTE-months')

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent.parent/'data'/'portfolio.csv'
    main(path)
