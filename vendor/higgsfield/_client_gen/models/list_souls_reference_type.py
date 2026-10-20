from typing import Literal, cast

ListSoulsReferenceType = Literal["soul_2", "soul_cinematic"]

LIST_SOULS_REFERENCE_TYPE_VALUES: set[ListSoulsReferenceType] = {
    "soul_2",
    "soul_cinematic",
}


def check_list_souls_reference_type(value: str) -> ListSoulsReferenceType:
    if value in LIST_SOULS_REFERENCE_TYPE_VALUES:
        return cast(ListSoulsReferenceType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_SOULS_REFERENCE_TYPE_VALUES!r}"
    )
