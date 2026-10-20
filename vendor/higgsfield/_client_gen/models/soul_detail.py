import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.soul_status import SoulStatus, check_soul_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_input import MediaInput


T = TypeVar("T", bound="SoulDetail")


@_attrs_define
class SoulDetail:
    """Soul with its training images, as returned by getSoul and listSouls items. Unlike the createSoul response (Soul),
    this omits user and workspace.

        Attributes:
            id (UUID): Unique Soul identifier.
            type_ (str): The custom-reference type of this Soul (e.g. soul_2, soul_cinematic, soul_v2_preset).
            status (SoulStatus): Training status of a Soul. not_ready is normalized to queued in responses, so callers
                observe queued (waiting in the training queue), in_progress (training running), completed (ready to use),
                failed, or showcase_completed (training done and showcase images generated).
            created_at (datetime.datetime): Creation time (ISO 8601).
            is_shared (bool): Whether the Soul is shareable.
            name (Union[None, Unset, str]): Display name of the Soul.
            fail_reason (Union[None, Unset, str]): Human-readable reason the training failed; null unless status is failed.
            thumbnail_url (Union[None, Unset, str]): URL of the Soul's thumbnail image.
            in_progress_at (Union[None, Unset, float]): Time training entered the in-progress state as a Unix epoch
                timestamp (seconds, fractional); null until training starts.
            images (Union[Unset, list['MediaInput']]): The Soul's training images, each a flat media reference ({id, type}).
    """

    id: UUID
    type_: str
    status: SoulStatus
    created_at: datetime.datetime
    is_shared: bool
    name: Union[None, Unset, str] = UNSET
    fail_reason: Union[None, Unset, str] = UNSET
    thumbnail_url: Union[None, Unset, str] = UNSET
    in_progress_at: Union[None, Unset, float] = UNSET
    images: Union[Unset, list["MediaInput"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_ = self.type_

        status: str = self.status

        created_at = self.created_at.isoformat()

        is_shared = self.is_shared

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        fail_reason: Union[None, Unset, str]
        if isinstance(self.fail_reason, Unset):
            fail_reason = UNSET
        else:
            fail_reason = self.fail_reason

        thumbnail_url: Union[None, Unset, str]
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        in_progress_at: Union[None, Unset, float]
        if isinstance(self.in_progress_at, Unset):
            in_progress_at = UNSET
        else:
            in_progress_at = self.in_progress_at

        images: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "status": status,
                "created_at": created_at,
                "is_shared": is_shared,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if fail_reason is not UNSET:
            field_dict["fail_reason"] = fail_reason
        if thumbnail_url is not UNSET:
            field_dict["thumbnail_url"] = thumbnail_url
        if in_progress_at is not UNSET:
            field_dict["in_progress_at"] = in_progress_at
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_input import MediaInput

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = d.pop("type")

        status = check_soul_status(d.pop("status"))

        created_at = isoparse(d.pop("created_at"))

        is_shared = d.pop("is_shared")

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_fail_reason(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fail_reason = _parse_fail_reason(d.pop("fail_reason", UNSET))

        def _parse_thumbnail_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnail_url", UNSET))

        def _parse_in_progress_at(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        in_progress_at = _parse_in_progress_at(d.pop("in_progress_at", UNSET))

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = MediaInput.from_dict(images_item_data)

            images.append(images_item)

        soul_detail = cls(
            id=id,
            type_=type_,
            status=status,
            created_at=created_at,
            is_shared=is_shared,
            name=name,
            fail_reason=fail_reason,
            thumbnail_url=thumbnail_url,
            in_progress_at=in_progress_at,
            images=images,
        )

        soul_detail.additional_properties = d
        return soul_detail

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
