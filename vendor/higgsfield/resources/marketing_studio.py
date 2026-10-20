"""Marketing Studio: avatars, products, setup items, ad references, brand kits."""

from __future__ import annotations

from typing import Any, List, Optional, Union

from .._client_gen.models.marketing_ad_reference import MarketingAdReference
from .._client_gen.models.marketing_ad_reference_list import MarketingAdReferenceList
from .._client_gen.models.marketing_avatar import MarketingAvatar
from .._client_gen.models.marketing_avatar_list import MarketingAvatarList
from .._client_gen.models.marketing_brand_kit import MarketingBrandKit
from .._client_gen.models.marketing_brand_kit_list import MarketingBrandKitList
from .._client_gen.models.marketing_image_style_list import MarketingImageStyleList
from .._client_gen.models.marketing_product import MarketingProduct
from .._client_gen.models.marketing_product_list import MarketingProductList
from .._client_gen.models.marketing_setup_item_list import MarketingSetupItemList
from .._client_gen.models.marketing_ad_reference_create_request import (
    MarketingAdReferenceCreateRequest,
)
from .._client_gen.models.marketing_ad_reference_update_request import (
    MarketingAdReferenceUpdateRequest,
)
from .._client_gen.models.marketing_avatar_batch_create_request import (
    MarketingAvatarBatchCreateRequest,
)
from .._client_gen.models.marketing_brand_kit_create_request import (
    MarketingBrandKitCreateRequest,
)
from .._client_gen.models.marketing_brand_kit_data import MarketingBrandKitData
from .._client_gen.models.marketing_product_create_request import MarketingProductCreateRequest
from .._client_gen.models.marketing_product_update_request import MarketingProductUpdateRequest
from .._transport import RequestOptions, Unpack, body_dict, query
from ._base import Resource


