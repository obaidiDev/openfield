from typing import Literal, cast

MarketingProductMediaViewportType3Type1 = Literal["desktop", "mobile"]

MARKETING_PRODUCT_MEDIA_VIEWPORT_TYPE_3_TYPE_1_VALUES: set[
    MarketingProductMediaViewportType3Type1
] = {
    "desktop",
    "mobile",
}


def check_marketing_product_media_viewport_type_3_type_1(
    value: str,
) -> MarketingProductMediaViewportType3Type1:
    if value in MARKETING_PRODUCT_MEDIA_VIEWPORT_TYPE_3_TYPE_1_VALUES:
        return cast(MarketingProductMediaViewportType3Type1, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MARKETING_PRODUCT_MEDIA_VIEWPORT_TYPE_3_TYPE_1_VALUES!r}"
    )
