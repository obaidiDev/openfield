from typing import Literal, cast

MediaImportStatus = Literal["error", "ip_detected", "not_ready", "nsfw", "uploaded"]

MEDIA_IMPORT_STATUS_VALUES: set[MediaImportStatus] = {
    "error",
    "ip_detected",
    "not_ready",
    "nsfw",
    "uploaded",
}


def check_media_import_status(value: str) -> MediaImportStatus:
    return cast(MediaImportStatus, value)
