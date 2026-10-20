from typing import Literal, cast

WorkflowPresetInputType = Literal["audio", "file", "image", "video"]

WORKFLOW_PRESET_INPUT_TYPE_VALUES: set[WorkflowPresetInputType] = {
    "audio",
    "file",
    "image",
    "video",
}


def check_workflow_preset_input_type(value: str) -> WorkflowPresetInputType:
    if value in WORKFLOW_PRESET_INPUT_TYPE_VALUES:
        return cast(WorkflowPresetInputType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKFLOW_PRESET_INPUT_TYPE_VALUES!r}"
    )
