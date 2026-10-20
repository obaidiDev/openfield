"""Base class for every ergonomic resource."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .._transport import RequestOptions, Unpack

if TYPE_CHECKING:
    import httpx

    from .._client import Higgsfield


class Resource:
    """Holds the parent client and delegates HTTP to its shared transport."""

    def __init__(self, client: "Higgsfield") -> None:
        self._client = client

    def _request(
        self,
        method: str,
        url: str,
        *,
        params: Optional[dict[str, Any]] = None,
        json: Any = None,
        **options: Unpack[RequestOptions],
    ) -> "httpx.Response":
        return self._client._request(method, url, params=params, json=json, **options)

    # Verb-named JSON helpers. scripts/check_coverage.py extracts (verb, path)
    # from these calls, so paths passed to them must stay literal f-strings.
    def _get_json(
        self,
        url: str,
        *,
        params: Optional[dict[str, Any]] = None,
        **options: Unpack[RequestOptions],
    ) -> Any:
        return self._request("get", url, params=params, **options).json()

    def _post_json(
        self,
        url: str,
        *,
        params: Optional[dict[str, Any]] = None,
        json: Any = None,
        **options: Unpack[RequestOptions],
    ) -> Any:
        return self._request("post", url, params=params, json=json, **options).json()

    def _patch_json(self, url: str, *, json: Any = None, **options: Unpack[RequestOptions]) -> Any:
        return self._request("patch", url, json=json, **options).json()

    def _delete_json(self, url: str, **options: Unpack[RequestOptions]) -> Any:
        return self._request("delete", url, **options).json()

    def _delete(self, url: str, **options: Unpack[RequestOptions]) -> None:
        self._request("delete", url, **options)
