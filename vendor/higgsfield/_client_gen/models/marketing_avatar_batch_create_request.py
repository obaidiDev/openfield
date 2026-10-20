from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.marketing_avatar_create_item import MarketingAvatarCreateItem


T = TypeVar("T", bound="MarketingAvatarBatchCreateRequest")


@_attrs_define
class MarketingAvatarBatchCreateRequest:
    """Create up to four custom avatars in one call.

    Attributes:
        avatars (list['MarketingAvatarCreateItem']):
    """

    avatars: list["MarketingAvatarCreateItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatars = []
        for avatars_item_data in self.avatars:
            avatars_item = avatars_item_data.to_dict()
            avatars.append(avatars_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "avatars": avatars,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.marketing_avatar_create_item import MarketingAvatarCreateItem

        d = dict(src_dict)
        avatars = []
        _avatars = d.pop("avatars")
        for avatars_item_data in _avatars:
            avatars_item = MarketingAvatarCreateItem.from_dict(avatars_item_data)

            avatars.append(avatars_item)

        marketing_avatar_batch_create_request = cls(
            avatars=avatars,
        )

        marketing_avatar_batch_create_request.additional_properties = d
        return marketing_avatar_batch_create_request

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
