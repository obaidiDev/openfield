from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reference_element_type import ReferenceElementType, check_reference_element_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_input import MediaInput


T = TypeVar("T", bound="CreateReferenceElementRequest")


@_attrs_define
class CreateReferenceElementRequest:
    """Payload to create a reference element.

    Attributes:
        category (ReferenceElementType): Kind of a reference element. auto is an input-only request value that triggers
            server-side classification; the server then stores and returns one of the auto:* variants. The *_ip_verified
            variants are reserved for elements sourced from IP-verified soul jobs.
        name (Union[None, Unset, str]): Display name (max 128 chars). Spaces are replaced with hyphens. When omitted,
            the name is auto-derived from the source job of the first media.
        description (Union[None, Unset, str]):
        images (Union[Unset, list['MediaInput']]): Image media for the element. The first image is what most models
            inject as the reference; AUTO classification reads up to the first 3.
        videos (Union[Unset, list['MediaInput']]): Video media for the element.
        audios (Union[Unset, list['MediaInput']]): Audio media for the element, for voice elements.
    """

    category: ReferenceElementType
    name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    images: Union[Unset, list["MediaInput"]] = UNSET
    videos: Union[Unset, list["MediaInput"]] = UNSET
    audios: Union[Unset, list["MediaInput"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category: str = self.category

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        images: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        videos: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.videos, Unset):
            videos = []
            for videos_item_data in self.videos:
                videos_item = videos_item_data.to_dict()
                videos.append(videos_item)

        audios: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.audios, Unset):
            audios = []
            for audios_item_data in self.audios:
                audios_item = audios_item_data.to_dict()
                audios.append(audios_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if images is not UNSET:
            field_dict["images"] = images
        if videos is not UNSET:
            field_dict["videos"] = videos
        if audios is not UNSET:
            field_dict["audios"] = audios

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_input import MediaInput

        d = dict(src_dict)
        category = check_reference_element_type(d.pop("category"))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = MediaInput.from_dict(images_item_data)

            images.append(images_item)

        videos = []
        _videos = d.pop("videos", UNSET)
        for videos_item_data in _videos or []:
            videos_item = MediaInput.from_dict(videos_item_data)

            videos.append(videos_item)

        audios = []
        _audios = d.pop("audios", UNSET)
        for audios_item_data in _audios or []:
            audios_item = MediaInput.from_dict(audios_item_data)

            audios.append(audios_item)

        create_reference_element_request = cls(
            category=category,
            name=name,
            description=description,
            images=images,
            videos=videos,
            audios=audios,
        )

        create_reference_element_request.additional_properties = d
        return create_reference_element_request

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
