from typing import Literal, cast

ListMediaOrder = Literal["asc", "desc"]

LIST_MEDIA_ORDER_VALUES: set[ListMediaOrder] = {
    "asc",
    "desc",
}


def check_list_media_order(value: str) -> ListMediaOrder:
    return cast(ListMediaOrder, value)
