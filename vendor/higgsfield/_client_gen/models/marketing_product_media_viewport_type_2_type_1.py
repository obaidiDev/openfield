from typing import Literal, cast

MarketingProductMediaViewportType2Type1 = Literal["desktop", "mobile"]

MARKETING_PRODUCT_MEDIA_VIEWPORT_TYPE_2_TYPE_1_VALUES: set[
    MarketingProductMediaViewportType2Type1
] = {
    "desktop",
    "mobile",
}


def check_marketing_product_media_viewport_type_2_type_1(
    value: str,
) -> MarketingProductMediaViewportType2Type1:
    if value in MARKETING_PRODUCT_MEDIA_VIEWPORT_TYPE_2_TYPE_1_VALUES:
        return cast(MarketingProductMediaViewportType2Type1, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MARKETING_PRODUCT_MEDIA_VIEWPORT_TYPE_2_TYPE_1_VALUES!r}"
    )
