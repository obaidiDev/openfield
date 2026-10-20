from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RealtimeChainCostEstimate")


@_attrs_define
class RealtimeChainCostEstimate:
    """Estimated realtime edit cost. credits is rounded for display; credits_exact preserves the fractional value.

    Attributes:
        credits_ (int): Rounded display credit cost.
        credits_exact (float): Exact fractional credit cost.
    """

    credits_: int
    credits_exact: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credits_ = self.credits_

        credits_exact = self.credits_exact

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credits": credits_,
                "credits_exact": credits_exact,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credits_ = d.pop("credits")

        credits_exact = d.pop("credits_exact")

        realtime_chain_cost_estimate = cls(
            credits_=credits_,
            credits_exact=credits_exact,
        )

        realtime_chain_cost_estimate.additional_properties = d
        return realtime_chain_cost_estimate

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
