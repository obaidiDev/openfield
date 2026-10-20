from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RealtimeCustomStyleReference")


@_attrs_define
class RealtimeCustomStyleReference:
    """Optional reference image stored with a custom realtime style.

    Attributes:
        media_id (UUID): Uploaded media id used as the style reference.
        url (Union[None, Unset, str]): Optional display URL the client already has.
        source_name (Union[None, Unset, str]): Optional source filename or display name.
        content_type (Union[None, Unset, str]): Optional media MIME type.
    """

    media_id: UUID
    url: Union[None, Unset, str] = UNSET
    source_name: Union[None, Unset, str] = UNSET
    content_type: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media_id = str(self.media_id)

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        source_name: Union[None, Unset, str]
        if isinstance(self.source_name, Unset):
            source_name = UNSET
        else:
            source_name = self.source_name

        content_type: Union[None, Unset, str]
        if isinstance(self.content_type, Unset):
            content_type = UNSET
        else:
            content_type = self.content_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "media_id": media_id,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if source_name is not UNSET:
            field_dict["source_name"] = source_name
        if content_type is not UNSET:
            field_dict["content_type"] = content_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        media_id = UUID(d.pop("media_id"))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_source_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_name = _parse_source_name(d.pop("source_name", UNSET))

        def _parse_content_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        content_type = _parse_content_type(d.pop("content_type", UNSET))

        realtime_custom_style_reference = cls(
            media_id=media_id,
            url=url,
            source_name=source_name,
            content_type=content_type,
        )

        realtime_custom_style_reference.additional_properties = d
        return realtime_custom_style_reference

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
