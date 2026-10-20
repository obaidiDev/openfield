from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.realtime_image_media_role import (
    RealtimeImageMediaRole,
    check_realtime_image_media_role,
)

if TYPE_CHECKING:
    from ..models.media_input import MediaInput


T = TypeVar("T", bound="RealtimeImageMedia")


@_attrs_define
class RealtimeImageMedia:
    """Image input for a realtime edit.

    Attributes:
        role (RealtimeImageMediaRole):
        data (MediaInput): A reference to an uploaded/imported media asset used as a generation input. Upload or import
            the asset first (media endpoints), then reference it here by id. The asset's ROLE is determined by which
            parameter it is assigned to — start_image, end_image, image_references, video_references, audio_references,
            file_references, or a model-specific media key such as mask_input_image — so this object carries no role field
            of its own.
    """

    role: RealtimeImageMediaRole
    data: "MediaInput"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role: str = self.role

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_input import MediaInput

        d = dict(src_dict)
        role = check_realtime_image_media_role(d.pop("role"))

        data = MediaInput.from_dict(d.pop("data"))

        realtime_image_media = cls(
            role=role,
            data=data,
        )

        realtime_image_media.additional_properties = d
        return realtime_image_media

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
