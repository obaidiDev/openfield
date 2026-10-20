from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PlanDiscount")


@_attrs_define
class PlanDiscount:
    """Discount applied to a subscription plan card. amount_off is money (minor units, cents) in the card's currency.

    Attributes:
        amount_off (int): Flat discount in minor currency units (cents).
        actual_percent_off (float): Exact discount percentage.
        display_percent_off (int): Rounded discount percentage for display.
        use_percent_off (bool): Whether the discount should be presented as a percentage rather than a flat amount.
    """

    amount_off: int
    actual_percent_off: float
    display_percent_off: int
    use_percent_off: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_off = self.amount_off

        actual_percent_off = self.actual_percent_off

        display_percent_off = self.display_percent_off

        use_percent_off = self.use_percent_off

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount_off": amount_off,
                "actual_percent_off": actual_percent_off,
                "display_percent_off": display_percent_off,
                "use_percent_off": use_percent_off,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount_off = d.pop("amount_off")

        actual_percent_off = d.pop("actual_percent_off")

        display_percent_off = d.pop("display_percent_off")

        use_percent_off = d.pop("use_percent_off")

        plan_discount = cls(
            amount_off=amount_off,
            actual_percent_off=actual_percent_off,
            display_percent_off=display_percent_off,
            use_percent_off=use_percent_off,
        )

        plan_discount.additional_properties = d
        return plan_discount

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
