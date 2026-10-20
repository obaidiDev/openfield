import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.reference_element_status import ReferenceElementStatus, check_reference_element_status
from ..models.reference_element_type import ReferenceElementType, check_reference_element_type
from ..models.reference_element_voice_type_type_0 import (
    ReferenceElementVoiceTypeType0,
    check_reference_element_voice_type_type_0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReferenceElement")


@_attrs_define
class ReferenceElement:
    """A reusable reference element.

    Attributes:
        id (UUID):
        category (ReferenceElementType): Kind of a reference element. auto is an input-only request value that triggers
            server-side classification; the server then stores and returns one of the auto:* variants. The *_ip_verified
            variants are reserved for elements sourced from IP-verified soul jobs.
        name (Union[None, str]):
        status (ReferenceElementStatus): Lifecycle status of a reference element.
        created_at (datetime.datetime): Creation time (ISO 8601).
        description (Union[None, Unset, str]):
        voice_type (Union[None, ReferenceElementVoiceTypeType0, Unset]): How to pass this item into generation params
            when category is voice: preset for built-in CMS voices, element for custom voice reference elements.
        ip_detected (Union[None, Unset, bool]): IP-check verdict: null = not checked, true = potential IP found, false =
            clean.
    """

    id: UUID
    category: ReferenceElementType
    name: Union[None, str]
    status: ReferenceElementStatus
    created_at: datetime.datetime
    description: Union[None, Unset, str] = UNSET
    voice_type: Union[None, ReferenceElementVoiceTypeType0, Unset] = UNSET
    ip_detected: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        category: str = self.category

        name: Union[None, str]
        name = self.name

        status: str = self.status

        created_at = self.created_at.isoformat()

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        voice_type: Union[None, Unset, str]
        if isinstance(self.voice_type, Unset):
            voice_type = UNSET
        elif isinstance(self.voice_type, str):
            voice_type = self.voice_type
        else:
            voice_type = self.voice_type

        ip_detected: Union[None, Unset, bool]
        if isinstance(self.ip_detected, Unset):
            ip_detected = UNSET
        else:
            ip_detected = self.ip_detected

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "category": category,
                "name": name,
                "status": status,
                "created_at": created_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if voice_type is not UNSET:
            field_dict["voice_type"] = voice_type
        if ip_detected is not UNSET:
            field_dict["ip_detected"] = ip_detected

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        category = check_reference_element_type(d.pop("category"))

        def _parse_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        name = _parse_name(d.pop("name"))

        status = check_reference_element_status(d.pop("status"))

        created_at = isoparse(d.pop("created_at"))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_voice_type(data: object) -> Union[None, ReferenceElementVoiceTypeType0, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                voice_type_type_0 = check_reference_element_voice_type_type_0(data)

                return voice_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, ReferenceElementVoiceTypeType0, Unset], data)

        voice_type = _parse_voice_type(d.pop("voice_type", UNSET))

        def _parse_ip_detected(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        ip_detected = _parse_ip_detected(d.pop("ip_detected", UNSET))

        reference_element = cls(
            id=id,
            category=category,
            name=name,
            status=status,
            created_at=created_at,
            description=description,
            voice_type=voice_type,
            ip_detected=ip_detected,
        )

        reference_element.additional_properties = d
        return reference_element

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
