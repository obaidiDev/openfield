from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebsiteCreateResponse")


@_attrs_define
class WebsiteCreateResponse:
    """A newly created website and its git repo.

    Attributes:
        website_id (UUID): The website id. Pass it to every later website call.
        slug (Union[None, Unset, str]): URL slug of the website (also the repo name).
        name (Union[None, Unset, str]): Display name of the website.
        preview_url (Union[None, Unset, str]): Preview URL once deployed.
        production_url (Union[None, Unset, str]): Production URL once deployed.
        type_ (Union[Unset, str]): Product kind: 'website' (no higgsfield integration) or 'app' (Sign in with Higgsfield
            + the fnf SDK). Default: 'website'.
        category (Union[Unset, str]): Content category slug the website is filed under (from the marketplace taxonomy).
            'other' when unspecified. Default: 'other'.
    """

    website_id: UUID
    slug: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    preview_url: Union[None, Unset, str] = UNSET
    production_url: Union[None, Unset, str] = UNSET
    type_: Union[Unset, str] = "website"
    category: Union[Unset, str] = "other"
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

        preview_url: Union[None, Unset, str]
        if isinstance(self.preview_url, Unset):
            preview_url = UNSET
        else:
            preview_url = self.preview_url

        production_url: Union[None, Unset, str]
        if isinstance(self.production_url, Unset):
            production_url = UNSET
        else:
            production_url = self.production_url

        type_ = self.type_

        category = self.category

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
        if preview_url is not UNSET:
            field_dict["preview_url"] = preview_url
        if production_url is not UNSET:
            field_dict["production_url"] = production_url
        if type_ is not UNSET:
            field_dict["type"] = type_
        if category is not UNSET:
            field_dict["category"] = category

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

        def _parse_preview_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        preview_url = _parse_preview_url(d.pop("preview_url", UNSET))

        def _parse_production_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        production_url = _parse_production_url(d.pop("production_url", UNSET))

        type_ = d.pop("type", UNSET)

        category = d.pop("category", UNSET)

        website_create_response = cls(
            website_id=website_id,
            slug=slug,
            name=name,
            preview_url=preview_url,
            production_url=production_url,
            type_=type_,
            category=category,
        )

        website_create_response.additional_properties = d
        return website_create_response

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
