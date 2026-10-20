"""Transport plumbing shared by the ergonomic facade.

The facade issues requests through the generated client's httpx transport and
parses responses into the generated models. Auth and client-wide default headers
are injected by an :class:`httpx.Auth` set on the client (so both the facade and
``client.raw`` are authenticated, per-instance — no global/shared state).

Per-call options follow the openai-python convention: every method accepts the
keys of :class:`RequestOptions` as keyword arguments (``extra_headers``,
``extra_query``, ``extra_body``, ``timeout``, ``idempotency_key``).
"""

from __future__ import annotations

import sys
from typing import Any, Callable, Generator, Union

import httpx

if sys.version_info >= (3, 11):
    from typing import TypedDict, Unpack
else:  # pragma: no cover - exercised on 3.9/3.10
    from typing_extensions import TypedDict, Unpack

__all__ = ["KeySource", "RequestOptions", "Unpack", "BearerAuth", "query", "body_dict"]

# A static key, or a callable re-invoked on every request (for rotating/OAuth tokens).
KeySource = Union[str, Callable[[], str]]


class RequestOptions(TypedDict, total=False):
    """Per-call options accepted as keyword arguments by every ergonomic method.

    Mirrors openai-python's per-request kwargs:

    * ``extra_headers`` (dict[str, str]): extra headers for this one request.
    * ``extra_query`` (dict): extra query params merged into the request.
    * ``extra_body`` (dict): extra fields merged into the JSON body.
    * ``timeout`` (float | httpx.Timeout): per-request timeout override.
    * ``idempotency_key`` (str): sent as ``Idempotency-Key`` for safe retries of
      generation/media POSTs — same key + same body returns the original result.
    """

    extra_headers: dict[str, str]
    extra_query: dict[str, Any]
    extra_body: dict[str, Any]
    timeout: Union[float, httpx.Timeout]
    idempotency_key: str


class BearerAuth(httpx.Auth):
    """Injects ``Authorization: Bearer <key>`` on every request.

    The key is resolved on every request, so a callable source can refresh
    rotating/OAuth tokens. (Client-wide default headers — User-Agent and any
    caller-supplied headers — live on the httpx client's header layer.)
    """

    def __init__(self, key_source: KeySource) -> None:
        self._key_source = key_source

    def auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, httpx.Response, None]:
        token = self._key_source() if callable(self._key_source) else self._key_source
        if token:
            request.headers["Authorization"] = f"Bearer {token}"
        yield request


def query(**params: Any) -> dict[str, Any]:
    """Drop ``None`` values so omitted query parameters aren't sent.

    Lists become repeated params and bools become ``true``/``false`` via httpx.
    """
    return {k: v for k, v in params.items() if v is not None}


def body_dict(body: Any) -> Any:
    """Accept either a plain dict or a generated model (anything with ``to_dict``)."""
    return body.to_dict() if hasattr(body, "to_dict") else body
