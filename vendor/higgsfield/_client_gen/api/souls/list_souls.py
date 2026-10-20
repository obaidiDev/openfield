from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.list_souls_reference_type import (
    ListSoulsReferenceType,
)
from ...models.soul_list import SoulList
from ...models.soul_status import SoulStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    reference_type: Union[Unset, ListSoulsReferenceType] = "soul_2",
    status: Union[Unset, list[SoulStatus]] = UNSET,
    search: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = 10,
    cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_reference_type: Union[Unset, str] = UNSET
    if not isinstance(reference_type, Unset):
        json_reference_type = reference_type

    params["reference_type"] = json_reference_type

    json_status: Union[Unset, list[str]] = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item: str = status_item_data
            json_status.append(status_item)

    params["status"] = json_status

    params["search"] = search

    params["size"] = size

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/developer/v2alpha/souls",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, SoulList]]:
    if response.status_code == 200:
        response_200 = SoulList.from_dict(response.json())

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
) -> Response[Union[Error, SoulList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    reference_type: Union[Unset, ListSoulsReferenceType] = "soul_2",
    status: Union[Unset, list[SoulStatus]] = UNSET,
    search: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = 10,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[Error, SoulList]]:
    """List Souls

     Returns the caller's Souls of the requested reference type, newest first, with cursor-based
    pagination. Optionally filter by one or more training statuses, or by a free-text name search.

    Args:
        reference_type (Union[Unset, ListSoulsReferenceType]):  Default: 'soul_2'.
        status (Union[Unset, list[SoulStatus]]):
        search (Union[Unset, str]):
        size (Union[Unset, int]):  Default: 10.
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SoulList]]
    """

    kwargs = _get_kwargs(
        reference_type=reference_type,
        status=status,
        search=search,
        size=size,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    reference_type: Union[Unset, ListSoulsReferenceType] = "soul_2",
    status: Union[Unset, list[SoulStatus]] = UNSET,
    search: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = 10,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, SoulList]]:
    """List Souls

     Returns the caller's Souls of the requested reference type, newest first, with cursor-based
    pagination. Optionally filter by one or more training statuses, or by a free-text name search.

    Args:
        reference_type (Union[Unset, ListSoulsReferenceType]):  Default: 'soul_2'.
        status (Union[Unset, list[SoulStatus]]):
        search (Union[Unset, str]):
        size (Union[Unset, int]):  Default: 10.
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, SoulList]
    """

    return sync_detailed(
        client=client,
        reference_type=reference_type,
        status=status,
        search=search,
        size=size,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    reference_type: Union[Unset, ListSoulsReferenceType] = "soul_2",
    status: Union[Unset, list[SoulStatus]] = UNSET,
    search: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = 10,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[Error, SoulList]]:
    """List Souls

     Returns the caller's Souls of the requested reference type, newest first, with cursor-based
    pagination. Optionally filter by one or more training statuses, or by a free-text name search.

    Args:
        reference_type (Union[Unset, ListSoulsReferenceType]):  Default: 'soul_2'.
        status (Union[Unset, list[SoulStatus]]):
        search (Union[Unset, str]):
        size (Union[Unset, int]):  Default: 10.
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SoulList]]
    """

    kwargs = _get_kwargs(
        reference_type=reference_type,
        status=status,
        search=search,
        size=size,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    reference_type: Union[Unset, ListSoulsReferenceType] = "soul_2",
    status: Union[Unset, list[SoulStatus]] = UNSET,
    search: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = 10,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, SoulList]]:
    """List Souls

     Returns the caller's Souls of the requested reference type, newest first, with cursor-based
    pagination. Optionally filter by one or more training statuses, or by a free-text name search.

    Args:
        reference_type (Union[Unset, ListSoulsReferenceType]):  Default: 'soul_2'.
        status (Union[Unset, list[SoulStatus]]):
        search (Union[Unset, str]):
        size (Union[Unset, int]):  Default: 10.
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, SoulList]
    """

    return (
        await asyncio_detailed(
            client=client,
            reference_type=reference_type,
            status=status,
            search=search,
            size=size,
            cursor=cursor,
        )
    ).parsed
