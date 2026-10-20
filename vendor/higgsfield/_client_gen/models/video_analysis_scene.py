from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VideoAnalysisScene")


@_attrs_define
class VideoAnalysisScene:
    """One detected scene of the storyboard, produced by the analyzer (an LLM) and stored verbatim. The label / shot_type
    taxonomies below are what the analyzer is instructed to emit, not a hard guarantee; additional analyzer-owned fields
    may be present.

        Attributes:
            scene_number (int): 1-based position of the scene within the video.
            timestamp_start (str): Scene start offset, formatted M:SS (e.g. 0:03).
            timestamp_end (str): Scene end offset, formatted M:SS.
            label (str): Functional role of the scene. Typically one of: Opening Hook, Product Information, Product Selling
                Points, Problem Solving, Usage Scenarios, Real Experience, Call to Action — or Analysis Failed for a section
                that could not be analyzed.
            shot_type (Union[None, str]): Camera framing. Typically one of: Extreme Close-Up, Close-Up, Medium Close-Up,
                Medium Shot, POV Shot, Wide Shot. Null for an unanalyzable section.
            visual (str): Detailed description of what is on screen — camera angle/movement, subject actions, product
                placement, lighting, color grading, and background.
            audio (Union[None, str]): Verbatim voiceover/dialogue, or a description of the sound design when there is no
                speech. Null for an unanalyzable section.
    """

    scene_number: int
    timestamp_start: str
    timestamp_end: str
    label: str
    shot_type: Union[None, str]
    visual: str
    audio: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scene_number = self.scene_number

        timestamp_start = self.timestamp_start

        timestamp_end = self.timestamp_end

        label = self.label

        shot_type: Union[None, str]
        shot_type = self.shot_type

        visual = self.visual

        audio: Union[None, str]
        audio = self.audio

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scene_number": scene_number,
                "timestamp_start": timestamp_start,
                "timestamp_end": timestamp_end,
                "label": label,
                "shot_type": shot_type,
                "visual": visual,
                "audio": audio,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scene_number = d.pop("scene_number")

        timestamp_start = d.pop("timestamp_start")

        timestamp_end = d.pop("timestamp_end")

        label = d.pop("label")

        def _parse_shot_type(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        shot_type = _parse_shot_type(d.pop("shot_type"))

        visual = d.pop("visual")

        def _parse_audio(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        audio = _parse_audio(d.pop("audio"))

        video_analysis_scene = cls(
            scene_number=scene_number,
            timestamp_start=timestamp_start,
            timestamp_end=timestamp_end,
            label=label,
            shot_type=shot_type,
            visual=visual,
            audio=audio,
        )

        video_analysis_scene.additional_properties = d
        return video_analysis_scene

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
