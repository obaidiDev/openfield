from typing import Literal, cast

BillingPeriod = Literal["annual", "eighteen_month", "monthly", "quarterly", "two_year"]

BILLING_PERIOD_VALUES: set[BillingPeriod] = {
    "annual",
    "eighteen_month",
    "monthly",
    "quarterly",
    "two_year",
}


def check_billing_period(value: str) -> BillingPeriod:
    return cast(BillingPeriod, value)
