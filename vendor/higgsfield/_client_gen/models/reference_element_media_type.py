from typing import Literal, cast

ReferenceElementMediaType = Literal["image_job", "media_input"]

REFERENCE_ELEMENT_MEDIA_TYPE_VALUES: set[ReferenceElementMediaType] = {
    "image_job",
    "media_input",
}


def check_reference_element_media_type(value: str) -> ReferenceElementMediaType:
    if value in REFERENCE_ELEMENT_MEDIA_TYPE_VALUES:
        return cast(ReferenceElementMediaType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REFERENCE_ELEMENT_MEDIA_TYPE_VALUES!r}"
    )
