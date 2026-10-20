from typing import Literal, cast

JobStatus = Literal[
    "canceled",
    "completed",
    "dna",
    "failed",
    "flow",
    "in_progress",
    "ip_detected",
    "nsfw",
    "queued",
    "script",
    "vision",
    "visuals",
    "waiting",
]

JOB_STATUS_VALUES: set[JobStatus] = {
    "canceled",
    "completed",
    "dna",
    "failed",
    "flow",
    "in_progress",
    "ip_detected",
    "nsfw",
    "queued",
    "script",
    "vision",
    "visuals",
    "waiting",
}


def check_job_status(value: str) -> JobStatus:
    return cast(JobStatus, value)
