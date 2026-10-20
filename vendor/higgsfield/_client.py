"""The :class:`Higgsfield` client — the ergonomic entry point to the SDK.

Every method takes a flat input, returns the result data directly, and raises a
typed :class:`HiggsfieldError` on failure::

    from higgsfield import Higgsfield

    client = Higgsfield(api_key=os.environ["HIGGSFIELD_API_KEY"])

    job = client.images.create(
        job_type="nano_banana_2",
        params={"prompt": "a serene mountain lake at dawn", "resolution": "2k"},
    )
    finished = client.wait_for_job(job.id)
    print(finished.result_url)

For endpoints the facade does not cover yet, reach the generated low-level
client via ``client.raw`` (see ``higgsfield._client_gen``).
"""

from __future__ import annotations

import platform
import time
from typing import Any, Callable, Optional, Union

import httpx

from ._client_gen import Client as _GeneratedClient
from ._client_gen.models.job import Job
from ._exceptions import HiggsfieldError
from ._transport import BearerAuth, KeySource, RequestOptions, Unpack
from ._version import __version__
from .resources.account import AccountResource
from .resources.games import GamesResource
from .resources.websites import WebsitesResource
from .resources.generation import (
    AudiosResource,
    DataResource,
    ImagesResource,
    Models3dResource,
    TextsResource,
    VideosResource,
)
from .resources.job_types import JobTypesResource
from .resources.jobs import JobsResource
from .resources.marketing_studio import MarketingStudioResource
from .resources.media import MediaResource
from .resources.presets import PresetsResource
from .resources.realtime import RealtimeResource
from .resources.references import ReferencesResource
from .resources.souls import SoulsResource
from .resources.video_analysis import VideoAnalysisResource
from .resources.workflows import WorkflowsResource

DEFAULT_BASE_URL = "https://fnf-api-gw.higgsfield.ai/fnf"
DEFAULT_USER_AGENT = f"higgsfield-python/{__version__} python/{platform.python_version()}"
# Bounded by default (httpx would otherwise leave a request without a deadline
# when constructed with timeout=None). Generous total to cover media uploads;
# short connect so a dead host fails fast.
DEFAULT_TIMEOUT = httpx.Timeout(600.0, connect=5.0)

# Terminal job statuses — polling stops once a job reaches one of these.
TERMINAL_STATUSES = frozenset({"completed", "failed", "canceled", "nsfw", "ip_detected"})


def is_terminal_status(status: str) -> bool:
    """Report whether a job status is terminal (polling stops)."""
    return str(status) in TERMINAL_STATUSES


