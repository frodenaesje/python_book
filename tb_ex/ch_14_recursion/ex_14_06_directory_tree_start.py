# file: ex_14_06_directory_tree.py
from pathlib import Path


def print_tree(path, indent=0):
    """Print a recursive directory tree with indentation."""
    # TODO: iterate over sorted contents of Path(path) with .iterdir()
    # TODO: for each item:
    #         if item.is_dir():
    #             print "  " * indent + item.name + "/"
    #             recurse: print_tree(item, indent + 1)
    #         elif item.is_file():
    #             print "  " * indent + item.name
    pass


def print_tree_filtered(path, indent=0, extensions=None):
    """Print tree and return file count. Optional extension filter."""
    # TODO: same as print_tree but:
    #         - count and return total files
    #         - only show files whose suffix is in extensions (if given)
    pass


if __name__ == "__main__":
    import sys
    root = sys.argv[1] if len(sys.argv) > 1 else "."

    print_tree(root)
    print()
    count = print_tree_filtered(root, extensions={".py"})
    print(f"\nTotal .py files: {count}")
