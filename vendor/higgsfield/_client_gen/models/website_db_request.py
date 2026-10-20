from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.website_db_request_operation import (
    WebsiteDbRequestOperation,
    check_website_db_request_operation,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebsiteDbRequest")


@_attrs_define
class WebsiteDbRequest:
    """A read-only operation against the website's D1 database.

    Attributes:
        operation (WebsiteDbRequestOperation): What to read: list tables, a table's schema, a page of rows, or a single
            read-only query.
        table (Union[None, Unset, str]): Table name. Required for 'schema' and 'rows'.
        filters (Union[None, Unset, list[str]]): Row filters for 'rows', each 'col:op[:value]' (eq ne gt gte lt lte like
            is_null).
        order_by (Union[None, Unset, str]): Column to sort by ('rows').
        order_dir (Union[None, Unset, str]): Sort direction for 'rows': 'asc' or 'desc'.
        limit (Union[None, Unset, int]): Max rows to return ('rows'). Default 50.
        offset (Union[None, Unset, int]): Row offset for paging ('rows').
        sql (Union[None, Unset, str]): A single read-only SELECT/WITH statement ('query').
        max_rows (Union[None, Unset, int]): Max rows for a 'query'.
    """

    operation: WebsiteDbRequestOperation
    table: Union[None, Unset, str] = UNSET
    filters: Union[None, Unset, list[str]] = UNSET
    order_by: Union[None, Unset, str] = UNSET
    order_dir: Union[None, Unset, str] = UNSET
    limit: Union[None, Unset, int] = UNSET
    offset: Union[None, Unset, int] = UNSET
    sql: Union[None, Unset, str] = UNSET
    max_rows: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation: str = self.operation

        table: Union[None, Unset, str]
        if isinstance(self.table, Unset):
            table = UNSET
        else:
            table = self.table

        filters: Union[None, Unset, list[str]]
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, list):
            filters = self.filters

        else:
            filters = self.filters

        order_by: Union[None, Unset, str]
        if isinstance(self.order_by, Unset):
            order_by = UNSET
        else:
            order_by = self.order_by

        order_dir: Union[None, Unset, str]
        if isinstance(self.order_dir, Unset):
            order_dir = UNSET
        else:
            order_dir = self.order_dir

        limit: Union[None, Unset, int]
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        offset: Union[None, Unset, int]
        if isinstance(self.offset, Unset):
            offset = UNSET
        else:
            offset = self.offset

        sql: Union[None, Unset, str]
        if isinstance(self.sql, Unset):
            sql = UNSET
        else:
            sql = self.sql

        max_rows: Union[None, Unset, int]
        if isinstance(self.max_rows, Unset):
            max_rows = UNSET
        else:
            max_rows = self.max_rows

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation": operation,
            }
        )
        if table is not UNSET:
            field_dict["table"] = table
        if filters is not UNSET:
            field_dict["filters"] = filters
        if order_by is not UNSET:
            field_dict["order_by"] = order_by
        if order_dir is not UNSET:
            field_dict["order_dir"] = order_dir
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if sql is not UNSET:
            field_dict["sql"] = sql
        if max_rows is not UNSET:
            field_dict["max_rows"] = max_rows

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation = check_website_db_request_operation(d.pop("operation"))

        def _parse_table(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        table = _parse_table(d.pop("table", UNSET))

        def _parse_filters(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filters_type_0 = cast(list[str], data)

                return filters_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_order_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        order_by = _parse_order_by(d.pop("order_by", UNSET))

        def _parse_order_dir(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        order_dir = _parse_order_dir(d.pop("order_dir", UNSET))

        def _parse_limit(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        limit = _parse_limit(d.pop("limit", UNSET))

        def _parse_offset(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        offset = _parse_offset(d.pop("offset", UNSET))

        def _parse_sql(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sql = _parse_sql(d.pop("sql", UNSET))

        def _parse_max_rows(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_rows = _parse_max_rows(d.pop("max_rows", UNSET))

        website_db_request = cls(
            operation=operation,
            table=table,
            filters=filters,
            order_by=order_by,
            order_dir=order_dir,
            limit=limit,
            offset=offset,
            sql=sql,
            max_rows=max_rows,
        )

        website_db_request.additional_properties = d
        return website_db_request

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
