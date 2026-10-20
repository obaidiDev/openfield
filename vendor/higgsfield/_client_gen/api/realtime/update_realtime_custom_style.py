from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.realtime_custom_style import RealtimeCustomStyle
from ...models.realtime_custom_style_update_request import RealtimeCustomStyleUpdateRequest
from ...types import Response


def _get_kwargs(
    style_id: UUID,
    *,
    body: RealtimeCustomStyleUpdateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/developer/v2alpha/realtime/custom-styles/{style_id}".format(
            style_id=style_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, RealtimeCustomStyle]]:
    if response.status_code == 200:
        response_200 = RealtimeCustomStyle.from_dict(response.json())

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
) -> Response[Union[Error, RealtimeCustomStyle]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    style_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RealtimeCustomStyleUpdateRequest,
) -> Response[Union[Error, RealtimeCustomStyle]]:
    """Update a realtime custom style

     Update a saved realtime custom style. Set clear_reference to true to remove the reference image.

    Args:
        style_id (UUID):
        body (RealtimeCustomStyleUpdateRequest): Request to update a realtime custom style.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, RealtimeCustomStyle]]
    """

    kwargs = _get_kwargs(
        style_id=style_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    style_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RealtimeCustomStyleUpdateRequest,
) -> Optional[Union[Error, RealtimeCustomStyle]]:
    """Update a realtime custom style

     Update a saved realtime custom style. Set clear_reference to true to remove the reference image.

    Args:
        style_id (UUID):
        body (RealtimeCustomStyleUpdateRequest): Request to update a realtime custom style.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, RealtimeCustomStyle]
    """

    return sync_detailed(
        style_id=style_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    style_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RealtimeCustomStyleUpdateRequest,
) -> Response[Union[Error, RealtimeCustomStyle]]:
    """Update a realtime custom style

     Update a saved realtime custom style. Set clear_reference to true to remove the reference image.

    Args:
        style_id (UUID):
        body (RealtimeCustomStyleUpdateRequest): Request to update a realtime custom style.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, RealtimeCustomStyle]]
    """

    kwargs = _get_kwargs(
        style_id=style_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    style_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RealtimeCustomStyleUpdateRequest,
) -> Optional[Union[Error, RealtimeCustomStyle]]:
    """Update a realtime custom style

     Update a saved realtime custom style. Set clear_reference to true to remove the reference image.

    Args:
        style_id (UUID):
        body (RealtimeCustomStyleUpdateRequest): Request to update a realtime custom style.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, RealtimeCustomStyle]
    """

    return (
        await asyncio_detailed(
            style_id=style_id,
            client=client,
            body=body,
        )
    ).parsed
