from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_input import MediaInput


T = TypeVar("T", bound="MarketingProductUpdateRequest")


@_attrs_define
class MarketingProductUpdateRequest:
    """Partial update of a product. Only fields valid for the product's type are applied; omitted fields are left
    unchanged.

        Attributes:
            title (Union[None, Unset, str]):
            subtitle (Union[None, Unset, str]): Web products only.
            description (Union[None, Unset, str]):
            favicon_url (Union[None, Unset, str]): Web products only.
            is_pinned (Union[None, Unset, bool]): Web products only.
            image_references (Union[None, Unset, list['MediaInput']]): Replaces the physical product's gallery; flat media
                references ({id, type}).
    """

    title: Union[None, Unset, str] = UNSET
    subtitle: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    favicon_url: Union[None, Unset, str] = UNSET
    is_pinned: Union[None, Unset, bool] = UNSET
    image_references: Union[None, Unset, list["MediaInput"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        subtitle: Union[None, Unset, str]
        if isinstance(self.subtitle, Unset):
            subtitle = UNSET
        else:
            subtitle = self.subtitle

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        favicon_url: Union[None, Unset, str]
        if isinstance(self.favicon_url, Unset):
            favicon_url = UNSET
        else:
            favicon_url = self.favicon_url

        is_pinned: Union[None, Unset, bool]
        if isinstance(self.is_pinned, Unset):
            is_pinned = UNSET
        else:
            is_pinned = self.is_pinned

        image_references: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.image_references, Unset):
            image_references = UNSET
        elif isinstance(self.image_references, list):
            image_references = []
            for image_references_type_0_item_data in self.image_references:
                image_references_type_0_item = image_references_type_0_item_data.to_dict()
                image_references.append(image_references_type_0_item)

        else:
            image_references = self.image_references

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if description is not UNSET:
            field_dict["description"] = description
        if favicon_url is not UNSET:
            field_dict["favicon_url"] = favicon_url
        if is_pinned is not UNSET:
            field_dict["is_pinned"] = is_pinned
        if image_references is not UNSET:
            field_dict["image_references"] = image_references

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_input import MediaInput

        d = dict(src_dict)

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_subtitle(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subtitle = _parse_subtitle(d.pop("subtitle", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_favicon_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        favicon_url = _parse_favicon_url(d.pop("favicon_url", UNSET))

        def _parse_is_pinned(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_pinned = _parse_is_pinned(d.pop("is_pinned", UNSET))

        def _parse_image_references(data: object) -> Union[None, Unset, list["MediaInput"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                image_references_type_0 = []
                _image_references_type_0 = data
                for image_references_type_0_item_data in _image_references_type_0:
                    image_references_type_0_item = MediaInput.from_dict(
                        image_references_type_0_item_data
                    )

                    image_references_type_0.append(image_references_type_0_item)

                return image_references_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["MediaInput"]], data)

        image_references = _parse_image_references(d.pop("image_references", UNSET))

        marketing_product_update_request = cls(
            title=title,
            subtitle=subtitle,
            description=description,
            favicon_url=favicon_url,
            is_pinned=is_pinned,
            image_references=image_references,
        )

        marketing_product_update_request.additional_properties = d
        return marketing_product_update_request

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
