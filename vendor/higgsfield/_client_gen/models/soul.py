import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.soul_status import SoulStatus, check_soul_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.soul_owner_type_0 import SoulOwnerType0
    from ..models.soul_workspace_type_0 import SoulWorkspaceType0


T = TypeVar("T", bound="Soul")


@_attrs_define
class Soul:
    """A Soul ID — a trained custom-reference identity.

    Attributes:
        id (UUID): Unique Soul identifier.
        type_ (str): The custom-reference type of this Soul (e.g. soul_2, soul_cinematic, soul_v2_preset).
        status (SoulStatus): Training status of a Soul. not_ready is normalized to queued in responses, so callers
            observe queued (waiting in the training queue), in_progress (training running), completed (ready to use),
            failed, or showcase_completed (training done and showcase images generated).
        created_at (datetime.datetime): Creation time (ISO 8601).
        is_shared (bool): Whether the Soul is shareable.
        name (Union[None, Unset, str]): Display name of the Soul.
        fail_reason (Union[None, Unset, str]): Human-readable reason the training failed; null unless status is failed.
        thumbnail_url (Union[None, Unset, str]): URL of the Soul's thumbnail image.
        in_progress_at (Union[None, Unset, float]): Time training entered the in-progress state as a Unix epoch
            timestamp (seconds, fractional); null until training starts.
        user (Union['SoulOwnerType0', None, Unset]): The user that owns the Soul. May be null if profile data is
            unavailable.
        workspace (Union['SoulWorkspaceType0', None, Unset]): The shared workspace the Soul belongs to, if any. Null for
            personal Souls.
    """

    id: UUID
    type_: str
    status: SoulStatus
    created_at: datetime.datetime
    is_shared: bool
    name: Union[None, Unset, str] = UNSET
    fail_reason: Union[None, Unset, str] = UNSET
    thumbnail_url: Union[None, Unset, str] = UNSET
    in_progress_at: Union[None, Unset, float] = UNSET
    user: Union["SoulOwnerType0", None, Unset] = UNSET
    workspace: Union["SoulWorkspaceType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.soul_owner_type_0 import SoulOwnerType0
        from ..models.soul_workspace_type_0 import SoulWorkspaceType0

        id = str(self.id)

        type_ = self.type_

        status: str = self.status

        created_at = self.created_at.isoformat()

        is_shared = self.is_shared

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        fail_reason: Union[None, Unset, str]
        if isinstance(self.fail_reason, Unset):
            fail_reason = UNSET
        else:
            fail_reason = self.fail_reason

        thumbnail_url: Union[None, Unset, str]
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        in_progress_at: Union[None, Unset, float]
        if isinstance(self.in_progress_at, Unset):
            in_progress_at = UNSET
        else:
            in_progress_at = self.in_progress_at

        user: Union[None, Unset, dict[str, Any]]
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, SoulOwnerType0):
            user = self.user.to_dict()
        else:
            user = self.user

        workspace: Union[None, Unset, dict[str, Any]]
        if isinstance(self.workspace, Unset):
            workspace = UNSET
        elif isinstance(self.workspace, SoulWorkspaceType0):
            workspace = self.workspace.to_dict()
        else:
            workspace = self.workspace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "status": status,
                "created_at": created_at,
                "is_shared": is_shared,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if fail_reason is not UNSET:
            field_dict["fail_reason"] = fail_reason
        if thumbnail_url is not UNSET:
            field_dict["thumbnail_url"] = thumbnail_url
        if in_progress_at is not UNSET:
            field_dict["in_progress_at"] = in_progress_at
        if user is not UNSET:
            field_dict["user"] = user
        if workspace is not UNSET:
            field_dict["workspace"] = workspace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.soul_owner_type_0 import SoulOwnerType0
        from ..models.soul_workspace_type_0 import SoulWorkspaceType0

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = d.pop("type")

        status = check_soul_status(d.pop("status"))

        created_at = isoparse(d.pop("created_at"))

        is_shared = d.pop("is_shared")

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_fail_reason(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fail_reason = _parse_fail_reason(d.pop("fail_reason", UNSET))

        def _parse_thumbnail_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnail_url", UNSET))

        def _parse_in_progress_at(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        in_progress_at = _parse_in_progress_at(d.pop("in_progress_at", UNSET))

        def _parse_user(data: object) -> Union["SoulOwnerType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_soul_owner_type_0 = SoulOwnerType0.from_dict(data)

                return componentsschemas_soul_owner_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SoulOwnerType0", None, Unset], data)

        user = _parse_user(d.pop("user", UNSET))

        def _parse_workspace(data: object) -> Union["SoulWorkspaceType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_soul_workspace_type_0 = SoulWorkspaceType0.from_dict(data)

                return componentsschemas_soul_workspace_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SoulWorkspaceType0", None, Unset], data)

        workspace = _parse_workspace(d.pop("workspace", UNSET))

        soul = cls(
            id=id,
            type_=type_,
            status=status,
            created_at=created_at,
            is_shared=is_shared,
            name=name,
            fail_reason=fail_reason,
            thumbnail_url=thumbnail_url,
            in_progress_at=in_progress_at,
            user=user,
            workspace=workspace,
        )

        soul.additional_properties = d
        return soul

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
