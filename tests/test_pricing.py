from __future__ import annotations

import unittest
from datetime import date

from everwork_checkout import Coupon, calculate_total


class PricingTests(unittest.TestCase):
    def test_checkout_without_coupon_keeps_subtotal(self) -> None:
        self.assertEqual(
            calculate_total(12_50, coupon=None, today=date(2026, 8, 30)),
            12_50,
        )

    def test_active_coupon_reduces_total_using_integer_cents(self) -> None:
        coupon = Coupon("EVERWORK15", 15, date(2026, 9, 30))
        self.assertEqual(
            calculate_total(10_01, coupon=coupon, today=date(2026, 8, 30)),
            8_51,
        )

    def test_coupon_is_valid_on_expiration_date(self) -> None:
        coupon = Coupon("LASTDAY", 25, date(2026, 8, 30))
        self.assertEqual(
            calculate_total(20_00, coupon=coupon, today=date(2026, 8, 30)),
            15_00,
        )

    def test_expired_coupon_does_not_change_total(self) -> None:
        coupon = Coupon("EXPIRED50", 50, date(2026, 8, 29))
        self.assertEqual(
            calculate_total(20_00, coupon=coupon, today=date(2026, 8, 30)),
            20_00,
        )

    def test_invalid_inputs_fail_closed(self) -> None:
        with self.assertRaises(ValueError):
            calculate_total(-1, coupon=None, today=date(2026, 8, 30))
        with self.assertRaises(ValueError):
            Coupon("TOO-MUCH", 101, date(2026, 8, 30))


if __name__ == "__main__":
    unittest.main()

