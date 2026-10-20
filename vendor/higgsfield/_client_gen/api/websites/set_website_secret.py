from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.website_secret_set_request import WebsiteSecretSetRequest
from ...models.website_secrets_response import WebsiteSecretsResponse
from ...types import Response


def _get_kwargs(
    website_id: UUID,
    *,
    body: WebsiteSecretSetRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/developer/v1alpha/websites/{website_id}/secrets".format(
            website_id=website_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, WebsiteSecretsResponse]]:
    if response.status_code == 200:
        response_200 = WebsiteSecretsResponse.from_dict(response.json())

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

    if 500 <= response.status_code <= 599:
        response_5xx = Error.from_dict(response.json())

        return response_5xx

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, WebsiteSecretsResponse]]:
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
    body: WebsiteSecretSetRequest,
) -> Response[Union[Error, WebsiteSecretsResponse]]:
    """Set a website secret

     Create or replace a secret (an environment variable like an API key). Staged: the value reaches the
    running site on its next deploy.

    Args:
        website_id (UUID):
        body (WebsiteSecretSetRequest): Create or replace one website secret (an environment
            variable).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, WebsiteSecretsResponse]]
    """

    kwargs = _get_kwargs(
        website_id=website_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    website_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: WebsiteSecretSetRequest,
) -> Optional[Union[Error, WebsiteSecretsResponse]]:
    """Set a website secret

     Create or replace a secret (an environment variable like an API key). Staged: the value reaches the
    running site on its next deploy.

    Args:
        website_id (UUID):
        body (WebsiteSecretSetRequest): Create or replace one website secret (an environment
            variable).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, WebsiteSecretsResponse]
    """

    return sync_detailed(
        website_id=website_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    website_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: WebsiteSecretSetRequest,
) -> Response[Union[Error, WebsiteSecretsResponse]]:
    """Set a website secret

     Create or replace a secret (an environment variable like an API key). Staged: the value reaches the
    running site on its next deploy.

    Args:
        website_id (UUID):
        body (WebsiteSecretSetRequest): Create or replace one website secret (an environment
            variable).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, WebsiteSecretsResponse]]
    """

    kwargs = _get_kwargs(
        website_id=website_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    website_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: WebsiteSecretSetRequest,
) -> Optional[Union[Error, WebsiteSecretsResponse]]:
    """Set a website secret

     Create or replace a secret (an environment variable like an API key). Staged: the value reaches the
    running site on its next deploy.

    Args:
        website_id (UUID):
        body (WebsiteSecretSetRequest): Create or replace one website secret (an environment
            variable).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, WebsiteSecretsResponse]
    """

    return (
        await asyncio_detailed(
            website_id=website_id,
            client=client,
            body=body,
        )
    ).parsed
