from typing import Literal, cast

WorkspaceMemberRole = Literal["admin", "member", "owner"]

WORKSPACE_MEMBER_ROLE_VALUES: set[WorkspaceMemberRole] = {
    "admin",
    "member",
    "owner",
}


def check_workspace_member_role(value: str) -> WorkspaceMemberRole:
    return cast(WorkspaceMemberRole, value)
