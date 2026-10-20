from typing import Literal, cast

MarketingAdReferenceStatus = Literal["completed", "failed", "in_progress", "queued"]

MARKETING_AD_REFERENCE_STATUS_VALUES: set[MarketingAdReferenceStatus] = {
    "completed",
    "failed",
    "in_progress",
    "queued",
}


def check_marketing_ad_reference_status(value: str) -> MarketingAdReferenceStatus:
    if value in MARKETING_AD_REFERENCE_STATUS_VALUES:
        return cast(MarketingAdReferenceStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MARKETING_AD_REFERENCE_STATUS_VALUES!r}"
    )
