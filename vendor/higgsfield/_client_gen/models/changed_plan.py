from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ChangedPlan")


@_attrs_define
class ChangedPlan:
    """Summary of the subscription plan after an upgrade. price_per_seat is money (minor units, cents) in the response
    currency.

        Attributes:
            tier (str): Plan tier the subscription was changed to.
            billing_period (str): Billing cadence of the new plan.
            credits_per_month (int): Credits granted per month under the new plan (a virtual unit, not money).
            price_per_seat (int): Per-seat price of the new plan, in minor currency units (cents).
    """

    tier: str
    billing_period: str
    credits_per_month: int
    price_per_seat: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tier = self.tier

        billing_period = self.billing_period

        credits_per_month = self.credits_per_month

        price_per_seat = self.price_per_seat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tier": tier,
                "billing_period": billing_period,
                "credits_per_month": credits_per_month,
                "price_per_seat": price_per_seat,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tier = d.pop("tier")

        billing_period = d.pop("billing_period")

        credits_per_month = d.pop("credits_per_month")

        price_per_seat = d.pop("price_per_seat")

        changed_plan = cls(
            tier=tier,
            billing_period=billing_period,
            credits_per_month=credits_per_month,
            price_per_seat=price_per_seat,
        )

        changed_plan.additional_properties = d
        return changed_plan

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
