from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generation_meta import GenerationMeta
    from ..models.pricing import Pricing
    from ..models.text_model_choice_params import TextModelChoiceParams


T = TypeVar("T", bound="TextModelChoice")


@_attrs_define
class TextModelChoice:
    """Request body for POST /developer/v2alpha/texts/{job_type}/generations. Carries the model params under params, with
    an optional top-level pricing. The accepted params fields depend on the {job_type} selected in the path.

        Attributes:
            params (TextModelChoiceParams): Model-specific parameters for the selected job_type. The accepted fields are
                defined by the backend job_types catalog; fetch them from GET /developer/v2alpha/job_types/{job_type}.
            pricing (Union[Unset, Pricing]): Optional pricing controls for this generation. Omit to charge the workspace's
                credit balance at the standard per-job rate.
            meta (Union[Unset, GenerationMeta]): Optional extensible metadata forwarded with a generation request. Known
                fields support chat/recovery context; extra fields are accepted and stored as job metadata.
            folder_id (Union[Unset, UUID]): Optional folder to file the created job(s) under. Best-effort: the job is
                created and billable even if the link fails. Folders are media-agnostic.
    """

    params: "TextModelChoiceParams"
    pricing: Union[Unset, "Pricing"] = UNSET
    meta: Union[Unset, "GenerationMeta"] = UNSET
    folder_id: Union[Unset, UUID] = UNSET

    def to_dict(self) -> dict[str, Any]:
        params = self.params.to_dict()

        pricing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pricing, Unset):
            pricing = self.pricing.to_dict()

        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        folder_id: Union[Unset, str] = UNSET
        if not isinstance(self.folder_id, Unset):
            folder_id = str(self.folder_id)

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
        if folder_id is not UNSET:
            field_dict["folder_id"] = folder_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generation_meta import GenerationMeta
        from ..models.pricing import Pricing
        from ..models.text_model_choice_params import TextModelChoiceParams

        d = dict(src_dict)
        params = TextModelChoiceParams.from_dict(d.pop("params"))

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

        _folder_id = d.pop("folder_id", UNSET)
        folder_id: Union[Unset, UUID]
        if isinstance(_folder_id, Unset):
            folder_id = UNSET
        else:
            folder_id = UUID(_folder_id)

        text_model_choice = cls(
            params=params,
            pricing=pricing,
            meta=meta,
            folder_id=folder_id,
        )

        return text_model_choice
