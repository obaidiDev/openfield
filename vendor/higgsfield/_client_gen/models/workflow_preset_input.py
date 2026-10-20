from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.workflow_preset_input_id import WorkflowPresetInputId, check_workflow_preset_input_id
from ..models.workflow_preset_input_type import (
    WorkflowPresetInputType,
    check_workflow_preset_input_type,
)

T = TypeVar("T", bound="WorkflowPresetInput")


@_attrs_define
class WorkflowPresetInput:
    """One media input accepted by a workflow preset. Send media under the id key in params when creating a workflow
    generation.

        Attributes:
            id (WorkflowPresetInputId): Public createWorkflowGeneration params key for this preset input. CMS input slots
                are mapped to these public names, e.g. input_images becomes image_references and input_videos becomes
                video_references.
            type_ (WorkflowPresetInputType): Media kind accepted by a workflow preset input.
            min_items (int): Minimum number of media references required for this input.
            max_items (int): Maximum number of media references accepted for this input.
    """

    id: WorkflowPresetInputId
    type_: WorkflowPresetInputType
    min_items: int
    max_items: int

    def to_dict(self) -> dict[str, Any]:
        id: str = self.id

        type_: str = self.type_

        min_items = self.min_items

        max_items = self.max_items

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "type": type_,
                "min_items": min_items,
                "max_items": max_items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = check_workflow_preset_input_id(d.pop("id"))

        type_ = check_workflow_preset_input_type(d.pop("type"))

        min_items = d.pop("min_items")

        max_items = d.pop("max_items")

        workflow_preset_input = cls(
            id=id,
            type_=type_,
            min_items=min_items,
            max_items=max_items,
        )

        return workflow_preset_input
