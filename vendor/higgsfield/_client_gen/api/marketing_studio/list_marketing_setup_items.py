from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.list_marketing_setup_items_type import (
    ListMarketingSetupItemsType,
)
from ...models.marketing_setup_item_list import MarketingSetupItemList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: ListMarketingSetupItemsType,
    size: Union[Unset, int] = 20,
    cursor: Union[None, Unset, float] = UNSET,
    search: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_type_: str = type_
    params["type"] = json_type_

    params["size"] = size

    json_cursor: Union[None, Unset, float]
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    json_search: Union[None, Unset, str]
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/developer/v1alpha/marketing-studio/hooks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, MarketingSetupItemList]]:
    if response.status_code == 200:
        response_200 = MarketingSetupItemList.from_dict(response.json())

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
) -> Response[Union[Error, MarketingSetupItemList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: ListMarketingSetupItemsType,
    size: Union[Unset, int] = 20,
    cursor: Union[None, Unset, float] = UNSET,
    search: Union[None, Unset, str] = UNSET,
) -> Response[Union[Error, MarketingSetupItemList]]:
    """List hooks or settings

     List setup items used to seed marketing generation — hooks or settings, selected by type. The
    caller's custom items come first, paged by cursor (float epoch seconds); once they are exhausted
    (cursor is null) the cached preset catalog is appended.

    Args:
        type_ (ListMarketingSetupItemsType):
        size (Union[Unset, int]):  Default: 20.
        cursor (Union[None, Unset, float]):
        search (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MarketingSetupItemList]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        size=size,
        cursor=cursor,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: ListMarketingSetupItemsType,
    size: Union[Unset, int] = 20,
    cursor: Union[None, Unset, float] = UNSET,
    search: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Error, MarketingSetupItemList]]:
    """List hooks or settings

     List setup items used to seed marketing generation — hooks or settings, selected by type. The
    caller's custom items come first, paged by cursor (float epoch seconds); once they are exhausted
    (cursor is null) the cached preset catalog is appended.

    Args:
        type_ (ListMarketingSetupItemsType):
        size (Union[Unset, int]):  Default: 20.
        cursor (Union[None, Unset, float]):
        search (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MarketingSetupItemList]
    """

    return sync_detailed(
        client=client,
        type_=type_,
        size=size,
        cursor=cursor,
        search=search,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: ListMarketingSetupItemsType,
    size: Union[Unset, int] = 20,
    cursor: Union[None, Unset, float] = UNSET,
    search: Union[None, Unset, str] = UNSET,
) -> Response[Union[Error, MarketingSetupItemList]]:
    """List hooks or settings

     List setup items used to seed marketing generation — hooks or settings, selected by type. The
    caller's custom items come first, paged by cursor (float epoch seconds); once they are exhausted
    (cursor is null) the cached preset catalog is appended.

    Args:
        type_ (ListMarketingSetupItemsType):
        size (Union[Unset, int]):  Default: 20.
        cursor (Union[None, Unset, float]):
        search (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MarketingSetupItemList]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        size=size,
        cursor=cursor,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: ListMarketingSetupItemsType,
    size: Union[Unset, int] = 20,
    cursor: Union[None, Unset, float] = UNSET,
    search: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Error, MarketingSetupItemList]]:
    """List hooks or settings

     List setup items used to seed marketing generation — hooks or settings, selected by type. The
    caller's custom items come first, paged by cursor (float epoch seconds); once they are exhausted
    (cursor is null) the cached preset catalog is appended.

    Args:
        type_ (ListMarketingSetupItemsType):
        size (Union[Unset, int]):  Default: 20.
        cursor (Union[None, Unset, float]):
        search (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MarketingSetupItemList]
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            size=size,
            cursor=cursor,
            search=search,
        )
    ).parsed
