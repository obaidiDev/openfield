from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.repo_access_response import RepoAccessResponse
from ...types import Response


def _get_kwargs(
    website_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/developer/v1alpha/websites/{website_id}/repo-access".format(
            website_id=website_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, RepoAccessResponse]]:
    if response.status_code == 200:
        response_200 = RepoAccessResponse.from_dict(response.json())

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
) -> Response[Union[Error, RepoAccessResponse]]:
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
) -> Response[Union[Error, RepoAccessResponse]]:
    """Get website repo access

     Get direct git access to the website's repo: the clone URL, branch, slug, and a scoped token (the
    owner's per-user Forgejo credentials). Clone, edit, commit and push the source yourself, then
    deploy. Do not echo the token back to the user.

    Args:
        website_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, RepoAccessResponse]]
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
) -> Optional[Union[Error, RepoAccessResponse]]:
    """Get website repo access

     Get direct git access to the website's repo: the clone URL, branch, slug, and a scoped token (the
    owner's per-user Forgejo credentials). Clone, edit, commit and push the source yourself, then
    deploy. Do not echo the token back to the user.

    Args:
        website_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, RepoAccessResponse]
    """

    return sync_detailed(
        website_id=website_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    website_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, RepoAccessResponse]]:
    """Get website repo access

     Get direct git access to the website's repo: the clone URL, branch, slug, and a scoped token (the
    owner's per-user Forgejo credentials). Clone, edit, commit and push the source yourself, then
    deploy. Do not echo the token back to the user.

    Args:
        website_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, RepoAccessResponse]]
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
) -> Optional[Union[Error, RepoAccessResponse]]:
    """Get website repo access

     Get direct git access to the website's repo: the clone URL, branch, slug, and a scoped token (the
    owner's per-user Forgejo credentials). Clone, edit, commit and push the source yourself, then
    deploy. Do not echo the token back to the user.

    Args:
        website_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, RepoAccessResponse]
    """

    return (
        await asyncio_detailed(
            website_id=website_id,
            client=client,
        )
    ).parsed
