import unittest
from src.invoice import calculate_invoice


class InvoiceReferenceTests(unittest.TestCase):
    def test_discount_then_tax(self):
        actual = calculate_invoice([{"unit_price": "19.99", "quantity": 2},
                                    {"unit_price": "5.00", "quantity": 1}], "0.05", "0.10")
        self.assertEqual(actual, {"subtotal": "44.98", "discount": "4.50",
                                  "tax": "2.02", "total": "42.50"})

    def test_half_cent_rounds_up(self):
        self.assertEqual(calculate_invoice([{"unit_price": "0.30", "quantity": 1}], "0.05")["tax"], "0.02")

    def test_multiple_lines_without_tax(self):
        self.assertEqual(calculate_invoice([{"unit_price": "1.00", "quantity": 3},
                                            {"unit_price": "2.50", "quantity": 2}], 0)["total"], "8.00")

    def test_full_discount(self):
        self.assertEqual(calculate_invoice([{"unit_price": "100", "quantity": 1}], "0.05", 1)["total"], "0.00")

    def test_invalid_discount_rate(self):
        with self.assertRaises(ValueError):
            calculate_invoice([{"unit_price": "10", "quantity": 1}], "0.05", "1.5")

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_invoice([{"unit_price": "-1", "quantity": 1}], "0.05")

    def test_zero_quantity(self):
        with self.assertRaises(ValueError):
            calculate_invoice([{"unit_price": "1", "quantity": 0}], "0.05")

    def test_bool_quantity_rejected(self):
        with self.assertRaises(ValueError):
            calculate_invoice([{"unit_price": "1", "quantity": True}], "0.05")

    def test_empty_lines(self):
        with self.assertRaises(ValueError):
            calculate_invoice([], "0.05")

    def test_non_finite_money(self):
        with self.assertRaises(ValueError):
            calculate_invoice([{"unit_price": "Infinity", "quantity": 1}], "0.05")

    def test_negative_tax_rate(self):
        with self.assertRaises(ValueError):
            calculate_invoice([{"unit_price": "1", "quantity": 1}], "-0.01")

    def test_nonnumeric_price(self):
        with self.assertRaises(ValueError):
            calculate_invoice([{"unit_price": "incorrect", "quantity": 1}], "0.05")


if __name__ == "__main__":
    unittest.main()
