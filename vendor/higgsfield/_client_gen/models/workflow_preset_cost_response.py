from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowPresetCostResponse")


@_attrs_define
class WorkflowPresetCostResponse:
    """Credit cost for one workflow preset.

    Attributes:
        preset_id (UUID): Workflow preset id.
        cost (int): Final credit cost to display and charge for the authenticated workspace.
        strikethrough_cost (Union[None, Unset, int]): Optional higher comparison credit cost to render as struck
            through.
    """

    preset_id: UUID
    cost: int
    strikethrough_cost: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        preset_id = str(self.preset_id)

        cost = self.cost

        strikethrough_cost: Union[None, Unset, int]
        if isinstance(self.strikethrough_cost, Unset):
            strikethrough_cost = UNSET
        else:
            strikethrough_cost = self.strikethrough_cost

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "preset_id": preset_id,
                "cost": cost,
            }
        )
        if strikethrough_cost is not UNSET:
            field_dict["strikethrough_cost"] = strikethrough_cost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        preset_id = UUID(d.pop("preset_id"))

        cost = d.pop("cost")

        def _parse_strikethrough_cost(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        strikethrough_cost = _parse_strikethrough_cost(d.pop("strikethrough_cost", UNSET))

        workflow_preset_cost_response = cls(
            preset_id=preset_id,
            cost=cost,
            strikethrough_cost=strikethrough_cost,
        )

        return workflow_preset_cost_response
