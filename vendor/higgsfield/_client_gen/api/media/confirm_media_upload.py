from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.confirm_media_upload_type import (
    ConfirmMediaUploadType,
)
from ...models.error import Error
from ...models.media_confirmation import MediaConfirmation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    media_id: UUID,
    *,
    type_: ConfirmMediaUploadType,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    params: dict[str, Any] = {}

    json_type_: str = type_
    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/developer/v2alpha/media/{media_id}/confirm".format(
            media_id=media_id,
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, MediaConfirmation]]:
    if response.status_code == 200:
        response_200 = MediaConfirmation.from_dict(response.json())

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
) -> Response[Union[Error, MediaConfirmation]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    media_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    type_: ConfirmMediaUploadType,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Response[Union[Error, MediaConfirmation]]:
    """Confirm a media upload

     Finalizes a previously created upload slot after the bytes have been PUT to its upload_url. The
    server validates the uploaded object, runs NSFW / IP safety checks (for image/video/audio), and
    flips the media to uploaded. Returns the media id and its resulting status. Rejected uploads (e.g.
    NSFW content, oversized or invalid images) surface as a 400.

    Args:
        media_id (UUID):
        type_ (ConfirmMediaUploadType):
        idempotency_key (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MediaConfirmation]]
    """

    kwargs = _get_kwargs(
        media_id=media_id,
        type_=type_,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    media_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    type_: ConfirmMediaUploadType,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Optional[Union[Error, MediaConfirmation]]:
    """Confirm a media upload

     Finalizes a previously created upload slot after the bytes have been PUT to its upload_url. The
    server validates the uploaded object, runs NSFW / IP safety checks (for image/video/audio), and
    flips the media to uploaded. Returns the media id and its resulting status. Rejected uploads (e.g.
    NSFW content, oversized or invalid images) surface as a 400.

    Args:
        media_id (UUID):
        type_ (ConfirmMediaUploadType):
        idempotency_key (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MediaConfirmation]
    """

    return sync_detailed(
        media_id=media_id,
        client=client,
        type_=type_,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    media_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    type_: ConfirmMediaUploadType,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Response[Union[Error, MediaConfirmation]]:
    """Confirm a media upload

     Finalizes a previously created upload slot after the bytes have been PUT to its upload_url. The
    server validates the uploaded object, runs NSFW / IP safety checks (for image/video/audio), and
    flips the media to uploaded. Returns the media id and its resulting status. Rejected uploads (e.g.
    NSFW content, oversized or invalid images) surface as a 400.

    Args:
        media_id (UUID):
        type_ (ConfirmMediaUploadType):
        idempotency_key (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MediaConfirmation]]
    """

    kwargs = _get_kwargs(
        media_id=media_id,
        type_=type_,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    media_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    type_: ConfirmMediaUploadType,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Optional[Union[Error, MediaConfirmation]]:
    """Confirm a media upload

     Finalizes a previously created upload slot after the bytes have been PUT to its upload_url. The
    server validates the uploaded object, runs NSFW / IP safety checks (for image/video/audio), and
    flips the media to uploaded. Returns the media id and its resulting status. Rejected uploads (e.g.
    NSFW content, oversized or invalid images) surface as a 400.

    Args:
        media_id (UUID):
        type_ (ConfirmMediaUploadType):
        idempotency_key (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MediaConfirmation]
    """

    return (
        await asyncio_detailed(
            media_id=media_id,
            client=client,
            type_=type_,
            idempotency_key=idempotency_key,
        )
    ).parsed
