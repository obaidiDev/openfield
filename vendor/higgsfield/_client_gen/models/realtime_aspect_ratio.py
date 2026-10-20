from typing import Literal, cast

RealtimeAspectRatio = Literal[
    "16:9", "1:1", "1:2", "21:9", "2:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16"
]

REALTIME_ASPECT_RATIO_VALUES: set[RealtimeAspectRatio] = {
    "16:9",
    "1:1",
    "1:2",
    "21:9",
    "2:1",
    "2:3",
    "3:2",
    "3:4",
    "4:3",
    "4:5",
    "5:4",
    "9:16",
}


def check_realtime_aspect_ratio(value: str) -> RealtimeAspectRatio:
    return cast(RealtimeAspectRatio, value)
