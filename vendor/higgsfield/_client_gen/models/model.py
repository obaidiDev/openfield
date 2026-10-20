from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_label import ModelLabel, check_model_label
from ..models.model_type import ModelType, check_model_type

if TYPE_CHECKING:
    from ..models.cross_field_rule import CrossFieldRule
    from ..models.model_json_schema import ModelJsonSchema


T = TypeVar("T", bound="Model")


@_attrs_define
class Model:
    """A generation model available behind the generation endpoints. Grounded in ModelMetadata
    (src/handlers/claude_code/executor.py).

        Attributes:
            job_type (str): The model identifier, sent as the job_type discriminant in the generation request body (e.g.
                POST /v2/generations/images with job_type in the body).
            display_name (str): Human-readable model name.
            type_ (ModelType): Media kind this model produces.
            label (ModelLabel): Catalog category of this job_type — model (a single generation model), chain (a multi-step
                studio/pipeline), or app (a packaged application feature).
            provider (str): Organization or lab that produces this model (e.g. Google, Bytedance, Higgsfield). Empty string
                when unspecified.
            tags (list[str]): Free-form capability/use-case tags for discovery and recommendation.
            description (str): One-line human-facing summary of what the model is good for.
            json_schema (ModelJsonSchema): JSON Schema (draft) describing the model's accepted generation parameters,
                derived from the model's pydantic Params class.
            rules (list['CrossFieldRule']): Cross-field constraints (CEL) the params must satisfy beyond what json_schema
                expresses. Empty when the model has no cross-field rules. Enforced server-side.
    """

    job_type: str
    display_name: str
    type_: ModelType
    label: ModelLabel
    provider: str
    tags: list[str]
    description: str
    json_schema: "ModelJsonSchema"
    rules: list["CrossFieldRule"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_type = self.job_type

        display_name = self.display_name

        type_: str = self.type_

        label: str = self.label

        provider = self.provider

        tags = self.tags

        description = self.description

        json_schema = self.json_schema.to_dict()

        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_type": job_type,
                "display_name": display_name,
                "type": type_,
                "label": label,
                "provider": provider,
                "tags": tags,
                "description": description,
                "json_schema": json_schema,
                "rules": rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cross_field_rule import CrossFieldRule
        from ..models.model_json_schema import ModelJsonSchema

        d = dict(src_dict)
        job_type = d.pop("job_type")

        display_name = d.pop("display_name")

        type_ = check_model_type(d.pop("type"))

        label = check_model_label(d.pop("label"))

        provider = d.pop("provider")

        tags = cast(list[str], d.pop("tags"))

        description = d.pop("description")

        json_schema = ModelJsonSchema.from_dict(d.pop("json_schema"))

        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = CrossFieldRule.from_dict(rules_item_data)

            rules.append(rules_item)

        model = cls(
            job_type=job_type,
            display_name=display_name,
            type_=type_,
            label=label,
            provider=provider,
            tags=tags,
            description=description,
            json_schema=json_schema,
            rules=rules,
        )

        model.additional_properties = d
        return model

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
