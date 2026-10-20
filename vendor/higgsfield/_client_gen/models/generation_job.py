from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GenerationJob")


@_attrs_define
class GenerationJob:
    """The job created by a generation submit. Poll it with getJob for status and, once complete, the result. Job sets are
    an internal grouping and are not exposed.

        Attributes:
            id (UUID): The created job's unique identifier. Poll it with getJob.
            job_type (str): The model (job_type) that produced this job.
            credits_ (float): Credits charged for this job. May be fractional.
    """

    id: UUID
    job_type: str
    credits_: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        job_type = self.job_type

        credits_ = self.credits_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "job_type": job_type,
                "credits": credits_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        job_type = d.pop("job_type")

        credits_ = d.pop("credits")

        generation_job = cls(
            id=id,
            job_type=job_type,
            credits_=credits_,
        )

        generation_job.additional_properties = d
        return generation_job

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
