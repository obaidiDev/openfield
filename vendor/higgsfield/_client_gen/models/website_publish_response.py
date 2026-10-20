from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebsitePublishResponse")


@_attrs_define
class WebsitePublishResponse:
    """Outcome of a website publish (production deploy + community listing).

    Attributes:
        status (str): deployed (live at url), failed (see error), or pending (CI still running — the website is listed
            automatically once the deploy succeeds).
        url (Union[None, Unset, str]): Live production URL when the deploy succeeded.
        slug (Union[None, Unset, str]): URL slug of the website.
        error (Union[None, Unset, str]): Build log / error when the deploy failed.
        listed_in_community (Union[Unset, bool]): Whether the website is now listed on the community feed. Default:
            False.
        listing_id (Union[None, UUID, Unset]): Community listing id once listed.
        marketplace_url (Union[None, Unset, str]): Public community-feed listing page (per-env). Null until the listing
            exists (a pending publish lists on CI success). Show it to the user.
    """

    status: str
    url: Union[None, Unset, str] = UNSET
    slug: Union[None, Unset, str] = UNSET
    error: Union[None, Unset, str] = UNSET
    listed_in_community: Union[Unset, bool] = False
    listing_id: Union[None, UUID, Unset] = UNSET
    marketplace_url: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        slug: Union[None, Unset, str]
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        error: Union[None, Unset, str]
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        listed_in_community = self.listed_in_community

        listing_id: Union[None, Unset, str]
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        elif isinstance(self.listing_id, UUID):
            listing_id = str(self.listing_id)
        else:
            listing_id = self.listing_id

        marketplace_url: Union[None, Unset, str]
        if isinstance(self.marketplace_url, Unset):
            marketplace_url = UNSET
        else:
            marketplace_url = self.marketplace_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if slug is not UNSET:
            field_dict["slug"] = slug
        if error is not UNSET:
            field_dict["error"] = error
        if listed_in_community is not UNSET:
            field_dict["listed_in_community"] = listed_in_community
        if listing_id is not UNSET:
            field_dict["listing_id"] = listing_id
        if marketplace_url is not UNSET:
            field_dict["marketplace_url"] = marketplace_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_error(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        error = _parse_error(d.pop("error", UNSET))

        listed_in_community = d.pop("listed_in_community", UNSET)

        def _parse_listing_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                listing_id_type_0 = UUID(data)

                return listing_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        listing_id = _parse_listing_id(d.pop("listing_id", UNSET))

        def _parse_marketplace_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        marketplace_url = _parse_marketplace_url(d.pop("marketplace_url", UNSET))

        website_publish_response = cls(
            status=status,
            url=url,
            slug=slug,
            error=error,
            listed_in_community=listed_in_community,
            listing_id=listing_id,
            marketplace_url=marketplace_url,
        )

        website_publish_response.additional_properties = d
        return website_publish_response

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
