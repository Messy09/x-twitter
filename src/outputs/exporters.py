import json
import logging
from pathlib import Path
from typing import Dict, List, Optional

from src.outputs.formatters import to_json, csv_string

LOGGER = logging.getLogger(__name__)

def export_json(data: List[Dict], file_path: Optional[str] = None) -> None:
    payload = to_json(data)
    if file_path:
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(payload, encoding="utf-8")
        LOGGER.info("Wrote JSON output to %s", path)
    else:
        print(payload)  # noqa: T201

def export_csv(data: List[Dict], file_path: str) -> None:
    csv_content = csv_string(data)
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(csv_content, encoding="utf-8")
    LOGGER.info("Wrote CSV output to %s", path)

def load_json_file(path: str) -> List[Dict]:
    p = Path(path)
    content = p.read_text(encoding="utf-8")
    loaded = json.loads(content)
    if isinstance(loaded, list):
        return loaded
    if isinstance(loaded, dict):
        return [loaded]
    raise ValueError(f"Unsupported JSON root type in {path}: {type(loaded)}")