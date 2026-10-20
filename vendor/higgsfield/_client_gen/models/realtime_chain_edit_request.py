from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.realtime_edit_params import RealtimeEditParams


T = TypeVar("T", bound="RealtimeChainEditRequest")


@_attrs_define
class RealtimeChainEditRequest:
    """Request to create one realtime Flux Klein chain edit attempt.

    Attributes:
        params (RealtimeEditParams): Realtime Flux Klein edit params. Exactly one of prompt or settings is required.
        chain_id (Union[None, UUID, Unset]): Existing chain id to continue. Omit or send null to start a new chain.
    """

    params: "RealtimeEditParams"
    chain_id: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        params = self.params.to_dict()

        chain_id: Union[None, Unset, str]
        if isinstance(self.chain_id, Unset):
            chain_id = UNSET
        elif isinstance(self.chain_id, UUID):
            chain_id = str(self.chain_id)
        else:
            chain_id = self.chain_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "params": params,
            }
        )
        if chain_id is not UNSET:
            field_dict["chain_id"] = chain_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.realtime_edit_params import RealtimeEditParams

        d = dict(src_dict)
        params = RealtimeEditParams.from_dict(d.pop("params"))

        def _parse_chain_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                chain_id_type_0 = UUID(data)

                return chain_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        chain_id = _parse_chain_id(d.pop("chain_id", UNSET))

        realtime_chain_edit_request = cls(
            params=params,
            chain_id=chain_id,
        )

        realtime_chain_edit_request.additional_properties = d
        return realtime_chain_edit_request

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
