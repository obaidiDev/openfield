from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audio_model_choice import AudioModelChoice
from ...models.error import Error
from ...models.generation_job import GenerationJob
from ...types import UNSET, Response, Unset


def _get_kwargs(
    job_type: str,
    *,
    body: AudioModelChoice,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/developer/v2alpha/audios/{job_type}/generations".format(
            job_type=job_type,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, GenerationJob]]:
    if response.status_code == 200:
        response_200 = GenerationJob.from_dict(response.json())

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
) -> Response[Union[Error, GenerationJob]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AudioModelChoice,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Response[Union[Error, GenerationJob]]:
    """Create an audio generation

     Submit an audio generation job. The audio model is the {job_type} path parameter. The request body
    is the matching AudioModelChoice variant — the model's typed params under params, with an optional
    top-level pricing. Returns the created job.

    Args:
        job_type (str):
        idempotency_key (Union[Unset, UUID]):
        body (AudioModelChoice): Request body for POST
            /developer/v2alpha/audios/{job_type}/generations. Carries the model params under params,
            with an optional top-level pricing. The accepted params fields depend on the {job_type}
            selected in the path.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GenerationJob]]
    """

    kwargs = _get_kwargs(
        job_type=job_type,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AudioModelChoice,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Optional[Union[Error, GenerationJob]]:
    """Create an audio generation

     Submit an audio generation job. The audio model is the {job_type} path parameter. The request body
    is the matching AudioModelChoice variant — the model's typed params under params, with an optional
    top-level pricing. Returns the created job.

    Args:
        job_type (str):
        idempotency_key (Union[Unset, UUID]):
        body (AudioModelChoice): Request body for POST
            /developer/v2alpha/audios/{job_type}/generations. Carries the model params under params,
            with an optional top-level pricing. The accepted params fields depend on the {job_type}
            selected in the path.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GenerationJob]
    """

    return sync_detailed(
        job_type=job_type,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    job_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AudioModelChoice,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Response[Union[Error, GenerationJob]]:
    """Create an audio generation

     Submit an audio generation job. The audio model is the {job_type} path parameter. The request body
    is the matching AudioModelChoice variant — the model's typed params under params, with an optional
    top-level pricing. Returns the created job.

    Args:
        job_type (str):
        idempotency_key (Union[Unset, UUID]):
        body (AudioModelChoice): Request body for POST
            /developer/v2alpha/audios/{job_type}/generations. Carries the model params under params,
            with an optional top-level pricing. The accepted params fields depend on the {job_type}
            selected in the path.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GenerationJob]]
    """

    kwargs = _get_kwargs(
        job_type=job_type,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AudioModelChoice,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Optional[Union[Error, GenerationJob]]:
    """Create an audio generation

     Submit an audio generation job. The audio model is the {job_type} path parameter. The request body
    is the matching AudioModelChoice variant — the model's typed params under params, with an optional
    top-level pricing. Returns the created job.

    Args:
        job_type (str):
        idempotency_key (Union[Unset, UUID]):
        body (AudioModelChoice): Request body for POST
            /developer/v2alpha/audios/{job_type}/generations. Carries the model params under params,
            with an optional top-level pricing. The accepted params fields depend on the {job_type}
            selected in the path.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GenerationJob]
    """

    return (
        await asyncio_detailed(
            job_type=job_type,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
