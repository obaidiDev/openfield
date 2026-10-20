from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_period import BillingPeriod, check_billing_period
from ..models.subscription_plan_type import SubscriptionPlanType, check_subscription_plan_type
from ..models.upgrade_plan_purchase_action import (
    UpgradePlanPurchaseAction,
    check_upgrade_plan_purchase_action,
)

T = TypeVar("T", bound="UpgradePlanPurchase")


@_attrs_define
class UpgradePlanPurchase:
    """Change the active individual subscription to a higher tier.

    Attributes:
        action (UpgradePlanPurchaseAction): Discriminator. Must be upgrade_plan.
        plan_type (SubscriptionPlanType): Subscription plan tier.
        billing_period (BillingPeriod): Billing cadence of a subscription plan.
    """

    action: UpgradePlanPurchaseAction
    plan_type: SubscriptionPlanType
    billing_period: BillingPeriod
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: str = self.action

        plan_type: str = self.plan_type

        billing_period: str = self.billing_period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "plan_type": plan_type,
                "billing_period": billing_period,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = check_upgrade_plan_purchase_action(d.pop("action"))

        plan_type = check_subscription_plan_type(d.pop("plan_type"))

        billing_period = check_billing_period(d.pop("billing_period"))

        upgrade_plan_purchase = cls(
            action=action,
            plan_type=plan_type,
            billing_period=billing_period,
        )

        upgrade_plan_purchase.additional_properties = d
        return upgrade_plan_purchase

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
