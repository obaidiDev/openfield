from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RealtimeChainFinalizeRequest")


@_attrs_define
class RealtimeChainFinalizeRequest:
    """Request to finalize a realtime Flux Klein chain.

    Attributes:
        chain_id (UUID): Realtime edit chain id.
    """

    chain_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chain_id = str(self.chain_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chain_id": chain_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chain_id = UUID(d.pop("chain_id"))

        realtime_chain_finalize_request = cls(
            chain_id=chain_id,
        )

        realtime_chain_finalize_request.additional_properties = d
        return realtime_chain_finalize_request

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
