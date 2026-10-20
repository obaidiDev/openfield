from typing import Literal, cast

ListReferenceElementsSortBy = Literal["created_at", "last_used_at", "pinned_at"]

LIST_REFERENCE_ELEMENTS_SORT_BY_VALUES: set[ListReferenceElementsSortBy] = {
    "created_at",
    "last_used_at",
    "pinned_at",
}


def check_list_reference_elements_sort_by(value: str) -> ListReferenceElementsSortBy:
    if value in LIST_REFERENCE_ELEMENTS_SORT_BY_VALUES:
        return cast(ListReferenceElementsSortBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_REFERENCE_ELEMENTS_SORT_BY_VALUES!r}"
    )
