import logging
from typing import Any, Dict, List

from src.clients.http_client import HttpClient
from src.extractors.user_parser import parse_user

LOGGER = logging.getLogger(__name__)

class UsernameSearchService:
    """
    Service for discovering usernames based on a search query.
    """

    def __init__(self, http_client: HttpClient) -> None:
        self.http_client = http_client

    @staticmethod
    def _sample_raw_user(query: str) -> Dict[str, Any]:
        handle = query.strip().lstrip("@") or "sampleuser"
        return {
            "username": handle,
            "fullname": handle.title(),
            "verified": False,
            "avatar": "",
            "content": f"Sample profile for @{handle} (offline fallback).",
            "url": f"https://x.com/{handle}",
            "type": "username",
        }

    def search(self, query: str, maximum: int = 50) -> List[Dict[str, Any]]:
        params = {"q": query, "maximum": maximum}
        data = self.http_client.get_json("/x/twitter/user-search", params=params)

        users_raw: List[Dict[str, Any]] = []
        if isinstance(data, dict) and isinstance(data.get("users"), list):
            users_raw = data["users"]
        elif isinstance(data, list):
            users_raw = data
        else:
            LOGGER.warning(
                "No remote data received for username search, using offline sample"
            )
            users_raw = [self._sample_raw_user(query)]

        parsed = [parse_user(raw) for raw in users_raw]
        return parsed[: maximum if maximum > 0 else len(parsed)]