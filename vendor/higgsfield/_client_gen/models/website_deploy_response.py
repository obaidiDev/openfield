from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebsiteDeployResponse")


@_attrs_define
class WebsiteDeployResponse:
    """Outcome of a website deploy.

    Attributes:
        status (str): deployed (live at url), failed (see error), or pending (CI still running).
        url (Union[None, Unset, str]): Live URL when the deploy succeeded.
        slug (Union[None, Unset, str]): URL slug of the website.
        error (Union[None, Unset, str]): Build log / error when the deploy failed.
    """

    status: str
    url: Union[None, Unset, str] = UNSET
    slug: Union[None, Unset, str] = UNSET
    error: Union[None, Unset, str] = UNSET
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

        website_deploy_response = cls(
            status=status,
            url=url,
            slug=slug,
            error=error,
        )

        website_deploy_response.additional_properties = d
        return website_deploy_response

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
