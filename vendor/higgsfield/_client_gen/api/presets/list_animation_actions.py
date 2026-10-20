from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.animation_action_list_response import AnimationActionListResponse
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = 50,
    cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/developer/v2alpha/animation-actions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AnimationActionListResponse, Error]]:
    if response.status_code == 200:
        response_200 = AnimationActionListResponse.from_dict(response.json())

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
) -> Response[Union[AnimationActionListResponse, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 50,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[AnimationActionListResponse, Error]]:
    """List animation actions

     List the baked 3D rig animation library used to resolve an animation_action_id for animated 3D
    generation (image_to_3d, multi_image_to_3d, 3d_rigging). Each action has a stable integer id that is
    passed back as the animation_action_id parameter. This catalog is static and not user-scoped.

    Args:
        limit (Union[Unset, int]):  Default: 50.
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AnimationActionListResponse, Error]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 50,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[AnimationActionListResponse, Error]]:
    """List animation actions

     List the baked 3D rig animation library used to resolve an animation_action_id for animated 3D
    generation (image_to_3d, multi_image_to_3d, 3d_rigging). Each action has a stable integer id that is
    passed back as the animation_action_id parameter. This catalog is static and not user-scoped.

    Args:
        limit (Union[Unset, int]):  Default: 50.
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AnimationActionListResponse, Error]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 50,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[AnimationActionListResponse, Error]]:
    """List animation actions

     List the baked 3D rig animation library used to resolve an animation_action_id for animated 3D
    generation (image_to_3d, multi_image_to_3d, 3d_rigging). Each action has a stable integer id that is
    passed back as the animation_action_id parameter. This catalog is static and not user-scoped.

    Args:
        limit (Union[Unset, int]):  Default: 50.
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AnimationActionListResponse, Error]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 50,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[AnimationActionListResponse, Error]]:
    """List animation actions

     List the baked 3D rig animation library used to resolve an animation_action_id for animated 3D
    generation (image_to_3d, multi_image_to_3d, 3d_rigging). Each action has a stable integer id that is
    passed back as the animation_action_id parameter. This catalog is static and not user-scoped.

    Args:
        limit (Union[Unset, int]):  Default: 50.
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AnimationActionListResponse, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
