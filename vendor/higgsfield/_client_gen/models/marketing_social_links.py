from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketingSocialLinks")


@_attrs_define
class MarketingSocialLinks:
    """Brand social links. Unknown extra fields are preserved.

    Attributes:
        instagram (Union[None, Unset, str]):
        tiktok (Union[None, Unset, str]):
        youtube (Union[None, Unset, str]):
        twitter (Union[None, Unset, str]):
        linkedin (Union[None, Unset, str]):
        facebook (Union[None, Unset, str]):
        pinterest (Union[None, Unset, str]):
    """

    instagram: Union[None, Unset, str] = UNSET
    tiktok: Union[None, Unset, str] = UNSET
    youtube: Union[None, Unset, str] = UNSET
    twitter: Union[None, Unset, str] = UNSET
    linkedin: Union[None, Unset, str] = UNSET
    facebook: Union[None, Unset, str] = UNSET
    pinterest: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instagram: Union[None, Unset, str]
        if isinstance(self.instagram, Unset):
            instagram = UNSET
        else:
            instagram = self.instagram

        tiktok: Union[None, Unset, str]
        if isinstance(self.tiktok, Unset):
            tiktok = UNSET
        else:
            tiktok = self.tiktok

        youtube: Union[None, Unset, str]
        if isinstance(self.youtube, Unset):
            youtube = UNSET
        else:
            youtube = self.youtube

        twitter: Union[None, Unset, str]
        if isinstance(self.twitter, Unset):
            twitter = UNSET
        else:
            twitter = self.twitter

        linkedin: Union[None, Unset, str]
        if isinstance(self.linkedin, Unset):
            linkedin = UNSET
        else:
            linkedin = self.linkedin

        facebook: Union[None, Unset, str]
        if isinstance(self.facebook, Unset):
            facebook = UNSET
        else:
            facebook = self.facebook

        pinterest: Union[None, Unset, str]
        if isinstance(self.pinterest, Unset):
            pinterest = UNSET
        else:
            pinterest = self.pinterest

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instagram is not UNSET:
            field_dict["instagram"] = instagram
        if tiktok is not UNSET:
            field_dict["tiktok"] = tiktok
        if youtube is not UNSET:
            field_dict["youtube"] = youtube
        if twitter is not UNSET:
            field_dict["twitter"] = twitter
        if linkedin is not UNSET:
            field_dict["linkedin"] = linkedin
        if facebook is not UNSET:
            field_dict["facebook"] = facebook
        if pinterest is not UNSET:
            field_dict["pinterest"] = pinterest

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_instagram(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        instagram = _parse_instagram(d.pop("instagram", UNSET))

        def _parse_tiktok(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tiktok = _parse_tiktok(d.pop("tiktok", UNSET))

        def _parse_youtube(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        youtube = _parse_youtube(d.pop("youtube", UNSET))

        def _parse_twitter(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        twitter = _parse_twitter(d.pop("twitter", UNSET))

        def _parse_linkedin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        linkedin = _parse_linkedin(d.pop("linkedin", UNSET))

        def _parse_facebook(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        facebook = _parse_facebook(d.pop("facebook", UNSET))

        def _parse_pinterest(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pinterest = _parse_pinterest(d.pop("pinterest", UNSET))

        marketing_social_links = cls(
            instagram=instagram,
            tiktok=tiktok,
            youtube=youtube,
            twitter=twitter,
            linkedin=linkedin,
            facebook=facebook,
            pinterest=pinterest,
        )

        marketing_social_links.additional_properties = d
        return marketing_social_links

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
