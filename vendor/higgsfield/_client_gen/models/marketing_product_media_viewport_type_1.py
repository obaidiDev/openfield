from typing import Literal, cast

MarketingProductMediaViewportType1 = Literal["desktop", "mobile"]

MARKETING_PRODUCT_MEDIA_VIEWPORT_TYPE_1_VALUES: set[MarketingProductMediaViewportType1] = {
    "desktop",
    "mobile",
}


def check_marketing_product_media_viewport_type_1(value: str) -> MarketingProductMediaViewportType1:
    if value in MARKETING_PRODUCT_MEDIA_VIEWPORT_TYPE_1_VALUES:
        return cast(MarketingProductMediaViewportType1, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MARKETING_PRODUCT_MEDIA_VIEWPORT_TYPE_1_VALUES!r}"
    )
