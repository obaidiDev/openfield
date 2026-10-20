from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subscription_plan_type import SubscriptionPlanType, check_subscription_plan_type

T = TypeVar("T", bound="Balance")


@_attrs_define
class Balance:
    """Credit balance and current plan for the caller's active workspace. Credits are a virtual unit, not money — there is
    no currency here.

        Attributes:
            email (Union[None, str]): The caller's email address, or null if unknown.
            credits_ (float): Available credit balance, in credits (a virtual unit). May be fractional.
            subscription_plan_type (SubscriptionPlanType): Subscription plan tier.
    """

    email: Union[None, str]
    credits_: float
    subscription_plan_type: SubscriptionPlanType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email: Union[None, str]
        email = self.email

        credits_ = self.credits_

        subscription_plan_type: str = self.subscription_plan_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "credits": credits_,
                "subscription_plan_type": subscription_plan_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_email(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        email = _parse_email(d.pop("email"))

        credits_ = d.pop("credits")

        subscription_plan_type = check_subscription_plan_type(d.pop("subscription_plan_type"))

        balance = cls(
            email=email,
            credits_=credits_,
            subscription_plan_type=subscription_plan_type,
        )

        balance.additional_properties = d
        return balance

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
