from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_soul_request_type import CreateSoulRequestType, check_create_soul_request_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_input import MediaInput


T = TypeVar("T", bound="CreateSoulRequest")


@_attrs_define
class CreateSoulRequest:
    """Request to train a new Soul ID (soul-v2 custom reference).

    Attributes:
        images (list['MediaInput']): Input images to train the Soul on. Each item is a flat media reference ({id, type})
            — a library upload (media_input) or a prior generation result referenced by its job type (e.g. image_job).
        type_ (Union[Unset, CreateSoulRequestType]): Soul custom-reference type to train. Defaults to soul_2 for
            backwards compatibility. Default: 'soul_2'.
        name (Union[None, Unset, str]): Optional display name for the Soul.
    """

    images: list["MediaInput"]
    type_: Union[Unset, CreateSoulRequestType] = "soul_2"
    name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "images": images,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_input import MediaInput

        d = dict(src_dict)
        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = MediaInput.from_dict(images_item_data)

            images.append(images_item)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, CreateSoulRequestType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_create_soul_request_type(_type_)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        create_soul_request = cls(
            images=images,
            type_=type_,
            name=name,
        )

        create_soul_request.additional_properties = d
        return create_soul_request

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
