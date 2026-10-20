"""Image / video / audio / text / 3D / data generation.

All generation endpoints share one shape: a ``job_type`` id and its ``params``. Job
types are dynamic, so ``params`` is a loose dict — discover a job type's schema
at runtime with ``client.job_types.get(job_type).json_schema``; the server
validates on submit.
"""

from __future__ import annotations

from typing import Any, Optional

from .._client_gen.models.generation_job import GenerationJob
from .._transport import RequestOptions, Unpack, body_dict
from ._base import Resource


def generation_body(
    params: dict[str, Any],
    pricing: Optional[Any],
    meta: Optional[Any] = None,
    folder_id: Optional[str] = None,
) -> dict[str, Any]:
    """Build the shared ``{params, pricing?, meta?, folder_id?}`` generation body."""
    body: dict[str, Any] = {"params": params}
    if pricing is not None:
        body["pricing"] = body_dict(pricing)
    if meta is not None:
        body["meta"] = body_dict(meta)
    if folder_id is not None:
        body["folder_id"] = folder_id
    return body


class _GenerationResource(Resource):
    """Shared create flow: POST the generation body, decode the created job."""

    def _post_generation(
        self, url: str, body: dict[str, Any], **options: Unpack[RequestOptions]
    ) -> GenerationJob:
        return GenerationJob.from_dict(self._post_json(url, json=body, **options))


class ImagesResource(_GenerationResource):
    def create(
        self,
        *,
        job_type: str,
        params: dict[str, Any],
        pricing: Optional[Any] = None,
        meta: Optional[Any] = None,
        folder_id: Optional[str] = None,
        **options: Unpack[RequestOptions],
    ) -> GenerationJob:
        """Submit an image generation job. Returns the created :class:`GenerationJob`;
        poll it with ``client.wait_for_job``."""
        return self._post_generation(
            f"/developer/v2alpha/images/{job_type}/generations",
            generation_body(params, pricing, meta, folder_id),
            **options,
        )


class VideosResource(_GenerationResource):
    def create(
        self,
        *,
        job_type: str,
        params: dict[str, Any],
        pricing: Optional[Any] = None,
        meta: Optional[Any] = None,
        folder_id: Optional[str] = None,
        **options: Unpack[RequestOptions],
    ) -> GenerationJob:
        """Submit a video generation job. Returns the created :class:`GenerationJob`."""
        return self._post_generation(
            f"/developer/v2alpha/videos/{job_type}/generations",
            generation_body(params, pricing, meta, folder_id),
            **options,
        )


class AudiosResource(_GenerationResource):
    def create(
        self,
        *,
        job_type: str,
        params: dict[str, Any],
        pricing: Optional[Any] = None,
        meta: Optional[Any] = None,
        folder_id: Optional[str] = None,
        **options: Unpack[RequestOptions],
    ) -> GenerationJob:
        """Submit an audio generation job. Returns the created :class:`GenerationJob`."""
        return self._post_generation(
            f"/developer/v2alpha/audios/{job_type}/generations",
            generation_body(params, pricing, meta, folder_id),
            **options,
        )


class TextsResource(_GenerationResource):
    def create(
        self,
        *,
        job_type: str,
        params: dict[str, Any],
        pricing: Optional[Any] = None,
        meta: Optional[Any] = None,
        folder_id: Optional[str] = None,
        **options: Unpack[RequestOptions],
    ) -> GenerationJob:
        """Submit a text generation job. Returns the created :class:`GenerationJob`."""
        return self._post_generation(
            f"/developer/v2alpha/texts/{job_type}/generations",
            generation_body(params, pricing, meta, folder_id),
            **options,
        )


class Models3dResource(_GenerationResource):
    def create(
        self,
        *,
        job_type: str,
        params: dict[str, Any],
        pricing: Optional[Any] = None,
        meta: Optional[Any] = None,
        folder_id: Optional[str] = None,
        **options: Unpack[RequestOptions],
    ) -> GenerationJob:
        """Submit a 3D generation job. Returns the created :class:`GenerationJob`."""
        return self._post_generation(
            f"/developer/v2alpha/3d/{job_type}/generations",
            generation_body(params, pricing, meta, folder_id),
            **options,
        )


class DataResource(_GenerationResource):
    def create(
        self,
        *,
        job_type: str,
        params: dict[str, Any],
        pricing: Optional[Any] = None,
        meta: Optional[Any] = None,
        folder_id: Optional[str] = None,
        **options: Unpack[RequestOptions],
    ) -> GenerationJob:
        """Submit a structured-data generation job. Returns the created :class:`GenerationJob`."""
        return self._post_generation(
            f"/developer/v2alpha/data/{job_type}/generations",
            generation_body(params, pricing, meta, folder_id),
            **options,
        )
