"""Workflows: multi-step generation chains.

The workflow product surface is selected by the ``product_key`` path parameter,
mirroring the generation API's ``job_type`` selector.
"""

from __future__ import annotations

from typing import Any, List, Optional, Union
from uuid import UUID

from .._client_gen.models.workflow_generation_request import WorkflowGenerationRequest
from .._client_gen.models.workflow_list_response import WorkflowListResponse
from .._client_gen.models.workflow_preset_cost_response import WorkflowPresetCostResponse
from .._client_gen.models.workflow_preset_list_response import WorkflowPresetListResponse
from .._exceptions import HiggsfieldError
from .._transport import RequestOptions, Unpack, body_dict
from ._base import Resource


class WorkflowsResource(Resource):
    def list(self, **options: Unpack[RequestOptions]) -> WorkflowListResponse:
        """List the workflow product surfaces available to developer clients. Each
        item has a ``product_key`` used to list presets and create generations."""
        return WorkflowListResponse.from_dict(
            self._get_json("/developer/v2alpha/workflows", **options)
        )

    def list_presets(
        self, product_key: str, **options: Unpack[RequestOptions]
    ) -> WorkflowPresetListResponse:
        """List the CMS job-set-chain presets for one workflow product surface. A
        preset's ``id`` is passed as ``params.preset_id`` to ``create_generation``."""
        data = self._get_json(f"/developer/v2alpha/workflows/{product_key}/presets", **options)
        return WorkflowPresetListResponse.from_dict(data)

    def get_preset_cost(
        self,
        product_key: str,
        preset_id: str,
        params: Optional[dict[str, Any]] = None,
        **options: Unpack[RequestOptions],
    ) -> WorkflowPresetCostResponse:
        """Fetch the credit cost for one workflow preset within a product surface.

        Dynamic-price presets calculate the final cost from runtime selections
        (e.g. ``duration``, ``resolution``) passed via ``params``."""
        data = self._post_json(
            f"/developer/v2alpha/workflows/{product_key}/presets/{preset_id}/cost",
            json={"params": params} if params is not None else None,
            **options,
        )
        return WorkflowPresetCostResponse.from_dict(data)

    def create_generation(
        self,
        product_key: str,
        body: Union[WorkflowGenerationRequest, dict[str, Any]],
        **options: Unpack[RequestOptions],
    ) -> List[UUID]:
        """Run a workflow chain for the given product surface. From a preset and
        source media it orchestrates the multi-step generation and returns the ids
        of the jobs it created, in creation order; poll each with ``jobs.get``."""
        resp = self._request(
            "post",
            f"/developer/v2alpha/workflows/{product_key}/generations",
            json=body_dict(body),
            **options,
        )
        try:
            return [UUID(job_id) for job_id in resp.json()]
        except (ValueError, TypeError) as exc:
            raise HiggsfieldError(f"unexpected workflow response: {exc}", response=resp) from exc
