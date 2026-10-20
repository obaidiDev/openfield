from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_reference_element_request import CreateReferenceElementRequest
from ...models.error import Error
from ...models.reference_element import ReferenceElement
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateReferenceElementRequest,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/developer/v2alpha/reference-elements",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, ReferenceElement]]:
    if response.status_code == 200:
        response_200 = ReferenceElement.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409

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
) -> Response[Union[Error, ReferenceElement]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateReferenceElementRequest,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Response[Union[Error, ReferenceElement]]:
    """Create a reference element

     Creates a reusable reference element from one or more media assets. The category selects the element
    kind; passing the auto value triggers server-side vision classification of the (first up to 3)
    images into character, environment, or prop (returned as the auto:* variants). When name is omitted
    it is auto-derived from the source job of the first media (falling back to a generic name). Spaces
    in name are replaced with hyphens. The created element starts in processing and is immediately set
    to completed for non-voice elements.

    Args:
        idempotency_key (Union[Unset, UUID]):
        body (CreateReferenceElementRequest): Payload to create a reference element.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ReferenceElement]]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateReferenceElementRequest,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Optional[Union[Error, ReferenceElement]]:
    """Create a reference element

     Creates a reusable reference element from one or more media assets. The category selects the element
    kind; passing the auto value triggers server-side vision classification of the (first up to 3)
    images into character, environment, or prop (returned as the auto:* variants). When name is omitted
    it is auto-derived from the source job of the first media (falling back to a generic name). Spaces
    in name are replaced with hyphens. The created element starts in processing and is immediately set
    to completed for non-voice elements.

    Args:
        idempotency_key (Union[Unset, UUID]):
        body (CreateReferenceElementRequest): Payload to create a reference element.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ReferenceElement]
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateReferenceElementRequest,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Response[Union[Error, ReferenceElement]]:
    """Create a reference element

     Creates a reusable reference element from one or more media assets. The category selects the element
    kind; passing the auto value triggers server-side vision classification of the (first up to 3)
    images into character, environment, or prop (returned as the auto:* variants). When name is omitted
    it is auto-derived from the source job of the first media (falling back to a generic name). Spaces
    in name are replaced with hyphens. The created element starts in processing and is immediately set
    to completed for non-voice elements.

    Args:
        idempotency_key (Union[Unset, UUID]):
        body (CreateReferenceElementRequest): Payload to create a reference element.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ReferenceElement]]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateReferenceElementRequest,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Optional[Union[Error, ReferenceElement]]:
    """Create a reference element

     Creates a reusable reference element from one or more media assets. The category selects the element
    kind; passing the auto value triggers server-side vision classification of the (first up to 3)
    images into character, environment, or prop (returned as the auto:* variants). When name is omitted
    it is auto-derived from the source job of the first media (falling back to a generic name). Spaces
    in name are replaced with hyphens. The created element starts in processing and is immediately set
    to completed for non-voice elements.

    Args:
        idempotency_key (Union[Unset, UUID]):
        body (CreateReferenceElementRequest): Payload to create a reference element.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ReferenceElement]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
