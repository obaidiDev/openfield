from typing import Literal, cast

SubscriptionPlanType = Literal[
    "basic",
    "creator",
    "enterprise",
    "free",
    "max",
    "plus",
    "pro",
    "scale",
    "starter",
    "team",
    "ultimate",
    "ultra",
]

SUBSCRIPTION_PLAN_TYPE_VALUES: set[SubscriptionPlanType] = {
    "basic",
    "creator",
    "enterprise",
    "free",
    "max",
    "plus",
    "pro",
    "scale",
    "starter",
    "team",
    "ultimate",
    "ultra",
}


def check_subscription_plan_type(value: str) -> SubscriptionPlanType:
    if value in SUBSCRIPTION_PLAN_TYPE_VALUES:
        return cast(SubscriptionPlanType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUBSCRIPTION_PLAN_TYPE_VALUES!r}"
    )
