#!/usr/bin/env python3
"""Write one short text for make.fun bounty u-pangg7-one-line-of-wonder-ee10fcd8."""

import os
import sys
from pathlib import Path

TEXT = "In the margin of the library book on tides: returned late, still wet."


def main() -> int:
    count = len(TEXT)
    assert 1 <= count <= 280, f"text must be 1..280 characters, got {count}"

    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    path = out_dir / "entry.txt"
    path.write_bytes(TEXT.encode("utf-8"))

    print(count, file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
