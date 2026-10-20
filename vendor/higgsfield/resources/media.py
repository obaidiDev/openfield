"""Media: upload bytes, import by URL, and list assets.

Generation params reference assets by a media input (``{"id", "type":
"media_input"}``). Every media object the facade returns carries an
:meth:`~_AsInput.as_input` method that builds that typed reference, so you never
hand-roll the dict::

    media = client.media.import_({"url": url, "type": "auto"})
    client.videos.create(job_type="veo3", params={"start_image": media.as_input()})
"""

from __future__ import annotations

import mimetypes
import os
from contextlib import contextmanager
from pathlib import Path
from typing import IO, Any, Iterator, NamedTuple, Optional, Union

from .._client_gen.models.import_media_request import ImportMediaRequest
from .._client_gen.models.media_confirmation import MediaConfirmation
from .._client_gen.models.media_import import MediaImport as _MediaImport
from .._client_gen.models.media_input import MediaInput as _MediaInput
from .._client_gen.models.media_list_response import MediaListResponse
from .._client_gen.models.media_upload_slot import MediaUploadSlot as _MediaUploadSlot
from .._exceptions import HiggsfieldError
from .._transport import RequestOptions, Unpack, body_dict, query
from ..types import FileTypes, MediaInputParam, MediaKind
from ._base import Resource


_CHUNK = 1024 * 1024  # 1 MiB — stream large files instead of buffering them.


def _iter_file(fp: IO[bytes], size: int) -> Iterator[bytes]:
    """Yield ``size`` bytes from ``fp`` in fixed chunks (low, constant memory)."""
    remaining = size
    while remaining > 0:
        chunk = fp.read(min(_CHUNK, remaining))
        if not chunk:
            break
        remaining -= len(chunk)
        yield chunk


class _Upload(NamedTuple):
    # Raw bytes (buffered; httpx derives the length) or a chunked byte iterator,
    # in which case `length` is its known size, sent as Content-Length (a
    # presigned S3 PUT requires it and rejects chunked encoding).
    body: Union[bytes, Iterator[bytes]]
    length: Optional[int]
    extension: Optional[str]


@contextmanager
def _open_upload(file: FileTypes, extension: Optional[str]) -> Iterator[_Upload]:
    """Resolve a ``FileTypes`` input to a streamable :class:`_Upload`, closing any
    file this opens on exit. A path or seekable file is streamed in chunks; raw
    bytes and non-seekable streams are buffered. When ``extension`` isn't given
    it's inferred from the filename/path suffix, else the media type.
    """
    filename: Optional[str] = None
    media_type: Optional[str] = None
    content: Any = file
    if isinstance(file, tuple):
        filename, content = file[0], file[1]
        media_type = file[2] if len(file) > 2 else None

    body: Union[bytes, Iterator[bytes]]
    length: Optional[int] = None
    opened: Optional[IO[bytes]] = None
    if isinstance(content, (bytes, bytearray)):
        body = content if isinstance(content, bytes) else bytes(content)
    elif isinstance(content, (str, os.PathLike)):
        path = Path(os.fspath(content))
        length = path.stat().st_size
        opened = path.open("rb")
        body = _iter_file(opened, length)
        filename = filename or path.name
    elif hasattr(content, "read"):  # a binary file-like object
        name = getattr(content, "name", None)
        filename = filename or (name if isinstance(name, str) else None)
        if callable(getattr(content, "seekable", None)) and content.seekable():
            start = content.tell()
            length = content.seek(0, os.SEEK_END) - start
            content.seek(start)
            body = _iter_file(content, length)  # caller owns the handle — don't close
        else:
            body = content.read()  # unknown size — must buffer for Content-Length
    else:
        raise TypeError(f"unsupported upload content: {type(content).__name__}")

    if extension is None:
        if filename and Path(filename).suffix:
            extension = Path(filename).suffix.lstrip(".")
        elif media_type:
            guessed = mimetypes.guess_extension(media_type)
            extension = guessed.lstrip(".") if guessed else None

    try:
        yield _Upload(body, length, extension)
    finally:
        if opened is not None:
            opened.close()


class _AsInput:
    """Mixin: turn a media object into a typed generation-param reference."""

    __slots__ = ()
    id: Any

    def as_input(self) -> MediaInputParam:
        """Return a ``media_input`` reference for generation params."""
        return {"id": str(self.id), "type": "media_input"}


