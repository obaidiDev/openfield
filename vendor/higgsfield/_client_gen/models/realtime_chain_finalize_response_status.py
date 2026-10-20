from typing import Literal, cast

RealtimeChainFinalizeResponseStatus = Literal["finalized", "released"]

REALTIME_CHAIN_FINALIZE_RESPONSE_STATUS_VALUES: set[RealtimeChainFinalizeResponseStatus] = {
    "finalized",
    "released",
}


def check_realtime_chain_finalize_response_status(
    value: str,
) -> RealtimeChainFinalizeResponseStatus:
    if value in REALTIME_CHAIN_FINALIZE_RESPONSE_STATUS_VALUES:
        return cast(RealtimeChainFinalizeResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REALTIME_CHAIN_FINALIZE_RESPONSE_STATUS_VALUES!r}"
    )
