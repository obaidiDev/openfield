from typing import Literal, cast

WorkflowGenerationParamsAspectRatio = Literal[
    "16:9", "1:1", "21:9", "2:3", "3:2", "3:4", "4:3", "9:16"
]

WORKFLOW_GENERATION_PARAMS_ASPECT_RATIO_VALUES: set[WorkflowGenerationParamsAspectRatio] = {
    "16:9",
    "1:1",
    "21:9",
    "2:3",
    "3:2",
    "3:4",
    "4:3",
    "9:16",
}


def check_workflow_generation_params_aspect_ratio(
    value: str,
) -> WorkflowGenerationParamsAspectRatio:
    if value in WORKFLOW_GENERATION_PARAMS_ASPECT_RATIO_VALUES:
        return cast(WorkflowGenerationParamsAspectRatio, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKFLOW_GENERATION_PARAMS_ASPECT_RATIO_VALUES!r}"
    )
