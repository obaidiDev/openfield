from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.auto_topup_purchase import AutoTopupPurchase
from ...models.billing_purchase_response import BillingPurchaseResponse
from ...models.credit_topup_purchase import CreditTopupPurchase
from ...models.error import Error
from ...models.upgrade_plan_purchase import UpgradePlanPurchase
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Union["AutoTopupPurchase", "CreditTopupPurchase", "UpgradePlanPurchase"],
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/developer/v2alpha/account/billing/purchase",
    }

    _kwargs["json"]: dict[str, Any]
    if isinstance(body, UpgradePlanPurchase):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, CreditTopupPurchase):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BillingPurchaseResponse, Error]]:
    if response.status_code == 200:
        response_200 = BillingPurchaseResponse.from_dict(response.json())

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
) -> Response[Union[BillingPurchaseResponse, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["AutoTopupPurchase", "CreditTopupPurchase", "UpgradePlanPurchase"],
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Response[Union[BillingPurchaseResponse, Error]]:
    """Confirm a billing purchase

     Confirm a billing action against the caller's saved payment method. The request is discriminated by
    action:

    - upgrade_plan — change the active individual subscription to a higher tier (plan_type +
    billing_period required).
    - topup — buy a one-time credit pack by its top-up id (topup_id required).
    - auto_topup — enable auto top-up at a chosen amount (enabled: true + top_up_amount_cents) or
    disable it (enabled: false).

    The backend either charges the saved card off-session (charge_succeeded: true) or returns a
    checkout_url to redirect the caller to (charge_succeeded: false). Money fields are currency-aware
    (cents + currency). Idempotent via the idempotency key.

    Args:
        idempotency_key (Union[Unset, UUID]):
        body (Union['AutoTopupPurchase', 'CreditTopupPurchase', 'UpgradePlanPurchase']): A billing
            action to confirm against the caller's saved payment method, discriminated by action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BillingPurchaseResponse, Error]]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["AutoTopupPurchase", "CreditTopupPurchase", "UpgradePlanPurchase"],
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Optional[Union[BillingPurchaseResponse, Error]]:
    """Confirm a billing purchase

     Confirm a billing action against the caller's saved payment method. The request is discriminated by
    action:

    - upgrade_plan — change the active individual subscription to a higher tier (plan_type +
    billing_period required).
    - topup — buy a one-time credit pack by its top-up id (topup_id required).
    - auto_topup — enable auto top-up at a chosen amount (enabled: true + top_up_amount_cents) or
    disable it (enabled: false).

    The backend either charges the saved card off-session (charge_succeeded: true) or returns a
    checkout_url to redirect the caller to (charge_succeeded: false). Money fields are currency-aware
    (cents + currency). Idempotent via the idempotency key.

    Args:
        idempotency_key (Union[Unset, UUID]):
        body (Union['AutoTopupPurchase', 'CreditTopupPurchase', 'UpgradePlanPurchase']): A billing
            action to confirm against the caller's saved payment method, discriminated by action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BillingPurchaseResponse, Error]
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["AutoTopupPurchase", "CreditTopupPurchase", "UpgradePlanPurchase"],
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Response[Union[BillingPurchaseResponse, Error]]:
    """Confirm a billing purchase

     Confirm a billing action against the caller's saved payment method. The request is discriminated by
    action:

    - upgrade_plan — change the active individual subscription to a higher tier (plan_type +
    billing_period required).
    - topup — buy a one-time credit pack by its top-up id (topup_id required).
    - auto_topup — enable auto top-up at a chosen amount (enabled: true + top_up_amount_cents) or
    disable it (enabled: false).

    The backend either charges the saved card off-session (charge_succeeded: true) or returns a
    checkout_url to redirect the caller to (charge_succeeded: false). Money fields are currency-aware
    (cents + currency). Idempotent via the idempotency key.

    Args:
        idempotency_key (Union[Unset, UUID]):
        body (Union['AutoTopupPurchase', 'CreditTopupPurchase', 'UpgradePlanPurchase']): A billing
            action to confirm against the caller's saved payment method, discriminated by action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BillingPurchaseResponse, Error]]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["AutoTopupPurchase", "CreditTopupPurchase", "UpgradePlanPurchase"],
    idempotency_key: Union[Unset, UUID] = UNSET,
) -> Optional[Union[BillingPurchaseResponse, Error]]:
    """Confirm a billing purchase

     Confirm a billing action against the caller's saved payment method. The request is discriminated by
    action:

    - upgrade_plan — change the active individual subscription to a higher tier (plan_type +
    billing_period required).
    - topup — buy a one-time credit pack by its top-up id (topup_id required).
    - auto_topup — enable auto top-up at a chosen amount (enabled: true + top_up_amount_cents) or
    disable it (enabled: false).

    The backend either charges the saved card off-session (charge_succeeded: true) or returns a
    checkout_url to redirect the caller to (charge_succeeded: false). Money fields are currency-aware
    (cents + currency). Idempotent via the idempotency key.

    Args:
        idempotency_key (Union[Unset, UUID]):
        body (Union['AutoTopupPurchase', 'CreditTopupPurchase', 'UpgradePlanPurchase']): A billing
            action to confirm against the caller's saved payment method, discriminated by action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BillingPurchaseResponse, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
