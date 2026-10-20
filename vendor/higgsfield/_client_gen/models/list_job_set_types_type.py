from typing import Literal, cast

ListJobSetTypesType = Literal["3d", "audio", "image", "text", "video"]

LIST_JOB_SET_TYPES_TYPE_VALUES: set[ListJobSetTypesType] = {
    "3d",
    "audio",
    "image",
    "text",
    "video",
}


def check_list_job_set_types_type(value: str) -> ListJobSetTypesType:
    if value in LIST_JOB_SET_TYPES_TYPE_VALUES:
        return cast(ListJobSetTypesType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_JOB_SET_TYPES_TYPE_VALUES!r}"
    )
