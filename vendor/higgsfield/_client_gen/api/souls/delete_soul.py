from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_soul_response import DeleteSoulResponse
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    soul_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/developer/v2alpha/souls/{soul_id}".format(
            soul_id=soul_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DeleteSoulResponse, Error]]:
    if response.status_code == 200:
        response_200 = DeleteSoulResponse.from_dict(response.json())

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
) -> Response[Union[DeleteSoulResponse, Error]]:
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
) -> Response[Union[DeleteSoulResponse, Error]]:
    """Delete a Soul

     Deletes a Soul. A Soul that is still training cannot be deleted (returns 400).

    Args:
        soul_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteSoulResponse, Error]]
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
) -> Optional[Union[DeleteSoulResponse, Error]]:
    """Delete a Soul

     Deletes a Soul. A Soul that is still training cannot be deleted (returns 400).

    Args:
        soul_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteSoulResponse, Error]
    """

    return sync_detailed(
        soul_id=soul_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    soul_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[DeleteSoulResponse, Error]]:
    """Delete a Soul

     Deletes a Soul. A Soul that is still training cannot be deleted (returns 400).

    Args:
        soul_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteSoulResponse, Error]]
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
) -> Optional[Union[DeleteSoulResponse, Error]]:
    """Delete a Soul

     Deletes a Soul. A Soul that is still training cannot be deleted (returns 400).

    Args:
        soul_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteSoulResponse, Error]
    """

    return (
        await asyncio_detailed(
            soul_id=soul_id,
            client=client,
        )
    ).parsed
