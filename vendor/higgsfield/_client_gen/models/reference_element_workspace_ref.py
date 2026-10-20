from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReferenceElementWorkspaceRef")


@_attrs_define
class ReferenceElementWorkspaceRef:
    """A workspace this element is associated with, via the element-workspace junction.

    Attributes:
        id (UUID):
        name (Union[None, str]):
        avatar_url (Union[None, Unset, str]):
        is_shared (Union[Unset, bool]): Whether the element is shared with other members in this workspace.
    """

    id: UUID
    name: Union[None, str]
    avatar_url: Union[None, Unset, str] = UNSET
    is_shared: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name: Union[None, str]
        name = self.name

        avatar_url: Union[None, Unset, str]
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        is_shared = self.is_shared

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if is_shared is not UNSET:
            field_dict["is_shared"] = is_shared

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

        def _parse_avatar_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        avatar_url = _parse_avatar_url(d.pop("avatar_url", UNSET))

        is_shared = d.pop("is_shared", UNSET)

        reference_element_workspace_ref = cls(
            id=id,
            name=name,
            avatar_url=avatar_url,
            is_shared=is_shared,
        )

        reference_element_workspace_ref.additional_properties = d
        return reference_element_workspace_ref

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
