from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Pricing")


@_attrs_define
class Pricing:
    """Optional pricing controls for this generation. Omit to charge the workspace's credit balance at the standard per-job
    rate.

        Attributes:
            use_unlim (Union[Unset, bool]): When true, draw this generation from the workspace's unlimited-plan allowance
                (relax / unlimited mode) instead of deducting credits, when the active plan permits it. Has no effect (the job
                is charged as credits) if the workspace has no eligible unlimited allowance.
                 Default: False.
    """

    use_unlim: Union[Unset, bool] = False

    def to_dict(self) -> dict[str, Any]:
        use_unlim = self.use_unlim

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if use_unlim is not UNSET:
            field_dict["use_unlim"] = use_unlim

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        use_unlim = d.pop("use_unlim", UNSET)

        pricing = cls(
            use_unlim=use_unlim,
        )

        return pricing
