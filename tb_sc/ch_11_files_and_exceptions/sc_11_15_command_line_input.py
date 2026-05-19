"""Tiny helper: classify file as text or binary from CLI arg or prompt."""

import sys
from pathlib import Path


def _is_text(data: bytes) -> bool:
    if not data:
        return True
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return False
    return all(ch.isprintable() or ch in "\n\r\t" for ch in text)


def main() -> None:
    filename = sys.argv[1] if len(sys.argv) > 1 else input("Filename: ").strip()
    if not filename:
        print("No filename provided.")
        return

    path = Path(filename)
    if not path.exists():
        print(f"File not found: {path}")
        return

    try:
        data = path.read_bytes()
    except OSError as exc:
        print(f"Cannot read file: {path} ({exc})")
        return

    kind = "text" if _is_text(data) else "binary"
    print(f"{path} looks like {kind} data.")


if __name__ == "__main__":
    main()
