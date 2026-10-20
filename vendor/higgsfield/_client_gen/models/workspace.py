from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subscription_plan_type import SubscriptionPlanType, check_subscription_plan_type
from ..models.workspace_member_role import WorkspaceMemberRole, check_workspace_member_role
from ..models.workspace_type import WorkspaceType, check_workspace_type

T = TypeVar("T", bound="Workspace")


@_attrs_define
class Workspace:
    """A workspace the caller can access, with the caller's role and the workspace's plan and credit balance.

    Attributes:
        id (UUID): Workspace identifier.
        name (Union[None, str]): Workspace name, or null for an unnamed (private) workspace.
        type_ (WorkspaceType): Whether the workspace is a single-member private workspace or a multi-member shared/team
            workspace.
        user_role (WorkspaceMemberRole): The caller's role within the workspace.
        is_selected (bool): True if this is the workspace that account/generation operations currently target.
        plan_type (SubscriptionPlanType): Subscription plan tier.
        credits_ (float): The workspace's available credit balance (a virtual unit, not money). May be fractional.
    """

    id: UUID
    name: Union[None, str]
    type_: WorkspaceType
    user_role: WorkspaceMemberRole
    is_selected: bool
    plan_type: SubscriptionPlanType
    credits_: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name: Union[None, str]
        name = self.name

        type_: str = self.type_

        user_role: str = self.user_role

        is_selected = self.is_selected

        plan_type: str = self.plan_type

        credits_ = self.credits_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
                "user_role": user_role,
                "is_selected": is_selected,
                "plan_type": plan_type,
                "credits": credits_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        name = _parse_name(d.pop("name"))

        type_ = check_workspace_type(d.pop("type"))

        user_role = check_workspace_member_role(d.pop("user_role"))

        is_selected = d.pop("is_selected")

        plan_type = check_subscription_plan_type(d.pop("plan_type"))

        credits_ = d.pop("credits")

        workspace = cls(
            id=id,
            name=name,
            type_=type_,
            user_role=user_role,
            is_selected=is_selected,
            plan_type=plan_type,
            credits_=credits_,
        )

        workspace.additional_properties = d
        return workspace

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
