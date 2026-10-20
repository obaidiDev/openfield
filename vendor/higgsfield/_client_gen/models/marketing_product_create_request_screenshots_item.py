from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.marketing_product_create_request_screenshots_item_viewport import (
    MarketingProductCreateRequestScreenshotsItemViewport,
    check_marketing_product_create_request_screenshots_item_viewport,
)

if TYPE_CHECKING:
    from ..models.media_input import MediaInput


T = TypeVar("T", bound="MarketingProductCreateRequestScreenshotsItem")


@_attrs_define
class MarketingProductCreateRequestScreenshotsItem:
    """
    Attributes:
        reference (MediaInput): A reference to an uploaded/imported media asset used as a generation input. Upload or
            import the asset first (media endpoints), then reference it here by id. The asset's ROLE is determined by which
            parameter it is assigned to — start_image, end_image, image_references, video_references, audio_references,
            file_references, or a model-specific media key such as mask_input_image — so this object carries no role field
            of its own.
        viewport (MarketingProductCreateRequestScreenshotsItemViewport):
    """

    reference: "MediaInput"
    viewport: MarketingProductCreateRequestScreenshotsItemViewport
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reference = self.reference.to_dict()

        viewport: str = self.viewport

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reference": reference,
                "viewport": viewport,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_input import MediaInput

        d = dict(src_dict)
        reference = MediaInput.from_dict(d.pop("reference"))

        viewport = check_marketing_product_create_request_screenshots_item_viewport(
            d.pop("viewport")
        )

        marketing_product_create_request_screenshots_item = cls(
            reference=reference,
            viewport=viewport,
        )

        marketing_product_create_request_screenshots_item.additional_properties = d
        return marketing_product_create_request_screenshots_item

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
