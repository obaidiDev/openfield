"""Account: balance, transactions, plans, billing, workspaces, and consents."""

from __future__ import annotations

from typing import Any, Optional, Union

from .._client_gen.models.accept_consent_request import AcceptConsentRequest
from .._client_gen.models.auto_topup_purchase import AutoTopupPurchase
from .._client_gen.models.balance import Balance
from .._client_gen.models.billing_purchase_response import BillingPurchaseResponse
from .._client_gen.models.consents_response import ConsentsResponse
from .._client_gen.models.credit_topup_purchase import CreditTopupPurchase
from .._client_gen.models.plans_and_credits_response import PlansAndCreditsResponse
from .._client_gen.models.transactions_response import TransactionsResponse
from .._client_gen.models.upgrade_plan_purchase import UpgradePlanPurchase
from .._client_gen.models.workspace_list import WorkspaceList
from .._transport import RequestOptions, Unpack, body_dict, query
from ._base import Resource

BillingPurchaseRequest = Union[
    AutoTopupPurchase, CreditTopupPurchase, UpgradePlanPurchase, dict[str, Any]
]
ConsentAcceptanceRequest = Union[AcceptConsentRequest, dict[str, Any]]


class AccountResource(Resource):
    def get_balance(self, **options: Unpack[RequestOptions]) -> Balance:
        """The active workspace's credit balance, email, and plan tier."""
        return Balance.from_dict(self._get_json("/developer/v2alpha/account/balance", **options))

    def list_transactions(
        self,
        *,
        cursor: Optional[str] = None,
        size: Optional[int] = None,
        **options: Unpack[RequestOptions],
    ) -> TransactionsResponse:
        """List credit transactions with cursor pagination."""
        data = self._get_json(
            "/developer/v2alpha/account/transactions",
            params=query(cursor=cursor, size=size),
            **options,
        )
        return TransactionsResponse.from_dict(data)

    def get_plans(self, **options: Unpack[RequestOptions]) -> PlansAndCreditsResponse:
        """Available plans and credit packs."""
        data = self._get_json("/developer/v2alpha/account/billing/plans", **options)
        return PlansAndCreditsResponse.from_dict(data)

    def confirm_purchase(
        self, body: BillingPurchaseRequest, **options: Unpack[RequestOptions]
    ) -> BillingPurchaseResponse:
        """Confirm a billing purchase."""
        data = self._post_json(
            "/developer/v2alpha/account/billing/purchase", json=body_dict(body), **options
        )
        return BillingPurchaseResponse.from_dict(data)

    def list_workspaces(self, **options: Unpack[RequestOptions]) -> WorkspaceList:
        """List workspaces you can access."""
        data = self._get_json("/developer/v2alpha/account/workspaces", **options)
        return WorkspaceList.from_dict(data)

    def get_consents(self, **options: Unpack[RequestOptions]) -> ConsentsResponse:
        """Get every registered consent and its current acceptance state."""
        data = self._get_json("/developer/v2alpha/account/consents", **options)
        return ConsentsResponse.from_dict(data)

    def accept_consent(
        self, body: ConsentAcceptanceRequest, **options: Unpack[RequestOptions]
    ) -> ConsentsResponse:
        """Accept the currently required version of a user consent."""
        data = self._post_json(
            "/developer/v2alpha/account/consents/accept", json=body_dict(body), **options
        )
        return ConsentsResponse.from_dict(data)
