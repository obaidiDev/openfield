from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GamePublishResponse")


@_attrs_define
class GamePublishResponse:
    """Result of publishing a game on the marketplace (proxied from the games backend).

    Attributes:
        game_id (Union[None, str]): Id of the published game.
        status (Union[None, str]): Listing status (e.g. published).
        url (Union[None, str]): Public marketplace URL of the game.
    """

    game_id: Union[None, str]
    status: Union[None, str]
    url: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        game_id: Union[None, str]
        game_id = self.game_id

        status: Union[None, str]
        status = self.status

        url: Union[None, str]
        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "game_id": game_id,
                "status": status,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_game_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        game_id = _parse_game_id(d.pop("game_id"))

        def _parse_status(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        status = _parse_status(d.pop("status"))

        def _parse_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        url = _parse_url(d.pop("url"))

        game_publish_response = cls(
            game_id=game_id,
            status=status,
            url=url,
        )

        game_publish_response.additional_properties = d
        return game_publish_response

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
