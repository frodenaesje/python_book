# file: ex_11_02_write_append_start.py

def write_list(filename: str, items: list[str]) -> None:
    """Write a list of items to a file, one per line. Overwrites if exists."""
    # TODO: open in "w" mode with encoding="utf-8"
    # TODO: use writelines() - remember to add "\n" to each item
    #       Hint: writelines([item + "\n" for item in items])
    pass


def append_items(filename: str, items: list[str]) -> None:
    """Append items to an existing file."""
    # TODO: open in "a" mode (append - never overwrites)
    # TODO: write the new items with "\n"
    pass


def read_list(filename: str) -> list[str]:
    """Read a file and return a clean list of items (no trailing newlines)."""
    # TODO: open and read all lines
    # TODO: strip "\n" from each line, skip empty lines
    pass


def write_list_manual_close(filename: str, items: list[str]) -> None:
    """Write list using try-finally instead of with - to show how with works."""
    # TODO: open file manually (no with)
    # TODO: use try-finally to guarantee f.close() is always called
    #       f = open(...)
    #       try:
    #           f.writelines(...)
    #       finally:
    #           f.close()
    pass


if __name__ == "__main__":
    write_list("shopping.txt", ["milk", "eggs", "bread"])
    print("Written 3 items to shopping.txt")

    append_items("shopping.txt", ["butter", "coffee"])

    items = read_list("shopping.txt")
    print(f"\nAfter appending 2 more items:")
    for i, item in enumerate(items, 1):
        print(f"  {i}. {item}")

    print(f"\nContents of shopping.txt verified: {len(items)} items")
