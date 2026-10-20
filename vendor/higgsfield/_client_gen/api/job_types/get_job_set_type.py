from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.model import Model
from ...types import Response


def _get_kwargs(
    job_type: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/developer/v2alpha/job_types/{job_type}".format(
            job_type=job_type,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, Model]]:
    if response.status_code == 200:
        response_200 = Model.from_dict(response.json())

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
) -> Response[Union[Error, Model]]:
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
) -> Response[Union[Error, Model]]:
    """Get a generation job_type

     Fetch a single generation job_type by its id, including the JSON Schema for its typed parameters.

    Args:
        job_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Model]]
    """

    kwargs = _get_kwargs(
        job_type=job_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, Model]]:
    """Get a generation job_type

     Fetch a single generation job_type by its id, including the JSON Schema for its typed parameters.

    Args:
        job_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, Model]
    """

    return sync_detailed(
        job_type=job_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, Model]]:
    """Get a generation job_type

     Fetch a single generation job_type by its id, including the JSON Schema for its typed parameters.

    Args:
        job_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Model]]
    """

    kwargs = _get_kwargs(
        job_type=job_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, Model]]:
    """Get a generation job_type

     Fetch a single generation job_type by its id, including the JSON Schema for its typed parameters.

    Args:
        job_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, Model]
    """

    return (
        await asyncio_detailed(
            job_type=job_type,
            client=client,
        )
    ).parsed
