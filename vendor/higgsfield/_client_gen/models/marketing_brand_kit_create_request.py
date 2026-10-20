from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.marketing_brand_kit_create_request_source import (
    MarketingBrandKitCreateRequestSource,
    check_marketing_brand_kit_create_request_source,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.marketing_brand_kit_data import MarketingBrandKitData


T = TypeVar("T", bound="MarketingBrandKitCreateRequest")


@_attrs_define
class MarketingBrandKitCreateRequest:
    """Create a brand kit. source selects the origin — url scrapes a website (async), manual builds directly from a
    supplied brand-identity payload.

        Attributes:
            source (MarketingBrandKitCreateRequestSource): The data origin for the brand kit.
            url (Union[None, Unset, str]): The brand website URL to scrape. Required when source is url.
            data (Union['MarketingBrandKitData', None, Unset]): The brand-identity payload. Required when source is manual.
    """

    source: MarketingBrandKitCreateRequestSource
    url: Union[None, Unset, str] = UNSET
    data: Union["MarketingBrandKitData", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.marketing_brand_kit_data import MarketingBrandKitData

        source: str = self.source

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, MarketingBrandKitData):
            data = self.data.to_dict()
        else:
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.marketing_brand_kit_data import MarketingBrandKitData

        d = dict(src_dict)
        source = check_marketing_brand_kit_create_request_source(d.pop("source"))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_data(data: object) -> Union["MarketingBrandKitData", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = MarketingBrandKitData.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["MarketingBrandKitData", None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        marketing_brand_kit_create_request = cls(
            source=source,
            url=url,
            data=data,
        )

        marketing_brand_kit_create_request.additional_properties = d
        return marketing_brand_kit_create_request

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
