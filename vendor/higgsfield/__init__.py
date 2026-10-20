"""higgsfield — Python SDK for the Higgsfield API.

The :class:`Higgsfield` client gives every endpoint a flat surface: pass a flat
input, get the result back, and catch a typed :class:`HiggsfieldError` on failure.

    from higgsfield import Higgsfield

    client = Higgsfield(api_key=os.environ["HIGGSFIELD_API_KEY"])
    job = client.images.create(
        job_type="nano_banana_2",
        params={"prompt": "a serene mountain lake at dawn", "resolution": "2k"},
    )
    finished = client.wait_for_job(job.id)
    print(finished.result_url)

All request/response model classes live in ``higgsfield.models``; the generated
low-level client (the ``client.raw`` escape hatch) is ``higgsfield._client_gen``.
"""

from . import models  # the public model surface (re-exported from _client_gen)
from ._client import DEFAULT_BASE_URL, Higgsfield, is_terminal_status
from ._exceptions import HiggsfieldError
from ._transport import RequestOptions
from ._version import __version__
from .resources.media import MediaImport, MediaInput, MediaUploadSlot
from .types import FileTypes, MediaInputParam, MediaKind

__all__ = [
    "Higgsfield",
    "HiggsfieldError",
    "RequestOptions",
    "MediaInputParam",
    "MediaKind",
    "FileTypes",
    "MediaInput",
    "MediaImport",
    "MediaUploadSlot",
    "DEFAULT_BASE_URL",
    "is_terminal_status",
    "models",
    "__version__",
]
