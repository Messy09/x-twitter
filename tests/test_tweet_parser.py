from src.extractors.tweet_parser import parse_tweet

def test_parse_tweet_normalizes_fields_and_time():
    raw = {
        "author": "Test User",
        "verified": True,
        "avatar": "https://example.com/avatar.jpg",
        "text": "Hello world",
        "created_at": "2024-11-10T12:34:56Z",
        "media_url": "",
        "quoted_text": None,
        "comments": 5,
        "retweets": 10,
        "quote_count": 2,
        "favorite_count": 20,
        "url": "https://x.com/test/status/1",
        "tweet_type": "tweet",
    }

    parsed = parse_tweet(raw, keyword="testkeyword")

    assert parsed["author"] == "Test User"
    assert parsed["verified"] is True
    assert parsed["content"] == "Hello world"
    assert parsed["time"] == "11-10"
    assert parsed["comments"] == 5
    assert parsed["reposts"] == 10
    assert parsed["mentions"] == 2
    assert parsed["likes"] == 20
    assert parsed["link"] == "https://x.com/test/status/1"
    assert parsed["type"] == "tweet"
    assert parsed["keyword"] == "testkeyword"