class MarketingStudioResource(Resource):
    # --- Avatars ----------------------------------------------------------

    def list_avatars(
        self,
        *,
        size: Optional[int] = None,
        cursor: Optional[float] = None,
        search: Optional[str] = None,
        **options: Unpack[RequestOptions],
    ) -> MarketingAvatarList:
        """List custom avatars plus curated avatar presets for the active workspace."""
        data = self._get_json(
            "/developer/v1alpha/marketing-studio/avatars",
            params=query(size=size, cursor=cursor, search=search),
            **options,
        )
        return MarketingAvatarList.from_dict(data)

    def create_avatars(
        self,
        body: Union[MarketingAvatarBatchCreateRequest, dict[str, Any]],
        **options: Unpack[RequestOptions],
    ) -> List[MarketingAvatar]:
        """Create up to four custom avatars in one call, each from an uploaded media asset."""
        data = self._post_json(
            "/developer/v1alpha/marketing-studio/avatars", json=body_dict(body), **options
        )
        return [MarketingAvatar.from_dict(item) for item in data]

    # --- Products ---------------------------------------------------------

    def list_products(
        self,
        *,
        size: Optional[int] = None,
        cursor: Optional[float] = None,
        **options: Unpack[RequestOptions],
    ) -> MarketingProductList:
        """List the caller's Marketing Studio products with offset pagination."""
        data = self._get_json(
            "/developer/v1alpha/marketing-studio/products",
            params=query(size=size, cursor=cursor),
            **options,
        )
        return MarketingProductList.from_dict(data)

    def create_product(
        self,
        body: Union[MarketingProductCreateRequest, dict[str, Any]],
        **options: Unpack[RequestOptions],
    ) -> MarketingProduct:
        """Create a product manually from one or more uploaded media assets."""
        data = self._post_json(
            "/developer/v1alpha/marketing-studio/products", json=body_dict(body), **options
        )
        return MarketingProduct.from_dict(data)

    def get_product(self, product_id: str, **options: Unpack[RequestOptions]) -> MarketingProduct:
        """Fetch a single product by its id."""
        data = self._get_json(
            f"/developer/v1alpha/marketing-studio/products/{product_id}", **options
        )
        return MarketingProduct.from_dict(data)

    def update_product(
        self,
        product_id: str,
        body: Union[MarketingProductUpdateRequest, dict[str, Any]],
        **options: Unpack[RequestOptions],
    ) -> MarketingProduct:
        """Partially update a product by id. Only fields valid for its ``type`` are applied."""
        data = self._patch_json(
            f"/developer/v1alpha/marketing-studio/products/{product_id}",
            json=body_dict(body),
            **options,
        )
        return MarketingProduct.from_dict(data)

    def delete_product(self, product_id: str, **options: Unpack[RequestOptions]) -> None:
        """Delete a product by id."""
        self._delete(f"/developer/v1alpha/marketing-studio/products/{product_id}", **options)

    # --- Setup: hooks & settings ------------------------------------------

    def _list_setup_items(
        self,
        type: str,
        size: Optional[int],
        cursor: Optional[float],
        search: Optional[str],
        **options: Unpack[RequestOptions],
    ) -> MarketingSetupItemList:
        data = self._get_json(
            "/developer/v1alpha/marketing-studio/hooks",
            params=query(type=type, size=size, cursor=cursor, search=search),
            **options,
        )
        return MarketingSetupItemList.from_dict(data)

    def list_hooks(
        self,
        *,
        size: Optional[int] = None,
        cursor: Optional[float] = None,
        search: Optional[str] = None,
        **options: Unpack[RequestOptions],
    ) -> MarketingSetupItemList:
        """List hook setup items — custom hooks plus curated hook presets."""
        return self._list_setup_items("hook", size, cursor, search, **options)

    def list_settings(
        self,
        *,
        size: Optional[int] = None,
        cursor: Optional[float] = None,
        search: Optional[str] = None,
        **options: Unpack[RequestOptions],
    ) -> MarketingSetupItemList:
        """List setting setup items — custom settings plus curated setting presets."""
        return self._list_setup_items("setting", size, cursor, search, **options)

    # --- Image styles -----------------------------------------------------

    def list_image_styles(self, **options: Unpack[RequestOptions]) -> MarketingImageStyleList:
        """List the curated Marketing Studio image-style catalog (full list, not paginated)."""
        data = self._get_json("/developer/v1alpha/marketing-studio/image-styles", **options)
        return MarketingImageStyleList.from_dict(data)

    # --- Ad references (CRUD) ---------------------------------------------

    def list_ad_references(
        self,
        *,
        size: Optional[int] = None,
        cursor: Optional[str] = None,
        **options: Unpack[RequestOptions],
    ) -> MarketingAdReferenceList:
        """List the caller's ad references, newest first, with cursor pagination."""
        data = self._get_json(
            "/developer/v1alpha/marketing-studio/ad-references",
            params=query(size=size, cursor=cursor),
            **options,
        )
        return MarketingAdReferenceList.from_dict(data)

    def create_ad_reference(
        self,
        body: Union[MarketingAdReferenceCreateRequest, dict[str, Any]],
        **options: Unpack[RequestOptions],
    ) -> MarketingAdReference:
        """Create an ad reference by cloning a source video into a reusable ad scenario."""
        data = self._post_json(
            "/developer/v1alpha/marketing-studio/ad-references", json=body_dict(body), **options
        )
        return MarketingAdReference.from_dict(data)

    def get_ad_reference(
        self, ad_reference_id: str, **options: Unpack[RequestOptions]
    ) -> MarketingAdReference:
        """Fetch a single ad reference by id, including its full concept arrays."""
        data = self._get_json(
            f"/developer/v1alpha/marketing-studio/ad-references/{ad_reference_id}", **options
        )
        return MarketingAdReference.from_dict(data)

    def update_ad_reference(
        self,
        ad_reference_id: str,
        body: Union[MarketingAdReferenceUpdateRequest, dict[str, Any]],
        **options: Unpack[RequestOptions],
    ) -> MarketingAdReference:
        """Partially update the editable concept of an ad reference by id."""
        data = self._patch_json(
            f"/developer/v1alpha/marketing-studio/ad-references/{ad_reference_id}",
            json=body_dict(body),
            **options,
        )
        return MarketingAdReference.from_dict(data)

    def delete_ad_reference(self, ad_reference_id: str, **options: Unpack[RequestOptions]) -> None:
        """Delete an ad reference by id."""
        self._delete(
            f"/developer/v1alpha/marketing-studio/ad-references/{ad_reference_id}", **options
        )

    # --- Brand kits (CRUD) ------------------------------------------------

    def list_brand_kits(
        self,
        *,
        size: Optional[int] = None,
        cursor: Optional[str] = None,
        **options: Unpack[RequestOptions],
    ) -> MarketingBrandKitList:
        """List the caller's brand kits, newest first, with cursor pagination."""
        data = self._get_json(
            "/developer/v1alpha/marketing-studio/brand-kits",
            params=query(size=size, cursor=cursor),
            **options,
        )
        return MarketingBrandKitList.from_dict(data)

    def create_brand_kit(
        self,
        body: Union[MarketingBrandKitCreateRequest, dict[str, Any]],
        **options: Unpack[RequestOptions],
    ) -> MarketingBrandKit:
        """Create a brand kit.

        ``source="url"`` scrapes a brand's website and extracts a kit (processes
        asynchronously); ``source="manual"`` builds it from the supplied ``data`` payload.
        """
        data = self._post_json(
            "/developer/v1alpha/marketing-studio/brand-kits", json=body_dict(body), **options
        )
        return MarketingBrandKit.from_dict(data)

    def get_brand_kit(
        self, brand_kit_id: str, **options: Unpack[RequestOptions]
    ) -> MarketingBrandKit:
        """Fetch a single brand kit by id, including its extracted brand data and progress."""
        data = self._get_json(
            f"/developer/v1alpha/marketing-studio/brand-kits/{brand_kit_id}", **options
        )
        return MarketingBrandKit.from_dict(data)

    def update_brand_kit(
        self,
        brand_kit_id: str,
        body: Union[MarketingBrandKitData, dict[str, Any]],
        **options: Unpack[RequestOptions],
    ) -> MarketingBrandKit:
        """Partially update a brand kit's brand-identity data.

        Only the fields supplied override the stored data; omitted fields are preserved.
        """
        data = self._patch_json(
            f"/developer/v1alpha/marketing-studio/brand-kits/{brand_kit_id}",
            json=body_dict(body),
            **options,
        )
        return MarketingBrandKit.from_dict(data)

    def delete_brand_kit(self, brand_kit_id: str, **options: Unpack[RequestOptions]) -> None:
        """Delete a brand kit by id."""
        self._delete(f"/developer/v1alpha/marketing-studio/brand-kits/{brand_kit_id}", **options)
