from typing import Literal, cast

MediaImportType = Literal["audio", "image", "video"]

MEDIA_IMPORT_TYPE_VALUES: set[MediaImportType] = {
    "audio",
    "image",
    "video",
}


def check_media_import_type(value: str) -> MediaImportType:
    return cast(MediaImportType, value)
