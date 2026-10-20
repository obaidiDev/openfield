from typing import Literal, cast

ListReferenceElementsOrder = Literal["asc", "desc"]

LIST_REFERENCE_ELEMENTS_ORDER_VALUES: set[ListReferenceElementsOrder] = {
    "asc",
    "desc",
}


def check_list_reference_elements_order(value: str) -> ListReferenceElementsOrder:
    if value in LIST_REFERENCE_ELEMENTS_ORDER_VALUES:
        return cast(ListReferenceElementsOrder, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_REFERENCE_ELEMENTS_ORDER_VALUES!r}"
    )
