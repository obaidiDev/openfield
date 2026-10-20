from typing import Literal, cast

WorkflowPresetInputId = Literal[
    "audio_references", "file_references", "image_references", "video_references"
]

WORKFLOW_PRESET_INPUT_ID_VALUES: set[WorkflowPresetInputId] = {
    "audio_references",
    "file_references",
    "image_references",
    "video_references",
}


def check_workflow_preset_input_id(value: str) -> WorkflowPresetInputId:
    if value in WORKFLOW_PRESET_INPUT_ID_VALUES:
        return cast(WorkflowPresetInputId, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKFLOW_PRESET_INPUT_ID_VALUES!r}"
    )
