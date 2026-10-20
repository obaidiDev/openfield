from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_media_upload_type import CreateMediaUploadType
from ...models.error import Error
from ...models.media_upload_slot import MediaUploadSlot
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: CreateMediaUploadType,
    extension: Union[Unset, str] = UNSET,
    chat_id: Union[Unset, UUID] = UNSET,
    filename: Union[Unset, str] = UNSET,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    params: dict[str, Any] = {}

    json_type_: str = type_
    params["type"] = json_type_

    params["extension"] = extension

    json_chat_id: Union[Unset, str] = UNSET
    if not isinstance(chat_id, Unset):
        json_chat_id = str(chat_id)
    params["chat_id"] = json_chat_id

    params["filename"] = filename

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/developer/v2alpha/media",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, MediaUploadSlot]]:
    if response.status_code == 200:
        response_200 = MediaUploadSlot.from_dict(response.json())

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
) -> Response[Union[Error, MediaUploadSlot]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: CreateMediaUploadType,
    extension: Union[Unset, str] = UNSET,
    chat_id: Union[Unset, UUID] = UNSET,
    filename: Union[Unset, str] = UNSET,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Response[Union[Error, MediaUploadSlot]]:
    """Create a media upload slot

     Mints a media slot for a presigned-PUT upload. Returns the created media id, the permanent public
    CloudFront url the media will be served from, a short-lived presigned S3 upload_url, and the
    required content_type. The client must PUT the raw bytes directly to upload_url (a direct S3 call,
    outside this API) with the Content-Type header set exactly to content_type, then call
    confirmMediaUpload to finalize. The media kind is selected by the type query parameter; for file an
    extension is required so the correct content-type can be applied.

    Args:
        type_ (CreateMediaUploadType):
        extension (Union[Unset, str]):
        chat_id (Union[Unset, UUID]):
        filename (Union[Unset, str]):
        idempotency_key (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MediaUploadSlot]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        extension=extension,
        chat_id=chat_id,
        filename=filename,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: CreateMediaUploadType,
    extension: Union[Unset, str] = UNSET,
    chat_id: Union[Unset, UUID] = UNSET,
    filename: Union[Unset, str] = UNSET,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Optional[Union[Error, MediaUploadSlot]]:
    """Create a media upload slot

     Mints a media slot for a presigned-PUT upload. Returns the created media id, the permanent public
    CloudFront url the media will be served from, a short-lived presigned S3 upload_url, and the
    required content_type. The client must PUT the raw bytes directly to upload_url (a direct S3 call,
    outside this API) with the Content-Type header set exactly to content_type, then call
    confirmMediaUpload to finalize. The media kind is selected by the type query parameter; for file an
    extension is required so the correct content-type can be applied.

    Args:
        type_ (CreateMediaUploadType):
        extension (Union[Unset, str]):
        chat_id (Union[Unset, UUID]):
        filename (Union[Unset, str]):
        idempotency_key (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MediaUploadSlot]
    """

    return sync_detailed(
        client=client,
        type_=type_,
        extension=extension,
        chat_id=chat_id,
        filename=filename,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: CreateMediaUploadType,
    extension: Union[Unset, str] = UNSET,
    chat_id: Union[Unset, UUID] = UNSET,
    filename: Union[Unset, str] = UNSET,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Response[Union[Error, MediaUploadSlot]]:
    """Create a media upload slot

     Mints a media slot for a presigned-PUT upload. Returns the created media id, the permanent public
    CloudFront url the media will be served from, a short-lived presigned S3 upload_url, and the
    required content_type. The client must PUT the raw bytes directly to upload_url (a direct S3 call,
    outside this API) with the Content-Type header set exactly to content_type, then call
    confirmMediaUpload to finalize. The media kind is selected by the type query parameter; for file an
    extension is required so the correct content-type can be applied.

    Args:
        type_ (CreateMediaUploadType):
        extension (Union[Unset, str]):
        chat_id (Union[Unset, UUID]):
        filename (Union[Unset, str]):
        idempotency_key (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MediaUploadSlot]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        extension=extension,
        chat_id=chat_id,
        filename=filename,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: CreateMediaUploadType,
    extension: Union[Unset, str] = UNSET,
    chat_id: Union[Unset, UUID] = UNSET,
    filename: Union[Unset, str] = UNSET,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Optional[Union[Error, MediaUploadSlot]]:
    """Create a media upload slot

     Mints a media slot for a presigned-PUT upload. Returns the created media id, the permanent public
    CloudFront url the media will be served from, a short-lived presigned S3 upload_url, and the
    required content_type. The client must PUT the raw bytes directly to upload_url (a direct S3 call,
    outside this API) with the Content-Type header set exactly to content_type, then call
    confirmMediaUpload to finalize. The media kind is selected by the type query parameter; for file an
    extension is required so the correct content-type can be applied.

    Args:
        type_ (CreateMediaUploadType):
        extension (Union[Unset, str]):
        chat_id (Union[Unset, UUID]):
        filename (Union[Unset, str]):
        idempotency_key (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MediaUploadSlot]
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            extension=extension,
            chat_id=chat_id,
            filename=filename,
            idempotency_key=idempotency_key,
        )
    ).parsed
