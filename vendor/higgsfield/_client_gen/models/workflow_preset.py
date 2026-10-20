from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_preset_preview_media_type import (
    WorkflowPresetPreviewMediaType,
    check_workflow_preset_preview_media_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_preset_input import WorkflowPresetInput


T = TypeVar("T", bound="WorkflowPreset")


@_attrs_define
class WorkflowPreset:
    """A CMS job-set-chain preset that can be used as params.preset_id when creating a workflow generation for its
    product_key.

        Attributes:
            id (UUID): Preset identifier passed as params.preset_id.
            product_key (str): CMS product surface key for workflow presets. Known values include the examples below, but
                the value is open-ended because CMS can add new workflow surfaces.
            name (str): Preset display name.
            description (str): Preset description from CMS.
            url (str): Primary preview media URL for this preset.
            thumbnail_url (str): Thumbnail or poster URL for this preset.
            inputs (list['WorkflowPresetInput']): Public media params this preset accepts for workflow generation.
            category (Union[None, Unset, str]): Preset category within its product surface.
            preview_media_type (Union[None, Unset, WorkflowPresetPreviewMediaType]): Preview media kind.
            width (Union[None, Unset, int]): Preview width in pixels, when known.
            height (Union[None, Unset, int]): Preview height in pixels, when known.
    """

    id: UUID
    product_key: str
    name: str
    description: str
    url: str
    thumbnail_url: str
    inputs: list["WorkflowPresetInput"]
    category: Union[None, Unset, str] = UNSET
    preview_media_type: Union[None, Unset, WorkflowPresetPreviewMediaType] = UNSET
    width: Union[None, Unset, int] = UNSET
    height: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        product_key = self.product_key

        name = self.name

        description = self.description

        url = self.url

        thumbnail_url = self.thumbnail_url

        inputs = []
        for inputs_item_data in self.inputs:
            inputs_item = inputs_item_data.to_dict()
            inputs.append(inputs_item)

        category: Union[None, Unset, str]
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        preview_media_type: Union[None, Unset, str]
        if isinstance(self.preview_media_type, Unset):
            preview_media_type = UNSET
        elif isinstance(self.preview_media_type, str):
            preview_media_type = self.preview_media_type
        else:
            preview_media_type = self.preview_media_type

        width: Union[None, Unset, int]
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        height: Union[None, Unset, int]
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "product_key": product_key,
                "name": name,
                "description": description,
                "url": url,
                "thumbnail_url": thumbnail_url,
                "inputs": inputs,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if preview_media_type is not UNSET:
            field_dict["preview_media_type"] = preview_media_type
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_preset_input import WorkflowPresetInput

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        product_key = d.pop("product_key")

        name = d.pop("name")

        description = d.pop("description")

        url = d.pop("url")

        thumbnail_url = d.pop("thumbnail_url")

        inputs = []
        _inputs = d.pop("inputs")
        for inputs_item_data in _inputs:
            inputs_item = WorkflowPresetInput.from_dict(inputs_item_data)

            inputs.append(inputs_item)

        def _parse_category(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_preview_media_type(
            data: object,
        ) -> Union[None, Unset, WorkflowPresetPreviewMediaType]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                preview_media_type_type_0 = check_workflow_preset_preview_media_type(data)

                return preview_media_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, WorkflowPresetPreviewMediaType], data)

        preview_media_type = _parse_preview_media_type(d.pop("preview_media_type", UNSET))

        def _parse_width(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        width = _parse_width(d.pop("width", UNSET))

        def _parse_height(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        height = _parse_height(d.pop("height", UNSET))

        workflow_preset = cls(
            id=id,
            product_key=product_key,
            name=name,
            description=description,
            url=url,
            thumbnail_url=thumbnail_url,
            inputs=inputs,
            category=category,
            preview_media_type=preview_media_type,
            width=width,
            height=height,
        )

        workflow_preset.additional_properties = d
        return workflow_preset

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
