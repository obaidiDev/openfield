from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.marketing_setup_item_type import (
    MarketingSetupItemType,
    check_marketing_setup_item_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketingSetupItem")


@_attrs_define
class MarketingSetupItem:
    """A hook or setting setup item — either a user-created custom item or a curated preset.

    Attributes:
        id (str): Item id (uuid as string).
        type_ (MarketingSetupItemType): The setup item kind.
        name (str):
        prompt (Union[None, str]): The hook/setting prompt text.
        job_id (Union[None, str]): Associated preview job id, when any.
        job_status (Union[None, str]): Status of the associated preview job, when any.
        is_pinned (bool):
        thumbnail_url (Union[None, str]):
        video_url (Union[None, str]):
        source (str): Item source — custom for a user item, preset for a curated preset.
        tag (Union[None, Unset, str]): For presets, the item's tag (e.g. a hook_type); null for user items.
    """

    id: str
    type_: MarketingSetupItemType
    name: str
    prompt: Union[None, str]
    job_id: Union[None, str]
    job_status: Union[None, str]
    is_pinned: bool
    thumbnail_url: Union[None, str]
    video_url: Union[None, str]
    source: str
    tag: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str = self.type_

        name = self.name

        prompt: Union[None, str]
        prompt = self.prompt

        job_id: Union[None, str]
        job_id = self.job_id

        job_status: Union[None, str]
        job_status = self.job_status

        is_pinned = self.is_pinned

        thumbnail_url: Union[None, str]
        thumbnail_url = self.thumbnail_url

        video_url: Union[None, str]
        video_url = self.video_url

        source = self.source

        tag: Union[None, Unset, str]
        if isinstance(self.tag, Unset):
            tag = UNSET
        else:
            tag = self.tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "name": name,
                "prompt": prompt,
                "job_id": job_id,
                "job_status": job_status,
                "is_pinned": is_pinned,
                "thumbnail_url": thumbnail_url,
                "video_url": video_url,
                "source": source,
            }
        )
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = check_marketing_setup_item_type(d.pop("type"))

        name = d.pop("name")

        def _parse_prompt(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        prompt = _parse_prompt(d.pop("prompt"))

        def _parse_job_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        job_id = _parse_job_id(d.pop("job_id"))

        def _parse_job_status(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        job_status = _parse_job_status(d.pop("job_status"))

        is_pinned = d.pop("is_pinned")

        def _parse_thumbnail_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnail_url"))

        def _parse_video_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        video_url = _parse_video_url(d.pop("video_url"))

        source = d.pop("source")

        def _parse_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tag = _parse_tag(d.pop("tag", UNSET))

        marketing_setup_item = cls(
            id=id,
            type_=type_,
            name=name,
            prompt=prompt,
            job_id=job_id,
            job_status=job_status,
            is_pinned=is_pinned,
            thumbnail_url=thumbnail_url,
            video_url=video_url,
            source=source,
            tag=tag,
        )

        marketing_setup_item.additional_properties = d
        return marketing_setup_item

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
