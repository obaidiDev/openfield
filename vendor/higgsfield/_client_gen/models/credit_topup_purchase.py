from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credit_topup_purchase_action import (
    CreditTopupPurchaseAction,
    check_credit_topup_purchase_action,
)

T = TypeVar("T", bound="CreditTopupPurchase")


@_attrs_define
class CreditTopupPurchase:
    """Buy a one-time credit top-up pack.

    Attributes:
        action (CreditTopupPurchaseAction): Discriminator. Must be topup.
        topup_id (str): The CreditTopup.id of the pack to purchase (e.g. "credits_4000").
    """

    action: CreditTopupPurchaseAction
    topup_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: str = self.action

        topup_id = self.topup_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "topup_id": topup_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = check_credit_topup_purchase_action(d.pop("action"))

        topup_id = d.pop("topup_id")

        credit_topup_purchase = cls(
            action=action,
            topup_id=topup_id,
        )

        credit_topup_purchase.additional_properties = d
        return credit_topup_purchase

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
