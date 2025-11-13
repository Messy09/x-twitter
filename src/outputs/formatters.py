import csv
import io
import json
from typing import Dict, Iterable, List, Set

def to_json(data: List[Dict]) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False)

def to_csv_rows(data: List[Dict]) -> List[List[str]]:
    if not data:
        return []

    # Compute union of keys across all rows to ensure consistent columns
    all_keys: Set[str] = set()
    for item in data:
        all_keys.update(item.keys())

    headers = sorted(all_keys)
    rows: List[List[str]] = [headers]

    for item in data:
        row: List[str] = []
        for key in headers:
            value = item.get(key, "")
            if isinstance(value, (list, dict)):
                row.append(json.dumps(value, ensure_ascii=False))
            elif value is None:
                row.append("")
            else:
                row.append(str(value))
        rows.append(row)

    return rows

def csv_string(data: List[Dict]) -> str:
    rows = to_csv_rows(data)
    if not rows:
        return ""

    buffer = io.StringIO()
    writer = csv.writer(buffer)
    for row in rows:
        writer.writerow(row)
    return buffer.getvalue()