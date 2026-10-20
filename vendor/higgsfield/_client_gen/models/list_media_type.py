from typing import Literal, cast

ListMediaType = Literal["audio", "image", "video"]

LIST_MEDIA_TYPE_VALUES: set[ListMediaType] = {
    "audio",
    "image",
    "video",
}


def check_list_media_type(value: str) -> ListMediaType:
    return cast(ListMediaType, value)
