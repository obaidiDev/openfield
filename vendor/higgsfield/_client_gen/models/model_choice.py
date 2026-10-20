from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generation_meta import GenerationMeta
    from ..models.model_choice_params import ModelChoiceParams
    from ..models.pricing import Pricing


T = TypeVar("T", bound="ModelChoice")


@_attrs_define
class ModelChoice:
    """A generation request for any public model, used to estimate cost. Carries the model params under params, with an
    optional top-level pricing.

        Attributes:
            params (ModelChoiceParams): Model-specific parameters for the selected job_type. The accepted fields are defined
                by the backend job_types catalog; fetch them from GET /developer/v2alpha/job_types/{job_type}.
            pricing (Union[Unset, Pricing]): Optional pricing controls for this generation. Omit to charge the workspace's
                credit balance at the standard per-job rate.
            meta (Union[Unset, GenerationMeta]): Optional extensible metadata forwarded with a generation request. Known
                fields support chat/recovery context; extra fields are accepted and stored as job metadata.
    """

    params: "ModelChoiceParams"
    pricing: Union[Unset, "Pricing"] = UNSET
    meta: Union[Unset, "GenerationMeta"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        params = self.params.to_dict()

        pricing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pricing, Unset):
            pricing = self.pricing.to_dict()

        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "params": params,
            }
        )
        if pricing is not UNSET:
            field_dict["pricing"] = pricing
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generation_meta import GenerationMeta
        from ..models.model_choice_params import ModelChoiceParams
        from ..models.pricing import Pricing

        d = dict(src_dict)
        params = ModelChoiceParams.from_dict(d.pop("params"))

        _pricing = d.pop("pricing", UNSET)
        pricing: Union[Unset, Pricing]
        if isinstance(_pricing, Unset):
            pricing = UNSET
        else:
            pricing = Pricing.from_dict(_pricing)

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, GenerationMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = GenerationMeta.from_dict(_meta)

        model_choice = cls(
            params=params,
            pricing=pricing,
            meta=meta,
        )

        return model_choice