class Higgsfield:
    """Ergonomic entry point to the Higgsfield API."""

    def __init__(
        self,
        api_key: KeySource,
        *,
        base_url: str = DEFAULT_BASE_URL,
        timeout: Union[float, httpx.Timeout, None] = None,
        headers: Optional[dict[str, str]] = None,
        http_client: Optional[httpx.Client] = None,
    ) -> None:
        """Construct a client.

        Args:
            api_key: API key sent as ``Authorization: Bearer <key>``. A string,
                or a no-arg callable re-invoked on every request (rotating/OAuth
                tokens).
            base_url: API base URL. Defaults to the production gateway.
            timeout: Request timeout — seconds (float) or an ``httpx.Timeout``.
                Defaults to 600s total / 5s connect. Override per request with
                the ``timeout`` keyword. Ignored when ``http_client`` is supplied
                (that client's own timeout applies).
            headers: Default headers merged into every request.
            http_client: A pre-configured ``httpx.Client`` (proxies, transports,
                testing). Auth is set on it via ``httpx.Auth`` — use a distinct
                client per ``Higgsfield`` instance.
        """
        if http_client is None:
            http_client = httpx.Client(
                base_url=base_url,
                timeout=DEFAULT_TIMEOUT if timeout is None else timeout,
            )
        # Client-wide default headers (our User-Agent, then any caller override)
        # on the httpx header layer — so they apply to the facade and client.raw
        # alike, and a per-call extra_headers value still wins. Setting them here
        # (rather than via setdefault in auth) lets our User-Agent replace httpx's.
        http_client.headers.update({"User-Agent": DEFAULT_USER_AGENT, **(headers or {})})
        # Per-instance auth, set on the client (not an event hook) so two
        # instances never share/duplicate auth state.
        http_client.auth = BearerAuth(api_key)
        self._http = http_client

        #: The generated low-level client — escape hatch for endpoints the facade
        #: does not cover. Shares the same authenticated httpx transport.
        self.raw = _GeneratedClient(base_url=base_url).set_httpx_client(http_client)

        self.images = ImagesResource(self)
        self.videos = VideosResource(self)
        self.audios = AudiosResource(self)
        self.texts = TextsResource(self)
        self.models3d = Models3dResource(self)
        self.data = DataResource(self)
        self.jobs = JobsResource(self)
        self.media = MediaResource(self)
        self.account = AccountResource(self)
        self.references = ReferencesResource(self)
        self.souls = SoulsResource(self)
        self.job_types = JobTypesResource(self)
        self.presets = PresetsResource(self)
        self.realtime = RealtimeResource(self)
        self.games = GamesResource(self)
        self.websites = WebsitesResource(self)
        self.workflows = WorkflowsResource(self)
        self.video_analysis = VideoAnalysisResource(self)
        self.marketing_studio = MarketingStudioResource(self)

    def _request(
        self,
        method: str,
        url: str,
        *,
        params: Optional[dict[str, Any]] = None,
        json: Any = None,
        **options: Unpack[RequestOptions],
    ) -> httpx.Response:
        """Issue a request through the shared transport, raising on failure.

        Honors the openai-style per-call options in ``**options``."""
        if options.get("extra_query"):
            params = {**(params or {}), **options["extra_query"]}
        if options.get("extra_body") and isinstance(json, dict):
            json = {**json, **options["extra_body"]}

        headers = dict(options.get("extra_headers") or {})
        if options.get("idempotency_key"):
            headers["Idempotency-Key"] = options["idempotency_key"]

        kwargs: dict[str, Any] = {}
        if options.get("timeout") is not None:
            kwargs["timeout"] = options["timeout"]

        try:
            response = self._http.request(
                method, url, params=params, json=json, headers=headers or None, **kwargs
            )
        except httpx.HTTPError as exc:
            raise HiggsfieldError(f"request failed: {exc}") from exc
        except (TypeError, ValueError) as exc:  # e.g. a non-JSON-serializable body
            raise HiggsfieldError(f"failed to encode request: {exc}") from exc
        if not 200 <= response.status_code < 300:
            raise HiggsfieldError.from_response(response)
        return response

    def _request_unauthed(
        self,
        method: str,
        url: str,
        *,
        content: Any = None,
        headers: Optional[dict[str, str]] = None,
    ) -> httpx.Response:
        """Issue a request to an absolute URL WITHOUT the bearer token (e.g. a
        presigned S3 upload), through the shared transport, wrapping transport
        errors. The caller inspects the returned response."""
        try:
            return self._http.request(method, url, content=content, headers=headers, auth=None)
        except httpx.HTTPError as exc:
            raise HiggsfieldError(f"request failed: {exc}") from exc

    def close(self) -> None:
        """Close the underlying HTTP transport."""
        self._http.close()

    def __enter__(self) -> "Higgsfield":
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()

    def wait_for_job(
        self,
        job_id: str,
        *,
        interval: float = 3.0,
        timeout: float = 600.0,
        on_poll: Optional[Callable[[Job], None]] = None,
    ) -> Job:
        """Poll a job until it reaches a terminal status (or ``timeout`` elapses).

        Returns the final :class:`Job`. Raises :class:`HiggsfieldError` if the job
        ends in any non-``completed`` terminal state (the failed job is attached
        as ``error.body``) or the timeout is exceeded.
        """
        deadline = time.monotonic() + timeout
        while True:
            job = self.jobs.get(job_id)
            if on_poll is not None:
                on_poll(job)

            status = str(job.status)
            if is_terminal_status(status):
                if status != "completed":
                    raise HiggsfieldError(
                        f'Job {job_id} ended with status "{status}".',
                        error_type=status,
                        body=job,
                    )
                return job

            if time.monotonic() >= deadline:
                raise HiggsfieldError(
                    f"Timed out after {timeout}s waiting for job {job_id} "
                    f'(last status "{status}").',
                    body=job,
                )
            time.sleep(interval)
