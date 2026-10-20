from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GameDeployRequest")


@_attrs_define
class GameDeployRequest:
    """Request to deploy an agent-built game from an uploaded source archive.

    Attributes:
        title (str): Display title of the game.
        description (str): Short description shown on the game's marketplace card.
        source_game (str): https URL of the zipped game build to deploy (previously uploaded by the agent).
        thumbnail (Union[None, Unset, str]): Optional https URL of a thumbnail image.
        favicon (Union[None, Unset, str]): Optional https URL of a favicon.
        game_id (Union[None, Unset, str]): Existing game id to redeploy over. Omit to create a new game.
    """

    title: str
    description: str
    source_game: str
    thumbnail: Union[None, Unset, str] = UNSET
    favicon: Union[None, Unset, str] = UNSET
    game_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        description = self.description

        source_game = self.source_game

        thumbnail: Union[None, Unset, str]
        if isinstance(self.thumbnail, Unset):
            thumbnail = UNSET
        else:
            thumbnail = self.thumbnail

        favicon: Union[None, Unset, str]
        if isinstance(self.favicon, Unset):
            favicon = UNSET
        else:
            favicon = self.favicon

        game_id: Union[None, Unset, str]
        if isinstance(self.game_id, Unset):
            game_id = UNSET
        else:
            game_id = self.game_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "description": description,
                "source_game": source_game,
            }
        )
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if favicon is not UNSET:
            field_dict["favicon"] = favicon
        if game_id is not UNSET:
            field_dict["game_id"] = game_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        description = d.pop("description")

        source_game = d.pop("source_game")

        def _parse_thumbnail(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        thumbnail = _parse_thumbnail(d.pop("thumbnail", UNSET))

        def _parse_favicon(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        favicon = _parse_favicon(d.pop("favicon", UNSET))

        def _parse_game_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        game_id = _parse_game_id(d.pop("game_id", UNSET))

        game_deploy_request = cls(
            title=title,
            description=description,
            source_game=source_game,
            thumbnail=thumbnail,
            favicon=favicon,
            game_id=game_id,
        )

        game_deploy_request.additional_properties = d
        return game_deploy_request

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
