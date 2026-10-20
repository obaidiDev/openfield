from typing import Literal, cast

RealtimeMode = Literal["advanced", "basic"]

REALTIME_MODE_VALUES: set[RealtimeMode] = {
    "advanced",
    "basic",
}


def check_realtime_mode(value: str) -> RealtimeMode:
    return cast(RealtimeMode, value)
