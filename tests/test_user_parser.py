from src.extractors.user_parser import parse_user

def test_parse_user_normalizes_profile_fields():
    raw = {
        "screen_name": "testuser",
        "name": "Test User",
        "verified": False,
        "profile_image_url_https": "https://example.com/avatar.jpg",
        "description": "Bio here",
    }

    parsed = parse_user(raw)

    assert parsed["username"] == "testuser"
    assert parsed["fullname"] == "Test User"
    assert parsed["verified"] is False
    assert parsed["avatar"] == "https://example.com/avatar.jpg"
    assert parsed["content"] == "Bio here"
    assert parsed["url"].endswith("/testuser")
    assert parsed["type"] == "username"