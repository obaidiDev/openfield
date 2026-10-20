from typing import Literal, cast

ReferenceElementType = Literal[
    "auto",
    "auto:character",
    "auto:environment",
    "auto:prop",
    "character",
    "character_ip_verified",
    "environment",
    "environment_ip_verified",
    "prop",
    "voice",
]

REFERENCE_ELEMENT_TYPE_VALUES: set[ReferenceElementType] = {
    "auto",
    "auto:character",
    "auto:environment",
    "auto:prop",
    "character",
    "character_ip_verified",
    "environment",
    "environment_ip_verified",
    "prop",
    "voice",
}


def check_reference_element_type(value: str) -> ReferenceElementType:
    if value in REFERENCE_ELEMENT_TYPE_VALUES:
        return cast(ReferenceElementType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REFERENCE_ELEMENT_TYPE_VALUES!r}"
    )
