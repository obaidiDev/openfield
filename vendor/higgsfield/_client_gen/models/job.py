import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.job_status import JobStatus, check_job_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_debug_type_0 import JobDebugType0
    from ..models.job_params import JobParams
    from ..models.job_result_json_type_0 import JobResultJsonType0


T = TypeVar("T", bound="Job")


@_attrs_define
class Job:
    """A generation job and, once completed, its result. Result fields are populated only when status is completed, and
    which one is populated depends on the job set type: media jobs expose result_url/min_result_url/thumbnail_url, and
    structured jobs expose result_json.

        Attributes:
            id (UUID): The job's unique identifier.
            status (JobStatus): Lifecycle status of a job. Terminal statuses are completed, failed, nsfw, canceled, and
                ip_detected.
            job_type (str): The generation model / job set type that produced this job (e.g. image2video, text2image_soul,
                veo3).
            display_name (str): Human-readable name for the job's job set type.
            result_url (Union[None, str]): Full-resolution result artifact URL (image or video). Null until completed or for
                non-media job types.
            min_result_url (Union[None, str]): Web-optimized (smaller) result artifact URL. Null when unavailable.
            created_at (datetime.datetime): Job creation time (ISO 8601).
            params (JobParams): The (sanitized) generation parameters the job was created with.
            thumbnail_url (Union[None, Unset, str]): Poster/thumbnail image URL for results that aren't themselves images
                (e.g. a rendered preview for a 3D mesh). Null when no preview exists.
            result_json (Union['JobResultJsonType0', None, Unset]): Structured machine-readable result for non-media job
                types (e.g. color-grading LUT data or image decomposition output). Null for media and text jobs.
            debug (Union['JobDebugType0', None, Unset]): Diagnostic fields (e.g. enhanced prompt, RAG query/images).
                Populated only in non-production environments; null in production.
    """

    id: UUID
    status: JobStatus
    job_type: str
    display_name: str
    result_url: Union[None, str]
    min_result_url: Union[None, str]
    created_at: datetime.datetime
    params: "JobParams"
    thumbnail_url: Union[None, Unset, str] = UNSET
    result_json: Union["JobResultJsonType0", None, Unset] = UNSET
    debug: Union["JobDebugType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.job_debug_type_0 import JobDebugType0
        from ..models.job_result_json_type_0 import JobResultJsonType0

        id = str(self.id)

        status: str = self.status

        job_type = self.job_type

        display_name = self.display_name

        result_url: Union[None, str]
        result_url = self.result_url

        min_result_url: Union[None, str]
        min_result_url = self.min_result_url

        created_at = self.created_at.isoformat()

        params = self.params.to_dict()

        thumbnail_url: Union[None, Unset, str]
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        result_json: Union[None, Unset, dict[str, Any]]
        if isinstance(self.result_json, Unset):
            result_json = UNSET
        elif isinstance(self.result_json, JobResultJsonType0):
            result_json = self.result_json.to_dict()
        else:
            result_json = self.result_json

        debug: Union[None, Unset, dict[str, Any]]
        if isinstance(self.debug, Unset):
            debug = UNSET
        elif isinstance(self.debug, JobDebugType0):
            debug = self.debug.to_dict()
        else:
            debug = self.debug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "job_type": job_type,
                "display_name": display_name,
                "result_url": result_url,
                "min_result_url": min_result_url,
                "created_at": created_at,
                "params": params,
            }
        )
        if thumbnail_url is not UNSET:
            field_dict["thumbnail_url"] = thumbnail_url
        if result_json is not UNSET:
            field_dict["result_json"] = result_json
        if debug is not UNSET:
            field_dict["debug"] = debug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_debug_type_0 import JobDebugType0
        from ..models.job_params import JobParams
        from ..models.job_result_json_type_0 import JobResultJsonType0

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        status = check_job_status(d.pop("status"))

        job_type = d.pop("job_type")

        display_name = d.pop("display_name")

        def _parse_result_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        result_url = _parse_result_url(d.pop("result_url"))

        def _parse_min_result_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        min_result_url = _parse_min_result_url(d.pop("min_result_url"))

        created_at = isoparse(d.pop("created_at"))

        params = JobParams.from_dict(d.pop("params"))

        def _parse_thumbnail_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnail_url", UNSET))

        def _parse_result_json(data: object) -> Union["JobResultJsonType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_json_type_0 = JobResultJsonType0.from_dict(data)

                return result_json_type_0
            except:  # noqa: E722
                pass
            return cast(Union["JobResultJsonType0", None, Unset], data)

        result_json = _parse_result_json(d.pop("result_json", UNSET))

        def _parse_debug(data: object) -> Union["JobDebugType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                debug_type_0 = JobDebugType0.from_dict(data)

                return debug_type_0
            except:  # noqa: E722
                pass
            return cast(Union["JobDebugType0", None, Unset], data)

        debug = _parse_debug(d.pop("debug", UNSET))

        job = cls(
            id=id,
            status=status,
            job_type=job_type,
            display_name=display_name,
            result_url=result_url,
            min_result_url=min_result_url,
            created_at=created_at,
            params=params,
            thumbnail_url=thumbnail_url,
            result_json=result_json,
            debug=debug,
        )

        job.additional_properties = d
        return job

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
