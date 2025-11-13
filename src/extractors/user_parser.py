from typing import Any, Dict

def parse_user(raw: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalizes raw user-like objects into the documented username search schema.
    """
    username = raw.get("username") or raw.get("screen_name") or ""
    fullname = raw.get("fullname") or raw.get("name") or ""
    verified = bool(raw.get("verified", False))
    avatar = (
        raw.get("avatar")
        or raw.get("profile_image_url_https")
        or raw.get("profile_image_url")
        or ""
    )
    content = raw.get("content") or raw.get("description") or ""
    url = raw.get("url") or raw.get("profile_url") or f"https://x.com/{username}" if username else ""
    user_type = raw.get("type") or "username"

    return {
        "username": username,
        "fullname": fullname,
        "verified": verified,
        "avatar": avatar,
        "content": content,
        "url": url,
        "type": user_type,
    }