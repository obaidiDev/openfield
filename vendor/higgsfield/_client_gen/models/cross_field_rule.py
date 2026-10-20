from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CrossFieldRule")


@_attrs_define
class CrossFieldRule:
    """A cross-field constraint on the model's params that JSON Schema cannot express, given as a CEL expression. cel
    evaluates to true when the params are valid; the same rule is enforced server-side. Bound variable is params (the
    request body). Grounded in ContractRule / CelValidatedParams (src/schemas/job/contract.py).

        Attributes:
            cel (str): CEL expression over params; true == valid.
            message (str): Human-readable violation message, surfaced when the rule does not hold.
    """

    cel: str
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cel = self.cel

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cel": cel,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cel = d.pop("cel")

        message = d.pop("message")

        cross_field_rule = cls(
            cel=cel,
            message=message,
        )

        cross_field_rule.additional_properties = d
        return cross_field_rule

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
