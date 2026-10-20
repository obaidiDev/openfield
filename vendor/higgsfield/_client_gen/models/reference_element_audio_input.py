from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReferenceElementAudioInput")


@_attrs_define
class ReferenceElementAudioInput:
    """A cloned-voice audio input backing a voice element.

    Attributes:
        id (UUID):
        name (Union[None, str]):
        status (str):
        duration (Union[None, float]): Audio duration in seconds.
    """

    id: UUID
    name: Union[None, str]
    status: str
    duration: Union[None, float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name: Union[None, str]
        name = self.name

        status = self.status

        duration: Union[None, float]
        duration = self.duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "duration": duration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        name = _parse_name(d.pop("name"))

        status = d.pop("status")

        def _parse_duration(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        duration = _parse_duration(d.pop("duration"))

        reference_element_audio_input = cls(
            id=id,
            name=name,
            status=status,
            duration=duration,
        )

        reference_element_audio_input.additional_properties = d
        return reference_element_audio_input

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
