from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pricing import Pricing
    from ..models.workflow_generation_params import WorkflowGenerationParams


T = TypeVar("T", bound="WorkflowGenerationRequest")


@_attrs_define
class WorkflowGenerationRequest:
    """Request body for POST /developer/v2alpha/workflows/{product_key}/generations. Mirrors the media generation envelope:
    workflow params live under params, with optional top-level pricing.

        Attributes:
            params (WorkflowGenerationParams): Parameters for a workflow generation. Provide source media using the public
                keys advertised by the selected preset's inputs, such as image_references or video_references.
            pricing (Union[Unset, Pricing]): Optional pricing controls for this generation. Omit to charge the workspace's
                credit balance at the standard per-job rate.
    """

    params: "WorkflowGenerationParams"
    pricing: Union[Unset, "Pricing"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        params = self.params.to_dict()

        pricing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pricing, Unset):
            pricing = self.pricing.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "params": params,
            }
        )
        if pricing is not UNSET:
            field_dict["pricing"] = pricing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pricing import Pricing
        from ..models.workflow_generation_params import WorkflowGenerationParams

        d = dict(src_dict)
        params = WorkflowGenerationParams.from_dict(d.pop("params"))

        _pricing = d.pop("pricing", UNSET)
        pricing: Union[Unset, Pricing]
        if isinstance(_pricing, Unset):
            pricing = UNSET
        else:
            pricing = Pricing.from_dict(_pricing)

        workflow_generation_request = cls(
            params=params,
            pricing=pricing,
        )

        return workflow_generation_request
