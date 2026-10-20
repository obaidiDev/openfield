from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.import_media_request_type import (
    ImportMediaRequestType,
    check_import_media_request_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportMediaRequest")


@_attrs_define
class ImportMediaRequest:
    """Request to import a remote media URL.

    Attributes:
        url (str): HTTP(S) URL of the media file to import.
        type_ (Union[Unset, ImportMediaRequestType]): Expected media kind. Use auto (or omit) when unknown; the server
            infers the kind from the fetched content. Default: 'auto'.
    """

    url: str
    type_: Union[Unset, ImportMediaRequestType] = "auto"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ImportMediaRequestType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_import_media_request_type(_type_)

        import_media_request = cls(
            url=url,
            type_=type_,
        )

        import_media_request.additional_properties = d
        return import_media_request

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
