from typing import Literal, cast

MediaItemType = Literal["audio", "image", "video"]

MEDIA_ITEM_TYPE_VALUES: set[MediaItemType] = {
    "audio",
    "image",
    "video",
}


def check_media_item_type(value: str) -> MediaItemType:
    return cast(MediaItemType, value)
