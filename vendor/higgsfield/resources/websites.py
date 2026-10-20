"""Websites: build and ship full-stack websites (create, edit, deploy, db, secrets)."""

from __future__ import annotations

from typing import Any, List, Literal, Optional, Union

from .._client_gen.models.website_create_response import WebsiteCreateResponse
from .._client_gen.models.website_delete_response import WebsiteDeleteResponse
from .._client_gen.models.deploy_website_request import DeployWebsiteRequest
from .._client_gen.models.website_deploy_response import WebsiteDeployResponse
from .._client_gen.models.website_publish_response import WebsitePublishResponse
from .._client_gen.models.website_rename_response import WebsiteRenameResponse
from .._client_gen.models.website_contest_participate_response import (
    WebsiteContestParticipateResponse,
)
from .._client_gen.models.repo_access_response import RepoAccessResponse
from .._client_gen.models.website_categories_response import WebsiteCategoriesResponse
from .._client_gen.models.website_db_request import WebsiteDbRequest
from .._client_gen.models.website_db_result import WebsiteDbResult
from .._client_gen.models.website_list_response import WebsiteListResponse
from .._client_gen.models.website_secret_set_request import WebsiteSecretSetRequest
from .._client_gen.models.website_secrets_response import WebsiteSecretsResponse
from .._client_gen.models.website_status_response import WebsiteStatusResponse
from .._transport import RequestOptions, Unpack, body_dict
from ._base import Resource


