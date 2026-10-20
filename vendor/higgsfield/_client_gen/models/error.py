from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.error_error_type import ErrorErrorType, check_error_error_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_details import ErrorDetails


T = TypeVar("T", bound="Error")


@_attrs_define
class Error:
    """Standard error envelope returned on every non-2xx response.

    Attributes:
        error_type (ErrorErrorType): Stable machine-readable error code the SDK can switch on.
        message (str): Human-readable message.
        request_id (Union[Unset, str]): Correlation id for support/debugging.
        details (Union[Unset, ErrorDetails]): Optional structured context (e.g. field-level validation errors).
    """

    error_type: ErrorErrorType
    message: str
    request_id: Union[Unset, str] = UNSET
    details: Union[Unset, "ErrorDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_type: str = self.error_type

        message = self.message

        request_id = self.request_id

        details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error_type": error_type,
                "message": message,
            }
        )
        if request_id is not UNSET:
            field_dict["request_id"] = request_id
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_details import ErrorDetails

        d = dict(src_dict)
        error_type = check_error_error_type(d.pop("error_type"))

        message = d.pop("message")

        request_id = d.pop("request_id", UNSET)

        _details = d.pop("details", UNSET)
        details: Union[Unset, ErrorDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = ErrorDetails.from_dict(_details)

        error = cls(
            error_type=error_type,
            message=message,
            request_id=request_id,
            details=details,
        )

        error.additional_properties = d
        return error

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
