from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RepoAccessResponse")


@_attrs_define
class RepoAccessResponse:
    """Direct git access to a website's repo. Do not echo the token back to the user.

    Attributes:
        repo_url (str): Git clone URL of the website's repo.
        branch (str): Default branch to push to.
        token (str): Scoped access token for the owner's own repos.
        slug (Union[None, Unset, str]): Repo slug (a good clone-directory name).
        username (Union[None, Unset, str]): Git username for the scoped credentials.
    """

    repo_url: str
    branch: str
    token: str
    slug: Union[None, Unset, str] = UNSET
    username: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repo_url = self.repo_url

        branch = self.branch

        token = self.token

        slug: Union[None, Unset, str]
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        username: Union[None, Unset, str]
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repo_url": repo_url,
                "branch": branch,
                "token": token,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repo_url = d.pop("repo_url")

        branch = d.pop("branch")

        token = d.pop("token")

        def _parse_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_username(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        username = _parse_username(d.pop("username", UNSET))

        repo_access_response = cls(
            repo_url=repo_url,
            branch=branch,
            token=token,
            slug=slug,
            username=username,
        )

        repo_access_response.additional_properties = d
        return repo_access_response

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
