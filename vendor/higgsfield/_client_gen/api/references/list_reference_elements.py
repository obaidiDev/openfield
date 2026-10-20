from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.list_reference_elements_order import (
    ListReferenceElementsOrder,
)
from ...models.list_reference_elements_sort_by import (
    ListReferenceElementsSortBy,
)
from ...models.reference_element_list import ReferenceElementList
from ...models.reference_element_type import ReferenceElementType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    folder_id: Union[Unset, UUID] = UNSET,
    include_subfolders: Union[Unset, bool] = False,
    author_user_ids: Union[Unset, list[str]] = UNSET,
    query: Union[Unset, str] = UNSET,
    category: Union[Unset, ReferenceElementType] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = 20,
    created_after: Union[Unset, float] = UNSET,
    created_before: Union[Unset, float] = UNSET,
    only_unpinned: Union[Unset, bool] = False,
    only_pinned: Union[Unset, bool] = False,
    sort_by: Union[Unset, ListReferenceElementsSortBy] = "created_at",
    order: Union[Unset, ListReferenceElementsOrder] = "desc",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_folder_id: Union[Unset, str] = UNSET
    if not isinstance(folder_id, Unset):
        json_folder_id = str(folder_id)
    params["folder_id"] = json_folder_id

    params["include_subfolders"] = include_subfolders

    json_author_user_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(author_user_ids, Unset):
        json_author_user_ids = author_user_ids

    params["author_user_ids"] = json_author_user_ids

    params["query"] = query

    json_category: Union[Unset, str] = UNSET
    if not isinstance(category, Unset):
        json_category = category

    params["category"] = json_category

    params["cursor"] = cursor

    params["size"] = size

    params["created_after"] = created_after

    params["created_before"] = created_before

    params["only_unpinned"] = only_unpinned

    params["only_pinned"] = only_pinned

    json_sort_by: Union[Unset, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by

    params["sort_by"] = json_sort_by

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/developer/v2alpha/reference-elements",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, ReferenceElementList]]:
    if response.status_code == 200:
        response_200 = ReferenceElementList.from_dict(response.json())

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
) -> Response[Union[Error, ReferenceElementList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    folder_id: Union[Unset, UUID] = UNSET,
    include_subfolders: Union[Unset, bool] = False,
    author_user_ids: Union[Unset, list[str]] = UNSET,
    query: Union[Unset, str] = UNSET,
    category: Union[Unset, ReferenceElementType] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = 20,
    created_after: Union[Unset, float] = UNSET,
    created_before: Union[Unset, float] = UNSET,
    only_unpinned: Union[Unset, bool] = False,
    only_pinned: Union[Unset, bool] = False,
    sort_by: Union[Unset, ListReferenceElementsSortBy] = "created_at",
    order: Union[Unset, ListReferenceElementsOrder] = "desc",
) -> Response[Union[Error, ReferenceElementList]]:
    """List reference elements

     Lists the reference elements visible in the caller's picker scope. With no folder_id the scope is
    the caller's personal + accessible-folder set; with folder_id set the scope is that folder
    (optionally including its subfolders). Supports filtering by author, free-text query, and category,
    plus created-at range bounds and sort controls. Cursor-paginated: pass the cursor returned by the
    previous page to fetch the next one.

    Args:
        folder_id (Union[Unset, UUID]):
        include_subfolders (Union[Unset, bool]):  Default: False.
        author_user_ids (Union[Unset, list[str]]):
        query (Union[Unset, str]):
        category (Union[Unset, ReferenceElementType]): Kind of a reference element. auto is an
            input-only request value that triggers server-side classification; the server then stores
            and returns one of the auto:* variants. The *_ip_verified variants are reserved for
            elements sourced from IP-verified soul jobs.
        cursor (Union[Unset, str]):
        size (Union[Unset, int]):  Default: 20.
        created_after (Union[Unset, float]):
        created_before (Union[Unset, float]):
        only_unpinned (Union[Unset, bool]):  Default: False.
        only_pinned (Union[Unset, bool]):  Default: False.
        sort_by (Union[Unset, ListReferenceElementsSortBy]):  Default: 'created_at'.
        order (Union[Unset, ListReferenceElementsOrder]):  Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ReferenceElementList]]
    """

    kwargs = _get_kwargs(
        folder_id=folder_id,
        include_subfolders=include_subfolders,
        author_user_ids=author_user_ids,
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
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    folder_id: Union[Unset, UUID] = UNSET,
    include_subfolders: Union[Unset, bool] = False,
    author_user_ids: Union[Unset, list[str]] = UNSET,
    query: Union[Unset, str] = UNSET,
    category: Union[Unset, ReferenceElementType] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = 20,
    created_after: Union[Unset, float] = UNSET,
    created_before: Union[Unset, float] = UNSET,
    only_unpinned: Union[Unset, bool] = False,
    only_pinned: Union[Unset, bool] = False,
    sort_by: Union[Unset, ListReferenceElementsSortBy] = "created_at",
    order: Union[Unset, ListReferenceElementsOrder] = "desc",
) -> Optional[Union[Error, ReferenceElementList]]:
    """List reference elements

     Lists the reference elements visible in the caller's picker scope. With no folder_id the scope is
    the caller's personal + accessible-folder set; with folder_id set the scope is that folder
    (optionally including its subfolders). Supports filtering by author, free-text query, and category,
    plus created-at range bounds and sort controls. Cursor-paginated: pass the cursor returned by the
    previous page to fetch the next one.

    Args:
        folder_id (Union[Unset, UUID]):
        include_subfolders (Union[Unset, bool]):  Default: False.
        author_user_ids (Union[Unset, list[str]]):
        query (Union[Unset, str]):
        category (Union[Unset, ReferenceElementType]): Kind of a reference element. auto is an
            input-only request value that triggers server-side classification; the server then stores
            and returns one of the auto:* variants. The *_ip_verified variants are reserved for
            elements sourced from IP-verified soul jobs.
        cursor (Union[Unset, str]):
        size (Union[Unset, int]):  Default: 20.
        created_after (Union[Unset, float]):
        created_before (Union[Unset, float]):
        only_unpinned (Union[Unset, bool]):  Default: False.
        only_pinned (Union[Unset, bool]):  Default: False.
        sort_by (Union[Unset, ListReferenceElementsSortBy]):  Default: 'created_at'.
        order (Union[Unset, ListReferenceElementsOrder]):  Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ReferenceElementList]
    """

    return sync_detailed(
        client=client,
        folder_id=folder_id,
        include_subfolders=include_subfolders,
        author_user_ids=author_user_ids,
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
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    folder_id: Union[Unset, UUID] = UNSET,
    include_subfolders: Union[Unset, bool] = False,
    author_user_ids: Union[Unset, list[str]] = UNSET,
    query: Union[Unset, str] = UNSET,
    category: Union[Unset, ReferenceElementType] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = 20,
    created_after: Union[Unset, float] = UNSET,
    created_before: Union[Unset, float] = UNSET,
    only_unpinned: Union[Unset, bool] = False,
    only_pinned: Union[Unset, bool] = False,
    sort_by: Union[Unset, ListReferenceElementsSortBy] = "created_at",
    order: Union[Unset, ListReferenceElementsOrder] = "desc",
) -> Response[Union[Error, ReferenceElementList]]:
    """List reference elements

     Lists the reference elements visible in the caller's picker scope. With no folder_id the scope is
    the caller's personal + accessible-folder set; with folder_id set the scope is that folder
    (optionally including its subfolders). Supports filtering by author, free-text query, and category,
    plus created-at range bounds and sort controls. Cursor-paginated: pass the cursor returned by the
    previous page to fetch the next one.

    Args:
        folder_id (Union[Unset, UUID]):
        include_subfolders (Union[Unset, bool]):  Default: False.
        author_user_ids (Union[Unset, list[str]]):
        query (Union[Unset, str]):
        category (Union[Unset, ReferenceElementType]): Kind of a reference element. auto is an
            input-only request value that triggers server-side classification; the server then stores
            and returns one of the auto:* variants. The *_ip_verified variants are reserved for
            elements sourced from IP-verified soul jobs.
        cursor (Union[Unset, str]):
        size (Union[Unset, int]):  Default: 20.
        created_after (Union[Unset, float]):
        created_before (Union[Unset, float]):
        only_unpinned (Union[Unset, bool]):  Default: False.
        only_pinned (Union[Unset, bool]):  Default: False.
        sort_by (Union[Unset, ListReferenceElementsSortBy]):  Default: 'created_at'.
        order (Union[Unset, ListReferenceElementsOrder]):  Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ReferenceElementList]]
    """

    kwargs = _get_kwargs(
        folder_id=folder_id,
        include_subfolders=include_subfolders,
        author_user_ids=author_user_ids,
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
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    folder_id: Union[Unset, UUID] = UNSET,
    include_subfolders: Union[Unset, bool] = False,
    author_user_ids: Union[Unset, list[str]] = UNSET,
    query: Union[Unset, str] = UNSET,
    category: Union[Unset, ReferenceElementType] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = 20,
    created_after: Union[Unset, float] = UNSET,
    created_before: Union[Unset, float] = UNSET,
    only_unpinned: Union[Unset, bool] = False,
    only_pinned: Union[Unset, bool] = False,
    sort_by: Union[Unset, ListReferenceElementsSortBy] = "created_at",
    order: Union[Unset, ListReferenceElementsOrder] = "desc",
) -> Optional[Union[Error, ReferenceElementList]]:
    """List reference elements

     Lists the reference elements visible in the caller's picker scope. With no folder_id the scope is
    the caller's personal + accessible-folder set; with folder_id set the scope is that folder
    (optionally including its subfolders). Supports filtering by author, free-text query, and category,
    plus created-at range bounds and sort controls. Cursor-paginated: pass the cursor returned by the
    previous page to fetch the next one.

    Args:
        folder_id (Union[Unset, UUID]):
        include_subfolders (Union[Unset, bool]):  Default: False.
        author_user_ids (Union[Unset, list[str]]):
        query (Union[Unset, str]):
        category (Union[Unset, ReferenceElementType]): Kind of a reference element. auto is an
            input-only request value that triggers server-side classification; the server then stores
            and returns one of the auto:* variants. The *_ip_verified variants are reserved for
            elements sourced from IP-verified soul jobs.
        cursor (Union[Unset, str]):
        size (Union[Unset, int]):  Default: 20.
        created_after (Union[Unset, float]):
        created_before (Union[Unset, float]):
        only_unpinned (Union[Unset, bool]):  Default: False.
        only_pinned (Union[Unset, bool]):  Default: False.
        sort_by (Union[Unset, ListReferenceElementsSortBy]):  Default: 'created_at'.
        order (Union[Unset, ListReferenceElementsOrder]):  Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ReferenceElementList]
    """

    return (
        await asyncio_detailed(
            client=client,
            folder_id=folder_id,
            include_subfolders=include_subfolders,
            author_user_ids=author_user_ids,
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
        )
    ).parsed
