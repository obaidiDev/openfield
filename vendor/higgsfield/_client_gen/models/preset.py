from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preset_image import PresetImage


T = TypeVar("T", bound="Preset")


@_attrs_define
class Preset:
    """A preset/style entry from the CMS Soul style catalog. Grounded in serialize_soul_v2_preset
    (src/handlers/soul_v2_preset.py).

        Attributes:
            id (UUID): Preset identifier.
            name (str): Preset display name.
            images (list['PresetImage']): All images associated with the preset (thumbnails / showcase samples). Each item
                is a CloudFront-hosted image with optional pixel dimensions. These are catalog assets, not uploaded media
                inputs, so they are not flat media references ({id, type}).
            is_custom (bool): True for a user-created custom preset, false for a built-in CMS preset.
            status (str): Preset status. Built-in CMS presets are always 'completed'; custom presets carry their reference
                status.
            category (Union[None, Unset, str]): Category this preset belongs to; null for custom presets.
            description (Union[None, Unset, str]): Optional preset description; null for custom presets.
            in_progress_at (Union[None, Unset, float]): Epoch seconds when a custom preset began processing, or null.
    """

    id: UUID
    name: str
    images: list["PresetImage"]
    is_custom: bool
    status: str
    category: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    in_progress_at: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)

        is_custom = self.is_custom

        status = self.status

        category: Union[None, Unset, str]
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        in_progress_at: Union[None, Unset, float]
        if isinstance(self.in_progress_at, Unset):
            in_progress_at = UNSET
        else:
            in_progress_at = self.in_progress_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "images": images,
                "is_custom": is_custom,
                "status": status,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if description is not UNSET:
            field_dict["description"] = description
        if in_progress_at is not UNSET:
            field_dict["in_progress_at"] = in_progress_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preset_image import PresetImage

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = PresetImage.from_dict(images_item_data)

            images.append(images_item)

        is_custom = d.pop("is_custom")

        status = d.pop("status")

        def _parse_category(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_in_progress_at(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        in_progress_at = _parse_in_progress_at(d.pop("in_progress_at", UNSET))

        preset = cls(
            id=id,
            name=name,
            images=images,
            is_custom=is_custom,
            status=status,
            category=category,
            description=description,
            in_progress_at=in_progress_at,
        )

        preset.additional_properties = d
        return preset

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
