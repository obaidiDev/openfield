import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="Transaction")


@_attrs_define
class Transaction:
    """A grouped credit-ledger entry. Amounts are in credits (a virtual unit), not money.

    Attributes:
        display_name (str): Human-readable label for the transaction (e.g. the feature or model that produced it).
        credits_ (float): Net credits for this entry (a virtual unit). Negative for spends, positive for grants/refunds.
            May be fractional.
        action (str): The ledger event/action that produced the entry (e.g. spend, refund, grant, deduct).
        created_at (datetime.datetime): Timestamp of the earliest event in the grouped entry.
    """

    display_name: str
    credits_: float
    action: str
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        credits_ = self.credits_

        action = self.action

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "display_name": display_name,
                "credits": credits_,
                "action": action,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("display_name")

        credits_ = d.pop("credits")

        action = d.pop("action")

        created_at = isoparse(d.pop("created_at"))

        transaction = cls(
            display_name=display_name,
            credits_=credits_,
            action=action,
            created_at=created_at,
        )

        transaction.additional_properties = d
        return transaction

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
