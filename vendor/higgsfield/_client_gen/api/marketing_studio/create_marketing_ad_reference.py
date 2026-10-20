from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.marketing_ad_reference import MarketingAdReference
from ...models.marketing_ad_reference_create_request import MarketingAdReferenceCreateRequest
from ...types import Response


def _get_kwargs(
    *,
    body: MarketingAdReferenceCreateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/developer/v1alpha/marketing-studio/ad-references",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, MarketingAdReference]]:
    if response.status_code == 200:
        response_200 = MarketingAdReference.from_dict(response.json())

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
) -> Response[Union[Error, MarketingAdReference]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: MarketingAdReferenceCreateRequest,
) -> Response[Union[Error, MarketingAdReference]]:
    """Create an ad reference

     Create an ad reference by cloning a source video into a reusable ad scenario. Provide exactly one
    source — source_url (a public URL), video_input_id (an uploaded video input), or job_id (a completed
    generation job whose result is a video). Optionally bind an avatar_id and product_id.

    Args:
        body (MarketingAdReferenceCreateRequest): Create an ad reference by cloning a source
            video. Provide exactly one source — source_url (a public video URL) or video (a flat media
            reference to an uploaded video input or a prior job's video result).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MarketingAdReference]]
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
    body: MarketingAdReferenceCreateRequest,
) -> Optional[Union[Error, MarketingAdReference]]:
    """Create an ad reference

     Create an ad reference by cloning a source video into a reusable ad scenario. Provide exactly one
    source — source_url (a public URL), video_input_id (an uploaded video input), or job_id (a completed
    generation job whose result is a video). Optionally bind an avatar_id and product_id.

    Args:
        body (MarketingAdReferenceCreateRequest): Create an ad reference by cloning a source
            video. Provide exactly one source — source_url (a public video URL) or video (a flat media
            reference to an uploaded video input or a prior job's video result).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MarketingAdReference]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: MarketingAdReferenceCreateRequest,
) -> Response[Union[Error, MarketingAdReference]]:
    """Create an ad reference

     Create an ad reference by cloning a source video into a reusable ad scenario. Provide exactly one
    source — source_url (a public URL), video_input_id (an uploaded video input), or job_id (a completed
    generation job whose result is a video). Optionally bind an avatar_id and product_id.

    Args:
        body (MarketingAdReferenceCreateRequest): Create an ad reference by cloning a source
            video. Provide exactly one source — source_url (a public video URL) or video (a flat media
            reference to an uploaded video input or a prior job's video result).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MarketingAdReference]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: MarketingAdReferenceCreateRequest,
) -> Optional[Union[Error, MarketingAdReference]]:
    """Create an ad reference

     Create an ad reference by cloning a source video into a reusable ad scenario. Provide exactly one
    source — source_url (a public URL), video_input_id (an uploaded video input), or job_id (a completed
    generation job whose result is a video). Optionally bind an avatar_id and product_id.

    Args:
        body (MarketingAdReferenceCreateRequest): Create an ad reference by cloning a source
            video. Provide exactly one source — source_url (a public video URL) or video (a flat media
            reference to an uploaded video input or a prior job's video result).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MarketingAdReference]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
