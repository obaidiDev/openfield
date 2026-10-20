from typing import Literal, cast

ListMarketingSetupItemsType = Literal["hook", "setting"]

LIST_MARKETING_SETUP_ITEMS_TYPE_VALUES: set[ListMarketingSetupItemsType] = {
    "hook",
    "setting",
}


def check_list_marketing_setup_items_type(value: str) -> ListMarketingSetupItemsType:
    if value in LIST_MARKETING_SETUP_ITEMS_TYPE_VALUES:
        return cast(ListMarketingSetupItemsType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_MARKETING_SETUP_ITEMS_TYPE_VALUES!r}"
    )
