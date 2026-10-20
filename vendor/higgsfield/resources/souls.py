"""Souls: train and manage custom identity models."""

from __future__ import annotations

from typing import Any, Optional, Sequence, Union

from .._client_gen.models.create_soul_request import CreateSoulRequest
from .._client_gen.models.delete_soul_response import DeleteSoulResponse
from .._client_gen.models.soul import Soul
from .._client_gen.models.soul_detail import SoulDetail
from .._client_gen.models.soul_list import SoulList
from .._transport import RequestOptions, Unpack, body_dict, query
from ._base import Resource


class SoulsResource(Resource):
    def list(
        self,
        *,
        status: Optional[Sequence[str]] = None,
        search: Optional[str] = None,
        size: Optional[int] = None,
        cursor: Optional[str] = None,
        reference_type: Optional[str] = None,
        **options: Unpack[RequestOptions],
    ) -> SoulList:
        """List your Souls, newest first, with cursor pagination and optional
        status/name filters."""
        data = self._get_json(
            "/developer/v2alpha/souls",
            params=query(
                status=list(status) if status else None,
                search=search,
                size=size,
                cursor=cursor,
                reference_type=reference_type,
            ),
            **options,
        )
        return SoulList.from_dict(data)

    def create(
        self, body: Union[CreateSoulRequest, dict[str, Any]], **options: Unpack[RequestOptions]
    ) -> Soul:
        """Start training a new Soul from input images; charges credits and
        returns the Soul in a non-terminal status."""
        return Soul.from_dict(
            self._post_json("/developer/v2alpha/souls", json=body_dict(body), **options)
        )

    def get(self, soul_id: str, **options: Unpack[RequestOptions]) -> SoulDetail:
        """Fetch a single Soul by id, including its current training status."""
        return SoulDetail.from_dict(
            self._get_json(f"/developer/v2alpha/souls/{soul_id}", **options)
        )

    def delete(self, soul_id: str, **options: Unpack[RequestOptions]) -> DeleteSoulResponse:
        """Delete a Soul by id. A Soul that is still training cannot be deleted."""
        data = self._delete_json(f"/developer/v2alpha/souls/{soul_id}", **options)
        return DeleteSoulResponse.from_dict(data)
