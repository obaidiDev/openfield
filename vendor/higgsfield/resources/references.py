"""Reference elements: reusable assets for the picker scope."""

from __future__ import annotations

from typing import Any, Optional, Sequence, Union

from .._client_gen.models.create_reference_element_request import CreateReferenceElementRequest
from .._client_gen.models.reference_element import ReferenceElement
from .._client_gen.models.reference_element_detail import ReferenceElementDetail
from .._client_gen.models.reference_element_list import ReferenceElementList
from .._transport import RequestOptions, Unpack, body_dict
from .._transport import query as _query  # aliased: `query` is also a filter param below
from ._base import Resource


class ReferencesResource(Resource):
    def list(
        self,
        *,
        folder_id: Optional[str] = None,
        include_subfolders: Optional[bool] = None,
        author_user_ids: Optional[Sequence[str]] = None,
        query: Optional[str] = None,
        category: Optional[str] = None,
        cursor: Optional[str] = None,
        size: Optional[int] = None,
        created_after: Optional[float] = None,
        created_before: Optional[float] = None,
        only_unpinned: Optional[bool] = None,
        only_pinned: Optional[bool] = None,
        sort_by: Optional[str] = None,
        order: Optional[str] = None,
        **options: Unpack[RequestOptions],
    ) -> ReferenceElementList:
        """List reference elements in the caller's picker scope, with cursor
        pagination. ``query`` is a text search; ``category`` filters by element
        type."""
        data = self._get_json(
            "/developer/v2alpha/reference-elements",
            params=_query(
                folder_id=folder_id,
                include_subfolders=include_subfolders,
                author_user_ids=list(author_user_ids) if author_user_ids else None,
                query=query,
                category=category,
                cursor=cursor,
                size=size,
                created_after=created_after,
                created_before=created_before,
                only_unpinned=only_unpinned,
                only_pinned=only_pinned,
                sort_by=sort_by,
                order=order,
            ),
            **options,
        )
        return ReferenceElementList.from_dict(data)

    def create(
        self,
        body: Union[CreateReferenceElementRequest, dict[str, Any]],
        **options: Unpack[RequestOptions],
    ) -> ReferenceElement:
        """Create a reusable reference element from one or more media assets."""
        data = self._post_json(
            "/developer/v2alpha/reference-elements", json=body_dict(body), **options
        )
        return ReferenceElement.from_dict(data)

    def get(self, element_id: str, **options: Unpack[RequestOptions]) -> ReferenceElementDetail:
        """Fetch a single reference element by id."""
        data = self._get_json(f"/developer/v2alpha/reference-elements/{element_id}", **options)
        return ReferenceElementDetail.from_dict(data)
