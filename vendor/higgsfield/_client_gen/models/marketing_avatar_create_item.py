from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_input import MediaInput


T = TypeVar("T", bound="MarketingAvatarCreateItem")


@_attrs_define
class MarketingAvatarCreateItem:
    """One avatar to create. Provide the source image via image_references (flat media references, {id, type}); the avatar
    uses the first reference and the server resolves its URL.

        Attributes:
            name (str):
            image_references (list['MediaInput']): Source image reference(s); the avatar uses the first.
            is_pinned (Union[Unset, bool]):  Default: False.
    """

    name: str
    image_references: list["MediaInput"]
    is_pinned: Union[Unset, bool] = False

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        image_references = []
        for image_references_item_data in self.image_references:
            image_references_item = image_references_item_data.to_dict()
            image_references.append(image_references_item)

        is_pinned = self.is_pinned

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "image_references": image_references,
            }
        )
        if is_pinned is not UNSET:
            field_dict["is_pinned"] = is_pinned

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_input import MediaInput

        d = dict(src_dict)
        name = d.pop("name")

        image_references = []
        _image_references = d.pop("image_references")
        for image_references_item_data in _image_references:
            image_references_item = MediaInput.from_dict(image_references_item_data)

            image_references.append(image_references_item)

        is_pinned = d.pop("is_pinned", UNSET)

        marketing_avatar_create_item = cls(
            name=name,
            image_references=image_references,
            is_pinned=is_pinned,
        )

        return marketing_avatar_create_item
