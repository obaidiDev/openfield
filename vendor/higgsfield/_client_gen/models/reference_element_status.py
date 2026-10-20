from typing import Literal, cast

ReferenceElementStatus = Literal[
    "completed", "failed", "ip_checking", "kling_failed", "nsfw", "processing", "voice_clone_failed"
]

REFERENCE_ELEMENT_STATUS_VALUES: set[ReferenceElementStatus] = {
    "completed",
    "failed",
    "ip_checking",
    "kling_failed",
    "nsfw",
    "processing",
    "voice_clone_failed",
}


def check_reference_element_status(value: str) -> ReferenceElementStatus:
    if value in REFERENCE_ELEMENT_STATUS_VALUES:
        return cast(ReferenceElementStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REFERENCE_ELEMENT_STATUS_VALUES!r}"
    )
