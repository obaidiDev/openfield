from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.marketing_brand_kit import MarketingBrandKit
from ...models.marketing_brand_kit_data import MarketingBrandKitData
from ...types import Response


def _get_kwargs(
    brand_kit_id: UUID,
    *,
    body: MarketingBrandKitData,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/developer/v1alpha/marketing-studio/brand-kits/{brand_kit_id}".format(
            brand_kit_id=brand_kit_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, MarketingBrandKit]]:
    if response.status_code == 200:
        response_200 = MarketingBrandKit.from_dict(response.json())

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
) -> Response[Union[Error, MarketingBrandKit]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    brand_kit_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: MarketingBrandKitData,
) -> Response[Union[Error, MarketingBrandKit]]:
    """Update a brand kit

     Partially update a brand kit's brand-identity data. Only the fields supplied override the stored
    data; omitted fields are preserved (a full payload still replaces everything). Unknown extra fields
    are preserved.

    Args:
        brand_kit_id (UUID):
        body (MarketingBrandKitData): A brand's identity data. All fields are optional and unknown
            extra fields are preserved. Used both as a brand kit's data and as the create/update
            request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MarketingBrandKit]]
    """

    kwargs = _get_kwargs(
        brand_kit_id=brand_kit_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    brand_kit_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: MarketingBrandKitData,
) -> Optional[Union[Error, MarketingBrandKit]]:
    """Update a brand kit

     Partially update a brand kit's brand-identity data. Only the fields supplied override the stored
    data; omitted fields are preserved (a full payload still replaces everything). Unknown extra fields
    are preserved.

    Args:
        brand_kit_id (UUID):
        body (MarketingBrandKitData): A brand's identity data. All fields are optional and unknown
            extra fields are preserved. Used both as a brand kit's data and as the create/update
            request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MarketingBrandKit]
    """

    return sync_detailed(
        brand_kit_id=brand_kit_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    brand_kit_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: MarketingBrandKitData,
) -> Response[Union[Error, MarketingBrandKit]]:
    """Update a brand kit

     Partially update a brand kit's brand-identity data. Only the fields supplied override the stored
    data; omitted fields are preserved (a full payload still replaces everything). Unknown extra fields
    are preserved.

    Args:
        brand_kit_id (UUID):
        body (MarketingBrandKitData): A brand's identity data. All fields are optional and unknown
            extra fields are preserved. Used both as a brand kit's data and as the create/update
            request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MarketingBrandKit]]
    """

    kwargs = _get_kwargs(
        brand_kit_id=brand_kit_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    brand_kit_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: MarketingBrandKitData,
) -> Optional[Union[Error, MarketingBrandKit]]:
    """Update a brand kit

     Partially update a brand kit's brand-identity data. Only the fields supplied override the stored
    data; omitted fields are preserved (a full payload still replaces everything). Unknown extra fields
    are preserved.

    Args:
        brand_kit_id (UUID):
        body (MarketingBrandKitData): A brand's identity data. All fields are optional and unknown
            extra fields are preserved. Used both as a brand kit's data and as the create/update
            request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MarketingBrandKit]
    """

    return (
        await asyncio_detailed(
            brand_kit_id=brand_kit_id,
            client=client,
            body=body,
        )
    ).parsed
