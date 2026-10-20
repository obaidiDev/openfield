from typing import Literal, cast

ListJobsType = Literal["audio", "image", "text", "video"]

LIST_JOBS_TYPE_VALUES: set[ListJobsType] = {
    "audio",
    "image",
    "text",
    "video",
}


def check_list_jobs_type(value: str) -> ListJobsType:
    return cast(ListJobsType, value)
