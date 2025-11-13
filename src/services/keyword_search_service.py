import logging
from typing import Any, Dict, List, Optional

from src.clients.http_client import HttpClient
from src.extractors.tweet_parser import parse_tweet

LOGGER = logging.getLogger(__name__)

class KeywordSearchService:
    """
    Service for searching tweets by keyword, hashtag, or free text.
    """

    def __init__(self, http_client: HttpClient) -> None:
        self.http_client = http_client

    @staticmethod
    def _sample_raw_tweet(keyword: str) -> Dict[str, Any]:
        return {
            "author": "sample_author",
            "verified": True,
            "avatar": "",
            "content": f"Sample tweet containing '{keyword}' (offline fallback).",
            "time": "2024-01-02",
            "media": "",
            "quote": None,
            "comments": 1,
            "reposts": 2,
            "mentions": 0,
            "likes": 3,
            "link": "https://x.com/sample_author/status/2",
            "type": "tweet_w_media",
        }

    def search(
        self,
        keyword: str,
        sincedate: Optional[str] = None,
        untildate: Optional[str] = None,
        maximum: int = 100,
    ) -> List[Dict[str, Any]]:
        params = {
            "keyword": keyword,
            "sincedate": sincedate,
            "untildate": untildate,
            "maximum": maximum,
        }
        data = self.http_client.get_json("/x/twitter/keyword-search", params=params)

        tweets_raw: List[Dict[str, Any]] = []
        if isinstance(data, dict) and isinstance(data.get("tweets"), list):
            tweets_raw = data["tweets"]
        elif isinstance(data, list):
            tweets_raw = data
        else:
            LOGGER.warning(
                "No remote data received for keyword search, using offline sample"
            )
            tweets_raw = [self._sample_raw_tweet(keyword)]

        parsed = [parse_tweet(raw, keyword=keyword) for raw in tweets_raw]
        return parsed[: maximum if maximum > 0 else len(parsed)]