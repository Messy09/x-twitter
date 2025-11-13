import logging
from datetime import datetime
from typing import Optional

from dateutil import parser as date_parser

LOGGER = logging.getLogger(__name__)

def parse_date(date_str: str) -> Optional[datetime]:
    if not date_str:
        return None
    try:
        return date_parser.parse(date_str)
    except (ValueError, TypeError) as exc:
        LOGGER.debug("Failed to parse date %r: %s", date_str, exc)
        return None

def ensure_mm_dd(date_str: str) -> str:
    """
    Normalizes a date-like string into MM-DD format.

    Accepts:
    - Already formatted MM-DD
    - ISO dates (YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS, etc.)
    - Other formats supported by dateutil.parser
    """
    if not date_str:
        return ""

    date_str = str(date_str).strip()
    if len(date_str) == 5 and date_str[2] == "-" and date_str.replace("-", "").isdigit():
        return date_str

    dt = parse_date(date_str)
    if not dt:
        return date_str

    return f"{dt.month:02d}-{dt.day:02d}"