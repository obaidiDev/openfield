"""The single error type raised by every ergonomic client method.

Facade methods return data directly on success and raise ``HiggsfieldError`` on
any non-2xx response, network failure, or transport error — so you catch one
exception type instead of inspecting ``Response`` envelopes.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    import httpx


class HiggsfieldError(Exception):
    """Raised on a failed Higgsfield API request.

    Attributes:
        status: HTTP status code, when a response was received.
        error_type: Stable machine-readable error code from the API envelope.
        request_id: Server request id from the API envelope — quote it to support.
        body: The raw error body (parsed JSON, or text).
        response: The underlying ``httpx.Response``, when one was received.
    """

    def __init__(
        self,
        message: str,
        *,
        status: Optional[int] = None,
        error_type: Optional[str] = None,
        request_id: Optional[str] = None,
        body: Any = None,
        response: "Optional[httpx.Response]" = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status = status
        self.error_type = error_type
        self.request_id = request_id
        self.body = body
        self.response = response

    @classmethod
    def from_response(cls, response: "httpx.Response") -> "HiggsfieldError":
        """Build an error from a non-2xx ``httpx.Response``."""
        body: Any = None
        envelope: Optional[dict[str, Any]] = None
        if response.content:
            try:
                body = response.json()
                if isinstance(body, dict):
                    envelope = body
            except ValueError:
                body = response.text

        api_message = envelope.get("message") if envelope else None
        message = api_message or f"Request failed with status {response.status_code}"

        return cls(
            message,
            status=response.status_code,
            error_type=envelope.get("error_type") if envelope else None,
            request_id=envelope.get("request_id") if envelope else None,
            body=body,
            response=response,
        )
