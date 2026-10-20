from typing import Literal, cast

VideoAnalysisStatus = Literal["completed", "failed", "in_progress", "queued"]

VIDEO_ANALYSIS_STATUS_VALUES: set[VideoAnalysisStatus] = {
    "completed",
    "failed",
    "in_progress",
    "queued",
}


def check_video_analysis_status(value: str) -> VideoAnalysisStatus:
    return cast(VideoAnalysisStatus, value)
