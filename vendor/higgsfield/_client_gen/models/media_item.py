import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.media_item_type import MediaItemType, check_media_item_type

T = TypeVar("T", bound="MediaItem")


@_attrs_define
class MediaItem:
    """A single media item in a listing.

    Attributes:
        id (UUID): The media id.
        type_ (MediaItemType): The media kind.
        url (str): Public CloudFront URL the media is served from.
        created_at (datetime.datetime): Creation time (ISO 8601).
    """

    id: UUID
    type_: MediaItemType
    url: str
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_: str = self.type_

        url = self.url

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "url": url,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = check_media_item_type(d.pop("type"))

        url = d.pop("url")

        created_at = isoparse(d.pop("created_at"))

        media_item = cls(
            id=id,
            type_=type_,
            url=url,
            created_at=created_at,
        )

        media_item.additional_properties = d
        return media_item

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
