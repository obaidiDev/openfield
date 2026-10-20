from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_period import BillingPeriod, check_billing_period
from ..models.currency import Currency, check_currency
from ..models.subscription_plan_type import SubscriptionPlanType, check_subscription_plan_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plan_discount import PlanDiscount


T = TypeVar("T", bound="Plan")


@_attrs_define
class Plan:
    """A subscription plan card with currency-aware pricing. Price fields are integer minor units (cents) in currency.

    Attributes:
        plan_type (SubscriptionPlanType): Subscription plan tier.
        billing_period (BillingPeriod): Billing cadence of a subscription plan.
        name (str): Display name of the plan (e.g. "Plus").
        tagline (str): Short marketing tagline for the plan.
        credits_ (int): Credits granted per billing period (a virtual unit, not money).
        original_price_cents (int): Pre-discount price in minor currency units (cents).
        final_price_cents (int): Final charged price in minor currency units (cents).
        url (str): Hosted checkout/upgrade URL for this plan card.
        most_popular (bool): Whether this card is flagged as the most popular option.
        button_color (str): Hint color for the card's call-to-action button.
        currency (Currency): ISO 4217 currency code, lowercased. Higgsfield supports these three; amounts are the same
            number across currencies (no FX conversion of our prices).
        discount (Union['PlanDiscount', None, Unset]): Discount applied to the card, if any.
        savings_amount (Union[None, Unset, int]): Savings versus the original price, in minor currency units (cents).
            Null when not applicable.
    """

    plan_type: SubscriptionPlanType
    billing_period: BillingPeriod
    name: str
    tagline: str
    credits_: int
    original_price_cents: int
    final_price_cents: int
    url: str
    most_popular: bool
    button_color: str
    currency: Currency
    discount: Union["PlanDiscount", None, Unset] = UNSET
    savings_amount: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.plan_discount import PlanDiscount

        plan_type: str = self.plan_type

        billing_period: str = self.billing_period

        name = self.name

        tagline = self.tagline

        credits_ = self.credits_

        original_price_cents = self.original_price_cents

        final_price_cents = self.final_price_cents

        url = self.url

        most_popular = self.most_popular

        button_color = self.button_color

        currency: str = self.currency

        discount: Union[None, Unset, dict[str, Any]]
        if isinstance(self.discount, Unset):
            discount = UNSET
        elif isinstance(self.discount, PlanDiscount):
            discount = self.discount.to_dict()
        else:
            discount = self.discount

        savings_amount: Union[None, Unset, int]
        if isinstance(self.savings_amount, Unset):
            savings_amount = UNSET
        else:
            savings_amount = self.savings_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plan_type": plan_type,
                "billing_period": billing_period,
                "name": name,
                "tagline": tagline,
                "credits": credits_,
                "original_price_cents": original_price_cents,
                "final_price_cents": final_price_cents,
                "url": url,
                "most_popular": most_popular,
                "button_color": button_color,
                "currency": currency,
            }
        )
        if discount is not UNSET:
            field_dict["discount"] = discount
        if savings_amount is not UNSET:
            field_dict["savings_amount"] = savings_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plan_discount import PlanDiscount

        d = dict(src_dict)
        plan_type = check_subscription_plan_type(d.pop("plan_type"))

        billing_period = check_billing_period(d.pop("billing_period"))

        name = d.pop("name")

        tagline = d.pop("tagline")

        credits_ = d.pop("credits")

        original_price_cents = d.pop("original_price_cents")

        final_price_cents = d.pop("final_price_cents")

        url = d.pop("url")

        most_popular = d.pop("most_popular")

        button_color = d.pop("button_color")

        currency = check_currency(d.pop("currency"))

        def _parse_discount(data: object) -> Union["PlanDiscount", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                discount_type_0 = PlanDiscount.from_dict(data)

                return discount_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PlanDiscount", None, Unset], data)

        discount = _parse_discount(d.pop("discount", UNSET))

        def _parse_savings_amount(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        savings_amount = _parse_savings_amount(d.pop("savings_amount", UNSET))

        plan = cls(
            plan_type=plan_type,
            billing_period=billing_period,
            name=name,
            tagline=tagline,
            credits_=credits_,
            original_price_cents=original_price_cents,
            final_price_cents=final_price_cents,
            url=url,
            most_popular=most_popular,
            button_color=button_color,
            currency=currency,
            discount=discount,
            savings_amount=savings_amount,
        )

        plan.additional_properties = d
        return plan

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
