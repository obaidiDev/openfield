from typing import Literal, cast

WorkspaceType = Literal["private", "shared"]

WORKSPACE_TYPE_VALUES: set[WorkspaceType] = {
    "private",
    "shared",
}


def check_workspace_type(value: str) -> WorkspaceType:
    return cast(WorkspaceType, value)
