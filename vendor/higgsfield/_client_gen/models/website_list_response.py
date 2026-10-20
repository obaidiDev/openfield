from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.website_list_item import WebsiteListItem


T = TypeVar("T", bound="WebsiteListResponse")


@_attrs_define
class WebsiteListResponse:
    """The caller's websites.

    Attributes:
        websites (list['WebsiteListItem']):
    """

    websites: list["WebsiteListItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        websites = []
        for websites_item_data in self.websites:
            websites_item = websites_item_data.to_dict()
            websites.append(websites_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "websites": websites,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.website_list_item import WebsiteListItem

        d = dict(src_dict)
        websites = []
        _websites = d.pop("websites")
        for websites_item_data in _websites:
            websites_item = WebsiteListItem.from_dict(websites_item_data)

            websites.append(websites_item)

        website_list_response = cls(
            websites=websites,
        )

        website_list_response.additional_properties = d
        return website_list_response

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
