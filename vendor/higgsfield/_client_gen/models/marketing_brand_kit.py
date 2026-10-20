import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.marketing_brand_kit_status import (
    MarketingBrandKitStatus,
    check_marketing_brand_kit_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.marketing_brand_kit_data import MarketingBrandKitData
    from ..models.marketing_brand_kit_progress import MarketingBrandKitProgress


T = TypeVar("T", bound="MarketingBrandKit")


@_attrs_define
class MarketingBrandKit:
    """A brand kit — scraped / agent-extracted brand identity.

    Attributes:
        id (UUID):
        status (MarketingBrandKitStatus): Processing status of a brand kit.
        data (MarketingBrandKitData): A brand's identity data. All fields are optional and unknown extra fields are
            preserved. Used both as a brand kit's data and as the create/update request body.
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        scrap_url (Union[None, Unset, str]): Source URL the brand kit was scraped from.
        screenshot_url (Union[None, Unset, str]):
        error (Union[None, Unset, str]):
        latest_progress (Union['MarketingBrandKitProgress', None, Unset]): Latest pipeline progress, or null.
    """

    id: UUID
    status: MarketingBrandKitStatus
    data: "MarketingBrandKitData"
    created_at: datetime.datetime
    updated_at: datetime.datetime
    scrap_url: Union[None, Unset, str] = UNSET
    screenshot_url: Union[None, Unset, str] = UNSET
    error: Union[None, Unset, str] = UNSET
    latest_progress: Union["MarketingBrandKitProgress", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.marketing_brand_kit_progress import MarketingBrandKitProgress

        id = str(self.id)

        status: str = self.status

        data = self.data.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        scrap_url: Union[None, Unset, str]
        if isinstance(self.scrap_url, Unset):
            scrap_url = UNSET
        else:
            scrap_url = self.scrap_url

        screenshot_url: Union[None, Unset, str]
        if isinstance(self.screenshot_url, Unset):
            screenshot_url = UNSET
        else:
            screenshot_url = self.screenshot_url

        error: Union[None, Unset, str]
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        latest_progress: Union[None, Unset, dict[str, Any]]
        if isinstance(self.latest_progress, Unset):
            latest_progress = UNSET
        elif isinstance(self.latest_progress, MarketingBrandKitProgress):
            latest_progress = self.latest_progress.to_dict()
        else:
            latest_progress = self.latest_progress

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "data": data,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if scrap_url is not UNSET:
            field_dict["scrap_url"] = scrap_url
        if screenshot_url is not UNSET:
            field_dict["screenshot_url"] = screenshot_url
        if error is not UNSET:
            field_dict["error"] = error
        if latest_progress is not UNSET:
            field_dict["latest_progress"] = latest_progress

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.marketing_brand_kit_data import MarketingBrandKitData
        from ..models.marketing_brand_kit_progress import MarketingBrandKitProgress

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        status = check_marketing_brand_kit_status(d.pop("status"))

        data = MarketingBrandKitData.from_dict(d.pop("data"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_scrap_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        scrap_url = _parse_scrap_url(d.pop("scrap_url", UNSET))

        def _parse_screenshot_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        screenshot_url = _parse_screenshot_url(d.pop("screenshot_url", UNSET))

        def _parse_error(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_latest_progress(data: object) -> Union["MarketingBrandKitProgress", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                latest_progress_type_0 = MarketingBrandKitProgress.from_dict(data)

                return latest_progress_type_0
            except:  # noqa: E722
                pass
            return cast(Union["MarketingBrandKitProgress", None, Unset], data)

        latest_progress = _parse_latest_progress(d.pop("latest_progress", UNSET))

        marketing_brand_kit = cls(
            id=id,
            status=status,
            data=data,
            created_at=created_at,
            updated_at=updated_at,
            scrap_url=scrap_url,
            screenshot_url=screenshot_url,
            error=error,
            latest_progress=latest_progress,
        )

        marketing_brand_kit.additional_properties = d
        return marketing_brand_kit

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
