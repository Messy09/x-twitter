import logging
import os
from typing import Dict, Optional

LOGGER = logging.getLogger(__name__)

class ProxyManager:
    """
    Simple proxy manager that can be configured from environment variables.

    Supported environment variables:
    - HTTP_PROXY / HTTPS_PROXY / ALL_PROXY: standard proxy URLs
    - X_TWITTER_PROXY: overrides all proxies when set
    """

    def __init__(self, http: Optional[str] = None, https: Optional[str] = None) -> None:
        self.http = http
        self.https = https

    @classmethod
    def from_env(cls) -> "ProxyManager":
        custom = os.getenv("X_TWITTER_PROXY")
        if custom:
            LOGGER.info("Using custom proxy from X_TWITTER_PROXY")
            return cls(http=custom, https=custom)

        http = os.getenv("HTTP_PROXY") or os.getenv("http_proxy")
        https = os.getenv("HTTPS_PROXY") or os.getenv("https_proxy") or http

        if http or https:
            LOGGER.info("Using proxies from HTTP_PROXY/HTTPS_PROXY")
        else:
            LOGGER.info("No proxies configured; running without proxy")

        return cls(http=http, https=https)

    def get_requests_proxies(self) -> Dict[str, str]:
        proxies: Dict[str, str] = {}
        if self.http:
            proxies["http"] = self.http
        if self.https:
            proxies["https"] = self.https
        return proxies