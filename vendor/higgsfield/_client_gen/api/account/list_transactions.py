from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.transactions_response import TransactionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cursor: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = 10,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["size"] = size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/developer/v2alpha/account/transactions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, TransactionsResponse]]:
    if response.status_code == 200:
        response_200 = TransactionsResponse.from_dict(response.json())

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
) -> Response[Union[Error, TransactionsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    cursor: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = 10,
) -> Response[Union[Error, TransactionsResponse]]:
    """List credit transactions

     Cursor-paginated credit ledger history (newest first). Each entry is a grouped transaction: a credit
    amount (credits, a virtual unit), the action that produced it, and a display name. Pass the cursor
    from the previous page back as the cursor query parameter to fetch the next page; cursor is null on
    the last page.

    Args:
        cursor (Union[Unset, str]):
        size (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, TransactionsResponse]]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        size=size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    cursor: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = 10,
) -> Optional[Union[Error, TransactionsResponse]]:
    """List credit transactions

     Cursor-paginated credit ledger history (newest first). Each entry is a grouped transaction: a credit
    amount (credits, a virtual unit), the action that produced it, and a display name. Pass the cursor
    from the previous page back as the cursor query parameter to fetch the next page; cursor is null on
    the last page.

    Args:
        cursor (Union[Unset, str]):
        size (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, TransactionsResponse]
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        size=size,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    cursor: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = 10,
) -> Response[Union[Error, TransactionsResponse]]:
    """List credit transactions

     Cursor-paginated credit ledger history (newest first). Each entry is a grouped transaction: a credit
    amount (credits, a virtual unit), the action that produced it, and a display name. Pass the cursor
    from the previous page back as the cursor query parameter to fetch the next page; cursor is null on
    the last page.

    Args:
        cursor (Union[Unset, str]):
        size (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, TransactionsResponse]]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        size=size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    cursor: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = 10,
) -> Optional[Union[Error, TransactionsResponse]]:
    """List credit transactions

     Cursor-paginated credit ledger history (newest first). Each entry is a grouped transaction: a credit
    amount (credits, a virtual unit), the action that produced it, and a display name. Pass the cursor
    from the previous page back as the cursor query parameter to fetch the next page; cursor is null on
    the last page.

    Args:
        cursor (Union[Unset, str]):
        size (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, TransactionsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            size=size,
        )
    ).parsed
