from typing import Literal, cast

RealtimeImageMediaRole = Literal["image"]

REALTIME_IMAGE_MEDIA_ROLE_VALUES: set[RealtimeImageMediaRole] = {
    "image",
}


def check_realtime_image_media_role(value: str) -> RealtimeImageMediaRole:
    if value in REALTIME_IMAGE_MEDIA_ROLE_VALUES:
        return cast(RealtimeImageMediaRole, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REALTIME_IMAGE_MEDIA_ROLE_VALUES!r}"
    )
