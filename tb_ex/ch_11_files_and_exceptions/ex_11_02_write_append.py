# file: ex_11_02_write_append.py

def write_list(filename: str, items: list[str]) -> None:
    """Write a list of items to a file, one per line. Overwrites if exists."""
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines([item + "\n" for item in items])


def append_items(filename: str, items: list[str]) -> None:
    """Append items to an existing file."""
    with open(filename, "a", encoding="utf-8") as f:
        f.writelines([item + "\n" for item in items])


def read_list(filename: str) -> list[str]:
    """Read a file and return a clean list of items (no trailing newlines)."""
    with open(filename, encoding="utf-8") as f:
        return [line.rstrip() for line in f if line.strip()]


def write_list_manual_close(filename: str, items: list[str]) -> None:
    """Write list using try-finally instead of with - to show how with works."""
    f = open(filename, "w", encoding="utf-8")
    try:
        f.writelines([item + "\n" for item in items])
    finally:
        f.close()  # always runs, even if writelines() raises


if __name__ == "__main__":
    write_list("shopping.txt", ["milk", "eggs", "bread"])
    print("Written 3 items to shopping.txt")

    append_items("shopping.txt", ["butter", "coffee"])

    items = read_list("shopping.txt")
    print(f"\nAfter appending 2 more items:")
    for i, item in enumerate(items, 1):
        print(f"  {i}. {item}")

    print(f"\nContents of shopping.txt verified: {len(items)} items")
