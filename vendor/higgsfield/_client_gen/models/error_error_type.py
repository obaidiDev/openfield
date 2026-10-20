from typing import Literal, cast

ErrorErrorType = Literal[
    "account_suspended",
    "idempotency_conflict",
    "insufficient_credits",
    "internal_error",
    "invalid_media",
    "rate_limited",
    "unknown_job_type",
    "user_not_found",
    "validation_error",
    "workspace_membership_required",
    "workspace_not_found",
]

ERROR_ERROR_TYPE_VALUES: set[ErrorErrorType] = {
    "account_suspended",
    "idempotency_conflict",
    "insufficient_credits",
    "internal_error",
    "invalid_media",
    "rate_limited",
    "unknown_job_type",
    "user_not_found",
    "validation_error",
    "workspace_membership_required",
    "workspace_not_found",
}


def check_error_error_type(value: str) -> ErrorErrorType:
    return cast(ErrorErrorType, value)
