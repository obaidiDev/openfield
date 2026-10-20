from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.marketing_image_style_media_type_0 import MarketingImageStyleMediaType0


T = TypeVar("T", bound="MarketingImageStyle")


@_attrs_define
class MarketingImageStyle:
    """A curated Marketing Studio image style.

    Attributes:
        id (str):
        name (str):
        type_ (str): Image-style type / category.
        priority (int): Sort priority.
        media (Union['MarketingImageStyleMediaType0', None]): Thumbnail media object for the style, or null.
    """

    id: str
    name: str
    type_: str
    priority: int
    media: Union["MarketingImageStyleMediaType0", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.marketing_image_style_media_type_0 import MarketingImageStyleMediaType0

        id = self.id

        name = self.name

        type_ = self.type_

        priority = self.priority

        media: Union[None, dict[str, Any]]
        if isinstance(self.media, MarketingImageStyleMediaType0):
            media = self.media.to_dict()
        else:
            media = self.media

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
                "priority": priority,
                "media": media,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.marketing_image_style_media_type_0 import MarketingImageStyleMediaType0

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        type_ = d.pop("type")

        priority = d.pop("priority")

        def _parse_media(data: object) -> Union["MarketingImageStyleMediaType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                media_type_0 = MarketingImageStyleMediaType0.from_dict(data)

                return media_type_0
            except:  # noqa: E722
                pass
            return cast(Union["MarketingImageStyleMediaType0", None], data)

        media = _parse_media(d.pop("media"))

        marketing_image_style = cls(
            id=id,
            name=name,
            type_=type_,
            priority=priority,
            media=media,
        )

        marketing_image_style.additional_properties = d
        return marketing_image_style

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
