from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reference_element_media_type import (
    ReferenceElementMediaType,
    check_reference_element_media_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReferenceElementMedia")


@_attrs_define
class ReferenceElementMedia:
    """A single image/video media item attached to a reference element.

    Attributes:
        id (str): Media identifier. For media_input items this is the media-input id; for image_job items this is the
            source job id.
        url (str): Resolvable URL of the media asset.
        type_ (Union[Unset, ReferenceElementMediaType]): Origin of a reference-element media item: an uploaded media
            input or a generated job image. Default: 'media_input'.
        width (Union[None, Unset, int]):
        height (Union[None, Unset, int]):
        duration (Union[None, Unset, float]): Duration in seconds (video media only).
    """

    id: str
    url: str
    type_: Union[Unset, ReferenceElementMediaType] = "media_input"
    width: Union[None, Unset, int] = UNSET
    height: Union[None, Unset, int] = UNSET
    duration: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

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

        duration: Union[None, Unset, float]
        if isinstance(self.duration, Unset):
            duration = UNSET
        else:
            duration = self.duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ReferenceElementMediaType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_reference_element_media_type(_type_)

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

        def _parse_duration(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        duration = _parse_duration(d.pop("duration", UNSET))

        reference_element_media = cls(
            id=id,
            url=url,
            type_=type_,
            width=width,
            height=height,
            duration=duration,
        )

        reference_element_media.additional_properties = d
        return reference_element_media

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
