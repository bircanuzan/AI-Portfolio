"""Synthetic enterprise AI tool portfolio management report.

Standard library only. Not a live platform integration or validated ROI model.
"""
from __future__ import annotations

import argparse
import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def nonnegative_decimal(value: str, field: str) -> Decimal:
    try:
        number = Decimal(str(value))
    except (InvalidOperation, ValueError) as exc:
        raise ValueError(f"Invalid {field}: {value!r}") from exc
    if not number.is_finite() or number < 0:
        raise ValueError(f"Expected non-negative finite {field}, got {value!r}")
    return number


def whole_number(value: str, field: str) -> int:
    number = nonnegative_decimal(value, field)
    if number != number.to_integral_value():
        raise ValueError(f"{field} must be a whole number")
    return int(number)


def money(amount: Decimal) -> str:
    return f"\${amount:,.2f}"


def build_report(registry: list[dict[str, str]], usage: list[dict[str, str]]) -> str:
    tools = {}
    for item in registry:
        tool_id = item["tool_id"].strip()
        if not tool_id or tool_id in tools:
            raise ValueError(f"Duplicate or empty tool_id in register: {tool_id!r}")
        tools[tool_id] = item

    seen = set()
    total_seats = total_active = 0
    total_spend = Decimal("0")
    total_gross = Decimal("0")
    risks = []
    output_rows = []

    for row in sorted(usage, key=lambda r: (r["month"], r["tool_id"])):
        tool_id, month = row["tool_id"].strip(), row["month"].strip()
        if tool_id not in tools:
            raise ValueError(f"Usage references an unregistered tool: {tool_id}")
        if (tool_id, month) in seen:
            raise ValueError(f"Duplicate usage row for {tool_id}, {month}")
        seen.add((tool_id, month))
        tool = tools[tool_id]
        seats = whole_number(row["licensed_seats"], "licensed_seats")
        active = whole_number(row["active_users"], "active_users")
        capacity = whole_number(tool["seat_limit"], "seat_limit")
        if active > seats or seats > capacity:
            raise ValueError(f"Seat mismatch for {tool_id}: active={active}, licensed={seats}, cap={capacity}")
        spend = nonnegative_decimal(row["monthly_spend_usd"], "monthly_spend_usd")
        hours = nonnegative_decimal(row["hours_saved_per_active_user"], "hours_saved_per_active_user")
        rate = nonnegative_decimal(row["loaded_hourly_rate_usd"], "loaded_hourly_rate_usd")
        gross = Decimal(active) * hours * rate
        net = gross - spend
        adoption = f"{active / seats * 100:.1f}%" if seats else "n/a"
        output_rows.append(
            f"| {month} | {tool['platform']} | {active}/{seats} | {adoption} | "
            f"{money(spend)} | {money(gross)} | {money(net)} |"
        )
        total_seats += seats
        total_active += active
        total_spend += spend
        total_gross += gross

        missing = [
            label for label, column in (
                ("InfoSec", "security_review"),
                ("Legal", "legal_review"),
                ("DPO", "dpo_review"),
            ) if tool[column].strip().lower() != "yes"
        ]
        if tool["approval_status"].strip().lower() != "approved":
            missing.append("Full approval")
        if missing:
            risks.append(f"- **{tool_id} ({tool['platform']}):** Gate not cleared: {', '.join(missing)}. Do not expand use pending approvals.")

    total_net = total_gross - total_spend
    adoption_total = f"{total_active / total_seats * 100:.1f}%" if total_seats else "n/a"
    roi = f"{total_net / total_spend * 100:.1f}%" if total_spend else "n/a"
    lines = [
        "# Enterprise AI Portfolio — Synthetic Monthly Review",
        "",
        "> **Illustrative inputs only.** These are not vendor prices, live usage, client results, or realised financial savings.",
        "> Hours saved and hourly values are assumptions requiring Finance validation.",
        "",
        f"**Registered tools:** {len(tools)} | **Usage records:** {len(usage)}",
        "",
        "| Month | Tool | Active/licensed | Utilisation | Assumed spend | Hypothetical gross value | Hypothetical net value |",
        "|---|---|---:|---:|---:|---:|---:|",
        *output_rows,
        "",
        "## Illustrative portfolio summary",
        f"- Licensed seats: **{total_seats}**",
        f"- Active users: **{total_active}**",
        f"- Seat utilisation: **{adoption_total}**",
        f"- Monthly spend: **{money(total_spend)}**",
        f"- Hypothetical gross productivity proxy: **{money(total_gross)}**",
        f"- Hypothetical net value: **{money(total_net)}**",
        f"- Hypothetical ROI on tool spend alone: **{roi}**",
        "",
        "## Governance exceptions — review before scaling",
        *(risks if risks else ["- No missing approvals flagged in the supplied sample."]),
        "",
        "## Management action",
        "Validate real vendor contracts and approval evidence, reconcile invoices with Finance, review unused seats, "
        "complete blocked reviews, verify adoption, and do not treat productivity assumptions as booked savings.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=ROOT / "data" / "ai_tool_register_synthetic.csv")
    parser.add_argument("--usage", type=Path, default=ROOT / "data" / "monthly_usage_synthetic.csv")
    parser.add_argument("--output", type=Path, help="Optional Markdown output path")
    args = parser.parse_args()
    report = build_report(read_csv(args.registry), read_csv(args.usage))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
        print(f"Wrote {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
