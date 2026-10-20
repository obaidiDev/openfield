from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebsiteListItem")


@_attrs_define
class WebsiteListItem:
    """One of the caller's websites.

    Attributes:
        website_id (UUID): The website id.
        slug (Union[None, Unset, str]): URL slug of the website.
        name (Union[None, Unset, str]): Display name of the website.
        url (Union[None, Unset, str]): Live URL of the website.
        production_deployed (Union[Unset, bool]): Whether the website has a live production deploy. Default: False.
        created_at (Union[None, Unset, str]): When the website was created (ISO 8601).
        type_ (Union[Unset, str]): Product kind: 'website' (no higgsfield integration) or 'app' (Sign in with Higgsfield
            + the fnf SDK). Default: 'website'.
    """

    website_id: UUID
    slug: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    url: Union[None, Unset, str] = UNSET
    production_deployed: Union[Unset, bool] = False
    created_at: Union[None, Unset, str] = UNSET
    type_: Union[Unset, str] = "website"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        website_id = str(self.website_id)

        slug: Union[None, Unset, str]
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        production_deployed = self.production_deployed

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "website_id": website_id,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if production_deployed is not UNSET:
            field_dict["production_deployed"] = production_deployed
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        website_id = UUID(d.pop("website_id"))

        def _parse_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        production_deployed = d.pop("production_deployed", UNSET)

        def _parse_created_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        type_ = d.pop("type", UNSET)

        website_list_item = cls(
            website_id=website_id,
            slug=slug,
            name=name,
            url=url,
            production_deployed=production_deployed,
            created_at=created_at,
            type_=type_,
        )

        website_list_item.additional_properties = d
        return website_list_item

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
