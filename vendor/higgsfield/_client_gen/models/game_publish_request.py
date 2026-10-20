from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GamePublishRequest")


@_attrs_define
class GamePublishRequest:
    """Request to publish (list on the marketplace) a previously deployed game.

    Attributes:
        game_id (UUID): Id of the deployed game to publish.
        cover_url (Union[None, Unset, str]): https URL of the catalog-card cover image.
        logo_url (Union[None, Unset, str]): https URL of the catalog-card logo image.
        name (Union[None, Unset, str]): Optional marketplace listing name override.
        description (Union[None, Unset, str]): Optional marketplace listing description override.
    """

    game_id: UUID
    cover_url: Union[None, Unset, str] = UNSET
    logo_url: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        game_id = str(self.game_id)

        cover_url: Union[None, Unset, str]
        if isinstance(self.cover_url, Unset):
            cover_url = UNSET
        else:
            cover_url = self.cover_url

        logo_url: Union[None, Unset, str]
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "game_id": game_id,
            }
        )
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        game_id = UUID(d.pop("game_id"))

        def _parse_cover_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cover_url = _parse_cover_url(d.pop("cover_url", UNSET))

        def _parse_logo_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        game_publish_request = cls(
            game_id=game_id,
            cover_url=cover_url,
            logo_url=logo_url,
            name=name,
            description=description,
        )

        game_publish_request.additional_properties = d
        return game_publish_request

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
