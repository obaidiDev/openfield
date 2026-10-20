from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnimationAction")


@_attrs_define
class AnimationAction:
    """An entry in the baked 3D rig animation library. Its integer id is passed back as the animation_action_id parameter
    for animated 3D generation.

        Attributes:
            id (int): Stable animation action id, passed as animation_action_id to 3D generation (valid range 0-696).
            name (str): Animation action name.
            group (Union[None, str]): Top-level grouping for the action.
            category (Union[None, str]): Sub-category for the action.
            preview_url (str): URL of a preview GIF demonstrating the action.
    """

    id: int
    name: str
    group: Union[None, str]
    category: Union[None, str]
    preview_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        group: Union[None, str]
        group = self.group

        category: Union[None, str]
        category = self.category

        preview_url = self.preview_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "group": group,
                "category": category,
                "preview_url": preview_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_group(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        group = _parse_group(d.pop("group"))

        def _parse_category(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        category = _parse_category(d.pop("category"))

        preview_url = d.pop("preview_url")

        animation_action = cls(
            id=id,
            name=name,
            group=group,
            category=category,
            preview_url=preview_url,
        )

        animation_action.additional_properties = d
        return animation_action

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
