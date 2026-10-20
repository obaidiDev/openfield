from typing import Literal, cast

WorkflowPresetPreviewMediaType = Literal["image", "video"]

WORKFLOW_PRESET_PREVIEW_MEDIA_TYPE_VALUES: set[WorkflowPresetPreviewMediaType] = {
    "image",
    "video",
}


def check_workflow_preset_preview_media_type(value: str) -> WorkflowPresetPreviewMediaType:
    if value in WORKFLOW_PRESET_PREVIEW_MEDIA_TYPE_VALUES:
        return cast(WorkflowPresetPreviewMediaType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKFLOW_PRESET_PREVIEW_MEDIA_TYPE_VALUES!r}"
    )
