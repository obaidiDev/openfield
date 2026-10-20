from typing import Literal, cast

MediaRole = Literal["audio", "end_image", "file", "image", "start_image", "video"]

MEDIA_ROLE_VALUES: set[MediaRole] = {
    "audio",
    "end_image",
    "file",
    "image",
    "start_image",
    "video",
}


def check_media_role(value: str) -> MediaRole:
    return cast(MediaRole, value)
