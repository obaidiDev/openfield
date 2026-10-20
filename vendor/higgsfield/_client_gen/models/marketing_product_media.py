from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.marketing_product_media_viewport_type_1 import (
    MarketingProductMediaViewportType1,
    check_marketing_product_media_viewport_type_1,
)
from ..models.marketing_product_media_viewport_type_2_type_1 import (
    MarketingProductMediaViewportType2Type1,
    check_marketing_product_media_viewport_type_2_type_1,
)
from ..models.marketing_product_media_viewport_type_3_type_1 import (
    MarketingProductMediaViewportType3Type1,
    check_marketing_product_media_viewport_type_3_type_1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketingProductMedia")


@_attrs_define
class MarketingProductMedia:
    """A media item attached to a product — a MediaInput-backed gallery image (physical products) or a desktop/mobile
    screenshot (web products).

        Attributes:
            url (str):
            is_primary (bool): Whether this is the product's primary image (gallery only).
            sort_order (int): Display order of the image.
            media_input_id (Union[None, Unset, str]): The media-input id (gallery images); null for web screenshots.
            viewport (Union[MarketingProductMediaViewportType1, MarketingProductMediaViewportType2Type1,
                MarketingProductMediaViewportType3Type1, None, Unset]): Screenshot form factor for web products; null for
                gallery images.
    """

    url: str
    is_primary: bool
    sort_order: int
    media_input_id: Union[None, Unset, str] = UNSET
    viewport: Union[
        MarketingProductMediaViewportType1,
        MarketingProductMediaViewportType2Type1,
        MarketingProductMediaViewportType3Type1,
        None,
        Unset,
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        is_primary = self.is_primary

        sort_order = self.sort_order

        media_input_id: Union[None, Unset, str]
        if isinstance(self.media_input_id, Unset):
            media_input_id = UNSET
        else:
            media_input_id = self.media_input_id

        viewport: Union[None, Unset, str]
        if isinstance(self.viewport, Unset):
            viewport = UNSET
        elif isinstance(self.viewport, str):
            viewport = self.viewport
        elif isinstance(self.viewport, str):
            viewport = self.viewport
        elif isinstance(self.viewport, str):
            viewport = self.viewport
        else:
            viewport = self.viewport

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "is_primary": is_primary,
                "sort_order": sort_order,
            }
        )
        if media_input_id is not UNSET:
            field_dict["media_input_id"] = media_input_id
        if viewport is not UNSET:
            field_dict["viewport"] = viewport

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        is_primary = d.pop("is_primary")

        sort_order = d.pop("sort_order")

        def _parse_media_input_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        media_input_id = _parse_media_input_id(d.pop("media_input_id", UNSET))

        def _parse_viewport(
            data: object,
        ) -> Union[
            MarketingProductMediaViewportType1,
            MarketingProductMediaViewportType2Type1,
            MarketingProductMediaViewportType3Type1,
            None,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                viewport_type_1 = check_marketing_product_media_viewport_type_1(data)

                return viewport_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                viewport_type_2_type_1 = check_marketing_product_media_viewport_type_2_type_1(data)

                return viewport_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                viewport_type_3_type_1 = check_marketing_product_media_viewport_type_3_type_1(data)

                return viewport_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    MarketingProductMediaViewportType1,
                    MarketingProductMediaViewportType2Type1,
                    MarketingProductMediaViewportType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        viewport = _parse_viewport(d.pop("viewport", UNSET))

        marketing_product_media = cls(
            url=url,
            is_primary=is_primary,
            sort_order=sort_order,
            media_input_id=media_input_id,
            viewport=viewport,
        )

        marketing_product_media.additional_properties = d
        return marketing_product_media

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
