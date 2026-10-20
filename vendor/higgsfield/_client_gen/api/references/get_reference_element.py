from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.reference_element_detail import ReferenceElementDetail
from ...types import Response


def _get_kwargs(
    element_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/developer/v2alpha/reference-elements/{element_id}".format(
            element_id=element_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, ReferenceElementDetail]]:
    if response.status_code == 200:
        response_200 = ReferenceElementDetail.from_dict(response.json())

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
) -> Response[Union[Error, ReferenceElementDetail]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    element_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, ReferenceElementDetail]]:
    """Get a reference element

     Fetches a single reference element by id. The caller must own the element or have access to at least
    one folder it is currently linked to; otherwise the element responds as not found (existence is
    never leaked).

    Args:
        element_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ReferenceElementDetail]]
    """

    kwargs = _get_kwargs(
        element_id=element_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    element_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, ReferenceElementDetail]]:
    """Get a reference element

     Fetches a single reference element by id. The caller must own the element or have access to at least
    one folder it is currently linked to; otherwise the element responds as not found (existence is
    never leaked).

    Args:
        element_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ReferenceElementDetail]
    """

    return sync_detailed(
        element_id=element_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    element_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, ReferenceElementDetail]]:
    """Get a reference element

     Fetches a single reference element by id. The caller must own the element or have access to at least
    one folder it is currently linked to; otherwise the element responds as not found (existence is
    never leaked).

    Args:
        element_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ReferenceElementDetail]]
    """

    kwargs = _get_kwargs(
        element_id=element_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    element_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, ReferenceElementDetail]]:
    """Get a reference element

     Fetches a single reference element by id. The caller must own the element or have access to at least
    one folder it is currently linked to; otherwise the element responds as not found (existence is
    never leaked).

    Args:
        element_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ReferenceElementDetail]
    """

    return (
        await asyncio_detailed(
            element_id=element_id,
            client=client,
        )
    ).parsed
