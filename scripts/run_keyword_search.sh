set -euo pipefail

MODE="keyword_search"
KEYWORD="${1:-spacex}"
MAXIMUM="${2:-20}"

python -m src.main --mode "$MODE" --keyword "$KEYWORD" --maximum "$MAXIMUM"