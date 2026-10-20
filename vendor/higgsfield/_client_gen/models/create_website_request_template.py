from typing import Literal, cast

CreateWebsiteRequestTemplate = Literal["app-detail", "custom", "preset", "scroll-scrub", "studio"]

CREATE_WEBSITE_REQUEST_TEMPLATE_VALUES: set[CreateWebsiteRequestTemplate] = {
    "app-detail",
    "custom",
    "preset",
    "scroll-scrub",
    "studio",
}


def check_create_website_request_template(value: str) -> CreateWebsiteRequestTemplate:
    if value in CREATE_WEBSITE_REQUEST_TEMPLATE_VALUES:
        return cast(CreateWebsiteRequestTemplate, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_WEBSITE_REQUEST_TEMPLATE_VALUES!r}"
    )
