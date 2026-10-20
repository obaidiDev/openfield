from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebsiteContestParticipateRequest")


@_attrs_define
class WebsiteContestParticipateRequest:
    """Enter a website in the current app contest with its social-media promo links.

    Attributes:
        urls (list[str]): Social-media links promoting the website (YouTube / X-Twitter / Instagram / TikTok). At least
            one, at most ten.
    """

    urls: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        urls = self.urls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "urls": urls,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        urls = cast(list[str], d.pop("urls"))

        website_contest_participate_request = cls(
            urls=urls,
        )

        website_contest_participate_request.additional_properties = d
        return website_contest_participate_request

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
