from typing import Literal, cast

ModelLabel = Literal["app", "chain", "model"]

MODEL_LABEL_VALUES: set[ModelLabel] = {
    "app",
    "chain",
    "model",
}


def check_model_label(value: str) -> ModelLabel:
    return cast(ModelLabel, value)
