from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_website_request import CreateWebsiteRequest
from ...models.error import Error
from ...models.website_create_response import WebsiteCreateResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateWebsiteRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/developer/v1alpha/websites",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, WebsiteCreateResponse]]:
    if response.status_code == 200:
        response_200 = WebsiteCreateResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

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
) -> Response[Union[Error, WebsiteCreateResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWebsiteRequest,
) -> Response[Union[Error, WebsiteCreateResponse]]:
    """Create a website

     Create a new full-stack website and its git repo from the standard template (React 19 + TanStack
    Start in one Cloudflare Worker, with D1/R2/KV/Durable Objects/Containers available, all off by
    default). Returns a website_id — pass it to every later website call.

    Args:
        body (CreateWebsiteRequest): Request to create a website.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, WebsiteCreateResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWebsiteRequest,
) -> Optional[Union[Error, WebsiteCreateResponse]]:
    """Create a website

     Create a new full-stack website and its git repo from the standard template (React 19 + TanStack
    Start in one Cloudflare Worker, with D1/R2/KV/Durable Objects/Containers available, all off by
    default). Returns a website_id — pass it to every later website call.

    Args:
        body (CreateWebsiteRequest): Request to create a website.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, WebsiteCreateResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWebsiteRequest,
) -> Response[Union[Error, WebsiteCreateResponse]]:
    """Create a website

     Create a new full-stack website and its git repo from the standard template (React 19 + TanStack
    Start in one Cloudflare Worker, with D1/R2/KV/Durable Objects/Containers available, all off by
    default). Returns a website_id — pass it to every later website call.

    Args:
        body (CreateWebsiteRequest): Request to create a website.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, WebsiteCreateResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWebsiteRequest,
) -> Optional[Union[Error, WebsiteCreateResponse]]:
    """Create a website

     Create a new full-stack website and its git repo from the standard template (React 19 + TanStack
    Start in one Cloudflare Worker, with D1/R2/KV/Durable Objects/Containers available, all off by
    default). Returns a website_id — pass it to every later website call.

    Args:
        body (CreateWebsiteRequest): Request to create a website.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, WebsiteCreateResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
