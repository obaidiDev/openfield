from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.realtime_aspect_ratio import RealtimeAspectRatio, check_realtime_aspect_ratio
from ..models.realtime_mode import RealtimeMode, check_realtime_mode
from ..models.realtime_resolution import RealtimeResolution, check_realtime_resolution
from ..types import UNSET, Unset

T = TypeVar("T", bound="RealtimeChainCostRequest")


@_attrs_define
class RealtimeChainCostRequest:
    """Request to estimate one realtime Flux Klein edit.

    Attributes:
        resolution (RealtimeResolution): Output resolution tier.
        aspect_ratio (RealtimeAspectRatio): Output aspect ratio for realtime Flux Klein edits.
        mode (Union[Unset, RealtimeMode]): Flux Klein realtime model mode.
    """

    resolution: RealtimeResolution
    aspect_ratio: RealtimeAspectRatio
    mode: Union[Unset, RealtimeMode] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resolution: str = self.resolution

        aspect_ratio: str = self.aspect_ratio

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resolution": resolution,
                "aspect_ratio": aspect_ratio,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resolution = check_realtime_resolution(d.pop("resolution"))

        aspect_ratio = check_realtime_aspect_ratio(d.pop("aspect_ratio"))

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, RealtimeMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = check_realtime_mode(_mode)

        realtime_chain_cost_request = cls(
            resolution=resolution,
            aspect_ratio=aspect_ratio,
            mode=mode,
        )

        realtime_chain_cost_request.additional_properties = d
        return realtime_chain_cost_request

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
