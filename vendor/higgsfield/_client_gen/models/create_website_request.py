from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_website_request_template import (
    CreateWebsiteRequestTemplate,
    check_create_website_request_template,
)
from ..models.create_website_request_type import (
    CreateWebsiteRequestType,
    check_create_website_request_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWebsiteRequest")


@_attrs_define
class CreateWebsiteRequest:
    """Request to create a website.

    Attributes:
        created_from (str): Which client is creating the website — declared by the caller and recorded by the
            marketplace for analytics. Known clients: 'mcp', 'cli', 'supercomputer'; any short tag is accepted so a new
            client can ship without a backend change.
        category (str): Content category the website is filed under — a slug from the marketplace taxonomy (fetched from
            GET /api/v1/apps/categories; e.g. 'viral-trends', 'ads-marketing', 'ugc-social', 'cinematic', 'characters-
            avatars', 'product-ecommerce', 'portrait-lifestyle', 'other'). The server validates it against the live taxonomy
            and returns 422 for an unknown slug. Pick the closest category for the site being built; use 'other' when
            nothing fits.
        type_ (CreateWebsiteRequestType): Product kind: 'website' = a standalone site with NO higgsfield integration (no
            Sign in with Higgsfield, no requests to higgsfield); 'app' = a product tightly integrated with higgsfield (Sign
            in with Higgsfield + the fnf SDK for image/video generation); 'game' = a browser game with realtime multiplayer
            rooms. Games run on the websites pipeline, so a game is a type here rather than a surface of its own: it takes
            NO template (the server scaffolds the only one a game can use) and DOES need a game-genre category. Defaults to
            'website'.
        subdomain (Union[Unset, str]): Optional agent-chosen subdomain. When set, the website is created with its slug
            equal to this subdomain instead of a random one. The server normalizes and validates it (lowercase, DNS-safe,
            not reserved, unique) and returns 422 for a reserved/malformed label or 409 when it is already taken. Omit it to
            keep the random slug.
        template (Union[Unset, CreateWebsiteRequestTemplate]): Optional starter template the repo is scaffolded from;
            the name encodes which product kind it belongs to. APP templates (type 'app'): 'app-detail', 'preset' and
            'studio' scaffold the app repo from the matching v2 template, and 'custom' is the bare legacy scaffold (recorded
            as metadata only) — required by convention for an app, so pick the closest and use 'custom' only when the user
            explicitly asks. WEBSITE templates (type 'website'): 'scroll-scrub' is the animated website, arriving with its
            scroll-scrub engine already built so the build fills in scenes instead of writing a controller — optional, and
            omitting it gives the plain scaffold. A CROSS-KIND pair (an app template on type 'website', or vice versa) is
            rejected with a 422, as is any name outside this list. Omitted entirely = the legacy scaffold, identical to
            previous releases.
    """

    created_from: str
    category: str
    type_: CreateWebsiteRequestType
    subdomain: Union[Unset, str] = UNSET
    template: Union[Unset, CreateWebsiteRequestTemplate] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_from = self.created_from

        category = self.category

        type_: str = self.type_

        subdomain = self.subdomain

        template: Union[Unset, str] = UNSET
        if not isinstance(self.template, Unset):
            template = self.template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_from": created_from,
                "category": category,
                "type": type_,
            }
        )
        if subdomain is not UNSET:
            field_dict["subdomain"] = subdomain
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_from = d.pop("created_from")

        category = d.pop("category")

        type_ = check_create_website_request_type(d.pop("type"))

        subdomain = d.pop("subdomain", UNSET)

        _template = d.pop("template", UNSET)
        template: Union[Unset, CreateWebsiteRequestTemplate]
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = check_create_website_request_template(_template)

        create_website_request = cls(
            created_from=created_from,
            category=category,
            type_=type_,
            subdomain=subdomain,
            template=template,
        )

        create_website_request.additional_properties = d
        return create_website_request

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
