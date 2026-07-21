#!/usr/bin/env python3
"""Basic JSON syntax checker for AXIS OMNI example and runtime files.

This is intentionally dependency-free. Full JSON Schema validation can be added
with a library such as jsonschema when the implementation phase begins.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


def validate_json(path: Path) -> None:
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")
    with path.open("r", encoding="utf-8") as handle:
        json.load(handle)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate JSON syntax.")
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()

    failed = False
    for path in args.paths:
        try:
            validate_json(path)
            print(f"PASS {path}")
        except (OSError, json.JSONDecodeError) as exc:
            failed = True
            print(f"FAIL {path}: {exc}", file=sys.stderr)

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
