from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cost_estimate import CostEstimate
from ...models.error import Error
from ...models.model_choice import ModelChoice
from ...types import Response


def _get_kwargs(
    job_type: str,
    *,
    body: ModelChoice,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/developer/v2alpha/jobs/{job_type}/cost".format(
            job_type=job_type,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CostEstimate, Error]]:
    if response.status_code == 200:
        response_200 = CostEstimate.from_dict(response.json())

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
) -> Response[Union[CostEstimate, Error]]:
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
    body: ModelChoice,
) -> Response[Union[CostEstimate, Error]]:
    """Estimate generation cost

     Estimates the credit cost of a generation for the given model parameters, without creating a job or
    charging anything. The model is selected by the {job_type} path parameter — the same mechanism the
    generation endpoints use — so the priced model is unambiguous; send the matching ModelChoice variant
    directly (model params under params, with an optional top-level pricing) — the same body shape as
    the generation endpoints. Credits are a virtual unit (not money) and are returned as a plain rounded
    integer plus the exact fractional value. This call is read-only and does not require an idempotency
    key.

    Args:
        job_type (str):
        body (ModelChoice): A generation request for any public model, used to estimate cost.
            Carries the model params under params, with an optional top-level pricing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CostEstimate, Error]]
    """

    kwargs = _get_kwargs(
        job_type=job_type,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ModelChoice,
) -> Optional[Union[CostEstimate, Error]]:
    """Estimate generation cost

     Estimates the credit cost of a generation for the given model parameters, without creating a job or
    charging anything. The model is selected by the {job_type} path parameter — the same mechanism the
    generation endpoints use — so the priced model is unambiguous; send the matching ModelChoice variant
    directly (model params under params, with an optional top-level pricing) — the same body shape as
    the generation endpoints. Credits are a virtual unit (not money) and are returned as a plain rounded
    integer plus the exact fractional value. This call is read-only and does not require an idempotency
    key.

    Args:
        job_type (str):
        body (ModelChoice): A generation request for any public model, used to estimate cost.
            Carries the model params under params, with an optional top-level pricing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CostEstimate, Error]
    """

    return sync_detailed(
        job_type=job_type,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    job_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ModelChoice,
) -> Response[Union[CostEstimate, Error]]:
    """Estimate generation cost

     Estimates the credit cost of a generation for the given model parameters, without creating a job or
    charging anything. The model is selected by the {job_type} path parameter — the same mechanism the
    generation endpoints use — so the priced model is unambiguous; send the matching ModelChoice variant
    directly (model params under params, with an optional top-level pricing) — the same body shape as
    the generation endpoints. Credits are a virtual unit (not money) and are returned as a plain rounded
    integer plus the exact fractional value. This call is read-only and does not require an idempotency
    key.

    Args:
        job_type (str):
        body (ModelChoice): A generation request for any public model, used to estimate cost.
            Carries the model params under params, with an optional top-level pricing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CostEstimate, Error]]
    """

    kwargs = _get_kwargs(
        job_type=job_type,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ModelChoice,
) -> Optional[Union[CostEstimate, Error]]:
    """Estimate generation cost

     Estimates the credit cost of a generation for the given model parameters, without creating a job or
    charging anything. The model is selected by the {job_type} path parameter — the same mechanism the
    generation endpoints use — so the priced model is unambiguous; send the matching ModelChoice variant
    directly (model params under params, with an optional top-level pricing) — the same body shape as
    the generation endpoints. Credits are a virtual unit (not money) and are returned as a plain rounded
    integer plus the exact fractional value. This call is read-only and does not require an idempotency
    key.

    Args:
        job_type (str):
        body (ModelChoice): A generation request for any public model, used to estimate cost.
            Carries the model params under params, with an optional top-level pricing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CostEstimate, Error]
    """

    return (
        await asyncio_detailed(
            job_type=job_type,
            client=client,
            body=body,
        )
    ).parsed
