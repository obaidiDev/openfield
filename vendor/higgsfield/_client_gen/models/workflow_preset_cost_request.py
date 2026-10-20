from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_preset_cost_request_params import WorkflowPresetCostRequestParams


T = TypeVar("T", bound="WorkflowPresetCostRequest")


@_attrs_define
class WorkflowPresetCostRequest:
    """Optional runtime params used to calculate dynamic workflow preset pricing.

    Attributes:
        params (Union[Unset, WorkflowPresetCostRequestParams]): Runtime selections for dynamic pricing, such as duration
            and resolution.
    """

    params: Union[Unset, "WorkflowPresetCostRequestParams"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        params: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_preset_cost_request_params import WorkflowPresetCostRequestParams

        d = dict(src_dict)
        _params = d.pop("params", UNSET)
        params: Union[Unset, WorkflowPresetCostRequestParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = WorkflowPresetCostRequestParams.from_dict(_params)

        workflow_preset_cost_request = cls(
            params=params,
        )

        return workflow_preset_cost_request
