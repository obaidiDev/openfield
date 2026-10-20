from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.website_secrets_response_secrets import WebsiteSecretsResponseSecrets


T = TypeVar("T", bound="WebsiteSecretsResponse")


@_attrs_define
class WebsiteSecretsResponse:
    """The website's secrets as a {name: value} map.

    Attributes:
        secrets (WebsiteSecretsResponseSecrets): Secret name to value.
    """

    secrets: "WebsiteSecretsResponseSecrets"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secrets = self.secrets.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secrets": secrets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.website_secrets_response_secrets import WebsiteSecretsResponseSecrets

        d = dict(src_dict)
        secrets = WebsiteSecretsResponseSecrets.from_dict(d.pop("secrets"))

        website_secrets_response = cls(
            secrets=secrets,
        )

        website_secrets_response.additional_properties = d
        return website_secrets_response

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
