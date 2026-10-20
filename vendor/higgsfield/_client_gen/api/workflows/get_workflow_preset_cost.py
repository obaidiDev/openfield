from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.workflow_preset_cost_request import WorkflowPresetCostRequest
from ...models.workflow_preset_cost_response import WorkflowPresetCostResponse
from ...types import Response


def _get_kwargs(
    product_key: str,
    preset_id: UUID,
    *,
    body: WorkflowPresetCostRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/developer/v2alpha/workflows/{product_key}/presets/{preset_id}/cost".format(
            product_key=product_key,
            preset_id=preset_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, WorkflowPresetCostResponse]]:
    if response.status_code == 200:
        response_200 = WorkflowPresetCostResponse.from_dict(response.json())

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
) -> Response[Union[Error, WorkflowPresetCostResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product_key: str,
    preset_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: WorkflowPresetCostRequest,
) -> Response[Union[Error, WorkflowPresetCostResponse]]:
    """Get workflow preset cost

     Fetch the display credit cost for one CMS workflow preset by id. Preset listing omits costs; use
    this endpoint when a client needs to show or confirm preset pricing. Dynamic-price presets may
    require the optional params request body so the server can calculate the final cost from runtime
    selections such as duration or resolution. The preset must belong to the supplied {product_key}.

    Args:
        product_key (str): CMS product surface key for workflow presets. Known values include the
            examples below, but the value is open-ended because CMS can add new workflow surfaces.
        preset_id (UUID):
        body (WorkflowPresetCostRequest): Optional runtime params used to calculate dynamic
            workflow preset pricing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, WorkflowPresetCostResponse]]
    """

    kwargs = _get_kwargs(
        product_key=product_key,
        preset_id=preset_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product_key: str,
    preset_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: WorkflowPresetCostRequest,
) -> Optional[Union[Error, WorkflowPresetCostResponse]]:
    """Get workflow preset cost

     Fetch the display credit cost for one CMS workflow preset by id. Preset listing omits costs; use
    this endpoint when a client needs to show or confirm preset pricing. Dynamic-price presets may
    require the optional params request body so the server can calculate the final cost from runtime
    selections such as duration or resolution. The preset must belong to the supplied {product_key}.

    Args:
        product_key (str): CMS product surface key for workflow presets. Known values include the
            examples below, but the value is open-ended because CMS can add new workflow surfaces.
        preset_id (UUID):
        body (WorkflowPresetCostRequest): Optional runtime params used to calculate dynamic
            workflow preset pricing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, WorkflowPresetCostResponse]
    """

    return sync_detailed(
        product_key=product_key,
        preset_id=preset_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    product_key: str,
    preset_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: WorkflowPresetCostRequest,
) -> Response[Union[Error, WorkflowPresetCostResponse]]:
    """Get workflow preset cost

     Fetch the display credit cost for one CMS workflow preset by id. Preset listing omits costs; use
    this endpoint when a client needs to show or confirm preset pricing. Dynamic-price presets may
    require the optional params request body so the server can calculate the final cost from runtime
    selections such as duration or resolution. The preset must belong to the supplied {product_key}.

    Args:
        product_key (str): CMS product surface key for workflow presets. Known values include the
            examples below, but the value is open-ended because CMS can add new workflow surfaces.
        preset_id (UUID):
        body (WorkflowPresetCostRequest): Optional runtime params used to calculate dynamic
            workflow preset pricing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, WorkflowPresetCostResponse]]
    """

    kwargs = _get_kwargs(
        product_key=product_key,
        preset_id=preset_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_key: str,
    preset_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: WorkflowPresetCostRequest,
) -> Optional[Union[Error, WorkflowPresetCostResponse]]:
    """Get workflow preset cost

     Fetch the display credit cost for one CMS workflow preset by id. Preset listing omits costs; use
    this endpoint when a client needs to show or confirm preset pricing. Dynamic-price presets may
    require the optional params request body so the server can calculate the final cost from runtime
    selections such as duration or resolution. The preset must belong to the supplied {product_key}.

    Args:
        product_key (str): CMS product surface key for workflow presets. Known values include the
            examples below, but the value is open-ended because CMS can add new workflow surfaces.
        preset_id (UUID):
        body (WorkflowPresetCostRequest): Optional runtime params used to calculate dynamic
            workflow preset pricing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, WorkflowPresetCostResponse]
    """

    return (
        await asyncio_detailed(
            product_key=product_key,
            preset_id=preset_id,
            client=client,
            body=body,
        )
    ).parsed
