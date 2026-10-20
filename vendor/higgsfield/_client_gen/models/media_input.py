from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="MediaInput")


@_attrs_define
class MediaInput:
    """A reference to an uploaded/imported media asset used as a generation input. Upload or import the asset first (media
    endpoints), then reference it here by id. The asset's ROLE is determined by which parameter it is assigned to —
    start_image, end_image, image_references, video_references, audio_references, file_references, or a model-specific
    media key such as mask_input_image — so this object carries no role field of its own.

        Attributes:
            id (UUID): Id of the uploaded media input (or a prior job that produced the asset).
            type_ (str): Asset source — media_input for an uploaded image, video_input for an uploaded video, audio_input
                for uploaded audio, file_input for uploaded files, or a prior job type. Required (no default): the server's
                media schema requires it, so a reference without type is rejected at the request boundary rather than failing
                the generation.
    """

    id: UUID
    type_: str

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = d.pop("type")

        media_input = cls(
            id=id,
            type_=type_,
        )

        return media_input
