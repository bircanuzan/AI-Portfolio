# AI Transformation Portfolio Lead Project (UAE Bank)

**Independent, synthetic portfolio case study | November 2026 | Bircan Uzan**

**Important:** This is NOT a Commercial Bank of Dubai client project or a real bank deployment. All initiatives, banking figures, risks and decisions are illustrative, and there is no customer data.

## Business challenge
A hypothetical UAE bank must shape and govern an enterprise change agenda across Investment & Transaction Banking, Institutional and Corporate Banking, Treasury, Asset Management and Global Markets. Group Heads have competing priorities, shared project resources, technology dependencies and regulatory obligations. The Transformation Portfolio Lead needs transparent, defensible executive decisions and measurable change adoption.

## Deliverables
1. [Portfolio charter, governance and resource/decision rights](docs/01-charter-governance.md)
2. [ExCo Steering Committee decision pack and business case](docs/02-exco-business-case.md)
3. [BRD, UAT, AI/CBUAE control considerations and adoption plan](docs/03-uat-risk-adoption.md)
4. [Synthetic initiative register](data/portfolio.csv)
5. [Deterministic, offline Python prioritisation example](src/portfolio_prioritisation.py)

## Demonstrated workflow
**Strategy -> intake -> business case -> priority and dependency review -> ExCo decision -> design/BRD -> UAT/risk acceptance -> training and communications -> benefits tracking -> audit closure.**

## Methodology
Each proposed initiative is evaluated using strategic fit (25%), benefits evidence (25%), feasibility (20%), controls readiness (20%) and change readiness (10%). This prioritisation model is an illustrative decision-support tool: high-ranking initiatives cannot bypass data privacy, security, risk or regulatory review. A realistic ExCo pack exposes competing resource demands and records explicit go / hold / re-sequence decisions.

## Running the example
```bash
python src/portfolio_prioritisation.py data/portfolio.csv
```
The Python script uses only the standard library. Input data is synthetic, not from any bank.

## Evidence boundaries
- Demonstrates portfolio architecture, requirements traceability, AI controls and executive reporting **as independent portfolio work**.
- It does not demonstrate direct employment in CBD, a production agent deployment, actual CBUAE compliance approval, independent audit sign-off, or realised savings.
- Controls require review against the latest applicable CBUAE requirements and the specific bank's legal, compliance, information-security, model-risk and privacy policies.
