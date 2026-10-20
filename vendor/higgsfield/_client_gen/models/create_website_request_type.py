from typing import Literal, cast

CreateWebsiteRequestType = Literal["app", "game", "website"]

CREATE_WEBSITE_REQUEST_TYPE_VALUES: set[CreateWebsiteRequestType] = {
    "app",
    "game",
    "website",
}


def check_create_website_request_type(value: str) -> CreateWebsiteRequestType:
    if value in CREATE_WEBSITE_REQUEST_TYPE_VALUES:
        return cast(CreateWebsiteRequestType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_WEBSITE_REQUEST_TYPE_VALUES!r}"
    )
