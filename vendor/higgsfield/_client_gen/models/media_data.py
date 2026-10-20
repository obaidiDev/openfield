from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="MediaData")


@_attrs_define
class MediaData:
    """
    Attributes:
        id (UUID): Id of the uploaded media input (or a prior job that produced the asset).
        type_ (str): Asset source — media_input for an uploaded image, video_input for an uploaded video, audio_input
            for uploaded audio, file_input for uploaded files, or a prior job type. Required (no default): the server's
            media schema requires it, so a data without type is rejected at the request boundary rather than failing the
            generation.
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

        media_data = cls(
            id=id,
            type_=type_,
        )

        return media_data
