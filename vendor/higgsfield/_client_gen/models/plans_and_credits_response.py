from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credit_topup import CreditTopup
    from ..models.plan import Plan


T = TypeVar("T", bound="PlansAndCreditsResponse")


@_attrs_define
class PlansAndCreditsResponse:
    """Subscription plans and one-time credit top-up packs available to the caller, with pricing.

    Attributes:
        plans (list['Plan']): Subscription plan cards.
        already_subscribed (bool): True when the active workspace is already on a paid plan (the upgrade options are
            hidden in that case).
        topups (list['CreditTopup']): One-time credit top-up packs.
        topups_expire_days (int): Number of days after which purchased top-up credits expire.
        current_plan (Union[None, Unset, str]): The caller's current plan tier, or null if none.
        auto_top_up_setup_url (Union[None, Unset, str]): Hosted URL to set up auto top-up, when available.
        top_annual_discount_percent (Union[None, Unset, int]): Largest annual-billing discount percentage across the
            plan cards, for display. Null when not applicable.
    """

    plans: list["Plan"]
    already_subscribed: bool
    topups: list["CreditTopup"]
    topups_expire_days: int
    current_plan: Union[None, Unset, str] = UNSET
    auto_top_up_setup_url: Union[None, Unset, str] = UNSET
    top_annual_discount_percent: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plans = []
        for plans_item_data in self.plans:
            plans_item = plans_item_data.to_dict()
            plans.append(plans_item)

        already_subscribed = self.already_subscribed

        topups = []
        for topups_item_data in self.topups:
            topups_item = topups_item_data.to_dict()
            topups.append(topups_item)

        topups_expire_days = self.topups_expire_days

        current_plan: Union[None, Unset, str]
        if isinstance(self.current_plan, Unset):
            current_plan = UNSET
        else:
            current_plan = self.current_plan

        auto_top_up_setup_url: Union[None, Unset, str]
        if isinstance(self.auto_top_up_setup_url, Unset):
            auto_top_up_setup_url = UNSET
        else:
            auto_top_up_setup_url = self.auto_top_up_setup_url

        top_annual_discount_percent: Union[None, Unset, int]
        if isinstance(self.top_annual_discount_percent, Unset):
            top_annual_discount_percent = UNSET
        else:
            top_annual_discount_percent = self.top_annual_discount_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plans": plans,
                "already_subscribed": already_subscribed,
                "topups": topups,
                "topups_expire_days": topups_expire_days,
            }
        )
        if current_plan is not UNSET:
            field_dict["current_plan"] = current_plan
        if auto_top_up_setup_url is not UNSET:
            field_dict["auto_top_up_setup_url"] = auto_top_up_setup_url
        if top_annual_discount_percent is not UNSET:
            field_dict["top_annual_discount_percent"] = top_annual_discount_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credit_topup import CreditTopup
        from ..models.plan import Plan

        d = dict(src_dict)
        plans = []
        _plans = d.pop("plans")
        for plans_item_data in _plans:
            plans_item = Plan.from_dict(plans_item_data)

            plans.append(plans_item)

        already_subscribed = d.pop("already_subscribed")

        topups = []
        _topups = d.pop("topups")
        for topups_item_data in _topups:
            topups_item = CreditTopup.from_dict(topups_item_data)

            topups.append(topups_item)

        topups_expire_days = d.pop("topups_expire_days")

        def _parse_current_plan(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        current_plan = _parse_current_plan(d.pop("current_plan", UNSET))

        def _parse_auto_top_up_setup_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        auto_top_up_setup_url = _parse_auto_top_up_setup_url(d.pop("auto_top_up_setup_url", UNSET))

        def _parse_top_annual_discount_percent(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        top_annual_discount_percent = _parse_top_annual_discount_percent(
            d.pop("top_annual_discount_percent", UNSET)
        )

        plans_and_credits_response = cls(
            plans=plans,
            already_subscribed=already_subscribed,
            topups=topups,
            topups_expire_days=topups_expire_days,
            current_plan=current_plan,
            auto_top_up_setup_url=auto_top_up_setup_url,
            top_annual_discount_percent=top_annual_discount_percent,
        )

        plans_and_credits_response.additional_properties = d
        return plans_and_credits_response

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
