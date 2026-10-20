from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GenerationMeta")


@_attrs_define
class GenerationMeta:
    """Optional extensible metadata forwarded with a generation request. Known fields support chat/recovery context; extra
    fields are accepted and stored as job metadata.

        Attributes:
            chat_id (Union[None, UUID, Unset]): Optional Hermes chat id associated with this generation.
            tool_use_id (Union[None, Unset, str]): Optional tool-use id associated with this generation.
    """

    chat_id: Union[None, UUID, Unset] = UNSET
    tool_use_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id: Union[None, Unset, str]
        if isinstance(self.chat_id, Unset):
            chat_id = UNSET
        elif isinstance(self.chat_id, UUID):
            chat_id = str(self.chat_id)
        else:
            chat_id = self.chat_id

        tool_use_id: Union[None, Unset, str]
        if isinstance(self.tool_use_id, Unset):
            tool_use_id = UNSET
        else:
            tool_use_id = self.tool_use_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chat_id is not UNSET:
            field_dict["chat_id"] = chat_id
        if tool_use_id is not UNSET:
            field_dict["tool_use_id"] = tool_use_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_chat_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                chat_id_type_0 = UUID(data)

                return chat_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        chat_id = _parse_chat_id(d.pop("chat_id", UNSET))

        def _parse_tool_use_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tool_use_id = _parse_tool_use_id(d.pop("tool_use_id", UNSET))

        generation_meta = cls(
            chat_id=chat_id,
            tool_use_id=tool_use_id,
        )

        generation_meta.additional_properties = d
        return generation_meta

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
