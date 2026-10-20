from typing import Literal, cast

ListVideoAnalysesOrder = Literal["asc", "desc"]

LIST_VIDEO_ANALYSES_ORDER_VALUES: set[ListVideoAnalysesOrder] = {
    "asc",
    "desc",
}


def check_list_video_analyses_order(value: str) -> ListVideoAnalysesOrder:
    if value in LIST_VIDEO_ANALYSES_ORDER_VALUES:
        return cast(ListVideoAnalysesOrder, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_VIDEO_ANALYSES_ORDER_VALUES!r}"
    )
