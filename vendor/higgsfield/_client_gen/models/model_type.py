from typing import Literal, cast

ModelType = Literal["3d", "audio", "image", "text", "video"]

MODEL_TYPE_VALUES: set[ModelType] = {
    "3d",
    "audio",
    "image",
    "text",
    "video",
}


def check_model_type(value: str) -> ModelType:
    return cast(ModelType, value)
