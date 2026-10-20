"""Typed input shapes for the SDK.

Following the openai-python convention: request inputs are ``TypedDict``\\s (typed
dict literals with editor autocomplete), responses are model objects. Generation
``params`` are intentionally loose (``dict[str, Any]``) because job types are
dynamic, but the recurring media-reference value has a stable shape, typed here.
"""

from __future__ import annotations

import os
from typing import IO, Literal, Optional, Tuple, TypedDict, Union

#: The kind of a media asset, for upload/confirm/list.
MediaKind = Literal["image", "video", "audio", "file"]

# Distinct from the generated _client_gen.types FileTypes (which models httpx
# multipart `files=` tuples): this is a path-aware input for the presigned-S3
# upload — `str` here means a filesystem path, and PathLike is accepted.
#: File content for an upload: raw bytes, a binary file object, or a path.
FileContent = Union[bytes, IO[bytes], str, "os.PathLike[str]"]
#: An upload input — content alone, or a ``(filename, content[, media_type])``
#: tuple (openai-python convention). The filename/path/media-type is used to
#: infer the asset ``extension`` when you don't pass one.
FileTypes = Union[
    FileContent,
    Tuple[Optional[str], FileContent],
    Tuple[Optional[str], FileContent, Optional[str]],
]


class MediaInputParam(TypedDict):
    """A media-asset reference for generation params.

    Drop it into ``start_image``, ``end_image``, or a ``*_references`` array.
    Build one from a media response with ``media.as_input()`` rather than by hand.
    """

    id: str
    # "media_input" for an uploaded/imported asset, or a prior job type.
    type: str
