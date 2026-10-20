from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.media_upload_slot_type import MediaUploadSlotType, check_media_upload_slot_type

T = TypeVar("T", bound="MediaUploadSlot")


@_attrs_define
class MediaUploadSlot:
    """A freshly minted media upload slot. PUT the raw bytes to upload_url, then call confirmMediaUpload with this id.

    Attributes:
        id (UUID): The created media id. Use this to confirm and later as a generation input.
        type_ (MediaUploadSlotType): The media kind of this slot.
        url (str): Permanent public CloudFront URL the media will be served from once confirmed.
        upload_url (str): Short-lived presigned S3 PUT URL. PUT the raw bytes here directly (outside this API), then
            confirm.
        content_type (str): MIME type that must be sent exactly as the Content-Type header when PUTting bytes to
            upload_url.
    """

    id: UUID
    type_: MediaUploadSlotType
    url: str
    upload_url: str
    content_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_: str = self.type_

        url = self.url

        upload_url = self.upload_url

        content_type = self.content_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "url": url,
                "upload_url": upload_url,
                "content_type": content_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = check_media_upload_slot_type(d.pop("type"))

        url = d.pop("url")

        upload_url = d.pop("upload_url")

        content_type = d.pop("content_type")

        media_upload_slot = cls(
            id=id,
            type_=type_,
            url=url,
            upload_url=upload_url,
            content_type=content_type,
        )

        media_upload_slot.additional_properties = d
        return media_upload_slot

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
