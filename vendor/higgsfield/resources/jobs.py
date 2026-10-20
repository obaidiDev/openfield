"""Jobs: fetch, list, and cost estimation."""

from __future__ import annotations

from typing import Any, Optional

from .._client_gen.models.cost_estimate import CostEstimate
from .._client_gen.models.job import Job
from .._client_gen.models.jobs_response import JobsResponse
from .._transport import RequestOptions, Unpack, query
from ._base import Resource
from .generation import generation_body


class JobsResource(Resource):
    def get(self, job_id: str, **options: Unpack[RequestOptions]) -> Job:
        """Fetch a single job by id, including its status and result URLs."""
        return Job.from_dict(self._get_json(f"/developer/v2alpha/jobs/{job_id}", **options))

    def list(
        self,
        *,
        type: Optional[str] = None,
        cursor: Optional[str] = None,
        size: Optional[int] = None,
        **options: Unpack[RequestOptions],
    ) -> JobsResponse:
        """List your jobs with cursor pagination."""
        data = self._get_json(
            "/developer/v2alpha/jobs",
            params=query(type=type, cursor=cursor, size=size),
            **options,
        )
        return JobsResponse.from_dict(data)

    def estimate_cost(
        self,
        *,
        job_type: str,
        params: dict[str, Any],
        pricing: Optional[Any] = None,
        meta: Optional[Any] = None,
        **options: Unpack[RequestOptions],
    ) -> CostEstimate:
        """Preview the credit cost of a generation without creating it. Takes the
        same ``job_type`` / ``params`` input as the ``create`` methods."""
        data = self._post_json(
            f"/developer/v2alpha/jobs/{job_type}/cost",
            json=generation_body(params, pricing, meta),
            **options,
        )
        return CostEstimate.from_dict(data)
