from typing import Literal, cast

MediaUploadSlotType = Literal["audio", "file", "image", "video"]

MEDIA_UPLOAD_SLOT_TYPE_VALUES: set[MediaUploadSlotType] = {
    "audio",
    "file",
    "image",
    "video",
}


def check_media_upload_slot_type(value: str) -> MediaUploadSlotType:
    if value in MEDIA_UPLOAD_SLOT_TYPE_VALUES:
        return cast(MediaUploadSlotType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDIA_UPLOAD_SLOT_TYPE_VALUES!r}"
    )
