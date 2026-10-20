from typing import Literal, cast

WebsiteDbRequestOperation = Literal["query", "rows", "schema", "tables"]

WEBSITE_DB_REQUEST_OPERATION_VALUES: set[WebsiteDbRequestOperation] = {
    "query",
    "rows",
    "schema",
    "tables",
}


def check_website_db_request_operation(value: str) -> WebsiteDbRequestOperation:
    if value in WEBSITE_DB_REQUEST_OPERATION_VALUES:
        return cast(WebsiteDbRequestOperation, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WEBSITE_DB_REQUEST_OPERATION_VALUES!r}"
    )
