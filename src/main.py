import argparse
import json
import logging
import logging.config
import sys
from pathlib import Path

# Ensure src package is importable whether run as `python -m src.main`
# or as `python src/main.py`.
if __package__ is None or __package__ == "":
    repo_root = Path(__file__).resolve().parents[1]
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))

from src.clients.http_client import HttpClient
from src.clients.proxy_manager import ProxyManager
from src.outputs.exporters import export_json, export_csv
from src.services.username_timeline_service import UsernameTimelineService
from src.services.username_search_service import UsernameSearchService
from src.services.keyword_search_service import KeywordSearchService

LOGGER = logging.getLogger("x_twitter.main")

def configure_logging() -> None:
    config_path = Path(__file__).resolve().parent / "config" / "logging.conf"
    if config_path.exists():
        logging.config.fileConfig(config_path, disable_existing_loggers=False)
    else:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        )

def build_services() -> dict:
    proxy_manager = ProxyManager.from_env()
    http_client = HttpClient.from_settings(proxy_manager=proxy_manager)
    return {
        "username_timeline": UsernameTimelineService(http_client),
        "username_search": UsernameSearchService(http_client),
        "keyword_search": KeywordSearchService(http_client),
    }

def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="X Twitter Tweets & Usernames Scraper CLI"
    )
    parser.add_argument(
        "--mode",
        required=True,
        choices=["username_timeline", "username_search", "keyword_search"],
        help="Scraping mode to run.",
    )
    parser.add_argument(
        "--keyword",
        required=True,
        help=(
            "Username for timeline/username_search or keyword/hashtag for "
            "keyword_search."
        ),
    )
    parser.add_argument(
        "--sincedate",
        help="Optional lower bound date (YYYY-MM-DD).",
    )
    parser.add_argument(
        "--untildate",
        help="Optional upper bound date (YYYY-MM-DD).",
    )
    parser.add_argument(
        "--maximum",
        type=int,
        default=100,
        help="Maximum number of items to return.",
    )
    parser.add_argument(
        "--output",
        help="Optional path to write JSON output. Defaults to STDOUT.",
    )
    parser.add_argument(
        "--output-csv",
        help="Optional path to also write CSV output.",
    )
    return parser.parse_args(argv)

def main(argv=None) -> int:
    configure_logging()
    args = parse_args(argv)

    LOGGER.info("Starting X Twitter scraper mode=%s", args.mode)

    services = build_services()
    service = services[args.mode]

    try:
        if args.mode == "username_timeline":
            result = service.fetch(
                username=args.keyword,
                sincedate=args.sincedate,
                untildate=args.untildate,
                maximum=args.maximum,
            )
        elif args.mode == "username_search":
            result = service.search(
                query=args.keyword,
                maximum=args.maximum,
            )
        else:
            result = service.search(
                keyword=args.keyword,
                sincedate=args.sincedate,
                untildate=args.untildate,
                maximum=args.maximum,
            )
    except Exception as exc:  # pylint: disable=broad-except
        LOGGER.exception("Fatal error while running scraper: %s", exc)
        return 1

    if not isinstance(result, list):
        LOGGER.warning("Service returned non-list result, coercing to list")
        result = [result]

    # Export JSON
    export_json(result, args.output)

    # Optionally export CSV
    if args.output_csv:
        export_csv(result, args.output_csv)

    LOGGER.info("Completed X Twitter scraping with %d records", len(result))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())