class MediaInput(_AsInput, _MediaInput):
    """An uploaded/imported asset reference (the value :meth:`MediaResource.upload` returns)."""

    __slots__ = ()


class MediaImport(_AsInput, _MediaImport):
    """The result of importing a remote asset by URL (see :meth:`MediaResource.import_`)."""

    __slots__ = ()


class MediaUploadSlot(_AsInput, _MediaUploadSlot):
    """A presigned upload slot (see :meth:`MediaResource.create_upload`)."""

    __slots__ = ()


class MediaResource(Resource):
    def create_upload(
        self,
        *,
        type: MediaKind,
        extension: Optional[str] = None,
        chat_id: Optional[str] = None,
        filename: Optional[str] = None,
        **options: Unpack[RequestOptions],
    ) -> MediaUploadSlot:
        """Create an upload slot with a presigned S3 ``upload_url`` — PUT your
        bytes there, then call :meth:`confirm`. ``filename`` is opt-in display
        metadata; existing callers omit it and keep the legacy query unchanged."""
        data = self._post_json(
            "/developer/v2alpha/media",
            params=query(type=type, extension=extension, chat_id=chat_id, filename=filename),
            **options,
        )
        return MediaUploadSlot.from_dict(data)

    def confirm(
        self, media_id: str, *, type: MediaKind, **options: Unpack[RequestOptions]
    ) -> MediaConfirmation:
        """Confirm an uploaded slot after the bytes have been PUT to its ``upload_url``."""
        data = self._post_json(
            f"/developer/v2alpha/media/{media_id}/confirm", params=query(type=type), **options
        )
        return MediaConfirmation.from_dict(data)

    def import_(
        self, body: Union[ImportMediaRequest, dict[str, Any]], **options: Unpack[RequestOptions]
    ) -> MediaImport:
        """Import a remote asset by URL; the server fetches and confirms it for you."""
        data = self._post_json("/developer/v2alpha/media/import", json=body_dict(body), **options)
        return MediaImport.from_dict(data)

    def list(
        self,
        *,
        type: MediaKind,
        size: Optional[int] = None,
        cursor: Optional[str] = None,
        order: Optional[str] = None,
        **options: Unpack[RequestOptions],
    ) -> MediaListResponse:
        """List your media of a given kind with cursor pagination."""
        data = self._get_json(
            "/developer/v2alpha/media",
            params=query(type=type, size=size, cursor=cursor, order=order),
            **options,
        )
        return MediaListResponse.from_dict(data)

    def upload(
        self,
        file: FileTypes,
        *,
        type: MediaKind,
        extension: Optional[str] = None,
        chat_id: Optional[str] = None,
        **options: Unpack[RequestOptions],
    ) -> MediaInput:
        """One-shot upload: create a slot, PUT the content to S3, and confirm.

        ``file`` may be raw ``bytes``, a binary file object, a path
        (``str``/``PathLike``), or a ``(filename, content[, media_type])`` tuple;
        the ``extension`` is inferred from it when not given. A path or seekable
        file is streamed in chunks (not read fully into memory). Returns a
        :class:`MediaInput` ready to drop into generation params via ``.as_input()``."""
        with _open_upload(file, extension) as up:
            slot = self.create_upload(
                type=type,
                extension=up.extension,
                chat_id=chat_id,
                **options,
            )

            # PUT to the presigned S3 URL through the configured (unauthenticated)
            # transport. A known length is sent as Content-Length so the streamed
            # body isn't chunk-encoded (which presigned S3 PUT rejects).
            headers = {"Content-Type": slot.content_type}
            if up.length is not None:
                headers["Content-Length"] = str(up.length)
            put = self._client._request_unauthed(
                "PUT", slot.upload_url, content=up.body, headers=headers
            )
        if not put.is_success:
            raise HiggsfieldError(
                f"Failed to PUT media bytes to upload_url: {put.status_code}",
                status=put.status_code,
            )

        confirmation = self.confirm(str(slot.id), type=type, **options)
        if str(confirmation.status) != "uploaded":
            raise HiggsfieldError(
                f'Uploaded media {slot.id} is not usable (status "{confirmation.status}").',
                body=confirmation,
            )
        return MediaInput.from_dict({"id": str(slot.id), "type": "media_input"})
