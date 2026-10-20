from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PresetImage")


@_attrs_define
class PresetImage:
    """A preset sample/thumbnail image hosted on the provider CDN. These are curated catalog assets referenced by URL, not
    uploaded media inputs.

        Attributes:
            url (str): Public CloudFront URL the image is served from.
            width (Union[None, Unset, int]): Image width in pixels, when known.
            height (Union[None, Unset, int]): Image height in pixels, when known.
    """

    url: str
    width: Union[None, Unset, int] = UNSET
    height: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        width: Union[None, Unset, int]
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        height: Union[None, Unset, int]
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        def _parse_width(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        width = _parse_width(d.pop("width", UNSET))

        def _parse_height(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        height = _parse_height(d.pop("height", UNSET))

        preset_image = cls(
            url=url,
            width=width,
            height=height,
        )

        preset_image.additional_properties = d
        return preset_image

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
