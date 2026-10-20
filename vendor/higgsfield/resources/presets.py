"""Presets: the curated style catalog and the 3D rig animation library."""

from __future__ import annotations

from typing import Optional

from .._client_gen.models.animation_action_list_response import AnimationActionListResponse
from .._client_gen.models.preset_list_response import PresetListResponse
from .._transport import RequestOptions, Unpack, query
from ._base import Resource


class PresetsResource(Resource):
    def list(
        self, *, pinned: Optional[bool] = None, **options: Unpack[RequestOptions]
    ) -> PresetListResponse:
        """List the CMS preset/style catalog (the curated Soul styles). Set
        ``pinned`` to restrict to the caller's pinned presets."""
        data = self._get_json("/developer/v2alpha/presets", params=query(pinned=pinned), **options)
        return PresetListResponse.from_dict(data)

    def list_animation_actions(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        **options: Unpack[RequestOptions],
    ) -> AnimationActionListResponse:
        """List the baked 3D rig animation library used to resolve an
        ``animation_action_id`` for animated 3D generation."""
        data = self._get_json(
            "/developer/v2alpha/animation-actions",
            params=query(limit=limit, cursor=cursor),
            **options,
        )
        return AnimationActionListResponse.from_dict(data)
