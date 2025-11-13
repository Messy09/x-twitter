import argparse
import sys
from pathlib import Path

# Ensure repo root is on sys.path
REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.outputs.exporters import export_csv, load_json_file  # noqa: E402

def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert JSON output from X Twitter scraper to CSV."
    )
    parser.add_argument("input_json", help="Path to JSON file with scraper output.")
    parser.add_argument(
        "output_csv",
        nargs="?",
        help="Optional path for CSV file. Defaults to input_json with .csv extension.",
    )
    return parser.parse_args(argv)

def main(argv=None) -> int:
    args = parse_args(argv)
    input_path = Path(args.input_json)
    if not input_path.exists():
        print(f"Input file not found: {input_path}", file=sys.stderr)  # noqa: T201
        return 1

    output_path = (
        Path(args.output_csv)
        if args.output_csv
        else input_path.with_suffix(".csv")
    )

    data = load_json_file(str(input_path))
    export_csv(data, str(output_path))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())