import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.marketing_ad_reference_status import (
    MarketingAdReferenceStatus,
    check_marketing_ad_reference_status,
)

if TYPE_CHECKING:
    from ..models.marketing_ad_reference_adapted_concept_type_0_item import (
        MarketingAdReferenceAdaptedConceptType0Item,
    )
    from ..models.marketing_ad_reference_edited_concept_json_type_0_item import (
        MarketingAdReferenceEditedConceptJsonType0Item,
    )
    from ..models.marketing_ad_reference_original_concept_type_0_item import (
        MarketingAdReferenceOriginalConceptType0Item,
    )


T = TypeVar("T", bound="MarketingAdReference")


@_attrs_define
class MarketingAdReference:
    """An ad reference — a video-clone scenario cloned from a source video, with its extracted/edited concept.

    Attributes:
        id (UUID):
        source_url (Union[None, str]): Source URL the video was cloned from, when applicable.
        video_input_id (Union[None, UUID]):
        job_id (Union[None, UUID]):
        source_platform (Union[None, str]): Detected source platform (e.g. tiktok, instagram), when known.
        status (MarketingAdReferenceStatus): Processing status of an ad reference (video clone).
        fail_reason (Union[None, str]):
        video_s3_url (Union[None, str]):
        video_thumbnail_url (Union[None, str]):
        video_duration_seconds (Union[None, float]):
        original_concept (Union[None, list['MarketingAdReferenceOriginalConceptType0Item']]): The concept extracted from
            the source video. Null until ready.
        adapted_concept (Union[None, list['MarketingAdReferenceAdaptedConceptType0Item']]): The concept adapted to the
            bound avatar/product. Null until ready.
        edited_concept_text (Union[None, str]): User-edited concept as free text.
        edited_concept_json (Union[None, list['MarketingAdReferenceEditedConceptJsonType0Item']]): User-edited
            structured concept.
        avatar_id (Union[None, UUID]):
        product_id (Union[None, UUID]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: UUID
    source_url: Union[None, str]
    video_input_id: Union[None, UUID]
    job_id: Union[None, UUID]
    source_platform: Union[None, str]
    status: MarketingAdReferenceStatus
    fail_reason: Union[None, str]
    video_s3_url: Union[None, str]
    video_thumbnail_url: Union[None, str]
    video_duration_seconds: Union[None, float]
    original_concept: Union[None, list["MarketingAdReferenceOriginalConceptType0Item"]]
    adapted_concept: Union[None, list["MarketingAdReferenceAdaptedConceptType0Item"]]
    edited_concept_text: Union[None, str]
    edited_concept_json: Union[None, list["MarketingAdReferenceEditedConceptJsonType0Item"]]
    avatar_id: Union[None, UUID]
    product_id: Union[None, UUID]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        source_url: Union[None, str]
        source_url = self.source_url

        video_input_id: Union[None, str]
        if isinstance(self.video_input_id, UUID):
            video_input_id = str(self.video_input_id)
        else:
            video_input_id = self.video_input_id

        job_id: Union[None, str]
        if isinstance(self.job_id, UUID):
            job_id = str(self.job_id)
        else:
            job_id = self.job_id

        source_platform: Union[None, str]
        source_platform = self.source_platform

        status: str = self.status

        fail_reason: Union[None, str]
        fail_reason = self.fail_reason

        video_s3_url: Union[None, str]
        video_s3_url = self.video_s3_url

        video_thumbnail_url: Union[None, str]
        video_thumbnail_url = self.video_thumbnail_url

        video_duration_seconds: Union[None, float]
        video_duration_seconds = self.video_duration_seconds

        original_concept: Union[None, list[dict[str, Any]]]
        if isinstance(self.original_concept, list):
            original_concept = []
            for original_concept_type_0_item_data in self.original_concept:
                original_concept_type_0_item = original_concept_type_0_item_data.to_dict()
                original_concept.append(original_concept_type_0_item)

        else:
            original_concept = self.original_concept

        adapted_concept: Union[None, list[dict[str, Any]]]
        if isinstance(self.adapted_concept, list):
            adapted_concept = []
            for adapted_concept_type_0_item_data in self.adapted_concept:
                adapted_concept_type_0_item = adapted_concept_type_0_item_data.to_dict()
                adapted_concept.append(adapted_concept_type_0_item)

        else:
            adapted_concept = self.adapted_concept

        edited_concept_text: Union[None, str]
        edited_concept_text = self.edited_concept_text

        edited_concept_json: Union[None, list[dict[str, Any]]]
        if isinstance(self.edited_concept_json, list):
            edited_concept_json = []
            for edited_concept_json_type_0_item_data in self.edited_concept_json:
                edited_concept_json_type_0_item = edited_concept_json_type_0_item_data.to_dict()
                edited_concept_json.append(edited_concept_json_type_0_item)

        else:
            edited_concept_json = self.edited_concept_json

        avatar_id: Union[None, str]
        if isinstance(self.avatar_id, UUID):
            avatar_id = str(self.avatar_id)
        else:
            avatar_id = self.avatar_id

        product_id: Union[None, str]
        if isinstance(self.product_id, UUID):
            product_id = str(self.product_id)
        else:
            product_id = self.product_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "source_url": source_url,
                "video_input_id": video_input_id,
                "job_id": job_id,
                "source_platform": source_platform,
                "status": status,
                "fail_reason": fail_reason,
                "video_s3_url": video_s3_url,
                "video_thumbnail_url": video_thumbnail_url,
                "video_duration_seconds": video_duration_seconds,
                "original_concept": original_concept,
                "adapted_concept": adapted_concept,
                "edited_concept_text": edited_concept_text,
                "edited_concept_json": edited_concept_json,
                "avatar_id": avatar_id,
                "product_id": product_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.marketing_ad_reference_adapted_concept_type_0_item import (
            MarketingAdReferenceAdaptedConceptType0Item,
        )
        from ..models.marketing_ad_reference_edited_concept_json_type_0_item import (
            MarketingAdReferenceEditedConceptJsonType0Item,
        )
        from ..models.marketing_ad_reference_original_concept_type_0_item import (
            MarketingAdReferenceOriginalConceptType0Item,
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_source_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        source_url = _parse_source_url(d.pop("source_url"))

        def _parse_video_input_id(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                video_input_id_type_0 = UUID(data)

                return video_input_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        video_input_id = _parse_video_input_id(d.pop("video_input_id"))

        def _parse_job_id(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_id_type_0 = UUID(data)

                return job_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        job_id = _parse_job_id(d.pop("job_id"))

        def _parse_source_platform(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        source_platform = _parse_source_platform(d.pop("source_platform"))

        status = check_marketing_ad_reference_status(d.pop("status"))

        def _parse_fail_reason(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        fail_reason = _parse_fail_reason(d.pop("fail_reason"))

        def _parse_video_s3_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        video_s3_url = _parse_video_s3_url(d.pop("video_s3_url"))

        def _parse_video_thumbnail_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        video_thumbnail_url = _parse_video_thumbnail_url(d.pop("video_thumbnail_url"))

        def _parse_video_duration_seconds(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        video_duration_seconds = _parse_video_duration_seconds(d.pop("video_duration_seconds"))

        def _parse_original_concept(
            data: object,
        ) -> Union[None, list["MarketingAdReferenceOriginalConceptType0Item"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                original_concept_type_0 = []
                _original_concept_type_0 = data
                for original_concept_type_0_item_data in _original_concept_type_0:
                    original_concept_type_0_item = (
                        MarketingAdReferenceOriginalConceptType0Item.from_dict(
                            original_concept_type_0_item_data
                        )
                    )

                    original_concept_type_0.append(original_concept_type_0_item)

                return original_concept_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["MarketingAdReferenceOriginalConceptType0Item"]], data)

        original_concept = _parse_original_concept(d.pop("original_concept"))

        def _parse_adapted_concept(
            data: object,
        ) -> Union[None, list["MarketingAdReferenceAdaptedConceptType0Item"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                adapted_concept_type_0 = []
                _adapted_concept_type_0 = data
                for adapted_concept_type_0_item_data in _adapted_concept_type_0:
                    adapted_concept_type_0_item = (
                        MarketingAdReferenceAdaptedConceptType0Item.from_dict(
                            adapted_concept_type_0_item_data
                        )
                    )

                    adapted_concept_type_0.append(adapted_concept_type_0_item)

                return adapted_concept_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["MarketingAdReferenceAdaptedConceptType0Item"]], data)

        adapted_concept = _parse_adapted_concept(d.pop("adapted_concept"))

        def _parse_edited_concept_text(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        edited_concept_text = _parse_edited_concept_text(d.pop("edited_concept_text"))

        def _parse_edited_concept_json(
            data: object,
        ) -> Union[None, list["MarketingAdReferenceEditedConceptJsonType0Item"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                edited_concept_json_type_0 = []
                _edited_concept_json_type_0 = data
                for edited_concept_json_type_0_item_data in _edited_concept_json_type_0:
                    edited_concept_json_type_0_item = (
                        MarketingAdReferenceEditedConceptJsonType0Item.from_dict(
                            edited_concept_json_type_0_item_data
                        )
                    )

                    edited_concept_json_type_0.append(edited_concept_json_type_0_item)

                return edited_concept_json_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["MarketingAdReferenceEditedConceptJsonType0Item"]], data)

        edited_concept_json = _parse_edited_concept_json(d.pop("edited_concept_json"))

        def _parse_avatar_id(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                avatar_id_type_0 = UUID(data)

                return avatar_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        avatar_id = _parse_avatar_id(d.pop("avatar_id"))

        def _parse_product_id(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                product_id_type_0 = UUID(data)

                return product_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        product_id = _parse_product_id(d.pop("product_id"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        marketing_ad_reference = cls(
            id=id,
            source_url=source_url,
            video_input_id=video_input_id,
            job_id=job_id,
            source_platform=source_platform,
            status=status,
            fail_reason=fail_reason,
            video_s3_url=video_s3_url,
            video_thumbnail_url=video_thumbnail_url,
            video_duration_seconds=video_duration_seconds,
            original_concept=original_concept,
            adapted_concept=adapted_concept,
            edited_concept_text=edited_concept_text,
            edited_concept_json=edited_concept_json,
            avatar_id=avatar_id,
            product_id=product_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        marketing_ad_reference.additional_properties = d
        return marketing_ad_reference

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
