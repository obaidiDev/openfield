from typing import Literal, cast

Currency = Literal["eur", "gbp", "usd"]

CURRENCY_VALUES: set[Currency] = {
    "eur",
    "gbp",
    "usd",
}


def check_currency(value: str) -> Currency:
    return cast(Currency, value)
