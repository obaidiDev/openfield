from typing import Literal, cast

ListJobSetTypesLabelItem = Literal["app", "chain", "model"]

LIST_JOB_SET_TYPES_LABEL_ITEM_VALUES: set[ListJobSetTypesLabelItem] = {
    "app",
    "chain",
    "model",
}


def check_list_job_set_types_label_item(value: str) -> ListJobSetTypesLabelItem:
    if value in LIST_JOB_SET_TYPES_LABEL_ITEM_VALUES:
        return cast(ListJobSetTypesLabelItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_JOB_SET_TYPES_LABEL_ITEM_VALUES!r}"
    )
