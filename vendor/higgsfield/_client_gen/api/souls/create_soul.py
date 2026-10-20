from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_soul_request import CreateSoulRequest
from ...models.error import Error
from ...models.soul import Soul
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateSoulRequest,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/developer/v2alpha/souls",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, Soul]]:
    if response.status_code == 200:
        response_200 = Soul.from_dict(response.json())

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
) -> Response[Union[Error, Soul]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateSoulRequest,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Response[Union[Error, Soul]]:
    """Train a new Soul

     Starts training a new Soul ID (soul-v2 custom reference) from a set of input images. Charges credits
    and kicks off an asynchronous 3-stage training run; the returned Soul starts in a non-terminal
    status (queued/in_progress). Poll getSoul until status becomes completed. Input images may reference
    library uploads (media_input) or prior generation results (e.g. image_job).

    Args:
        idempotency_key (Union[Unset, UUID]):
        body (CreateSoulRequest): Request to train a new Soul ID (soul-v2 custom reference).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Soul]]
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
    body: CreateSoulRequest,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Optional[Union[Error, Soul]]:
    """Train a new Soul

     Starts training a new Soul ID (soul-v2 custom reference) from a set of input images. Charges credits
    and kicks off an asynchronous 3-stage training run; the returned Soul starts in a non-terminal
    status (queued/in_progress). Poll getSoul until status becomes completed. Input images may reference
    library uploads (media_input) or prior generation results (e.g. image_job).

    Args:
        idempotency_key (Union[Unset, UUID]):
        body (CreateSoulRequest): Request to train a new Soul ID (soul-v2 custom reference).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, Soul]
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateSoulRequest,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Response[Union[Error, Soul]]:
    """Train a new Soul

     Starts training a new Soul ID (soul-v2 custom reference) from a set of input images. Charges credits
    and kicks off an asynchronous 3-stage training run; the returned Soul starts in a non-terminal
    status (queued/in_progress). Poll getSoul until status becomes completed. Input images may reference
    library uploads (media_input) or prior generation results (e.g. image_job).

    Args:
        idempotency_key (Union[Unset, UUID]):
        body (CreateSoulRequest): Request to train a new Soul ID (soul-v2 custom reference).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Soul]]
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
    body: CreateSoulRequest,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Optional[Union[Error, Soul]]:
    """Train a new Soul

     Starts training a new Soul ID (soul-v2 custom reference) from a set of input images. Charges credits
    and kicks off an asynchronous 3-stage training run; the returned Soul starts in a non-terminal
    status (queued/in_progress). Poll getSoul until status becomes completed. Input images may reference
    library uploads (media_input) or prior generation results (e.g. image_job).

    Args:
        idempotency_key (Union[Unset, UUID]):
        body (CreateSoulRequest): Request to train a new Soul ID (soul-v2 custom reference).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, Soul]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