class WebsitesResource(Resource):
    def create(
        self,
        *,
        type: str,
        created_from: str,
        category: str,
        subdomain: Optional[str] = None,
        template: Optional[Literal["app-detail", "preset", "studio", "custom"]] = None,
        **options: Unpack[RequestOptions],
    ) -> WebsiteCreateResponse:
        """Create a website + its git repo. Keep the ``website_id`` for every later call.

        ``created_from`` declares which client is creating the website (e.g. ``"mcp"``,
        ``"cli"``, ``"supercomputer"``; any short tag) — recorded for analytics.
        ``type`` picks the product kind: ``"website"`` (a standalone site with no
        higgsfield integration) or ``"app"`` (Sign in with Higgsfield + the fnf SDK
        for image/video generation).
        ``category`` files the website under a marketplace-taxonomy slug (fetch the
        options from ``GET /api/v1/apps/categories`` — e.g. ``"cinematic"``,
        ``"ads-marketing"``, ``"other"``); the server validates it (422 for an
        unknown slug). Pick the closest category, or ``"other"`` when nothing fits.
        ``subdomain`` optionally sets the website's slug (the chosen subdomain);
        the server validates + enforces uniqueness (422 for a reserved/malformed
        label, 409 when already taken). Omit it to get a random slug.
        ``template`` picks the scaffold for ``type="app"`` — required by convention
        there: choose the closest of ``"app-detail"`` / ``"preset"`` / ``"studio"``
        (``"custom"``, the bare legacy scaffold, only when the user explicitly asks).
        Omit it for ``type="website"``.
        """
        json: dict[str, Any] = {
            "type": type,
            "created_from": created_from,
            "category": category,
        }
        if subdomain is not None:
            json["subdomain"] = subdomain
        if template is not None:
            json["template"] = template
        data = self._post_json(
            "/developer/v1alpha/websites",
            json=json,
            **options,
        )
        return WebsiteCreateResponse.from_dict(data)

    def list(self, **options: Unpack[RequestOptions]) -> WebsiteListResponse:
        """List the websites you own (id, slug, name, live URL)."""
        return WebsiteListResponse.from_dict(
            self._get_json("/developer/v1alpha/websites", **options)
        )

    def list_categories(self, **options: Unpack[RequestOptions]) -> WebsiteCategoriesResponse:
        """List the content categories a website can be filed under (the
        marketplace taxonomy). Pass a returned ``slug`` as ``category`` to
        :meth:`create`."""
        return WebsiteCategoriesResponse.from_dict(
            self._get_json("/developer/v1alpha/website-categories", **options)
        )

    def status(self, website_id: str, **options: Unpack[RequestOptions]) -> WebsiteStatusResponse:
        """Get a website's deploy status — the live URL and last deploy state."""
        data = self._get_json(f"/developer/v1alpha/websites/{website_id}", **options)
        return WebsiteStatusResponse.from_dict(data)

    def delete(self, website_id: str, **options: Unpack[RequestOptions]) -> WebsiteDeleteResponse:
        """Permanently delete a website and everything it owns (site, db, storage, repo)."""
        data = self._delete_json(f"/developer/v1alpha/websites/{website_id}", **options)
        return WebsiteDeleteResponse.from_dict(data)

    def deploy(
        self,
        website_id: str,
        body: Union[DeployWebsiteRequest, dict[str, Any], None] = None,
        **options: Unpack[RequestOptions],
    ) -> WebsiteDeployResponse:
        """Build and deploy a website — ships the live site; returns its URL.

        ``body.env`` is deprecated and ignored (the preview stage was removed).
        """
        data = self._post_json(
            f"/developer/v1alpha/websites/{website_id}/deploy",
            json=body_dict(body) if body is not None else {},
            **options,
        )
        return WebsiteDeployResponse.from_dict(data)

    def rename(
        self,
        website_id: str,
        *,
        new_slug: str,
        **options: Unpack[RequestOptions],
    ) -> WebsiteRenameResponse:
        """Rename a website's subdomain (the slug in its public URL).

        The site is re-deployed under the new subdomain and the OLD subdomain
        stops working; storage and the source repo are kept. Blocking like
        ``deploy`` — returns once the site is live at the new URL (can take a
        couple of minutes). 409 when the subdomain is taken or a deploy is in
        flight; 422 when it is malformed or reserved.
        """
        data = self._post_json(
            f"/developer/v1alpha/websites/{website_id}/rename",
            json={"new_slug": new_slug},
            **options,
        )
        return WebsiteRenameResponse.from_dict(data)

    def publish(
        self,
        website_id: str,
        *,
        category_id: Optional[str] = None,
        **options: Unpack[RequestOptions],
    ) -> WebsitePublishResponse:
        """Publish a website: deploy the current main to production and list it on
        the community feed ("show in feed").

        Synchronous like ``deploy`` — a ``pending`` status means CI is still running
        (poll ``status``); a ``pending`` publish still lists the website automatically
        once the deploy succeeds.
        """
        data = self._post_json(
            f"/developer/v1alpha/websites/{website_id}/publish",
            json={"category_id": category_id},
            **options,
        )
        return WebsitePublishResponse.from_dict(data)

    def participate_in_contest(
        self,
        website_id: str,
        *,
        urls: List[str],
        **options: Unpack[RequestOptions],
    ) -> WebsiteContestParticipateResponse:
        """Enter the website in the current app contest with its social-media promo links.

        ``urls`` are the social-media links promoting the website (YouTube /
        X-Twitter / Instagram / TikTok; 1–10). A website not yet on the community
        feed is published automatically by the entry (it needs a live production
        deploy; else 422: deploy first). One entry per website — re-submitting
        overwrites the urls. The contest is fixed on the backend.
        """
        data = self._post_json(
            f"/developer/v1alpha/websites/{website_id}/contest",
            json={"urls": urls},
            **options,
        )
        return WebsiteContestParticipateResponse.from_dict(data)

    def repo_access(self, website_id: str, **options: Unpack[RequestOptions]) -> RepoAccessResponse:
        """Get scoped git access (clone URL + branch + token) to edit a website's repo."""
        data = self._post_json(f"/developer/v1alpha/websites/{website_id}/repo-access", **options)
        return RepoAccessResponse.from_dict(data)

    def db(
        self,
        website_id: str,
        body: Union[WebsiteDbRequest, dict[str, Any]],
        **options: Unpack[RequestOptions],
    ) -> WebsiteDbResult:
        """Read a website's D1 database, read-only (tables / schema / rows / query)."""
        data = self._post_json(
            f"/developer/v1alpha/websites/{website_id}/db", json=body_dict(body), **options
        )
        return WebsiteDbResult.from_dict(data)

    def list_secrets(
        self, website_id: str, **options: Unpack[RequestOptions]
    ) -> WebsiteSecretsResponse:
        """List a website's secrets (environment variables) as a {name: value} map."""
        data = self._get_json(f"/developer/v1alpha/websites/{website_id}/secrets", **options)
        return WebsiteSecretsResponse.from_dict(data)

    def set_secret(
        self,
        website_id: str,
        body: Union[WebsiteSecretSetRequest, dict[str, Any]],
        **options: Unpack[RequestOptions],
    ) -> WebsiteSecretsResponse:
        """Create or replace a secret. Staged: live on the website's next deploy."""
        data = self._post_json(
            f"/developer/v1alpha/websites/{website_id}/secrets", json=body_dict(body), **options
        )
        return WebsiteSecretsResponse.from_dict(data)

    def delete_secret(
        self, website_id: str, name: str, **options: Unpack[RequestOptions]
    ) -> WebsiteSecretsResponse:
        """Delete a secret by name. Staged: applied on the website's next deploy."""
        data = self._delete_json(
            f"/developer/v1alpha/websites/{website_id}/secrets/{name}", **options
        )
        return WebsiteSecretsResponse.from_dict(data)
