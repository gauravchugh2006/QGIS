"""Write report files in a consistent way and create folders when needed."""

import json
from pathlib import Path
from typing import Any


def ensure_parent_dir(path: Path | str) -> Path:
    """Ensure the output folder exists before a report file is written."""
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    return file_path


def write_text_report(path: Path | str, content: str) -> Path:
    """Save plain text reports such as CPU profile output or summaries."""
    file_path = ensure_parent_dir(path)
    file_path.write_text(content, encoding="utf-8")
    return file_path


def write_json_report(path: Path | str, content: dict[str, Any]) -> Path:
    """Save structured report data that is easier to parse later."""
    file_path = ensure_parent_dir(path)
    file_path.write_text(json.dumps(content, indent=2), encoding="utf-8")
    return file_path
