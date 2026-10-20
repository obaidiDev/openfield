from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.media_role import MediaRole, check_media_role

if TYPE_CHECKING:
    from ..models.media_data import MediaData


T = TypeVar("T", bound="Media")


@_attrs_define
class Media:
    """A reference to an uploaded/imported media asset used as a generation input. Upload or import the asset first (media
    endpoints), then reference it here by id. Which roles are valid depends on the model.

        Attributes:
            role (MediaRole): Role this asset plays in the request.
            data (MediaData):
    """

    role: MediaRole
    data: "MediaData"

    def to_dict(self) -> dict[str, Any]:
        role: str = self.role

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "role": role,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_data import MediaData

        d = dict(src_dict)
        role = check_media_role(d.pop("role"))

        data = MediaData.from_dict(d.pop("data"))

        media = cls(
            role=role,
            data=data,
        )

        return media
