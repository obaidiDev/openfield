from typing import Literal, cast

DeployWebsiteRequestEnv = Literal["preview", "production"]

DEPLOY_WEBSITE_REQUEST_ENV_VALUES: set[DeployWebsiteRequestEnv] = {
    "preview",
    "production",
}


def check_deploy_website_request_env(value: str) -> DeployWebsiteRequestEnv:
    if value in DEPLOY_WEBSITE_REQUEST_ENV_VALUES:
        return cast(DeployWebsiteRequestEnv, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DEPLOY_WEBSITE_REQUEST_ENV_VALUES!r}"
    )
