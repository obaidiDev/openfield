from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebsiteRenameResponse")


@_attrs_define
class WebsiteRenameResponse:
    """Outcome of a rename: the website is live at 'url' under 'slug'; the old subdomain stops working. A no-op rename
    (same slug) returns old_slug == slug.

        Attributes:
            slug (str): The website's subdomain after the rename.
            old_slug (Union[None, Unset, str]): The subdomain the website had before the rename.
            url (Union[None, Unset, str]): Live URL under the new subdomain.
    """

    slug: str
    old_slug: Union[None, Unset, str] = UNSET
    url: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        old_slug: Union[None, Unset, str]
        if isinstance(self.old_slug, Unset):
            old_slug = UNSET
        else:
            old_slug = self.old_slug

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
            }
        )
        if old_slug is not UNSET:
            field_dict["old_slug"] = old_slug
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")

        def _parse_old_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        old_slug = _parse_old_slug(d.pop("old_slug", UNSET))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        website_rename_response = cls(
            slug=slug,
            old_slug=old_slug,
            url=url,
        )

        website_rename_response.additional_properties = d
        return website_rename_response

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
