from typing import Literal, cast

SoulStatus = Literal["completed", "failed", "in_progress", "queued", "showcase_completed"]

SOUL_STATUS_VALUES: set[SoulStatus] = {
    "completed",
    "failed",
    "in_progress",
    "queued",
    "showcase_completed",
}


def check_soul_status(value: str) -> SoulStatus:
    return cast(SoulStatus, value)
