from typing import Literal, cast

AutoTopupPurchaseAction = Literal["auto_topup"]

AUTO_TOPUP_PURCHASE_ACTION_VALUES: set[AutoTopupPurchaseAction] = {
    "auto_topup",
}


def check_auto_topup_purchase_action(value: str) -> AutoTopupPurchaseAction:
    if value in AUTO_TOPUP_PURCHASE_ACTION_VALUES:
        return cast(AutoTopupPurchaseAction, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AUTO_TOPUP_PURCHASE_ACTION_VALUES!r}"
    )
