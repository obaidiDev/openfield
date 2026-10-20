from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.realtime_chain_cost_estimate import RealtimeChainCostEstimate
from ...models.realtime_chain_cost_request import RealtimeChainCostRequest
from ...types import Response


def _get_kwargs(
    *,
    body: RealtimeChainCostRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/developer/v2alpha/realtime/chain/cost",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, RealtimeChainCostEstimate]]:
    if response.status_code == 200:
        response_200 = RealtimeChainCostEstimate.from_dict(response.json())

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
) -> Response[Union[Error, RealtimeChainCostEstimate]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RealtimeChainCostRequest,
) -> Response[Union[Error, RealtimeChainCostEstimate]]:
    """Estimate realtime chain cost

     Estimate the credit cost for a realtime Flux Klein edit without creating a job or reserving credits.

    Args:
        body (RealtimeChainCostRequest): Request to estimate one realtime Flux Klein edit.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, RealtimeChainCostEstimate]]
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
    body: RealtimeChainCostRequest,
) -> Optional[Union[Error, RealtimeChainCostEstimate]]:
    """Estimate realtime chain cost

     Estimate the credit cost for a realtime Flux Klein edit without creating a job or reserving credits.

    Args:
        body (RealtimeChainCostRequest): Request to estimate one realtime Flux Klein edit.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, RealtimeChainCostEstimate]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RealtimeChainCostRequest,
) -> Response[Union[Error, RealtimeChainCostEstimate]]:
    """Estimate realtime chain cost

     Estimate the credit cost for a realtime Flux Klein edit without creating a job or reserving credits.

    Args:
        body (RealtimeChainCostRequest): Request to estimate one realtime Flux Klein edit.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, RealtimeChainCostEstimate]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RealtimeChainCostRequest,
) -> Optional[Union[Error, RealtimeChainCostEstimate]]:
    """Estimate realtime chain cost

     Estimate the credit cost for a realtime Flux Klein edit without creating a job or reserving credits.

    Args:
        body (RealtimeChainCostRequest): Request to estimate one realtime Flux Klein edit.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, RealtimeChainCostEstimate]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
