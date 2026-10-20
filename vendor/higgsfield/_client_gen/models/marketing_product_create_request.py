from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.marketing_product_create_request_source import (
    MarketingProductCreateRequestSource,
    check_marketing_product_create_request_source,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.marketing_product_create_request_screenshots_item import (
        MarketingProductCreateRequestScreenshotsItem,
    )
    from ..models.media_input import MediaInput


T = TypeVar("T", bound="MarketingProductCreateRequest")


@_attrs_define
class MarketingProductCreateRequest:
    """Create a product. source selects the data origin and the resulting product type — media (physical, from uploaded
    media — sync), product_url (physical, scraped from a product page — async), web_url (web, scraped from a landing
    page — async), web_media (web, from uploaded screenshots — sync).

        Attributes:
            source (MarketingProductCreateRequestSource):
            image_references (Union[Unset, list['MediaInput']]): Flat media references ({id, type}) for the product gallery.
                Required when source is media.
            screenshots (Union[Unset, list['MarketingProductCreateRequestScreenshotsItem']]): Uploaded web-product
                screenshots, each with its viewport. Required when source is web_media.
            title (Union[None, Unset, str]): Required when source is media.
            subtitle (Union[None, Unset, str]): Optional; web products only.
            description (Union[None, Unset, str]):
            favicon_url (Union[None, Unset, str]): Optional; web products only.
            url (Union[None, Unset, str]): Required when source is product_url or web_url; optional for web_media.
            folder_id (Union[None, UUID, Unset]): Optional folder for the created product (scrape sources).
    """

    source: MarketingProductCreateRequestSource
    image_references: Union[Unset, list["MediaInput"]] = UNSET
    screenshots: Union[Unset, list["MarketingProductCreateRequestScreenshotsItem"]] = UNSET
    title: Union[None, Unset, str] = UNSET
    subtitle: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    favicon_url: Union[None, Unset, str] = UNSET
    url: Union[None, Unset, str] = UNSET
    folder_id: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source: str = self.source

        image_references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.image_references, Unset):
            image_references = []
            for image_references_item_data in self.image_references:
                image_references_item = image_references_item_data.to_dict()
                image_references.append(image_references_item)

        screenshots: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.screenshots, Unset):
            screenshots = []
            for screenshots_item_data in self.screenshots:
                screenshots_item = screenshots_item_data.to_dict()
                screenshots.append(screenshots_item)

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

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        folder_id: Union[None, Unset, str]
        if isinstance(self.folder_id, Unset):
            folder_id = UNSET
        elif isinstance(self.folder_id, UUID):
            folder_id = str(self.folder_id)
        else:
            folder_id = self.folder_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
            }
        )
        if image_references is not UNSET:
            field_dict["image_references"] = image_references
        if screenshots is not UNSET:
            field_dict["screenshots"] = screenshots
        if title is not UNSET:
            field_dict["title"] = title
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if description is not UNSET:
            field_dict["description"] = description
        if favicon_url is not UNSET:
            field_dict["favicon_url"] = favicon_url
        if url is not UNSET:
            field_dict["url"] = url
        if folder_id is not UNSET:
            field_dict["folder_id"] = folder_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.marketing_product_create_request_screenshots_item import (
            MarketingProductCreateRequestScreenshotsItem,
        )
        from ..models.media_input import MediaInput

        d = dict(src_dict)
        source = check_marketing_product_create_request_source(d.pop("source"))

        image_references = []
        _image_references = d.pop("image_references", UNSET)
        for image_references_item_data in _image_references or []:
            image_references_item = MediaInput.from_dict(image_references_item_data)

            image_references.append(image_references_item)

        screenshots = []
        _screenshots = d.pop("screenshots", UNSET)
        for screenshots_item_data in _screenshots or []:
            screenshots_item = MarketingProductCreateRequestScreenshotsItem.from_dict(
                screenshots_item_data
            )

            screenshots.append(screenshots_item)

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

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_folder_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                folder_id_type_0 = UUID(data)

                return folder_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        folder_id = _parse_folder_id(d.pop("folder_id", UNSET))

        marketing_product_create_request = cls(
            source=source,
            image_references=image_references,
            screenshots=screenshots,
            title=title,
            subtitle=subtitle,
            description=description,
            favicon_url=favicon_url,
            url=url,
            folder_id=folder_id,
        )

        marketing_product_create_request.additional_properties = d
        return marketing_product_create_request

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
