from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.realtime_reference_mode import RealtimeReferenceMode, check_realtime_reference_mode
from ..models.realtime_target import RealtimeTarget, check_realtime_target
from ..types import UNSET, Unset

T = TypeVar("T", bound="RealtimeSettings")


@_attrs_define
class RealtimeSettings:
    """UI-driven realtime style controls. Send either params.prompt or params.settings, not both.

    Attributes:
        style (str): Built-in style key, or custom when using custom_style/custom_style_id.
        custom_style (Union[Unset, str]): Free-form style prompt used when style is custom. Default: ''.
        mood (Union[Unset, str]): Built-in mood key. Default: 'general'.
        palette (Union[Unset, str]): Built-in palette key. Default: 'auto'.
        custom_colors (Union[Unset, list[str]]): Optional custom hex colors.
        sketch_influence (Union[Unset, int]): Strength of the sketch/input structure influence. Default: 50.
        reference_mode (Union[Unset, RealtimeReferenceMode]): How the reference image should influence generation.
        target (Union[Unset, RealtimeTarget]): Whether the edit targets the full canvas or an active selection.
        custom_style_id (Union[None, UUID, Unset]): Saved custom style id to apply.
    """

    style: str
    custom_style: Union[Unset, str] = ""
    mood: Union[Unset, str] = "general"
    palette: Union[Unset, str] = "auto"
    custom_colors: Union[Unset, list[str]] = UNSET
    sketch_influence: Union[Unset, int] = 50
    reference_mode: Union[Unset, RealtimeReferenceMode] = UNSET
    target: Union[Unset, RealtimeTarget] = UNSET
    custom_style_id: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        style = self.style

        custom_style = self.custom_style

        mood = self.mood

        palette = self.palette

        custom_colors: Union[Unset, list[str]] = UNSET
        if not isinstance(self.custom_colors, Unset):
            custom_colors = self.custom_colors

        sketch_influence = self.sketch_influence

        reference_mode: Union[Unset, str] = UNSET
        if not isinstance(self.reference_mode, Unset):
            reference_mode = self.reference_mode

        target: Union[Unset, str] = UNSET
        if not isinstance(self.target, Unset):
            target = self.target

        custom_style_id: Union[None, Unset, str]
        if isinstance(self.custom_style_id, Unset):
            custom_style_id = UNSET
        elif isinstance(self.custom_style_id, UUID):
            custom_style_id = str(self.custom_style_id)
        else:
            custom_style_id = self.custom_style_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "style": style,
            }
        )
        if custom_style is not UNSET:
            field_dict["custom_style"] = custom_style
        if mood is not UNSET:
            field_dict["mood"] = mood
        if palette is not UNSET:
            field_dict["palette"] = palette
        if custom_colors is not UNSET:
            field_dict["custom_colors"] = custom_colors
        if sketch_influence is not UNSET:
            field_dict["sketch_influence"] = sketch_influence
        if reference_mode is not UNSET:
            field_dict["reference_mode"] = reference_mode
        if target is not UNSET:
            field_dict["target"] = target
        if custom_style_id is not UNSET:
            field_dict["custom_style_id"] = custom_style_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        style = d.pop("style")

        custom_style = d.pop("custom_style", UNSET)

        mood = d.pop("mood", UNSET)

        palette = d.pop("palette", UNSET)

        custom_colors = cast(list[str], d.pop("custom_colors", UNSET))

        sketch_influence = d.pop("sketch_influence", UNSET)

        _reference_mode = d.pop("reference_mode", UNSET)
        reference_mode: Union[Unset, RealtimeReferenceMode]
        if isinstance(_reference_mode, Unset):
            reference_mode = UNSET
        else:
            reference_mode = check_realtime_reference_mode(_reference_mode)

        _target = d.pop("target", UNSET)
        target: Union[Unset, RealtimeTarget]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = check_realtime_target(_target)

        def _parse_custom_style_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                custom_style_id_type_0 = UUID(data)

                return custom_style_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        custom_style_id = _parse_custom_style_id(d.pop("custom_style_id", UNSET))

        realtime_settings = cls(
            style=style,
            custom_style=custom_style,
            mood=mood,
            palette=palette,
            custom_colors=custom_colors,
            sketch_influence=sketch_influence,
            reference_mode=reference_mode,
            target=target,
            custom_style_id=custom_style_id,
        )

        realtime_settings.additional_properties = d
        return realtime_settings

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
