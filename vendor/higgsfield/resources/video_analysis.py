"""Video analysis: scene-level analysis of uploaded or YouTube videos."""

from __future__ import annotations

from typing import Any, Optional, Union

from .._client_gen.models.create_video_analysis_request import CreateVideoAnalysisRequest
from .._client_gen.models.video_analysis import VideoAnalysis
from .._client_gen.models.video_analysis_list import VideoAnalysisList
from .._transport import RequestOptions, Unpack, body_dict, query
from ._base import Resource


class VideoAnalysisResource(Resource):
    def list(
        self,
        *,
        size: Optional[int] = None,
        cursor: Optional[str] = None,
        order: Optional[str] = None,
        **options: Unpack[RequestOptions],
    ) -> VideoAnalysisList:
        """List your video analyses for the active workspace with cursor pagination."""
        data = self._get_json(
            "/developer/v1alpha/video-analysis",
            params=query(size=size, cursor=cursor, order=order),
            **options,
        )
        return VideoAnalysisList.from_dict(data)

    def create(
        self,
        body: Union[CreateVideoAnalysisRequest, dict[str, Any]],
        **options: Unpack[RequestOptions],
    ) -> VideoAnalysis:
        """Submit a video for scene-level analysis. Provide exactly one source —
        ``video`` (an uploaded video reference) or ``youtube_url``. Poll
        :meth:`get` until ``status`` is ``completed``."""
        data = self._post_json("/developer/v1alpha/video-analysis", json=body_dict(body), **options)
        return VideoAnalysis.from_dict(data)

    def get(self, video_analyze_id: str, **options: Unpack[RequestOptions]) -> VideoAnalysis:
        """Fetch a single video analysis by id, including its status and scenes."""
        data = self._get_json(f"/developer/v1alpha/video-analysis/{video_analyze_id}", **options)
        return VideoAnalysis.from_dict(data)
