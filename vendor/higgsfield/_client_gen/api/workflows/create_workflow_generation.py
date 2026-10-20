from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.workflow_generation_request import WorkflowGenerationRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    product_key: str,
    *,
    body: WorkflowGenerationRequest,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/developer/v2alpha/workflows/{product_key}/generations".format(
            product_key=product_key,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, list[UUID]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UUID(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Error, list[UUID]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product_key: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: WorkflowGenerationRequest,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Response[Union[Error, list[UUID]]]:
    """Create a workflow generation

     Submit a workflow generation. The workflow product surface is the {product_key} path parameter; the
    request body carries the selected CMS preset under params.preset_id plus the media reference params
    advertised by that preset's inputs. Returns the ids of the jobs created by the workflow; poll each
    with getJob.

    Args:
        product_key (str): CMS product surface key for workflow presets. Known values include the
            examples below, but the value is open-ended because CMS can add new workflow surfaces.
        idempotency_key (Union[Unset, UUID]):
        body (WorkflowGenerationRequest): Request body for POST
            /developer/v2alpha/workflows/{product_key}/generations. Mirrors the media generation
            envelope: workflow params live under params, with optional top-level pricing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, list[UUID]]]
    """

    kwargs = _get_kwargs(
        product_key=product_key,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product_key: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: WorkflowGenerationRequest,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Optional[Union[Error, list[UUID]]]:
    """Create a workflow generation

     Submit a workflow generation. The workflow product surface is the {product_key} path parameter; the
    request body carries the selected CMS preset under params.preset_id plus the media reference params
    advertised by that preset's inputs. Returns the ids of the jobs created by the workflow; poll each
    with getJob.

    Args:
        product_key (str): CMS product surface key for workflow presets. Known values include the
            examples below, but the value is open-ended because CMS can add new workflow surfaces.
        idempotency_key (Union[Unset, UUID]):
        body (WorkflowGenerationRequest): Request body for POST
            /developer/v2alpha/workflows/{product_key}/generations. Mirrors the media generation
            envelope: workflow params live under params, with optional top-level pricing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, list[UUID]]
    """

    return sync_detailed(
        product_key=product_key,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    product_key: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: WorkflowGenerationRequest,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Response[Union[Error, list[UUID]]]:
    """Create a workflow generation

     Submit a workflow generation. The workflow product surface is the {product_key} path parameter; the
    request body carries the selected CMS preset under params.preset_id plus the media reference params
    advertised by that preset's inputs. Returns the ids of the jobs created by the workflow; poll each
    with getJob.

    Args:
        product_key (str): CMS product surface key for workflow presets. Known values include the
            examples below, but the value is open-ended because CMS can add new workflow surfaces.
        idempotency_key (Union[Unset, UUID]):
        body (WorkflowGenerationRequest): Request body for POST
            /developer/v2alpha/workflows/{product_key}/generations. Mirrors the media generation
            envelope: workflow params live under params, with optional top-level pricing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, list[UUID]]]
    """

    kwargs = _get_kwargs(
        product_key=product_key,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_key: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: WorkflowGenerationRequest,
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Optional[Union[Error, list[UUID]]]:
    """Create a workflow generation

     Submit a workflow generation. The workflow product surface is the {product_key} path parameter; the
    request body carries the selected CMS preset under params.preset_id plus the media reference params
    advertised by that preset's inputs. Returns the ids of the jobs created by the workflow; poll each
    with getJob.

    Args:
        product_key (str): CMS product surface key for workflow presets. Known values include the
            examples below, but the value is open-ended because CMS can add new workflow surfaces.
        idempotency_key (Union[Unset, UUID]):
        body (WorkflowGenerationRequest): Request body for POST
            /developer/v2alpha/workflows/{product_key}/generations. Mirrors the media generation
            envelope: workflow params live under params, with optional top-level pricing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, list[UUID]]
    """

    return (
        await asyncio_detailed(
            product_key=product_key,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
