"""Synthetic candidate patches, not outputs from real or named AI systems.

Each candidate is an executable Python function. Intentional defects make
regressions, edge-case failures and benchmark scoring observable.
"""
from decimal import Decimal, ROUND_DOWN, ROUND_HALF_UP
from .invoice import calculate_invoice, CENT


def reference_candidate(lines, tax_rate, discount_rate=0):
    return calculate_invoice(lines, tax_rate, discount_rate)


def tax_before_discount_candidate(lines, tax_rate, discount_rate=0):
    result = calculate_invoice(lines, tax_rate, discount_rate)
    # PR-101 regression: tax assessed on gross subtotal, not discounted value.
    tax = (Decimal(result["subtotal"]) * Decimal(str(tax_rate))).quantize(
        CENT, rounding=ROUND_HALF_UP
    )
    result["tax"] = str(tax)
    result["total"] = str(Decimal(result["subtotal"]) - Decimal(result["discount"]) + tax)
    return result


def truncation_candidate(lines, tax_rate, discount_rate=0):
    result = calculate_invoice(lines, tax_rate, discount_rate)
    # PR-101 regression: always rounds tax DOWN, even at exact half-cent.
    taxable = Decimal(result["subtotal"]) - Decimal(result["discount"])
    tax = (taxable * Decimal(str(tax_rate))).quantize(CENT, rounding=ROUND_DOWN)
    result["tax"] = str(tax)
    result["total"] = str(taxable + tax)
    return result


CANDIDATES = {
    "synthetic-reference-patch": reference_candidate,
    "synthetic-tax-before-discount-patch": tax_before_discount_candidate,
    "synthetic-truncation-patch": truncation_candidate,
}
