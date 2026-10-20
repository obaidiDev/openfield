from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketingBrandColor")


@_attrs_define
class MarketingBrandColor:
    """A brand color. Unknown extra fields are preserved.

    Attributes:
        hex_ (Union[None, Unset, str]):
        rgb (Union[None, Unset, str]):
        usage (Union[None, Unset, str]): Where the color is used (e.g. primary, accent).
    """

    hex_: Union[None, Unset, str] = UNSET
    rgb: Union[None, Unset, str] = UNSET
    usage: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hex_: Union[None, Unset, str]
        if isinstance(self.hex_, Unset):
            hex_ = UNSET
        else:
            hex_ = self.hex_

        rgb: Union[None, Unset, str]
        if isinstance(self.rgb, Unset):
            rgb = UNSET
        else:
            rgb = self.rgb

        usage: Union[None, Unset, str]
        if isinstance(self.usage, Unset):
            usage = UNSET
        else:
            usage = self.usage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hex_ is not UNSET:
            field_dict["hex"] = hex_
        if rgb is not UNSET:
            field_dict["rgb"] = rgb
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_hex_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        hex_ = _parse_hex_(d.pop("hex", UNSET))

        def _parse_rgb(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        rgb = _parse_rgb(d.pop("rgb", UNSET))

        def _parse_usage(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        usage = _parse_usage(d.pop("usage", UNSET))

        marketing_brand_color = cls(
            hex_=hex_,
            rgb=rgb,
            usage=usage,
        )

        marketing_brand_color.additional_properties = d
        return marketing_brand_color

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
