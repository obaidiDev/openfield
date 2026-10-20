import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.video_analysis_status import VideoAnalysisStatus, check_video_analysis_status

if TYPE_CHECKING:
    from ..models.media_input import MediaInput
    from ..models.video_analysis_scene import VideoAnalysisScene


T = TypeVar("T", bound="VideoAnalysis")


@_attrs_define
class VideoAnalysis:
    """A video analysis and, once completed, its detected scenes.

    Attributes:
        id (UUID):
        video (Union['MediaInput', None]): Source video input ({id, type}), when created from an upload; null for a
            YouTube source.
        youtube_url (Union[None, str]): Source YouTube URL, when created from a YouTube link.
        status (VideoAnalysisStatus): Lifecycle status of a video analysis.
        fail_reason (Union[None, str]): Human-readable failure reason; null unless status is failed.
        scenes (Union[None, list['VideoAnalysisScene']]): Detected scenes, in order. Null until analysis completes
            (status = completed).
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: UUID
    video: Union["MediaInput", None]
    youtube_url: Union[None, str]
    status: VideoAnalysisStatus
    fail_reason: Union[None, str]
    scenes: Union[None, list["VideoAnalysisScene"]]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.media_input import MediaInput

        id = str(self.id)

        video: Union[None, dict[str, Any]]
        if isinstance(self.video, MediaInput):
            video = self.video.to_dict()
        else:
            video = self.video

        youtube_url: Union[None, str]
        youtube_url = self.youtube_url

        status: str = self.status

        fail_reason: Union[None, str]
        fail_reason = self.fail_reason

        scenes: Union[None, list[dict[str, Any]]]
        if isinstance(self.scenes, list):
            scenes = []
            for scenes_type_0_item_data in self.scenes:
                scenes_type_0_item = scenes_type_0_item_data.to_dict()
                scenes.append(scenes_type_0_item)

        else:
            scenes = self.scenes

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "video": video,
                "youtube_url": youtube_url,
                "status": status,
                "fail_reason": fail_reason,
                "scenes": scenes,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_input import MediaInput
        from ..models.video_analysis_scene import VideoAnalysisScene

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_video(data: object) -> Union["MediaInput", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                video_type_0 = MediaInput.from_dict(data)

                return video_type_0
            except:  # noqa: E722
                pass
            return cast(Union["MediaInput", None], data)

        video = _parse_video(d.pop("video"))

        def _parse_youtube_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        youtube_url = _parse_youtube_url(d.pop("youtube_url"))

        status = check_video_analysis_status(d.pop("status"))

        def _parse_fail_reason(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        fail_reason = _parse_fail_reason(d.pop("fail_reason"))

        def _parse_scenes(data: object) -> Union[None, list["VideoAnalysisScene"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scenes_type_0 = []
                _scenes_type_0 = data
                for scenes_type_0_item_data in _scenes_type_0:
                    scenes_type_0_item = VideoAnalysisScene.from_dict(scenes_type_0_item_data)

                    scenes_type_0.append(scenes_type_0_item)

                return scenes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["VideoAnalysisScene"]], data)

        scenes = _parse_scenes(d.pop("scenes"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        video_analysis = cls(
            id=id,
            video=video,
            youtube_url=youtube_url,
            status=status,
            fail_reason=fail_reason,
            scenes=scenes,
            created_at=created_at,
            updated_at=updated_at,
        )

        video_analysis.additional_properties = d
        return video_analysis

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
