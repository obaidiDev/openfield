from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.consents_state_items import ConsentsStateItems


T = TypeVar("T", bound="ConsentsState")


@_attrs_define
class ConsentsState:
    """The authenticated user's current consent state.

    Attributes:
        enabled (bool): Whether consent enforcement is currently enabled.
        items (ConsentsStateItems): Acceptance state keyed by dynamic consent type.
    """

    enabled: bool
    items: "ConsentsStateItems"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        items = self.items.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.consents_state_items import ConsentsStateItems

        d = dict(src_dict)
        enabled = d.pop("enabled")

        items = ConsentsStateItems.from_dict(d.pop("items"))

        consents_state = cls(
            enabled=enabled,
            items=items,
        )

        consents_state.additional_properties = d
        return consents_state

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
