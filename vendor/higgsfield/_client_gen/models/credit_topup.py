from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.currency import Currency, check_currency
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditTopup")


@_attrs_define
class CreditTopup:
    """A one-time credit top-up pack. Credits are a virtual unit; price fields are money (integer minor units, cents) in
    currency.

        Attributes:
            id (str): Stable identifier of the top-up pack (e.g. "credits_4000"). Pass this as topup_id to
                confirmBillingPurchase.
            credits_ (int): Credits granted by this pack (a virtual unit, not money).
            price_cents (int): Charged price in minor currency units (cents).
            dollar_to_credits_ratio (int): Credits granted per one unit of currency.
            checkout_url (str): Hosted checkout URL for this top-up pack.
            most_popular (bool): Whether this pack is flagged as the most popular option.
            currency (Currency): ISO 4217 currency code, lowercased. Higgsfield supports these three; amounts are the same
                number across currencies (no FX conversion of our prices).
            display_amount_cents (Union[None, Unset, int]): Price to display in minor currency units (cents), if it differs
                from the charged price. Null when not applicable.
            original_price_cents (Union[None, Unset, int]): Pre-discount price in minor currency units (cents). Null when
                there is no discount.
            discount_percent (Union[None, Unset, int]): Discount percentage on this pack, or null when there is none.
    """

    id: str
    credits_: int
    price_cents: int
    dollar_to_credits_ratio: int
    checkout_url: str
    most_popular: bool
    currency: Currency
    display_amount_cents: Union[None, Unset, int] = UNSET
    original_price_cents: Union[None, Unset, int] = UNSET
    discount_percent: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        credits_ = self.credits_

        price_cents = self.price_cents

        dollar_to_credits_ratio = self.dollar_to_credits_ratio

        checkout_url = self.checkout_url

        most_popular = self.most_popular

        currency: str = self.currency

        display_amount_cents: Union[None, Unset, int]
        if isinstance(self.display_amount_cents, Unset):
            display_amount_cents = UNSET
        else:
            display_amount_cents = self.display_amount_cents

        original_price_cents: Union[None, Unset, int]
        if isinstance(self.original_price_cents, Unset):
            original_price_cents = UNSET
        else:
            original_price_cents = self.original_price_cents

        discount_percent: Union[None, Unset, int]
        if isinstance(self.discount_percent, Unset):
            discount_percent = UNSET
        else:
            discount_percent = self.discount_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "credits": credits_,
                "price_cents": price_cents,
                "dollar_to_credits_ratio": dollar_to_credits_ratio,
                "checkout_url": checkout_url,
                "most_popular": most_popular,
                "currency": currency,
            }
        )
        if display_amount_cents is not UNSET:
            field_dict["display_amount_cents"] = display_amount_cents
        if original_price_cents is not UNSET:
            field_dict["original_price_cents"] = original_price_cents
        if discount_percent is not UNSET:
            field_dict["discount_percent"] = discount_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        credits_ = d.pop("credits")

        price_cents = d.pop("price_cents")

        dollar_to_credits_ratio = d.pop("dollar_to_credits_ratio")

        checkout_url = d.pop("checkout_url")

        most_popular = d.pop("most_popular")

        currency = check_currency(d.pop("currency"))

        def _parse_display_amount_cents(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        display_amount_cents = _parse_display_amount_cents(d.pop("display_amount_cents", UNSET))

        def _parse_original_price_cents(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        original_price_cents = _parse_original_price_cents(d.pop("original_price_cents", UNSET))

        def _parse_discount_percent(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        discount_percent = _parse_discount_percent(d.pop("discount_percent", UNSET))

        credit_topup = cls(
            id=id,
            credits_=credits_,
            price_cents=price_cents,
            dollar_to_credits_ratio=dollar_to_credits_ratio,
            checkout_url=checkout_url,
            most_popular=most_popular,
            currency=currency,
            display_amount_cents=display_amount_cents,
            original_price_cents=original_price_cents,
            discount_percent=discount_percent,
        )

        credit_topup.additional_properties = d
        return credit_topup

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
