from typing import Literal, cast

ImportMediaRequestType = Literal["audio", "auto", "image", "video"]

IMPORT_MEDIA_REQUEST_TYPE_VALUES: set[ImportMediaRequestType] = {
    "audio",
    "auto",
    "image",
    "video",
}


def check_import_media_request_type(value: str) -> ImportMediaRequestType:
    if value in IMPORT_MEDIA_REQUEST_TYPE_VALUES:
        return cast(ImportMediaRequestType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {IMPORT_MEDIA_REQUEST_TYPE_VALUES!r}"
    )
