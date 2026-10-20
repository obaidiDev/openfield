from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deploy_website_request_env import (
    DeployWebsiteRequestEnv,
    check_deploy_website_request_env,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeployWebsiteRequest")


@_attrs_define
class DeployWebsiteRequest:
    """Request to build and deploy a website.

    Attributes:
        env (Union[Unset, DeployWebsiteRequestEnv]): DEPRECATED, ignored: the preview stage was removed - every deploy
            ships the live (production) site. Kept so older clients that still send it don't fail. Default: 'production'.
    """

    env: Union[Unset, DeployWebsiteRequestEnv] = "production"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        env: Union[Unset, str] = UNSET
        if not isinstance(self.env, Unset):
            env = self.env

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if env is not UNSET:
            field_dict["env"] = env

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _env = d.pop("env", UNSET)
        env: Union[Unset, DeployWebsiteRequestEnv]
        if isinstance(_env, Unset):
            env = UNSET
        else:
            env = check_deploy_website_request_env(_env)

        deploy_website_request = cls(
            env=env,
        )

        deploy_website_request.additional_properties = d
        return deploy_website_request

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
