from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebsiteCategory")


@_attrs_define
class WebsiteCategory:
    """One content category a website can be filed under.

    Attributes:
        slug (str): Category identifier — pass this as the 'category' when creating a website.
        label (str): Human-facing category name.
        description (Union[None, Unset, str]): Short description of the category.
        position (Union[Unset, int]): Display order (ascending). Default: 0.
    """

    slug: str
    label: str
    description: Union[None, Unset, str] = UNSET
    position: Union[Unset, int] = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        label = self.label

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "label": label,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")

        label = d.pop("label")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        position = d.pop("position", UNSET)

        website_category = cls(
            slug=slug,
            label=label,
            description=description,
            position=position,
        )

        website_category.additional_properties = d
        return website_category

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
