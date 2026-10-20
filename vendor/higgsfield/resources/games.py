"""Games: deploy and publish agent-built browser games."""

from __future__ import annotations

from typing import Any, Union

from .._client_gen.models.game_deploy_request import GameDeployRequest
from .._client_gen.models.game_deploy_response import GameDeployResponse
from .._client_gen.models.game_publish_request import GamePublishRequest
from .._client_gen.models.game_publish_response import GamePublishResponse
from .._transport import RequestOptions, Unpack, body_dict
from ._base import Resource


class GamesResource(Resource):
    def deploy(
        self, body: Union[GameDeployRequest, dict[str, Any]], **options: Unpack[RequestOptions]
    ) -> GameDeployResponse:
        """Deploy an agent-built browser game from an uploaded source archive and
        register it in the marketplace. Pass ``game_id`` to redeploy."""
        data = self._post_json("/developer/v1alpha/games/deploy", json=body_dict(body), **options)
        return GameDeployResponse.from_dict(data)

    def publish(
        self, body: Union[GamePublishRequest, dict[str, Any]], **options: Unpack[RequestOptions]
    ) -> GamePublishResponse:
        """List a previously deployed game on the marketplace, optionally
        overriding the catalog-card images and listing copy."""
        data = self._post_json("/developer/v1alpha/games/publish", json=body_dict(body), **options)
        return GamePublishResponse.from_dict(data)
