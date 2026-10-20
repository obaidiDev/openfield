from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..models.workflow_generation_params_aspect_ratio import (
    WorkflowGenerationParamsAspectRatio,
    check_workflow_generation_params_aspect_ratio,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_input import MediaInput


T = TypeVar("T", bound="WorkflowGenerationParams")


@_attrs_define
class WorkflowGenerationParams:
    """Parameters for a workflow generation. Provide source media using the public keys advertised by the selected preset's
    inputs, such as image_references or video_references.

        Attributes:
            preset_id (UUID): Id of the CMS workflow preset to apply.
            image_references (Union[Unset, list['MediaInput']]): Source images for image-based workflow presets. The first
                image is the primary reference.
            video_references (Union[Unset, list['MediaInput']]): Source videos for video-based workflow presets such as
                Change light, Change weather, and Change time of day. Uploaded videos use type: video_input.
            aspect_ratio (Union[Unset, WorkflowGenerationParamsAspectRatio]): Aspect ratio applied to generated workflow
                steps.
            duration (Union[Unset, int]): Runtime duration selection accepted by compatible workflow presets.
            resolution (Union[Unset, str]): Runtime resolution selection accepted by compatible workflow presets.
    """

    preset_id: UUID
    image_references: Union[Unset, list["MediaInput"]] = UNSET
    video_references: Union[Unset, list["MediaInput"]] = UNSET
    aspect_ratio: Union[Unset, WorkflowGenerationParamsAspectRatio] = UNSET
    duration: Union[Unset, int] = UNSET
    resolution: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        preset_id = str(self.preset_id)

        image_references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.image_references, Unset):
            image_references = []
            for image_references_item_data in self.image_references:
                image_references_item = image_references_item_data.to_dict()
                image_references.append(image_references_item)

        video_references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.video_references, Unset):
            video_references = []
            for video_references_item_data in self.video_references:
                video_references_item = video_references_item_data.to_dict()
                video_references.append(video_references_item)

        aspect_ratio: Union[Unset, str] = UNSET
        if not isinstance(self.aspect_ratio, Unset):
            aspect_ratio = self.aspect_ratio

        duration = self.duration

        resolution = self.resolution

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "preset_id": preset_id,
            }
        )
        if image_references is not UNSET:
            field_dict["image_references"] = image_references
        if video_references is not UNSET:
            field_dict["video_references"] = video_references
        if aspect_ratio is not UNSET:
            field_dict["aspect_ratio"] = aspect_ratio
        if duration is not UNSET:
            field_dict["duration"] = duration
        if resolution is not UNSET:
            field_dict["resolution"] = resolution

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_input import MediaInput

        d = dict(src_dict)
        preset_id = UUID(d.pop("preset_id"))

        image_references = []
        _image_references = d.pop("image_references", UNSET)
        for image_references_item_data in _image_references or []:
            image_references_item = MediaInput.from_dict(image_references_item_data)

            image_references.append(image_references_item)

        video_references = []
        _video_references = d.pop("video_references", UNSET)
        for video_references_item_data in _video_references or []:
            video_references_item = MediaInput.from_dict(video_references_item_data)

            video_references.append(video_references_item)

        _aspect_ratio = d.pop("aspect_ratio", UNSET)
        aspect_ratio: Union[Unset, WorkflowGenerationParamsAspectRatio]
        if isinstance(_aspect_ratio, Unset):
            aspect_ratio = UNSET
        else:
            aspect_ratio = check_workflow_generation_params_aspect_ratio(_aspect_ratio)

        duration = d.pop("duration", UNSET)

        resolution = d.pop("resolution", UNSET)

        workflow_generation_params = cls(
            preset_id=preset_id,
            image_references=image_references,
            video_references=video_references,
            aspect_ratio=aspect_ratio,
            duration=duration,
            resolution=resolution,
        )

        return workflow_generation_params
