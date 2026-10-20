from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_status import JobStatus, check_job_status

T = TypeVar("T", bound="RealtimeChainEditResponse")


@_attrs_define
class RealtimeChainEditResponse:
    """Realtime chain edit attempt that was created.

    Attributes:
        chain_id (UUID): Realtime edit chain id. Pass this to continue or finalize the chain.
        job_set_id (UUID): Internal job-set id for this edit attempt.
        job_id (UUID): Created job id. Poll getJob with this id.
        status (JobStatus): Lifecycle status of a job. Terminal statuses are completed, failed, nsfw, canceled, and
            ip_detected.
        created_at (float): Creation time as Unix epoch seconds.
    """

    chain_id: UUID
    job_set_id: UUID
    job_id: UUID
    status: JobStatus
    created_at: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chain_id = str(self.chain_id)

        job_set_id = str(self.job_set_id)

        job_id = str(self.job_id)

        status: str = self.status

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chain_id": chain_id,
                "job_set_id": job_set_id,
                "job_id": job_id,
                "status": status,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chain_id = UUID(d.pop("chain_id"))

        job_set_id = UUID(d.pop("job_set_id"))

        job_id = UUID(d.pop("job_id"))

        status = check_job_status(d.pop("status"))

        created_at = d.pop("created_at")

        realtime_chain_edit_response = cls(
            chain_id=chain_id,
            job_set_id=job_set_id,
            job_id=job_id,
            status=status,
            created_at=created_at,
        )

        realtime_chain_edit_response.additional_properties = d
        return realtime_chain_edit_response

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
