from typing import Literal, cast

ConfirmMediaUploadType = Literal["audio", "file", "image", "video"]

CONFIRM_MEDIA_UPLOAD_TYPE_VALUES: set[ConfirmMediaUploadType] = {
    "audio",
    "file",
    "image",
    "video",
}


def check_confirm_media_upload_type(value: str) -> ConfirmMediaUploadType:
    if value in CONFIRM_MEDIA_UPLOAD_TYPE_VALUES:
        return cast(ConfirmMediaUploadType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONFIRM_MEDIA_UPLOAD_TYPE_VALUES!r}"
    )
