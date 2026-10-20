from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.game_deploy_request import GameDeployRequest
from ...models.game_deploy_response import GameDeployResponse
from ...types import Response


def _get_kwargs(
    *,
    body: GameDeployRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/developer/v1alpha/games/deploy",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, GameDeployResponse]]:
    if response.status_code == 200:
        response_200 = GameDeployResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if 500 <= response.status_code <= 599:
        response_5xx = Error.from_dict(response.json())

        return response_5xx

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, GameDeployResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GameDeployRequest,
) -> Response[Union[Error, GameDeployResponse]]:
    """Deploy a game

     Deploy an agent-built browser game from an uploaded source archive. source_game is the https URL of
    the zipped build the agent previously uploaded (e.g. via the media upload flow); the server
    downloads it, injects a manifest with the display metadata, forwards it to the games backend, and
    registers the game in the marketplace. Pass game_id to redeploy over an existing game.

    Args:
        body (GameDeployRequest): Request to deploy an agent-built game from an uploaded source
            archive.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GameDeployResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GameDeployRequest,
) -> Optional[Union[Error, GameDeployResponse]]:
    """Deploy a game

     Deploy an agent-built browser game from an uploaded source archive. source_game is the https URL of
    the zipped build the agent previously uploaded (e.g. via the media upload flow); the server
    downloads it, injects a manifest with the display metadata, forwards it to the games backend, and
    registers the game in the marketplace. Pass game_id to redeploy over an existing game.

    Args:
        body (GameDeployRequest): Request to deploy an agent-built game from an uploaded source
            archive.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GameDeployResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GameDeployRequest,
) -> Response[Union[Error, GameDeployResponse]]:
    """Deploy a game

     Deploy an agent-built browser game from an uploaded source archive. source_game is the https URL of
    the zipped build the agent previously uploaded (e.g. via the media upload flow); the server
    downloads it, injects a manifest with the display metadata, forwards it to the games backend, and
    registers the game in the marketplace. Pass game_id to redeploy over an existing game.

    Args:
        body (GameDeployRequest): Request to deploy an agent-built game from an uploaded source
            archive.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GameDeployResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GameDeployRequest,
) -> Optional[Union[Error, GameDeployResponse]]:
    """Deploy a game

     Deploy an agent-built browser game from an uploaded source archive. source_game is the https URL of
    the zipped build the agent previously uploaded (e.g. via the media upload flow); the server
    downloads it, injects a manifest with the display metadata, forwards it to the games backend, and
    registers the game in the marketplace. Pass game_id to redeploy over an existing game.

    Args:
        body (GameDeployRequest): Request to deploy an agent-built game from an uploaded source
            archive.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GameDeployResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
