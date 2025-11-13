from typing import Any, Dict, Optional

from src.extractors.utils_time import ensure_mm_dd

def parse_tweet(raw: Dict[str, Any], keyword: Optional[str] = None) -> Dict[str, Any]:
    """
    Normalizes raw tweet-like objects into the documented schema.
    """
    user = raw.get("user") or {}

    author = raw.get("author") or user.get("name") or ""
    verified = bool(raw.get("verified", user.get("verified", False)))
    avatar = raw.get("avatar") or user.get("avatar") or user.get("profile_image_url", "")

    # Normalize text field (tweet text vs. content)
    content = raw.get("content") or raw.get("text") or ""

    # Normalize timestamp
    time_raw = raw.get("time") or raw.get("created_at") or ""
    time_norm = ensure_mm_dd(time_raw) if time_raw else ""

    media = raw.get("media") or raw.get("media_url") or ""
    quote = raw.get("quote") or raw.get("quoted_text") or None

    comments = raw.get("comments")
    reposts = raw.get("reposts") or raw.get("retweets")
    mentions = raw.get("mentions") or raw.get("quote_count")
    likes = raw.get("likes") or raw.get("favorite_count")

    link = raw.get("link") or raw.get("url") or ""
    tweet_type = raw.get("type") or raw.get("tweet_type") or "tweet"

    return {
        "keyword": keyword or raw.get("keyword") or "",
        "sincedate": raw.get("sincedate"),
        "untildate": raw.get("untildate"),
        "maximum": raw.get("maximum"),
        "author": author,
        "verified": verified,
        "avatar": avatar,
        "content": content,
        "time": time_norm,
        "media": media,
        "quote": quote,
        "comments": comments if isinstance(comments, (int, type(None))) else None,
        "reposts": reposts if isinstance(reposts, (int, type(None))) else None,
        "mentions": mentions if isinstance(mentions, (int, type(None))) else None,
        "likes": likes if isinstance(likes, (int, type(None))) else None,
        "link": link,
        "type": tweet_type,
    }