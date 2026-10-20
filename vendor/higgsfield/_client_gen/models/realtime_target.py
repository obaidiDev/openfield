from typing import Literal, cast

RealtimeTarget = Literal["canvas", "selection"]

REALTIME_TARGET_VALUES: set[RealtimeTarget] = {
    "canvas",
    "selection",
}


def check_realtime_target(value: str) -> RealtimeTarget:
    return cast(RealtimeTarget, value)
