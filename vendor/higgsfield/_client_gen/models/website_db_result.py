from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.website_db_result_rows_type_0_item import WebsiteDbResultRowsType0Item


T = TypeVar("T", bound="WebsiteDbResult")


@_attrs_define
class WebsiteDbResult:
    """Result of a website_db operation. Shape depends on operation: tables -> {tables}; schema -> {table, columns}; rows
    -> {table, columns, rows, total, limit, offset}; query -> {columns, rows, row_count, truncated}.

        Attributes:
            operation (str): The operation this result is for.
            tables (Union[None, Unset, list[str]]): Table names (operation 'tables').
            table (Union[None, Unset, str]): Table name (operation 'schema' / 'rows').
            columns (Union[None, Unset, list[Any]]): Column descriptors (objects for 'schema') or column names (strings for
                'rows'/'query').
            rows (Union[None, Unset, list['WebsiteDbResultRowsType0Item']]): Row objects (operation 'rows' / 'query').
            total (Union[None, Unset, int]): Total matching rows (operation 'rows').
            limit (Union[None, Unset, int]): Applied page size (operation 'rows').
            offset (Union[None, Unset, int]): Applied row offset (operation 'rows').
            row_count (Union[None, Unset, int]): Number of rows returned (operation 'query').
            truncated (Union[None, Unset, bool]): Whether the query result was truncated (operation 'query').
    """

    operation: str
    tables: Union[None, Unset, list[str]] = UNSET
    table: Union[None, Unset, str] = UNSET
    columns: Union[None, Unset, list[Any]] = UNSET
    rows: Union[None, Unset, list["WebsiteDbResultRowsType0Item"]] = UNSET
    total: Union[None, Unset, int] = UNSET
    limit: Union[None, Unset, int] = UNSET
    offset: Union[None, Unset, int] = UNSET
    row_count: Union[None, Unset, int] = UNSET
    truncated: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation = self.operation

        tables: Union[None, Unset, list[str]]
        if isinstance(self.tables, Unset):
            tables = UNSET
        elif isinstance(self.tables, list):
            tables = self.tables

        else:
            tables = self.tables

        table: Union[None, Unset, str]
        if isinstance(self.table, Unset):
            table = UNSET
        else:
            table = self.table

        columns: Union[None, Unset, list[Any]]
        if isinstance(self.columns, Unset):
            columns = UNSET
        elif isinstance(self.columns, list):
            columns = self.columns

        else:
            columns = self.columns

        rows: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.rows, Unset):
            rows = UNSET
        elif isinstance(self.rows, list):
            rows = []
            for rows_type_0_item_data in self.rows:
                rows_type_0_item = rows_type_0_item_data.to_dict()
                rows.append(rows_type_0_item)

        else:
            rows = self.rows

        total: Union[None, Unset, int]
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total

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

        row_count: Union[None, Unset, int]
        if isinstance(self.row_count, Unset):
            row_count = UNSET
        else:
            row_count = self.row_count

        truncated: Union[None, Unset, bool]
        if isinstance(self.truncated, Unset):
            truncated = UNSET
        else:
            truncated = self.truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation": operation,
            }
        )
        if tables is not UNSET:
            field_dict["tables"] = tables
        if table is not UNSET:
            field_dict["table"] = table
        if columns is not UNSET:
            field_dict["columns"] = columns
        if rows is not UNSET:
            field_dict["rows"] = rows
        if total is not UNSET:
            field_dict["total"] = total
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if row_count is not UNSET:
            field_dict["row_count"] = row_count
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.website_db_result_rows_type_0_item import WebsiteDbResultRowsType0Item

        d = dict(src_dict)
        operation = d.pop("operation")

        def _parse_tables(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tables_type_0 = cast(list[str], data)

                return tables_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        tables = _parse_tables(d.pop("tables", UNSET))

        def _parse_table(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        table = _parse_table(d.pop("table", UNSET))

        def _parse_columns(data: object) -> Union[None, Unset, list[Any]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                columns_type_0 = cast(list[Any], data)

                return columns_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[Any]], data)

        columns = _parse_columns(d.pop("columns", UNSET))

        def _parse_rows(data: object) -> Union[None, Unset, list["WebsiteDbResultRowsType0Item"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rows_type_0 = []
                _rows_type_0 = data
                for rows_type_0_item_data in _rows_type_0:
                    rows_type_0_item = WebsiteDbResultRowsType0Item.from_dict(rows_type_0_item_data)

                    rows_type_0.append(rows_type_0_item)

                return rows_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["WebsiteDbResultRowsType0Item"]], data)

        rows = _parse_rows(d.pop("rows", UNSET))

        def _parse_total(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total = _parse_total(d.pop("total", UNSET))

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

        def _parse_row_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        row_count = _parse_row_count(d.pop("row_count", UNSET))

        def _parse_truncated(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        truncated = _parse_truncated(d.pop("truncated", UNSET))

        website_db_result = cls(
            operation=operation,
            tables=tables,
            table=table,
            columns=columns,
            rows=rows,
            total=total,
            limit=limit,
            offset=offset,
            row_count=row_count,
            truncated=truncated,
        )

        website_db_result.additional_properties = d
        return website_db_result

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
