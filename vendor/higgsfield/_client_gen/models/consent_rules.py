from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ConsentRules")


@_attrs_define
class ConsentRules:
    """Client and server enforcement behavior for this consent.

    Attributes:
        blocking (bool): Whether protected operations must stop until the required version is accepted.
    """

    blocking: bool

    def to_dict(self) -> dict[str, Any]:
        blocking = self.blocking

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "blocking": blocking,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        blocking = d.pop("blocking")

        consent_rules = cls(
            blocking=blocking,
        )

        return consent_rules
