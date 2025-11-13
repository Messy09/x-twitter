import json
import logging
from typing import Any, Dict, Optional

import requests

LOGGER = logging.getLogger(__name__)

class HttpClient:
    """Thin wrapper around requests for JSON-friendly HTTP access."""

    def __init__(
        self,
        base_url: str = "https://example.com",
        timeout: int = 10,
        proxies: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.proxies = proxies or {}
        self.headers = headers or {
            "User-Agent": "x-twitter-scraper/0.1",
            "Accept": "application/json, text/plain;q=0.9,*/*;q=0.8",
        }

    @classmethod
    def from_settings(cls, proxy_manager: "ProxyManager") -> "HttpClient":
        """
        Factory method that pulls configuration from the settings.example.json
        if present, and merges proxy configuration.
        """
        from pathlib import Path
        from src.clients.proxy_manager import ProxyManager  # type: ignore

        settings_path = (
            Path(__file__).resolve().parents[1] / "config" / "settings.example.json"
        )
        base_url = "https://example.com"
        timeout = 10
        headers = None

        if settings_path.exists():
            try:
                data = json.loads(settings_path.read_text(encoding="utf-8"))
                base_url = data.get("base_url", base_url)
                timeout = int(data.get("request_timeout", timeout))
                headers = data.get("headers")
            except Exception as exc:  # pylint: disable=broad-except
                LOGGER.warning("Failed to read settings.example.json: %s", exc)

        if not isinstance(proxy_manager, ProxyManager):
            # Avoid circular import typing issues
            proxy = ProxyManager.from_env()
        else:
            proxy = proxy_manager

        proxies = proxy.get_requests_proxies()
        return cls(base_url=base_url, timeout=timeout, proxies=proxies, headers=headers)

    def _build_url(self, path: str) -> str:
        if path.startswith("http://") or path.startswith("https://"):
            return path
        return f"{self.base_url}/{path.lstrip('/')}"

    def get_json(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        url = self._build_url(path)
        try:
            LOGGER.debug("GET %s params=%s", url, params)
            response = requests.get(
                url,
                params=params,
                timeout=self.timeout,
                proxies=self.proxies or None,
                headers=self.headers,
            )
            response.raise_for_status()
        except requests.RequestException as exc:
            LOGGER.error("HTTP GET failed for %s: %s", url, exc)
            return None

        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            try:
                return response.json()
            except ValueError as exc:
                LOGGER.error("Failed to decode JSON from %s: %s", url, exc)
                return None

        LOGGER.debug(
            "Received non-JSON response from %s (content-type=%s), returning raw text",
            url,
            content_type,
        )
        return {"raw": response.text}