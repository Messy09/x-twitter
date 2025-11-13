set -euo pipefail

MODE="username_timeline"
KEYWORD="${1:-elonmusk}"
MAXIMUM="${2:-20}"

python -m src.main --mode "$MODE" --keyword "$KEYWORD" --maximum "$MAXIMUM"