from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ConsentContent")


@_attrs_define
class ConsentContent:
    """Where the client can show the consent document.

    Attributes:
        type_ (str): Content delivery type. Currently url.
        url (str): URL where the user can read the consent document before accepting it.
    """

    type_: str
    url: str

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        url = d.pop("url")

        consent_content = cls(
            type_=type_,
            url=url,
        )

        return consent_content
