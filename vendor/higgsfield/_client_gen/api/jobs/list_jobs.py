from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.job_status import JobStatus
from ...models.jobs_response import JobsResponse
from ...models.list_jobs_type import ListJobsType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: Union[Unset, ListJobsType] = UNSET,
    status: Union[Unset, list[JobStatus]] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

    json_status: Union[Unset, list[str]] = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item: str = status_item_data
            json_status.append(status_item)

    params["status"] = json_status

    params["cursor"] = cursor

    params["size"] = size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/developer/v2alpha/jobs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, JobsResponse]]:
    if response.status_code == 200:
        response_200 = JobsResponse.from_dict(response.json())

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
) -> Response[Union[Error, JobsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, ListJobsType] = UNSET,
    status: Union[Unset, list[JobStatus]] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = 20,
) -> Response[Union[Error, JobsResponse]]:
    """List jobs

     Returns the authenticated user's accessible jobs across their workspaces, newest first, with cursor
    pagination. Jobs in every lifecycle status are returned by default; pass status to restrict the
    result to specific statuses. Pass the cursor from the previous page back as the cursor query
    parameter to fetch the next page; cursor is null when there are no more results.

    Args:
        type_ (Union[Unset, ListJobsType]):
        status (Union[Unset, list[JobStatus]]):
        cursor (Union[Unset, str]):
        size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, JobsResponse]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        status=status,
        cursor=cursor,
        size=size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, ListJobsType] = UNSET,
    status: Union[Unset, list[JobStatus]] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = 20,
) -> Optional[Union[Error, JobsResponse]]:
    """List jobs

     Returns the authenticated user's accessible jobs across their workspaces, newest first, with cursor
    pagination. Jobs in every lifecycle status are returned by default; pass status to restrict the
    result to specific statuses. Pass the cursor from the previous page back as the cursor query
    parameter to fetch the next page; cursor is null when there are no more results.

    Args:
        type_ (Union[Unset, ListJobsType]):
        status (Union[Unset, list[JobStatus]]):
        cursor (Union[Unset, str]):
        size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, JobsResponse]
    """

    return sync_detailed(
        client=client,
        type_=type_,
        status=status,
        cursor=cursor,
        size=size,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, ListJobsType] = UNSET,
    status: Union[Unset, list[JobStatus]] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = 20,
) -> Response[Union[Error, JobsResponse]]:
    """List jobs

     Returns the authenticated user's accessible jobs across their workspaces, newest first, with cursor
    pagination. Jobs in every lifecycle status are returned by default; pass status to restrict the
    result to specific statuses. Pass the cursor from the previous page back as the cursor query
    parameter to fetch the next page; cursor is null when there are no more results.

    Args:
        type_ (Union[Unset, ListJobsType]):
        status (Union[Unset, list[JobStatus]]):
        cursor (Union[Unset, str]):
        size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, JobsResponse]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        status=status,
        cursor=cursor,
        size=size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, ListJobsType] = UNSET,
    status: Union[Unset, list[JobStatus]] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = 20,
) -> Optional[Union[Error, JobsResponse]]:
    """List jobs

     Returns the authenticated user's accessible jobs across their workspaces, newest first, with cursor
    pagination. Jobs in every lifecycle status are returned by default; pass status to restrict the
    result to specific statuses. Pass the cursor from the previous page back as the cursor query
    parameter to fetch the next page; cursor is null when there are no more results.

    Args:
        type_ (Union[Unset, ListJobsType]):
        status (Union[Unset, list[JobStatus]]):
        cursor (Union[Unset, str]):
        size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, JobsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            status=status,
            cursor=cursor,
            size=size,
        )
    ).parsed
