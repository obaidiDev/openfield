from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.realtime_custom_style_reference import RealtimeCustomStyleReference


T = TypeVar("T", bound="RealtimeCustomStyle")


@_attrs_define
class RealtimeCustomStyle:
    """A saved reusable custom style for realtime Flux Klein editing.

    Attributes:
        id (UUID):
        prompt (str): Style prompt text.
        reference (Union['RealtimeCustomStyleReference', None]): Optional reference image metadata.
    """

    id: UUID
    prompt: str
    reference: Union["RealtimeCustomStyleReference", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.realtime_custom_style_reference import RealtimeCustomStyleReference

        id = str(self.id)

        prompt = self.prompt

        reference: Union[None, dict[str, Any]]
        if isinstance(self.reference, RealtimeCustomStyleReference):
            reference = self.reference.to_dict()
        else:
            reference = self.reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "prompt": prompt,
                "reference": reference,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.realtime_custom_style_reference import RealtimeCustomStyleReference

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        prompt = d.pop("prompt")

        def _parse_reference(data: object) -> Union["RealtimeCustomStyleReference", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reference_type_0 = RealtimeCustomStyleReference.from_dict(data)

                return reference_type_0
            except:  # noqa: E722
                pass
            return cast(Union["RealtimeCustomStyleReference", None], data)

        reference = _parse_reference(d.pop("reference"))

        realtime_custom_style = cls(
            id=id,
            prompt=prompt,
            reference=reference,
        )

        realtime_custom_style.additional_properties = d
        return realtime_custom_style

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
