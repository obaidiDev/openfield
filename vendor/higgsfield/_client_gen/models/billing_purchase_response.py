from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.currency import Currency, check_currency
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.changed_plan import ChangedPlan


T = TypeVar("T", bound="BillingPurchaseResponse")


@_attrs_define
class BillingPurchaseResponse:
    """Result of confirming a billing purchase. Either the saved card was charged (charge_succeeded: true) or a
    checkout_url was returned to complete the purchase. Money fields are currency-aware. Fields beyond
    charge_succeeded/checkout_url/currency are populated according to the action taken.

        Attributes:
            charge_succeeded (bool): True if the saved payment method was charged off-session; false if the caller must
                complete checkout via checkout_url.
            currency (Currency): ISO 4217 currency code, lowercased. Higgsfield supports these three; amounts are the same
                number across currencies (no FX conversion of our prices).
            checkout_url (Union[None, Unset, str]): Hosted checkout URL to complete the purchase, when the off-session
                charge did not occur.
            credits_ (Union[Unset, int]): Credits granted by the purchase (topup action). A virtual unit, not money.
            price_cents (Union[Unset, int]): Amount charged for the purchase, in minor currency units (cents) (topup
                action).
            due_today_amount (Union[Unset, int]): Amount charged today for an upgrade, in minor currency units (cents)
                (upgrade_plan action).
            total_to_pay (Union[Unset, int]): Total amount due for the new plan, in minor currency units (cents)
                (upgrade_plan action).
            additional_credits (Union[Unset, int]): Extra credits granted by the upgrade (upgrade_plan action). A virtual
                unit, not money.
            new_plan (Union['ChangedPlan', None, Unset]): Summary of the plan the subscription was changed to (upgrade_plan
                action).
    """

    charge_succeeded: bool
    currency: Currency
    checkout_url: Union[None, Unset, str] = UNSET
    credits_: Union[Unset, int] = UNSET
    price_cents: Union[Unset, int] = UNSET
    due_today_amount: Union[Unset, int] = UNSET
    total_to_pay: Union[Unset, int] = UNSET
    additional_credits: Union[Unset, int] = UNSET
    new_plan: Union["ChangedPlan", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.changed_plan import ChangedPlan

        charge_succeeded = self.charge_succeeded

        currency: str = self.currency

        checkout_url: Union[None, Unset, str]
        if isinstance(self.checkout_url, Unset):
            checkout_url = UNSET
        else:
            checkout_url = self.checkout_url

        credits_ = self.credits_

        price_cents = self.price_cents

        due_today_amount = self.due_today_amount

        total_to_pay = self.total_to_pay

        additional_credits = self.additional_credits

        new_plan: Union[None, Unset, dict[str, Any]]
        if isinstance(self.new_plan, Unset):
            new_plan = UNSET
        elif isinstance(self.new_plan, ChangedPlan):
            new_plan = self.new_plan.to_dict()
        else:
            new_plan = self.new_plan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "charge_succeeded": charge_succeeded,
                "currency": currency,
            }
        )
        if checkout_url is not UNSET:
            field_dict["checkout_url"] = checkout_url
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if price_cents is not UNSET:
            field_dict["price_cents"] = price_cents
        if due_today_amount is not UNSET:
            field_dict["due_today_amount"] = due_today_amount
        if total_to_pay is not UNSET:
            field_dict["total_to_pay"] = total_to_pay
        if additional_credits is not UNSET:
            field_dict["additional_credits"] = additional_credits
        if new_plan is not UNSET:
            field_dict["new_plan"] = new_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.changed_plan import ChangedPlan

        d = dict(src_dict)
        charge_succeeded = d.pop("charge_succeeded")

        currency = check_currency(d.pop("currency"))

        def _parse_checkout_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        checkout_url = _parse_checkout_url(d.pop("checkout_url", UNSET))

        credits_ = d.pop("credits", UNSET)

        price_cents = d.pop("price_cents", UNSET)

        due_today_amount = d.pop("due_today_amount", UNSET)

        total_to_pay = d.pop("total_to_pay", UNSET)

        additional_credits = d.pop("additional_credits", UNSET)

        def _parse_new_plan(data: object) -> Union["ChangedPlan", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                new_plan_type_0 = ChangedPlan.from_dict(data)

                return new_plan_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ChangedPlan", None, Unset], data)

        new_plan = _parse_new_plan(d.pop("new_plan", UNSET))

        billing_purchase_response = cls(
            charge_succeeded=charge_succeeded,
            currency=currency,
            checkout_url=checkout_url,
            credits_=credits_,
            price_cents=price_cents,
            due_today_amount=due_today_amount,
            total_to_pay=total_to_pay,
            additional_credits=additional_credits,
            new_plan=new_plan,
        )

        billing_purchase_response.additional_properties = d
        return billing_purchase_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
