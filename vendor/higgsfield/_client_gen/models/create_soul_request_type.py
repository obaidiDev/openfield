from typing import Literal, cast

CreateSoulRequestType = Literal["soul_2", "soul_cinematic"]

CREATE_SOUL_REQUEST_TYPE_VALUES: set[CreateSoulRequestType] = {
    "soul_2",
    "soul_cinematic",
}


def check_create_soul_request_type(value: str) -> CreateSoulRequestType:
    if value in CREATE_SOUL_REQUEST_TYPE_VALUES:
        return cast(CreateSoulRequestType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_SOUL_REQUEST_TYPE_VALUES!r}"
    )
