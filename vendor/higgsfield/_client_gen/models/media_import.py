from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.media_import_status import MediaImportStatus, check_media_import_status
from ..models.media_import_type import MediaImportType, check_media_import_type

T = TypeVar("T", bound="MediaImport")


@_attrs_define
class MediaImport:
    """An imported, confirmed media ready to use as a generation input.

    Attributes:
        id (UUID): The imported media id.
        type_ (MediaImportType): The resolved media kind.
        url (str): Public CloudFront URL the imported media is served from.
        status (MediaImportStatus): Resulting media status after the import safety checks.
    """

    id: UUID
    type_: MediaImportType
    url: str
    status: MediaImportStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_: str = self.type_

        url = self.url

        status: str = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "url": url,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = check_media_import_type(d.pop("type"))

        url = d.pop("url")

        status = check_media_import_status(d.pop("status"))

        media_import = cls(
            id=id,
            type_=type_,
            url=url,
            status=status,
        )

        media_import.additional_properties = d
        return media_import

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
