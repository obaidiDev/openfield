import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.reference_element_status import ReferenceElementStatus, check_reference_element_status
from ..models.reference_element_type import ReferenceElementType, check_reference_element_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference_element_audio_input import ReferenceElementAudioInput
    from ..models.reference_element_author_type_0 import ReferenceElementAuthorType0
    from ..models.reference_element_detail_workspace_type_0 import (
        ReferenceElementDetailWorkspaceType0,
    )
    from ..models.reference_element_media import ReferenceElementMedia
    from ..models.reference_element_workspace_ref import ReferenceElementWorkspaceRef


T = TypeVar("T", bound="ReferenceElementDetail")


@_attrs_define
class ReferenceElementDetail:
    """A reusable reference element with full detail (returned by get). is_shared is the wire name for the server's
    internal is_shareable flag.

        Attributes:
            id (UUID):
            category (ReferenceElementType): Kind of a reference element. auto is an input-only request value that triggers
                server-side classification; the server then stores and returns one of the auto:* variants. The *_ip_verified
                variants are reserved for elements sourced from IP-verified soul jobs.
            name (Union[None, str]):
            images (list['ReferenceElementMedia']): Image media attached to the element.
            videos (list['ReferenceElementMedia']): Video media attached to the element.
            status (ReferenceElementStatus): Lifecycle status of a reference element.
            is_pinned (bool):
            is_shared (bool): Whether the element is shared with other workspace members.
            is_audio_eligible (bool): Whether voice cloning is enabled for this element.
            workspaces (list['ReferenceElementWorkspaceRef']): All workspaces this element is associated with (via the
                junction table).
            folder_ids (list[UUID]): Ids of the folders this element is currently linked to.
            created_at (datetime.datetime): Creation time (ISO 8601).
            description (Union[None, Unset, str]):
            audios (Union[Unset, list['ReferenceElementAudioInput']]): Cloned-voice audio inputs backing the element (voice
                elements).
            user (Union['ReferenceElementAuthorType0', None, Unset]): The element's attributed author. Null when the owning
                user can't be resolved (e.g. anonymised clones from a member leaving a project).
            workspace (Union['ReferenceElementDetailWorkspaceType0', None, Unset]): Provenance workspace where the element
                was originally created. Null when not set.
            ip_detected (Union[None, Unset, bool]): IP-check verdict: null = not checked, true = potential IP found, false =
                clean.
    """

    id: UUID
    category: ReferenceElementType
    name: Union[None, str]
    images: list["ReferenceElementMedia"]
    videos: list["ReferenceElementMedia"]
    status: ReferenceElementStatus
    is_pinned: bool
    is_shared: bool
    is_audio_eligible: bool
    workspaces: list["ReferenceElementWorkspaceRef"]
    folder_ids: list[UUID]
    created_at: datetime.datetime
    description: Union[None, Unset, str] = UNSET
    audios: Union[Unset, list["ReferenceElementAudioInput"]] = UNSET
    user: Union["ReferenceElementAuthorType0", None, Unset] = UNSET
    workspace: Union["ReferenceElementDetailWorkspaceType0", None, Unset] = UNSET
    ip_detected: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.reference_element_author_type_0 import ReferenceElementAuthorType0
        from ..models.reference_element_detail_workspace_type_0 import (
            ReferenceElementDetailWorkspaceType0,
        )

        id = str(self.id)

        category: str = self.category

        name: Union[None, str]
        name = self.name

        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)

        videos = []
        for videos_item_data in self.videos:
            videos_item = videos_item_data.to_dict()
            videos.append(videos_item)

        status: str = self.status

        is_pinned = self.is_pinned

        is_shared = self.is_shared

        is_audio_eligible = self.is_audio_eligible

        workspaces = []
        for workspaces_item_data in self.workspaces:
            workspaces_item = workspaces_item_data.to_dict()
            workspaces.append(workspaces_item)

        folder_ids = []
        for folder_ids_item_data in self.folder_ids:
            folder_ids_item = str(folder_ids_item_data)
            folder_ids.append(folder_ids_item)

        created_at = self.created_at.isoformat()

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        audios: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.audios, Unset):
            audios = []
            for audios_item_data in self.audios:
                audios_item = audios_item_data.to_dict()
                audios.append(audios_item)

        user: Union[None, Unset, dict[str, Any]]
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, ReferenceElementAuthorType0):
            user = self.user.to_dict()
        else:
            user = self.user

        workspace: Union[None, Unset, dict[str, Any]]
        if isinstance(self.workspace, Unset):
            workspace = UNSET
        elif isinstance(self.workspace, ReferenceElementDetailWorkspaceType0):
            workspace = self.workspace.to_dict()
        else:
            workspace = self.workspace

        ip_detected: Union[None, Unset, bool]
        if isinstance(self.ip_detected, Unset):
            ip_detected = UNSET
        else:
            ip_detected = self.ip_detected

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "category": category,
                "name": name,
                "images": images,
                "videos": videos,
                "status": status,
                "is_pinned": is_pinned,
                "is_shared": is_shared,
                "is_audio_eligible": is_audio_eligible,
                "workspaces": workspaces,
                "folder_ids": folder_ids,
                "created_at": created_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if audios is not UNSET:
            field_dict["audios"] = audios
        if user is not UNSET:
            field_dict["user"] = user
        if workspace is not UNSET:
            field_dict["workspace"] = workspace
        if ip_detected is not UNSET:
            field_dict["ip_detected"] = ip_detected

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reference_element_audio_input import ReferenceElementAudioInput
        from ..models.reference_element_author_type_0 import ReferenceElementAuthorType0
        from ..models.reference_element_detail_workspace_type_0 import (
            ReferenceElementDetailWorkspaceType0,
        )
        from ..models.reference_element_media import ReferenceElementMedia
        from ..models.reference_element_workspace_ref import ReferenceElementWorkspaceRef

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        category = check_reference_element_type(d.pop("category"))

        def _parse_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        name = _parse_name(d.pop("name"))

        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = ReferenceElementMedia.from_dict(images_item_data)

            images.append(images_item)

        videos = []
        _videos = d.pop("videos")
        for videos_item_data in _videos:
            videos_item = ReferenceElementMedia.from_dict(videos_item_data)

            videos.append(videos_item)

        status = check_reference_element_status(d.pop("status"))

        is_pinned = d.pop("is_pinned")

        is_shared = d.pop("is_shared")

        is_audio_eligible = d.pop("is_audio_eligible")

        workspaces = []
        _workspaces = d.pop("workspaces")
        for workspaces_item_data in _workspaces:
            workspaces_item = ReferenceElementWorkspaceRef.from_dict(workspaces_item_data)

            workspaces.append(workspaces_item)

        folder_ids = []
        _folder_ids = d.pop("folder_ids")
        for folder_ids_item_data in _folder_ids:
            folder_ids_item = UUID(folder_ids_item_data)

            folder_ids.append(folder_ids_item)

        created_at = isoparse(d.pop("created_at"))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        audios = []
        _audios = d.pop("audios", UNSET)
        for audios_item_data in _audios or []:
            audios_item = ReferenceElementAudioInput.from_dict(audios_item_data)

            audios.append(audios_item)

        def _parse_user(data: object) -> Union["ReferenceElementAuthorType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_reference_element_author_type_0 = (
                    ReferenceElementAuthorType0.from_dict(data)
                )

                return componentsschemas_reference_element_author_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ReferenceElementAuthorType0", None, Unset], data)

        user = _parse_user(d.pop("user", UNSET))

        def _parse_workspace(
            data: object,
        ) -> Union["ReferenceElementDetailWorkspaceType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = ReferenceElementDetailWorkspaceType0.from_dict(data)

                return workspace_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ReferenceElementDetailWorkspaceType0", None, Unset], data)

        workspace = _parse_workspace(d.pop("workspace", UNSET))

        def _parse_ip_detected(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        ip_detected = _parse_ip_detected(d.pop("ip_detected", UNSET))

        reference_element_detail = cls(
            id=id,
            category=category,
            name=name,
            images=images,
            videos=videos,
            status=status,
            is_pinned=is_pinned,
            is_shared=is_shared,
            is_audio_eligible=is_audio_eligible,
            workspaces=workspaces,
            folder_ids=folder_ids,
            created_at=created_at,
            description=description,
            audios=audios,
            user=user,
            workspace=workspace,
            ip_detected=ip_detected,
        )

        reference_element_detail.additional_properties = d
        return reference_element_detail

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
