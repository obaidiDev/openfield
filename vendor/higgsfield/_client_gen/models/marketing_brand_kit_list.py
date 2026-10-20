from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.marketing_brand_kit import MarketingBrandKit


T = TypeVar("T", bound="MarketingBrandKitList")


@_attrs_define
class MarketingBrandKitList:
    """A cursor-paginated page of brand kits.

    Attributes:
        items (list['MarketingBrandKit']):
        has_more (bool): True while cursor is non-null.
        cursor (Union[None, Unset, float]): Float epoch-seconds cursor for the next page; pass it back as cursor. null
            on the last page.
    """

    items: list["MarketingBrandKit"]
    has_more: bool
    cursor: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        has_more = self.has_more

        cursor: Union[None, Unset, float]
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "has_more": has_more,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.marketing_brand_kit import MarketingBrandKit

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = MarketingBrandKit.from_dict(items_item_data)

            items.append(items_item)

        has_more = d.pop("has_more")

        def _parse_cursor(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        marketing_brand_kit_list = cls(
            items=items,
            has_more=has_more,
            cursor=cursor,
        )

        marketing_brand_kit_list.additional_properties = d
        return marketing_brand_kit_list

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
