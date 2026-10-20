from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.marketing_brand_color import MarketingBrandColor
    from ..models.marketing_brand_font import MarketingBrandFont
    from ..models.marketing_brand_image import MarketingBrandImage
    from ..models.marketing_social_links import MarketingSocialLinks


T = TypeVar("T", bound="MarketingBrandKitData")


@_attrs_define
class MarketingBrandKitData:
    """A brand's identity data. All fields are optional and unknown extra fields are preserved. Used both as a brand kit's
    data and as the create/update request body.

        Attributes:
            brand_name (Union[None, Unset, str]):
            website_url (Union[None, Unset, str]):
            logo (Union[None, Unset, str]):
            business_overview (Union[None, Unset, str]):
            short_description (Union[None, Unset, str]):
            tagline (Union[None, Unset, str]):
            fonts (Union[Unset, list['MarketingBrandFont']]):
            colors (Union[Unset, list['MarketingBrandColor']]):
            brand_values (Union[Unset, list[str]]):
            brand_aesthetics (Union[Unset, list[str]]):
            tone_of_voice (Union[Unset, list[str]]):
            products_or_services (Union[Unset, list[str]]):
            images (Union[Unset, list['MarketingBrandImage']]):
            social_links (Union[Unset, MarketingSocialLinks]): Brand social links. Unknown extra fields are preserved.
            keywords (Union[Unset, list[str]]):
            industry (Union[None, Unset, str]):
            company_type (Union[None, Unset, str]):
            detected_language (Union[None, Unset, str]):
    """

    brand_name: Union[None, Unset, str] = UNSET
    website_url: Union[None, Unset, str] = UNSET
    logo: Union[None, Unset, str] = UNSET
    business_overview: Union[None, Unset, str] = UNSET
    short_description: Union[None, Unset, str] = UNSET
    tagline: Union[None, Unset, str] = UNSET
    fonts: Union[Unset, list["MarketingBrandFont"]] = UNSET
    colors: Union[Unset, list["MarketingBrandColor"]] = UNSET
    brand_values: Union[Unset, list[str]] = UNSET
    brand_aesthetics: Union[Unset, list[str]] = UNSET
    tone_of_voice: Union[Unset, list[str]] = UNSET
    products_or_services: Union[Unset, list[str]] = UNSET
    images: Union[Unset, list["MarketingBrandImage"]] = UNSET
    social_links: Union[Unset, "MarketingSocialLinks"] = UNSET
    keywords: Union[Unset, list[str]] = UNSET
    industry: Union[None, Unset, str] = UNSET
    company_type: Union[None, Unset, str] = UNSET
    detected_language: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brand_name: Union[None, Unset, str]
        if isinstance(self.brand_name, Unset):
            brand_name = UNSET
        else:
            brand_name = self.brand_name

        website_url: Union[None, Unset, str]
        if isinstance(self.website_url, Unset):
            website_url = UNSET
        else:
            website_url = self.website_url

        logo: Union[None, Unset, str]
        if isinstance(self.logo, Unset):
            logo = UNSET
        else:
            logo = self.logo

        business_overview: Union[None, Unset, str]
        if isinstance(self.business_overview, Unset):
            business_overview = UNSET
        else:
            business_overview = self.business_overview

        short_description: Union[None, Unset, str]
        if isinstance(self.short_description, Unset):
            short_description = UNSET
        else:
            short_description = self.short_description

        tagline: Union[None, Unset, str]
        if isinstance(self.tagline, Unset):
            tagline = UNSET
        else:
            tagline = self.tagline

        fonts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fonts, Unset):
            fonts = []
            for fonts_item_data in self.fonts:
                fonts_item = fonts_item_data.to_dict()
                fonts.append(fonts_item)

        colors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.colors, Unset):
            colors = []
            for colors_item_data in self.colors:
                colors_item = colors_item_data.to_dict()
                colors.append(colors_item)

        brand_values: Union[Unset, list[str]] = UNSET
        if not isinstance(self.brand_values, Unset):
            brand_values = self.brand_values

        brand_aesthetics: Union[Unset, list[str]] = UNSET
        if not isinstance(self.brand_aesthetics, Unset):
            brand_aesthetics = self.brand_aesthetics

        tone_of_voice: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tone_of_voice, Unset):
            tone_of_voice = self.tone_of_voice

        products_or_services: Union[Unset, list[str]] = UNSET
        if not isinstance(self.products_or_services, Unset):
            products_or_services = self.products_or_services

        images: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        social_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.social_links, Unset):
            social_links = self.social_links.to_dict()

        keywords: Union[Unset, list[str]] = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        industry: Union[None, Unset, str]
        if isinstance(self.industry, Unset):
            industry = UNSET
        else:
            industry = self.industry

        company_type: Union[None, Unset, str]
        if isinstance(self.company_type, Unset):
            company_type = UNSET
        else:
            company_type = self.company_type

        detected_language: Union[None, Unset, str]
        if isinstance(self.detected_language, Unset):
            detected_language = UNSET
        else:
            detected_language = self.detected_language

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if brand_name is not UNSET:
            field_dict["brand_name"] = brand_name
        if website_url is not UNSET:
            field_dict["website_url"] = website_url
        if logo is not UNSET:
            field_dict["logo"] = logo
        if business_overview is not UNSET:
            field_dict["business_overview"] = business_overview
        if short_description is not UNSET:
            field_dict["short_description"] = short_description
        if tagline is not UNSET:
            field_dict["tagline"] = tagline
        if fonts is not UNSET:
            field_dict["fonts"] = fonts
        if colors is not UNSET:
            field_dict["colors"] = colors
        if brand_values is not UNSET:
            field_dict["brand_values"] = brand_values
        if brand_aesthetics is not UNSET:
            field_dict["brand_aesthetics"] = brand_aesthetics
        if tone_of_voice is not UNSET:
            field_dict["tone_of_voice"] = tone_of_voice
        if products_or_services is not UNSET:
            field_dict["products_or_services"] = products_or_services
        if images is not UNSET:
            field_dict["images"] = images
        if social_links is not UNSET:
            field_dict["social_links"] = social_links
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if industry is not UNSET:
            field_dict["industry"] = industry
        if company_type is not UNSET:
            field_dict["company_type"] = company_type
        if detected_language is not UNSET:
            field_dict["detected_language"] = detected_language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.marketing_brand_color import MarketingBrandColor
        from ..models.marketing_brand_font import MarketingBrandFont
        from ..models.marketing_brand_image import MarketingBrandImage
        from ..models.marketing_social_links import MarketingSocialLinks

        d = dict(src_dict)

        def _parse_brand_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        brand_name = _parse_brand_name(d.pop("brand_name", UNSET))

        def _parse_website_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        website_url = _parse_website_url(d.pop("website_url", UNSET))

        def _parse_logo(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo = _parse_logo(d.pop("logo", UNSET))

        def _parse_business_overview(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        business_overview = _parse_business_overview(d.pop("business_overview", UNSET))

        def _parse_short_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        short_description = _parse_short_description(d.pop("short_description", UNSET))

        def _parse_tagline(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tagline = _parse_tagline(d.pop("tagline", UNSET))

        fonts = []
        _fonts = d.pop("fonts", UNSET)
        for fonts_item_data in _fonts or []:
            fonts_item = MarketingBrandFont.from_dict(fonts_item_data)

            fonts.append(fonts_item)

        colors = []
        _colors = d.pop("colors", UNSET)
        for colors_item_data in _colors or []:
            colors_item = MarketingBrandColor.from_dict(colors_item_data)

            colors.append(colors_item)

        brand_values = cast(list[str], d.pop("brand_values", UNSET))

        brand_aesthetics = cast(list[str], d.pop("brand_aesthetics", UNSET))

        tone_of_voice = cast(list[str], d.pop("tone_of_voice", UNSET))

        products_or_services = cast(list[str], d.pop("products_or_services", UNSET))

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = MarketingBrandImage.from_dict(images_item_data)

            images.append(images_item)

        _social_links = d.pop("social_links", UNSET)
        social_links: Union[Unset, MarketingSocialLinks]
        if isinstance(_social_links, Unset):
            social_links = UNSET
        else:
            social_links = MarketingSocialLinks.from_dict(_social_links)

        keywords = cast(list[str], d.pop("keywords", UNSET))

        def _parse_industry(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        industry = _parse_industry(d.pop("industry", UNSET))

        def _parse_company_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_type = _parse_company_type(d.pop("company_type", UNSET))

        def _parse_detected_language(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        detected_language = _parse_detected_language(d.pop("detected_language", UNSET))

        marketing_brand_kit_data = cls(
            brand_name=brand_name,
            website_url=website_url,
            logo=logo,
            business_overview=business_overview,
            short_description=short_description,
            tagline=tagline,
            fonts=fonts,
            colors=colors,
            brand_values=brand_values,
            brand_aesthetics=brand_aesthetics,
            tone_of_voice=tone_of_voice,
            products_or_services=products_or_services,
            images=images,
            social_links=social_links,
            keywords=keywords,
            industry=industry,
            company_type=company_type,
            detected_language=detected_language,
        )

        marketing_brand_kit_data.additional_properties = d
        return marketing_brand_kit_data

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
