"""Realtime Flux Klein edit chains and saved custom styles."""

from __future__ import annotations

from typing import Any, Optional, Union

from .._client_gen.models.realtime_chain_cost_estimate import RealtimeChainCostEstimate
from .._client_gen.models.realtime_chain_cost_request import RealtimeChainCostRequest
from .._client_gen.models.realtime_chain_edit_request import RealtimeChainEditRequest
from .._client_gen.models.realtime_chain_edit_response import RealtimeChainEditResponse
from .._client_gen.models.realtime_chain_finalize_request import RealtimeChainFinalizeRequest
from .._client_gen.models.realtime_chain_finalize_response import RealtimeChainFinalizeResponse
from .._client_gen.models.realtime_custom_style import RealtimeCustomStyle
from .._client_gen.models.realtime_custom_style_create_request import (
    RealtimeCustomStyleCreateRequest,
)
from .._client_gen.models.realtime_custom_style_list import RealtimeCustomStyleList
from .._client_gen.models.realtime_custom_style_update_request import (
    RealtimeCustomStyleUpdateRequest,
)
from .._transport import RequestOptions, Unpack, body_dict, query
from ._base import Resource


class RealtimeResource(Resource):
    def edit_chain(
        self,
        body: Union[RealtimeChainEditRequest, dict[str, Any]],
        **options: Unpack[RequestOptions],
    ) -> RealtimeChainEditResponse:
        """Submit one realtime edit attempt."""
        data = self._post_json(
            "/developer/v2alpha/realtime/chain/edit", json=body_dict(body), **options
        )
        return RealtimeChainEditResponse.from_dict(data)

    def estimate_chain_cost(
        self,
        body: Union[RealtimeChainCostRequest, dict[str, Any]],
        **options: Unpack[RequestOptions],
    ) -> RealtimeChainCostEstimate:
        """Estimate one realtime edit without creating a job."""
        data = self._post_json(
            "/developer/v2alpha/realtime/chain/cost", json=body_dict(body), **options
        )
        return RealtimeChainCostEstimate.from_dict(data)

    def finalize_chain(
        self,
        body: Union[RealtimeChainFinalizeRequest, dict[str, Any]],
        **options: Unpack[RequestOptions],
    ) -> RealtimeChainFinalizeResponse:
        """Finalize a realtime edit chain and settle its reservation."""
        data = self._post_json(
            "/developer/v2alpha/realtime/chain/finalize", json=body_dict(body), **options
        )
        return RealtimeChainFinalizeResponse.from_dict(data)

    def list_custom_styles(
        self,
        *,
        size: Optional[int] = None,
        cursor: Optional[float] = None,
        **options: Unpack[RequestOptions],
    ) -> RealtimeCustomStyleList:
        """List saved realtime custom styles, newest updated first."""
        data = self._get_json(
            "/developer/v2alpha/realtime/custom-styles",
            params=query(size=size, cursor=cursor),
            **options,
        )
        return RealtimeCustomStyleList.from_dict(data)

    def create_custom_style(
        self,
        body: Union[RealtimeCustomStyleCreateRequest, dict[str, Any]],
        **options: Unpack[RequestOptions],
    ) -> RealtimeCustomStyle:
        """Save a reusable realtime custom style."""
        data = self._post_json(
            "/developer/v2alpha/realtime/custom-styles", json=body_dict(body), **options
        )
        return RealtimeCustomStyle.from_dict(data)

    def update_custom_style(
        self,
        style_id: str,
        body: Union[RealtimeCustomStyleUpdateRequest, dict[str, Any]],
        **options: Unpack[RequestOptions],
    ) -> RealtimeCustomStyle:
        """Update a saved realtime custom style."""
        data = self._patch_json(
            f"/developer/v2alpha/realtime/custom-styles/{style_id}",
            json=body_dict(body),
            **options,
        )
        return RealtimeCustomStyle.from_dict(data)

    def delete_custom_style(self, style_id: str, **options: Unpack[RequestOptions]) -> None:
        """Delete a saved realtime custom style."""
        self._delete(f"/developer/v2alpha/realtime/custom-styles/{style_id}", **options)
