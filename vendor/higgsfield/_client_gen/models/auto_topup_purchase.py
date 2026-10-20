from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auto_topup_purchase_action import (
    AutoTopupPurchaseAction,
    check_auto_topup_purchase_action,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AutoTopupPurchase")


@_attrs_define
class AutoTopupPurchase:
    """Enable or disable automatic credit top-up. When enabling, top_up_amount_cents is required (money: minor units in the
    caller's billing currency).

        Attributes:
            action (AutoTopupPurchaseAction): Discriminator. Must be auto_topup.
            enabled (Union[Unset, bool]): True to enable auto top-up (default), false to disable it. Default: True.
            top_up_amount_cents (Union[Unset, int]): Amount to auto-charge per refill, in minor currency units (cents).
                Required when enabled is true; ignored when disabling.
    """

    action: AutoTopupPurchaseAction
    enabled: Union[Unset, bool] = True
    top_up_amount_cents: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: str = self.action

        enabled = self.enabled

        top_up_amount_cents = self.top_up_amount_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if top_up_amount_cents is not UNSET:
            field_dict["top_up_amount_cents"] = top_up_amount_cents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = check_auto_topup_purchase_action(d.pop("action"))

        enabled = d.pop("enabled", UNSET)

        top_up_amount_cents = d.pop("top_up_amount_cents", UNSET)

        auto_topup_purchase = cls(
            action=action,
            enabled=enabled,
            top_up_amount_cents=top_up_amount_cents,
        )

        auto_topup_purchase.additional_properties = d
        return auto_topup_purchase

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
