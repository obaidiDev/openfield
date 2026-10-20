from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.website_status_response import WebsiteStatusResponse
from ...types import Response


def _get_kwargs(
    website_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/developer/v1alpha/websites/{website_id}".format(
            website_id=website_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, WebsiteStatusResponse]]:
    if response.status_code == 200:
        response_200 = WebsiteStatusResponse.from_dict(response.json())

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

    if 500 <= response.status_code <= 599:
        response_5xx = Error.from_dict(response.json())

        return response_5xx

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, WebsiteStatusResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    website_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, WebsiteStatusResponse]]:
    """Get website status

     Get the website's deploy status - the live URL and the status of the last deploy. The 'preview' slot
    is a deprecated alias that mirrors 'production'.

    Args:
        website_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, WebsiteStatusResponse]]
    """

    kwargs = _get_kwargs(
        website_id=website_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    website_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, WebsiteStatusResponse]]:
    """Get website status

     Get the website's deploy status - the live URL and the status of the last deploy. The 'preview' slot
    is a deprecated alias that mirrors 'production'.

    Args:
        website_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, WebsiteStatusResponse]
    """

    return sync_detailed(
        website_id=website_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    website_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, WebsiteStatusResponse]]:
    """Get website status

     Get the website's deploy status - the live URL and the status of the last deploy. The 'preview' slot
    is a deprecated alias that mirrors 'production'.

    Args:
        website_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, WebsiteStatusResponse]]
    """

    kwargs = _get_kwargs(
        website_id=website_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    website_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, WebsiteStatusResponse]]:
    """Get website status

     Get the website's deploy status - the live URL and the status of the last deploy. The 'preview' slot
    is a deprecated alias that mirrors 'production'.

    Args:
        website_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, WebsiteStatusResponse]
    """

    return (
        await asyncio_detailed(
            website_id=website_id,
            client=client,
        )
    ).parsed
