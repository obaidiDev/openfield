from typing import Literal, cast

CreateMediaUploadType = Literal["audio", "file", "image", "video"]

CREATE_MEDIA_UPLOAD_TYPE_VALUES: set[CreateMediaUploadType] = {
    "audio",
    "file",
    "image",
    "video",
}


def check_create_media_upload_type(value: str) -> CreateMediaUploadType:
    if value in CREATE_MEDIA_UPLOAD_TYPE_VALUES:
        return cast(CreateMediaUploadType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_MEDIA_UPLOAD_TYPE_VALUES!r}"
    )
