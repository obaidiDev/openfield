from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference_element import ReferenceElement


T = TypeVar("T", bound="ReferenceElementList")


@_attrs_define
class ReferenceElementList:
    """A cursor-paginated page of reference elements.

    Attributes:
        items (list['ReferenceElement']):
        cursor (Union[None, str]): Opaque cursor for the next page; pass it back as the cursor query parameter. null on
            the last page.
        total (Union[None, Unset, int]): Total number of elements matching the query across all pages.
    """

    items: list["ReferenceElement"]
    cursor: Union[None, str]
    total: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        cursor: Union[None, str]
        cursor = self.cursor

        total: Union[None, Unset, int]
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "cursor": cursor,
            }
        )
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reference_element import ReferenceElement

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ReferenceElement.from_dict(items_item_data)

            items.append(items_item)

        def _parse_cursor(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        cursor = _parse_cursor(d.pop("cursor"))

        def _parse_total(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total = _parse_total(d.pop("total", UNSET))

        reference_element_list = cls(
            items=items,
            cursor=cursor,
            total=total,
        )

        reference_element_list.additional_properties = d
        return reference_element_list

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
