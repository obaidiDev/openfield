"""The dynamic job-type catalog and per-job-type params schema."""

from __future__ import annotations

from typing import Optional, Sequence

from .._client_gen.models.model import Model
from .._client_gen.models.model_list_response import ModelListResponse
from .._transport import RequestOptions, Unpack, query
from ._base import Resource


class JobTypesResource(Resource):
    def list(
        self,
        *,
        type: Optional[str] = None,
        label: Optional[Sequence[str]] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        **options: Unpack[RequestOptions],
    ) -> ModelListResponse:
        """List the catalog of available job types. Each entry carries its
        ``job_type`` id (the value passed to ``create``), display name, media
        kind, and the JSON Schema for its accepted parameters.

        ``type`` filters by media kind (``image`` / ``video`` / ``audio`` /
        ``text`` / ``3d``); ``label`` (repeatable) by category (``model`` /
        ``chain`` / ``app``)."""
        data = self._get_json(
            "/developer/v2alpha/job_types",
            params=query(
                type=type, label=list(label) if label else None, limit=limit, cursor=cursor
            ),
            **options,
        )
        return ModelListResponse.from_dict(data)

    def get(self, job_type: str, **options: Unpack[RequestOptions]) -> Model:
        """Fetch a single job type by id, including the JSON Schema
        (``json_schema``) describing the parameters it accepts."""
        return Model.from_dict(
            self._get_json(f"/developer/v2alpha/job_types/{job_type}", **options)
        )
