from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.list_job_set_types_label_item import (
    ListJobSetTypesLabelItem,
)
from ...models.list_job_set_types_type import ListJobSetTypesType
from ...models.model_list_response import ModelListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: Union[Unset, ListJobSetTypesType] = UNSET,
    label: Union[Unset, list[ListJobSetTypesLabelItem]] = UNSET,
    limit: Union[Unset, int] = 50,
    cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

    json_label: Union[Unset, list[str]] = UNSET
    if not isinstance(label, Unset):
        json_label = []
        for label_item_data in label:
            label_item: str = label_item_data
            json_label.append(label_item)

    params["label"] = json_label

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/developer/v2alpha/job_types",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, ModelListResponse]]:
    if response.status_code == 200:
        response_200 = ModelListResponse.from_dict(response.json())

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
) -> Response[Union[Error, ModelListResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, ListJobSetTypesType] = UNSET,
    label: Union[Unset, list[ListJobSetTypesLabelItem]] = UNSET,
    limit: Union[Unset, int] = 50,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[Error, ModelListResponse]]:
    """List generation job_types

     List every generation model available behind the generation endpoints. Each entry carries its
    job_type (the path segment used to submit a job), a human display name, the media kind, and the JSON
    Schema for its typed parameters. This catalog is assembled in-process from the executor registry and
    is not user-scoped. Optionally filter by media kind.

    Args:
        type_ (Union[Unset, ListJobSetTypesType]):
        label (Union[Unset, list[ListJobSetTypesLabelItem]]):
        limit (Union[Unset, int]):  Default: 50.
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ModelListResponse]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        label=label,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, ListJobSetTypesType] = UNSET,
    label: Union[Unset, list[ListJobSetTypesLabelItem]] = UNSET,
    limit: Union[Unset, int] = 50,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, ModelListResponse]]:
    """List generation job_types

     List every generation model available behind the generation endpoints. Each entry carries its
    job_type (the path segment used to submit a job), a human display name, the media kind, and the JSON
    Schema for its typed parameters. This catalog is assembled in-process from the executor registry and
    is not user-scoped. Optionally filter by media kind.

    Args:
        type_ (Union[Unset, ListJobSetTypesType]):
        label (Union[Unset, list[ListJobSetTypesLabelItem]]):
        limit (Union[Unset, int]):  Default: 50.
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ModelListResponse]
    """

    return sync_detailed(
        client=client,
        type_=type_,
        label=label,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, ListJobSetTypesType] = UNSET,
    label: Union[Unset, list[ListJobSetTypesLabelItem]] = UNSET,
    limit: Union[Unset, int] = 50,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[Error, ModelListResponse]]:
    """List generation job_types

     List every generation model available behind the generation endpoints. Each entry carries its
    job_type (the path segment used to submit a job), a human display name, the media kind, and the JSON
    Schema for its typed parameters. This catalog is assembled in-process from the executor registry and
    is not user-scoped. Optionally filter by media kind.

    Args:
        type_ (Union[Unset, ListJobSetTypesType]):
        label (Union[Unset, list[ListJobSetTypesLabelItem]]):
        limit (Union[Unset, int]):  Default: 50.
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ModelListResponse]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        label=label,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, ListJobSetTypesType] = UNSET,
    label: Union[Unset, list[ListJobSetTypesLabelItem]] = UNSET,
    limit: Union[Unset, int] = 50,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, ModelListResponse]]:
    """List generation job_types

     List every generation model available behind the generation endpoints. Each entry carries its
    job_type (the path segment used to submit a job), a human display name, the media kind, and the JSON
    Schema for its typed parameters. This catalog is assembled in-process from the executor registry and
    is not user-scoped. Optionally filter by media kind.

    Args:
        type_ (Union[Unset, ListJobSetTypesType]):
        label (Union[Unset, list[ListJobSetTypesLabelItem]]):
        limit (Union[Unset, int]):  Default: 50.
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ModelListResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            label=label,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
