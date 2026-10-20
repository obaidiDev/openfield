from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_input import MediaInput


T = TypeVar("T", bound="MarketingAdReferenceCreateRequest")


@_attrs_define
class MarketingAdReferenceCreateRequest:
    """Create an ad reference by cloning a source video. Provide exactly one source — source_url (a public video URL) or
    video (a flat media reference to an uploaded video input or a prior job's video result).

        Attributes:
            source_url (Union[None, Unset, str]): Public video URL to clone (downloaded server-side).
            video (Union['MediaInput', None, Unset]): Flat media reference ({id, type}) — media_input for an uploaded video
                input, any other type for a prior job whose video result to clone.
            avatar_id (Union[None, UUID, Unset]): Optional avatar to bind to the scenario.
            product_id (Union[None, UUID, Unset]): Optional product to bind to the scenario.
    """

    source_url: Union[None, Unset, str] = UNSET
    video: Union["MediaInput", None, Unset] = UNSET
    avatar_id: Union[None, UUID, Unset] = UNSET
    product_id: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.media_input import MediaInput

        source_url: Union[None, Unset, str]
        if isinstance(self.source_url, Unset):
            source_url = UNSET
        else:
            source_url = self.source_url

        video: Union[None, Unset, dict[str, Any]]
        if isinstance(self.video, Unset):
            video = UNSET
        elif isinstance(self.video, MediaInput):
            video = self.video.to_dict()
        else:
            video = self.video

        avatar_id: Union[None, Unset, str]
        if isinstance(self.avatar_id, Unset):
            avatar_id = UNSET
        elif isinstance(self.avatar_id, UUID):
            avatar_id = str(self.avatar_id)
        else:
            avatar_id = self.avatar_id

        product_id: Union[None, Unset, str]
        if isinstance(self.product_id, Unset):
            product_id = UNSET
        elif isinstance(self.product_id, UUID):
            product_id = str(self.product_id)
        else:
            product_id = self.product_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_url is not UNSET:
            field_dict["source_url"] = source_url
        if video is not UNSET:
            field_dict["video"] = video
        if avatar_id is not UNSET:
            field_dict["avatar_id"] = avatar_id
        if product_id is not UNSET:
            field_dict["product_id"] = product_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_input import MediaInput

        d = dict(src_dict)

        def _parse_source_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_url = _parse_source_url(d.pop("source_url", UNSET))

        def _parse_video(data: object) -> Union["MediaInput", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                video_type_0 = MediaInput.from_dict(data)

                return video_type_0
            except:  # noqa: E722
                pass
            return cast(Union["MediaInput", None, Unset], data)

        video = _parse_video(d.pop("video", UNSET))

        def _parse_avatar_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                avatar_id_type_0 = UUID(data)

                return avatar_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        avatar_id = _parse_avatar_id(d.pop("avatar_id", UNSET))

        def _parse_product_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                product_id_type_0 = UUID(data)

                return product_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        product_id = _parse_product_id(d.pop("product_id", UNSET))

        marketing_ad_reference_create_request = cls(
            source_url=source_url,
            video=video,
            avatar_id=avatar_id,
            product_id=product_id,
        )

        marketing_ad_reference_create_request.additional_properties = d
        return marketing_ad_reference_create_request

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
