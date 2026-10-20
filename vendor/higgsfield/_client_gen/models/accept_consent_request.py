from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AcceptConsentRequest")


@_attrs_define
class AcceptConsentRequest:
    """The consent document to accept at its currently required version.

    Attributes:
        consent_type (str): Consent type returned as a key in ConsentsState.items. Kept open so existing clients can
            accept newly registered consent types.
    """

    consent_type: str

    def to_dict(self) -> dict[str, Any]:
        consent_type = self.consent_type

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "consent_type": consent_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        consent_type = d.pop("consent_type")

        accept_consent_request = cls(
            consent_type=consent_type,
        )

        return accept_consent_request
