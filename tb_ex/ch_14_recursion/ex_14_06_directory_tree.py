# file: ex_14_06_directory_tree.py
from pathlib import Path
import sys


def print_tree(path, indent=0):
    """Print a recursive directory tree with indentation."""
    for item in sorted(Path(path).iterdir(), key=lambda p: (p.is_file(), p.name)):
        if item.is_dir():
            print("  " * indent + item.name + "/")
            print_tree(item, indent + 1)
        elif item.is_file():
            print("  " * indent + item.name)


def print_tree_filtered(path, indent=0, extensions=None):
    """Print tree and return file count. Optional extension filter."""
    count = 0
    for item in sorted(Path(path).iterdir(), key=lambda p: (p.is_file(), p.name)):
        if item.is_dir():
            print("  " * indent + item.name + "/")
            count += print_tree_filtered(item, indent + 1, extensions)
        elif item.is_file():
            if extensions is None or item.suffix in extensions:
                print("  " * indent + item.name)
                count += 1
    return count


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "."

    print_tree(root)
    print()
    count = print_tree_filtered(root, extensions={".py"})
    print(f"\nTotal .py files: {count}")
