from typing import Any, Dict

from src.services.keyword_search_service import KeywordSearchService
from src.services.username_search_service import UsernameSearchService
from src.services.username_timeline_service import UsernameTimelineService

class DummyHttpClient:
    def __init__(self, payload: Any) -> None:
        self.payload = payload
        self.called_with: Dict[str, Any] = {}

    def get_json(self, path: str, params=None) -> Any:  # noqa: D401
        self.called_with = {"path": path, "params": params}
        return self.payload

def test_username_timeline_service_uses_http_client():
    payload = {
        "tweets": [
            {
                "author": "alice",
                "verified": True,
                "content": "Hello from Alice",
                "time": "2024-10-01",
                "comments": 1,
                "reposts": 2,
                "mentions": 0,
                "likes": 3,
                "link": "https://x.com/alice/status/1",
                "type": "tweet",
            }
        ]
    }
    client = DummyHttpClient(payload)
    service = UsernameTimelineService(client)  # type: ignore[arg-type]

    results = service.fetch(username="alice", maximum=10)

    assert len(results) == 1
    assert results[0]["author"] == "alice"
    assert client.called_with["params"]["username"] == "alice"

def test_username_search_service_uses_http_client():
    payload = {
        "users": [
            {
                "username": "bob",
                "fullname": "Bob Builder",
                "verified": True,
                "avatar": "",
                "content": "Can we fix it?",
                "url": "https://x.com/bob",
                "type": "username",
            }
        ]
    }
    client = DummyHttpClient(payload)
    service = UsernameSearchService(client)  # type: ignore[arg-type]

    results = service.search(query="bob", maximum=5)

    assert len(results) == 1
    assert results[0]["username"] == "bob"
    assert client.called_with["params"]["q"] == "bob"

def test_keyword_search_service_uses_http_client():
    payload = {
        "tweets": [
            {
                "author": "charlie",
                "verified": False,
                "content": "keyword inside tweet",
                "time": "2024-10-02",
                "comments": 0,
                "reposts": 0,
                "mentions": 0,
                "likes": 1,
                "link": "https://x.com/charlie/status/2",
                "type": "tweet",
            }
        ]
    }
    client = DummyHttpClient(payload)
    service = KeywordSearchService(client)  # type: ignore[arg-type]

    results = service.search(keyword="keyword", maximum=5)

    assert len(results) == 1
    assert "keyword" in results[0]["content"]
    assert client.called_with["params"]["keyword"] == "keyword"