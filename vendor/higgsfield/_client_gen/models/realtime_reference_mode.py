from typing import Literal, cast

RealtimeReferenceMode = Literal["character", "style"]

REALTIME_REFERENCE_MODE_VALUES: set[RealtimeReferenceMode] = {
    "character",
    "style",
}


def check_realtime_reference_mode(value: str) -> RealtimeReferenceMode:
    if value in REALTIME_REFERENCE_MODE_VALUES:
        return cast(RealtimeReferenceMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REALTIME_REFERENCE_MODE_VALUES!r}"
    )
