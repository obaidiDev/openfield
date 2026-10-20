from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketingAvatar")


@_attrs_define
class MarketingAvatar:
    """A Marketing Studio avatar — either a user-created custom avatar or a curated preset.

    Attributes:
        id (UUID):
        name (str):
        is_pinned (bool):
        type_ (str): Avatar source — custom for a user avatar, preset for a curated preset.
        preview_url (Union[None, Unset, str]): Preview image URL, when available.
        gender (Union[None, Unset, str]): Avatar gender, when derived (preset avatars only).
    """

    id: UUID
    name: str
    is_pinned: bool
    type_: str
    preview_url: Union[None, Unset, str] = UNSET
    gender: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        is_pinned = self.is_pinned

        type_ = self.type_

        preview_url: Union[None, Unset, str]
        if isinstance(self.preview_url, Unset):
            preview_url = UNSET
        else:
            preview_url = self.preview_url

        gender: Union[None, Unset, str]
        if isinstance(self.gender, Unset):
            gender = UNSET
        else:
            gender = self.gender

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "is_pinned": is_pinned,
                "type": type_,
            }
        )
        if preview_url is not UNSET:
            field_dict["preview_url"] = preview_url
        if gender is not UNSET:
            field_dict["gender"] = gender

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        is_pinned = d.pop("is_pinned")

        type_ = d.pop("type")

        def _parse_preview_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        preview_url = _parse_preview_url(d.pop("preview_url", UNSET))

        def _parse_gender(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        gender = _parse_gender(d.pop("gender", UNSET))

        marketing_avatar = cls(
            id=id,
            name=name,
            is_pinned=is_pinned,
            type_=type_,
            preview_url=preview_url,
            gender=gender,
        )

        marketing_avatar.additional_properties = d
        return marketing_avatar

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
