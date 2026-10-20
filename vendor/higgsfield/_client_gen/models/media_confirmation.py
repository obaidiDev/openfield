from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.media_confirmation_status import (
    MediaConfirmationStatus,
    check_media_confirmation_status,
)

T = TypeVar("T", bound="MediaConfirmation")


@_attrs_define
class MediaConfirmation:
    """Result of finalizing a media upload.

    Attributes:
        id (UUID): The confirmed media id.
        status (MediaConfirmationStatus): Resulting media status after confirmation.
    """

    id: UUID
    status: MediaConfirmationStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        status: str = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        status = check_media_confirmation_status(d.pop("status"))

        media_confirmation = cls(
            id=id,
            status=status,
        )

        media_confirmation.additional_properties = d
        return media_confirmation

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
