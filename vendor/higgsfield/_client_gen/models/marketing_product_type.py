from typing import Literal, cast

MarketingProductType = Literal["physical", "web"]

MARKETING_PRODUCT_TYPE_VALUES: set[MarketingProductType] = {
    "physical",
    "web",
}


def check_marketing_product_type(value: str) -> MarketingProductType:
    if value in MARKETING_PRODUCT_TYPE_VALUES:
        return cast(MarketingProductType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MARKETING_PRODUCT_TYPE_VALUES!r}"
    )
