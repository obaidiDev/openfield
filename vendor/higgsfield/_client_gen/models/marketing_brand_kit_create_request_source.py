from typing import Literal, cast

MarketingBrandKitCreateRequestSource = Literal["manual", "url"]

MARKETING_BRAND_KIT_CREATE_REQUEST_SOURCE_VALUES: set[MarketingBrandKitCreateRequestSource] = {
    "manual",
    "url",
}


def check_marketing_brand_kit_create_request_source(
    value: str,
) -> MarketingBrandKitCreateRequestSource:
    if value in MARKETING_BRAND_KIT_CREATE_REQUEST_SOURCE_VALUES:
        return cast(MarketingBrandKitCreateRequestSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MARKETING_BRAND_KIT_CREATE_REQUEST_SOURCE_VALUES!r}"
    )
