from typing import Literal, cast

RealtimeResolution = Literal["1k", "2k"]

REALTIME_RESOLUTION_VALUES: set[RealtimeResolution] = {
    "1k",
    "2k",
}


def check_realtime_resolution(value: str) -> RealtimeResolution:
    return cast(RealtimeResolution, value)
