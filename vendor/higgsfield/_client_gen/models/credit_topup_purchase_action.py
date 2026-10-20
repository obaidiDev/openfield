from typing import Literal, cast

CreditTopupPurchaseAction = Literal["topup"]

CREDIT_TOPUP_PURCHASE_ACTION_VALUES: set[CreditTopupPurchaseAction] = {
    "topup",
}


def check_credit_topup_purchase_action(value: str) -> CreditTopupPurchaseAction:
    if value in CREDIT_TOPUP_PURCHASE_ACTION_VALUES:
        return cast(CreditTopupPurchaseAction, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREDIT_TOPUP_PURCHASE_ACTION_VALUES!r}"
    )
