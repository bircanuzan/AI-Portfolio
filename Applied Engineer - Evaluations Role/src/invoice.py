"""Reference implementation for synthetic PR-101: invoice discount/tax calculation.

Money uses Decimal and explicit ROUND_HALF_UP at invoice-level monetary boundaries.
This is a small reference fixture, NOT a production financial application.
"""
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

CENT = Decimal("0.01")
ONE = Decimal("1")


def decimal_value(value, field):
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError):
        raise ValueError(f"{field} must be a decimal") from None
    if not result.is_finite():
        raise ValueError(f"{field} must be finite")
    return result


def calculate_invoice(lines, tax_rate, discount_rate=0):
    """Return string-encoded amounts; validate quantities, money and rates.

    Price and discount inputs are kept at full precision; ROUND_HALF_UP is
    applied to the discount amount and tax only once at invoice level.
    """
    if not isinstance(lines, list) or not lines:
        raise ValueError("lines must be a non-empty list")
    tax = decimal_value(tax_rate, "tax_rate")
    discount_rate = decimal_value(discount_rate, "discount_rate")
    if not 0 <= tax <= ONE or not 0 <= discount_rate <= ONE:
        raise ValueError("tax and discount rates must be between 0 and 1")
    subtotal = Decimal("0")
    for index, line in enumerate(lines):
        if not isinstance(line, dict):
            raise ValueError(f"line {index} must be an object")
        price = decimal_value(line.get("unit_price"), "unit_price")
        quantity = line.get("quantity")
        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("quantity must be a positive integer")
        if price < 0:
            raise ValueError("unit_price cannot be negative")
        subtotal += price * quantity
    subtotal = subtotal.quantize(CENT, rounding=ROUND_HALF_UP)
    discount = (subtotal * discount_rate).quantize(CENT, rounding=ROUND_HALF_UP)
    taxable = subtotal - discount
    tax_amount = (taxable * tax).quantize(CENT, rounding=ROUND_HALF_UP)
    total = taxable + tax_amount
    return {
        "subtotal": str(subtotal),
        "discount": str(discount),
        "tax": str(tax_amount),
        "total": str(total),
    }
