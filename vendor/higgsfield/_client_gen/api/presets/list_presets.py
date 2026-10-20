from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.preset_list_response import PresetListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pinned: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["pinned"] = pinned

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/developer/v2alpha/presets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, PresetListResponse]]:
    if response.status_code == 200:
        response_200 = PresetListResponse.from_dict(response.json())

        return response_200

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
) -> Response[Union[Error, PresetListResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    pinned: Union[Unset, bool] = UNSET,
) -> Response[Union[Error, PresetListResponse]]:
    """List presets

     List the CMS preset/style catalog (the curated Soul styles). Returned as a full list. Optionally
    restrict to the caller's pinned presets; pinned ordering is applied for an authenticated caller.

    Args:
        pinned (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PresetListResponse]]
    """

    kwargs = _get_kwargs(
        pinned=pinned,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    pinned: Union[Unset, bool] = UNSET,
) -> Optional[Union[Error, PresetListResponse]]:
    """List presets

     List the CMS preset/style catalog (the curated Soul styles). Returned as a full list. Optionally
    restrict to the caller's pinned presets; pinned ordering is applied for an authenticated caller.

    Args:
        pinned (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PresetListResponse]
    """

    return sync_detailed(
        client=client,
        pinned=pinned,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    pinned: Union[Unset, bool] = UNSET,
) -> Response[Union[Error, PresetListResponse]]:
    """List presets

     List the CMS preset/style catalog (the curated Soul styles). Returned as a full list. Optionally
    restrict to the caller's pinned presets; pinned ordering is applied for an authenticated caller.

    Args:
        pinned (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PresetListResponse]]
    """

    kwargs = _get_kwargs(
        pinned=pinned,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    pinned: Union[Unset, bool] = UNSET,
) -> Optional[Union[Error, PresetListResponse]]:
    """List presets

     List the CMS preset/style catalog (the curated Soul styles). Returned as a full list. Optionally
    restrict to the caller's pinned presets; pinned ordering is applied for an authenticated caller.

    Args:
        pinned (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PresetListResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            pinned=pinned,
        )
    ).parsed
