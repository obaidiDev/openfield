from typing import Literal, cast

MarketingSetupItemType = Literal["hook", "setting"]

MARKETING_SETUP_ITEM_TYPE_VALUES: set[MarketingSetupItemType] = {
    "hook",
    "setting",
}


def check_marketing_setup_item_type(value: str) -> MarketingSetupItemType:
    if value in MARKETING_SETUP_ITEM_TYPE_VALUES:
        return cast(MarketingSetupItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MARKETING_SETUP_ITEM_TYPE_VALUES!r}"
    )
