from typing import Literal, cast

UpgradePlanPurchaseAction = Literal["upgrade_plan"]

UPGRADE_PLAN_PURCHASE_ACTION_VALUES: set[UpgradePlanPurchaseAction] = {
    "upgrade_plan",
}


def check_upgrade_plan_purchase_action(value: str) -> UpgradePlanPurchaseAction:
    if value in UPGRADE_PLAN_PURCHASE_ACTION_VALUES:
        return cast(UpgradePlanPurchaseAction, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPGRADE_PLAN_PURCHASE_ACTION_VALUES!r}"
    )
