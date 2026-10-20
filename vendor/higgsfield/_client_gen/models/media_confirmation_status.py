from typing import Literal, cast

MediaConfirmationStatus = Literal["error", "ip_detected", "not_ready", "nsfw", "uploaded"]

MEDIA_CONFIRMATION_STATUS_VALUES: set[MediaConfirmationStatus] = {
    "error",
    "ip_detected",
    "not_ready",
    "nsfw",
    "uploaded",
}


def check_media_confirmation_status(value: str) -> MediaConfirmationStatus:
    if value in MEDIA_CONFIRMATION_STATUS_VALUES:
        return cast(MediaConfirmationStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDIA_CONFIRMATION_STATUS_VALUES!r}"
    )
