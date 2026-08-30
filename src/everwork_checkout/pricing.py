"""Integer-cents checkout pricing with explicit coupon eligibility."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True, slots=True)
class Coupon:
    """A percentage coupon that remains valid through ``expires_on``."""

    code: str
    percent_off: int
    expires_on: date

    def __post_init__(self) -> None:
        if not self.code.strip():
            raise ValueError("coupon code is required")
        if not 0 <= self.percent_off <= 100:
            raise ValueError("percent_off must be between 0 and 100")


def calculate_total(subtotal_cents: int, *, coupon: Coupon | None, today: date) -> int:
    """Return a deterministic checkout total in cents.

    Discounts round down to the nearest cent. Expired coupons are ignored.
    """

    if subtotal_cents < 0:
        raise ValueError("subtotal_cents cannot be negative")
    if coupon is None or today > coupon.expires_on:
        return subtotal_cents
    discount_cents = subtotal_cents * coupon.percent_off // 100
    return subtotal_cents - discount_cents

