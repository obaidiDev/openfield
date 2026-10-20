from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.transaction import Transaction


T = TypeVar("T", bound="TransactionsResponse")


@_attrs_define
class TransactionsResponse:
    """A cursor-paginated page of credit transactions.

    Attributes:
        items (list['Transaction']): The transactions in this page, newest first.
        cursor (Union[None, str]): Opaque cursor for the next page; pass it back as the cursor query parameter. null on
            the last page.
    """

    items: list["Transaction"]
    cursor: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        cursor: Union[None, str]
        cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "cursor": cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transaction import Transaction

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = Transaction.from_dict(items_item_data)

            items.append(items_item)

        def _parse_cursor(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        cursor = _parse_cursor(d.pop("cursor"))

        transactions_response = cls(
            items=items,
            cursor=cursor,
        )

        transactions_response.additional_properties = d
        return transactions_response

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
