import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.marketing_product_status import MarketingProductStatus, check_marketing_product_status
from ..models.marketing_product_type import MarketingProductType, check_marketing_product_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.marketing_product_media import MarketingProductMedia


T = TypeVar("T", bound="MarketingProduct")


@_attrs_define
class MarketingProduct:
    """A Marketing Studio product. type is physical (a tangible product — a gallery of MediaInput images) or web (a landing
    page — desktop/mobile screenshots plus a favicon). type is set from the create source and is immutable.

        Attributes:
            id (UUID):
            type_ (MarketingProductType):
            status (MarketingProductStatus): Processing status of a Marketing Studio product.
            is_pinned (bool):
            medias (list['MarketingProductMedia']):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            title (Union[None, Unset, str]):
            subtitle (Union[None, Unset, str]): Web products only.
            description (Union[None, Unset, str]):
            source_url (Union[None, Unset, str]): Source URL the product was scraped from, when applicable.
            source_url_domain (Union[None, Unset, str]):
            favicon_url (Union[None, Unset, str]): Web products only.
            fail_reason (Union[None, Unset, str]):
            fail_reason_type (Union[None, Unset, str]): Categorized failure reason (physical products; e.g. non_product,
                not_enough_data, ip).
    """

    id: UUID
    type_: MarketingProductType
    status: MarketingProductStatus
    is_pinned: bool
    medias: list["MarketingProductMedia"]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    title: Union[None, Unset, str] = UNSET
    subtitle: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    source_url: Union[None, Unset, str] = UNSET
    source_url_domain: Union[None, Unset, str] = UNSET
    favicon_url: Union[None, Unset, str] = UNSET
    fail_reason: Union[None, Unset, str] = UNSET
    fail_reason_type: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_: str = self.type_

        status: str = self.status

        is_pinned = self.is_pinned

        medias = []
        for medias_item_data in self.medias:
            medias_item = medias_item_data.to_dict()
            medias.append(medias_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

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

        source_url: Union[None, Unset, str]
        if isinstance(self.source_url, Unset):
            source_url = UNSET
        else:
            source_url = self.source_url

        source_url_domain: Union[None, Unset, str]
        if isinstance(self.source_url_domain, Unset):
            source_url_domain = UNSET
        else:
            source_url_domain = self.source_url_domain

        favicon_url: Union[None, Unset, str]
        if isinstance(self.favicon_url, Unset):
            favicon_url = UNSET
        else:
            favicon_url = self.favicon_url

        fail_reason: Union[None, Unset, str]
        if isinstance(self.fail_reason, Unset):
            fail_reason = UNSET
        else:
            fail_reason = self.fail_reason

        fail_reason_type: Union[None, Unset, str]
        if isinstance(self.fail_reason_type, Unset):
            fail_reason_type = UNSET
        else:
            fail_reason_type = self.fail_reason_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "status": status,
                "is_pinned": is_pinned,
                "medias": medias,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if description is not UNSET:
            field_dict["description"] = description
        if source_url is not UNSET:
            field_dict["source_url"] = source_url
        if source_url_domain is not UNSET:
            field_dict["source_url_domain"] = source_url_domain
        if favicon_url is not UNSET:
            field_dict["favicon_url"] = favicon_url
        if fail_reason is not UNSET:
            field_dict["fail_reason"] = fail_reason
        if fail_reason_type is not UNSET:
            field_dict["fail_reason_type"] = fail_reason_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.marketing_product_media import MarketingProductMedia

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = check_marketing_product_type(d.pop("type"))

        status = check_marketing_product_status(d.pop("status"))

        is_pinned = d.pop("is_pinned")

        medias = []
        _medias = d.pop("medias")
        for medias_item_data in _medias:
            medias_item = MarketingProductMedia.from_dict(medias_item_data)

            medias.append(medias_item)

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

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

        def _parse_source_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_url = _parse_source_url(d.pop("source_url", UNSET))

        def _parse_source_url_domain(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_url_domain = _parse_source_url_domain(d.pop("source_url_domain", UNSET))

        def _parse_favicon_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        favicon_url = _parse_favicon_url(d.pop("favicon_url", UNSET))

        def _parse_fail_reason(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fail_reason = _parse_fail_reason(d.pop("fail_reason", UNSET))

        def _parse_fail_reason_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fail_reason_type = _parse_fail_reason_type(d.pop("fail_reason_type", UNSET))

        marketing_product = cls(
            id=id,
            type_=type_,
            status=status,
            is_pinned=is_pinned,
            medias=medias,
            created_at=created_at,
            updated_at=updated_at,
            title=title,
            subtitle=subtitle,
            description=description,
            source_url=source_url,
            source_url_domain=source_url_domain,
            favicon_url=favicon_url,
            fail_reason=fail_reason,
            fail_reason_type=fail_reason_type,
        )

        marketing_product.additional_properties = d
        return marketing_product

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
