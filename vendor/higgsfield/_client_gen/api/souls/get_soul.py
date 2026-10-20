from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.soul_detail import SoulDetail
from ...types import Response


def _get_kwargs(
    soul_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/developer/v2alpha/souls/{soul_id}".format(
            soul_id=soul_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, SoulDetail]]:
    if response.status_code == 200:
        response_200 = SoulDetail.from_dict(response.json())

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
) -> Response[Union[Error, SoulDetail]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    soul_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, SoulDetail]]:
    """Get a Soul

     Returns a single Soul, including its current training status. Poll this endpoint after createSoul
    until status is completed (or failed, in which case fail_reason may explain why).

    Args:
        soul_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SoulDetail]]
    """

    kwargs = _get_kwargs(
        soul_id=soul_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    soul_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, SoulDetail]]:
    """Get a Soul

     Returns a single Soul, including its current training status. Poll this endpoint after createSoul
    until status is completed (or failed, in which case fail_reason may explain why).

    Args:
        soul_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, SoulDetail]
    """

    return sync_detailed(
        soul_id=soul_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    soul_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, SoulDetail]]:
    """Get a Soul

     Returns a single Soul, including its current training status. Poll this endpoint after createSoul
    until status is completed (or failed, in which case fail_reason may explain why).

    Args:
        soul_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SoulDetail]]
    """

    kwargs = _get_kwargs(
        soul_id=soul_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    soul_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, SoulDetail]]:
    """Get a Soul

     Returns a single Soul, including its current training status. Poll this endpoint after createSoul
    until status is completed (or failed, in which case fail_reason may explain why).

    Args:
        soul_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, SoulDetail]
    """

    return (
        await asyncio_detailed(
            soul_id=soul_id,
            client=client,
        )
    ).parsed
