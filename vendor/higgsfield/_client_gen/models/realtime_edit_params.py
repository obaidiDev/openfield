from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.realtime_aspect_ratio import RealtimeAspectRatio, check_realtime_aspect_ratio
from ..models.realtime_mode import RealtimeMode, check_realtime_mode
from ..models.realtime_resolution import RealtimeResolution, check_realtime_resolution
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.realtime_image_media import RealtimeImageMedia
    from ..models.realtime_settings import RealtimeSettings


T = TypeVar("T", bound="RealtimeEditParams")


@_attrs_define
class RealtimeEditParams:
    """Realtime Flux Klein edit params. Exactly one of prompt or settings is required.

    Attributes:
        resolution (RealtimeResolution): Output resolution tier.
        aspect_ratio (RealtimeAspectRatio): Output aspect ratio for realtime Flux Klein edits.
        medias (list['RealtimeImageMedia']): Source images for this realtime edit.
        prompt (Union[None, Unset, str]): Free-form edit prompt. Required when settings is omitted.
        settings (Union['RealtimeSettings', None, Unset]): Structured realtime controls. Required when prompt is
            omitted.
        mode (Union[Unset, RealtimeMode]): Flux Klein realtime model mode.
    """

    resolution: RealtimeResolution
    aspect_ratio: RealtimeAspectRatio
    medias: list["RealtimeImageMedia"]
    prompt: Union[None, Unset, str] = UNSET
    settings: Union["RealtimeSettings", None, Unset] = UNSET
    mode: Union[Unset, RealtimeMode] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.realtime_settings import RealtimeSettings

        resolution: str = self.resolution

        aspect_ratio: str = self.aspect_ratio

        medias = []
        for medias_item_data in self.medias:
            medias_item = medias_item_data.to_dict()
            medias.append(medias_item)

        prompt: Union[None, Unset, str]
        if isinstance(self.prompt, Unset):
            prompt = UNSET
        else:
            prompt = self.prompt

        settings: Union[None, Unset, dict[str, Any]]
        if isinstance(self.settings, Unset):
            settings = UNSET
        elif isinstance(self.settings, RealtimeSettings):
            settings = self.settings.to_dict()
        else:
            settings = self.settings

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resolution": resolution,
                "aspect_ratio": aspect_ratio,
                "medias": medias,
            }
        )
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if settings is not UNSET:
            field_dict["settings"] = settings
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.realtime_image_media import RealtimeImageMedia
        from ..models.realtime_settings import RealtimeSettings

        d = dict(src_dict)
        resolution = check_realtime_resolution(d.pop("resolution"))

        aspect_ratio = check_realtime_aspect_ratio(d.pop("aspect_ratio"))

        medias = []
        _medias = d.pop("medias")
        for medias_item_data in _medias:
            medias_item = RealtimeImageMedia.from_dict(medias_item_data)

            medias.append(medias_item)

        def _parse_prompt(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        prompt = _parse_prompt(d.pop("prompt", UNSET))

        def _parse_settings(data: object) -> Union["RealtimeSettings", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_type_0 = RealtimeSettings.from_dict(data)

                return settings_type_0
            except:  # noqa: E722
                pass
            return cast(Union["RealtimeSettings", None, Unset], data)

        settings = _parse_settings(d.pop("settings", UNSET))

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, RealtimeMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = check_realtime_mode(_mode)

        realtime_edit_params = cls(
            resolution=resolution,
            aspect_ratio=aspect_ratio,
            medias=medias,
            prompt=prompt,
            settings=settings,
            mode=mode,
        )

        realtime_edit_params.additional_properties = d
        return realtime_edit_params

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
