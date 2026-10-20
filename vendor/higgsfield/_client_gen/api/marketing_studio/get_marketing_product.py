from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.marketing_product import MarketingProduct
from ...types import Response


def _get_kwargs(
    product_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/developer/v1alpha/marketing-studio/products/{product_id}".format(
            product_id=product_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, MarketingProduct]]:
    if response.status_code == 200:
        response_200 = MarketingProduct.from_dict(response.json())

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
) -> Response[Union[Error, MarketingProduct]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, MarketingProduct]]:
    """Get a product

     Fetch a single product by id, including its images. Poll this after a URL fetch until status is
    completed.

    Args:
        product_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MarketingProduct]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, MarketingProduct]]:
    """Get a product

     Fetch a single product by id, including its images. Poll this after a URL fetch until status is
    completed.

    Args:
        product_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MarketingProduct]
    """

    return sync_detailed(
        product_id=product_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    product_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, MarketingProduct]]:
    """Get a product

     Fetch a single product by id, including its images. Poll this after a URL fetch until status is
    completed.

    Args:
        product_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MarketingProduct]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, MarketingProduct]]:
    """Get a product

     Fetch a single product by id, including its images. Poll this after a URL fetch until status is
    completed.

    Args:
        product_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MarketingProduct]
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
        )
    ).parsed
