from typing import Literal, cast

MarketingProductStatus = Literal["completed", "failed", "in_progress", "queued"]

MARKETING_PRODUCT_STATUS_VALUES: set[MarketingProductStatus] = {
    "completed",
    "failed",
    "in_progress",
    "queued",
}


def check_marketing_product_status(value: str) -> MarketingProductStatus:
    if value in MARKETING_PRODUCT_STATUS_VALUES:
        return cast(MarketingProductStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MARKETING_PRODUCT_STATUS_VALUES!r}"
    )
