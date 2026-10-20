from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_input import MediaInput


T = TypeVar("T", bound="CreateVideoAnalysisRequest")


@_attrs_define
class CreateVideoAnalysisRequest:
    """Request to analyze a video. Provide exactly one of video or youtube_url; when youtube_url is given it must point to
    a YouTube host.

        Attributes:
            video (Union['MediaInput', None, Unset]): An already-uploaded video input to analyze, as a flat media reference
                ({id, type}).
            youtube_url (Union[None, Unset, str]): A public/unlisted YouTube URL to analyze.
    """

    video: Union["MediaInput", None, Unset] = UNSET
    youtube_url: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.media_input import MediaInput

        video: Union[None, Unset, dict[str, Any]]
        if isinstance(self.video, Unset):
            video = UNSET
        elif isinstance(self.video, MediaInput):
            video = self.video.to_dict()
        else:
            video = self.video

        youtube_url: Union[None, Unset, str]
        if isinstance(self.youtube_url, Unset):
            youtube_url = UNSET
        else:
            youtube_url = self.youtube_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if video is not UNSET:
            field_dict["video"] = video
        if youtube_url is not UNSET:
            field_dict["youtube_url"] = youtube_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_input import MediaInput

        d = dict(src_dict)

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

        def _parse_youtube_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        youtube_url = _parse_youtube_url(d.pop("youtube_url", UNSET))

        create_video_analysis_request = cls(
            video=video,
            youtube_url=youtube_url,
        )

        create_video_analysis_request.additional_properties = d
        return create_video_analysis_request

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
