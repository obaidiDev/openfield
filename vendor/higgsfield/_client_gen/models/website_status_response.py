from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.website_env_status import WebsiteEnvStatus


T = TypeVar("T", bound="WebsiteStatusResponse")


@_attrs_define
class WebsiteStatusResponse:
    """A website's live URL and last deploy status (the preview stage was removed, so there is a single live deploy).

    Attributes:
        production (WebsiteEnvStatus): Deploy status of the live site.
        slug (Union[None, Unset, str]): URL slug of the website.
        listed_in_community (Union[Unset, bool]): Whether the website is currently listed on the community feed.
            Default: False.
        marketplace_url (Union[None, Unset, str]): Public community-feed listing page (per-env). Null when not listed.
        submitted_to_contest (Union[Unset, bool]): Whether the website is currently entered in the app contest. Default:
            False.
        contest_urls (Union[Unset, list[str]]): The social-media links submitted with the contest entry (empty when not
            entered).
    """

    production: "WebsiteEnvStatus"
    slug: Union[None, Unset, str] = UNSET
    listed_in_community: Union[Unset, bool] = False
    marketplace_url: Union[None, Unset, str] = UNSET
    submitted_to_contest: Union[Unset, bool] = False
    contest_urls: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        production = self.production.to_dict()

        slug: Union[None, Unset, str]
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        listed_in_community = self.listed_in_community

        marketplace_url: Union[None, Unset, str]
        if isinstance(self.marketplace_url, Unset):
            marketplace_url = UNSET
        else:
            marketplace_url = self.marketplace_url

        submitted_to_contest = self.submitted_to_contest

        contest_urls: Union[Unset, list[str]] = UNSET
        if not isinstance(self.contest_urls, Unset):
            contest_urls = self.contest_urls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "production": production,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if listed_in_community is not UNSET:
            field_dict["listed_in_community"] = listed_in_community
        if marketplace_url is not UNSET:
            field_dict["marketplace_url"] = marketplace_url
        if submitted_to_contest is not UNSET:
            field_dict["submitted_to_contest"] = submitted_to_contest
        if contest_urls is not UNSET:
            field_dict["contest_urls"] = contest_urls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.website_env_status import WebsiteEnvStatus

        d = dict(src_dict)
        production = WebsiteEnvStatus.from_dict(d.pop("production"))

        def _parse_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slug = _parse_slug(d.pop("slug", UNSET))

        listed_in_community = d.pop("listed_in_community", UNSET)

        def _parse_marketplace_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        marketplace_url = _parse_marketplace_url(d.pop("marketplace_url", UNSET))

        submitted_to_contest = d.pop("submitted_to_contest", UNSET)

        contest_urls = cast(list[str], d.pop("contest_urls", UNSET))

        website_status_response = cls(
            production=production,
            slug=slug,
            listed_in_community=listed_in_community,
            marketplace_url=marketplace_url,
            submitted_to_contest=submitted_to_contest,
            contest_urls=contest_urls,
        )

        website_status_response.additional_properties = d
        return website_status_response

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
