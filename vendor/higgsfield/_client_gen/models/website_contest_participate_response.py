from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebsiteContestParticipateResponse")


@_attrs_define
class WebsiteContestParticipateResponse:
    """A website's contest entry after it is recorded. One entry per website — re-submitting overwrites the urls.

    Attributes:
        submission_id (UUID): The contest entry id.
        contest_id (UUID): The contest the website was entered in (backend-fixed).
        website_id (UUID): The website that was entered.
        urls (list[str]): The submitted social-media links.
    """

    submission_id: UUID
    contest_id: UUID
    website_id: UUID
    urls: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        submission_id = str(self.submission_id)

        contest_id = str(self.contest_id)

        website_id = str(self.website_id)

        urls = self.urls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "submission_id": submission_id,
                "contest_id": contest_id,
                "website_id": website_id,
                "urls": urls,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        submission_id = UUID(d.pop("submission_id"))

        contest_id = UUID(d.pop("contest_id"))

        website_id = UUID(d.pop("website_id"))

        urls = cast(list[str], d.pop("urls"))

        website_contest_participate_response = cls(
            submission_id=submission_id,
            contest_id=contest_id,
            website_id=website_id,
            urls=urls,
        )

        website_contest_participate_response.additional_properties = d
        return website_contest_participate_response

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
