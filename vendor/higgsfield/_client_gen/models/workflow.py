from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Workflow")


@_attrs_define
class Workflow:
    """A workflow product surface. Use product_key with listWorkflowPresets and createWorkflowGeneration.

    Attributes:
        product_key (str): CMS product surface key for workflow presets. Known values include the examples below, but
            the value is open-ended because CMS can add new workflow surfaces.
        name (str): Display name for the workflow surface.
        description (str): Short workflow description.
    """

    product_key: str
    name: str
    description: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_key = self.product_key

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_key": product_key,
                "name": name,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_key = d.pop("product_key")

        name = d.pop("name")

        description = d.pop("description")

        workflow = cls(
            product_key=product_key,
            name=name,
            description=description,
        )

        workflow.additional_properties = d
        return workflow

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
