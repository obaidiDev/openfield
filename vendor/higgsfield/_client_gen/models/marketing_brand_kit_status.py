from typing import Literal, cast

MarketingBrandKitStatus = Literal["canceled", "completed", "failed", "in_progress", "queued"]

MARKETING_BRAND_KIT_STATUS_VALUES: set[MarketingBrandKitStatus] = {
    "canceled",
    "completed",
    "failed",
    "in_progress",
    "queued",
}


def check_marketing_brand_kit_status(value: str) -> MarketingBrandKitStatus:
    if value in MARKETING_BRAND_KIT_STATUS_VALUES:
        return cast(MarketingBrandKitStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MARKETING_BRAND_KIT_STATUS_VALUES!r}"
    )
