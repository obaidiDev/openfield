from typing import Literal, cast

MarketingProductCreateRequestScreenshotsItemViewport = Literal["desktop", "mobile"]

MARKETING_PRODUCT_CREATE_REQUEST_SCREENSHOTS_ITEM_VIEWPORT_VALUES: set[
    MarketingProductCreateRequestScreenshotsItemViewport
] = {
    "desktop",
    "mobile",
}


def check_marketing_product_create_request_screenshots_item_viewport(
    value: str,
) -> MarketingProductCreateRequestScreenshotsItemViewport:
    if value in MARKETING_PRODUCT_CREATE_REQUEST_SCREENSHOTS_ITEM_VIEWPORT_VALUES:
        return cast(MarketingProductCreateRequestScreenshotsItemViewport, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MARKETING_PRODUCT_CREATE_REQUEST_SCREENSHOTS_ITEM_VIEWPORT_VALUES!r}"
    )
