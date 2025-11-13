import logging
from typing import Any, Dict, List, Optional

from src.clients.http_client import HttpClient
from src.extractors.tweet_parser import parse_tweet

LOGGER = logging.getLogger(__name__)

class UsernameTimelineService:
    """
    Service responsible for fetching tweets from a specific username timeline.
    """

    def __init__(self, http_client: HttpClient) -> None:
        self.http_client = http_client

    def _sample_raw_tweet(self, username: str) -> Dict[str, Any]:
        return {
            "author": username,
            "verified": False,
            "avatar": "",
            "content": f"Sample tweet for @{username} (offline fallback).",
            "time": "2024-01-01",
            "media": "",
            "quote": None,
            "comments": 0,
            "reposts": 0,
            "mentions": 0,
            "likes": 0,
            "link": f"https://x.com/{username}/status/1",
            "type": "tweet",
        }

    def fetch(
        self,
        username: str,
        sincedate: Optional[str] = None,
        untildate: Optional[str] = None,
        maximum: int = 100,
    ) -> List[Dict[str, Any]]:
        """
        Fetches a username timeline. When the remote endpoint is not reachable,
        it falls back to a small offline sample for demonstration purposes.
        """
        params = {
            "username": username,
            "sincedate": sincedate,
            "untildate": untildate,
            "maximum": maximum,
        }
        data = self.http_client.get_json("/x/twitter/timeline", params=params)
        tweets_raw: List[Dict[str, Any]] = []

        if isinstance(data, dict) and isinstance(data.get("tweets"), list):
            tweets_raw = data["tweets"]
        elif isinstance(data, list):
            tweets_raw = data
        else:
            LOGGER.warning(
                "No remote data received for username timeline, using offline sample"
            )
            tweets_raw = [self._sample_raw_tweet(username)]

        parsed = [parse_tweet(raw, keyword=username) for raw in tweets_raw]
        return parsed[: maximum if maximum > 0 else len(parsed)]