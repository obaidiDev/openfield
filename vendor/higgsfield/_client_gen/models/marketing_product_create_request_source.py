from typing import Literal, cast

MarketingProductCreateRequestSource = Literal["media", "product_url", "web_media", "web_url"]

MARKETING_PRODUCT_CREATE_REQUEST_SOURCE_VALUES: set[MarketingProductCreateRequestSource] = {
    "media",
    "product_url",
    "web_media",
    "web_url",
}


def check_marketing_product_create_request_source(
    value: str,
) -> MarketingProductCreateRequestSource:
    if value in MARKETING_PRODUCT_CREATE_REQUEST_SOURCE_VALUES:
        return cast(MarketingProductCreateRequestSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MARKETING_PRODUCT_CREATE_REQUEST_SOURCE_VALUES!r}"
    )
