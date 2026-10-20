from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.consent_content import ConsentContent
    from ..models.consent_rules import ConsentRules


T = TypeVar("T", bound="ConsentState")


@_attrs_define
class ConsentState:
    """The authenticated user's acceptance state for one consent document.

    Attributes:
        required_version (int): The version currently required by the service.
        accepted_version (int): The highest version accepted by the user, or zero when never accepted.
        is_accepted (bool): Whether accepted_version satisfies the currently required version.
        title (str): Human-readable consent document title.
        content (ConsentContent): Where the client can show the consent document.
        rules (ConsentRules): Client and server enforcement behavior for this consent.
    """

    required_version: int
    accepted_version: int
    is_accepted: bool
    title: str
    content: "ConsentContent"
    rules: "ConsentRules"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        required_version = self.required_version

        accepted_version = self.accepted_version

        is_accepted = self.is_accepted

        title = self.title

        content = self.content.to_dict()

        rules = self.rules.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "required_version": required_version,
                "accepted_version": accepted_version,
                "is_accepted": is_accepted,
                "title": title,
                "content": content,
                "rules": rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.consent_content import ConsentContent
        from ..models.consent_rules import ConsentRules

        d = dict(src_dict)
        required_version = d.pop("required_version")

        accepted_version = d.pop("accepted_version")

        is_accepted = d.pop("is_accepted")

        title = d.pop("title")

        content = ConsentContent.from_dict(d.pop("content"))

        rules = ConsentRules.from_dict(d.pop("rules"))

        consent_state = cls(
            required_version=required_version,
            accepted_version=accepted_version,
            is_accepted=is_accepted,
            title=title,
            content=content,
            rules=rules,
        )

        consent_state.additional_properties = d
        return consent_state

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
