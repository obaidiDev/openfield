import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.marketing_brand_kit_status import (
    MarketingBrandKitStatus,
    check_marketing_brand_kit_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketingBrandKitProgress")


@_attrs_define
class MarketingBrandKitProgress:
    """Latest progress of a brand kit extraction pipeline.

    Attributes:
        step (str):
        step_label (str):
        step_index (int):
        total_steps (int):
        progress (float): Fractional progress (0..1).
        status (MarketingBrandKitStatus): Processing status of a brand kit.
        at (datetime.datetime):
        error (Union[None, Unset, str]):
    """

    step: str
    step_label: str
    step_index: int
    total_steps: int
    progress: float
    status: MarketingBrandKitStatus
    at: datetime.datetime
    error: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step = self.step

        step_label = self.step_label

        step_index = self.step_index

        total_steps = self.total_steps

        progress = self.progress

        status: str = self.status

        at = self.at.isoformat()

        error: Union[None, Unset, str]
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "step": step,
                "step_label": step_label,
                "step_index": step_index,
                "total_steps": total_steps,
                "progress": progress,
                "status": status,
                "at": at,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        step = d.pop("step")

        step_label = d.pop("step_label")

        step_index = d.pop("step_index")

        total_steps = d.pop("total_steps")

        progress = d.pop("progress")

        status = check_marketing_brand_kit_status(d.pop("status"))

        at = isoparse(d.pop("at"))

        def _parse_error(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        error = _parse_error(d.pop("error", UNSET))

        marketing_brand_kit_progress = cls(
            step=step,
            step_label=step_label,
            step_index=step_index,
            total_steps=total_steps,
            progress=progress,
            status=status,
            at=at,
            error=error,
        )

        marketing_brand_kit_progress.additional_properties = d
        return marketing_brand_kit_progress

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
