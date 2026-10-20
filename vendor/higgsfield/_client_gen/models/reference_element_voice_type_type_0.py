from typing import Literal, cast

ReferenceElementVoiceTypeType0 = Literal["element", "preset"]

REFERENCE_ELEMENT_VOICE_TYPE_TYPE_0_VALUES: set[ReferenceElementVoiceTypeType0] = {
    "element",
    "preset",
}


def check_reference_element_voice_type_type_0(value: str) -> ReferenceElementVoiceTypeType0:
    if value in REFERENCE_ELEMENT_VOICE_TYPE_TYPE_0_VALUES:
        return cast(ReferenceElementVoiceTypeType0, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REFERENCE_ELEMENT_VOICE_TYPE_TYPE_0_VALUES!r}"
    )
