# file: ex_11_09_pathlibpathlib_start.py
from pathlib import Path


# --- Part 1: Script directory vs CWD ---

# TODO: print Path.cwd()
# TODO: print Path(__file__).resolve().parent
# TODO: print whether they are the same


# --- Part 2: Read and write relative to the script ---

def read_relative(filename: str) -> str:
    """Read a file located in the same folder as this script."""
    # TODO: build the full path using Path(__file__).resolve().parent / filename
    # TODO: return the file contents using read_text(encoding="utf-8")
    pass


def write_relative(filename: str, content: str) -> None:
    """Write a file to the same folder as this script."""
    # TODO: build the full path using Path(__file__).resolve().parent / filename
    # TODO: write using write_text(content, encoding="utf-8")
    pass


# --- Part 3: List Python files ---

def list_py_files(folder: str) -> list[Path]:
    """Return all .py files in the given folder (non-recursive)."""
    # TODO: use Path(folder).glob("*.py") to find all .py files
    # TODO: return as a sorted list
    pass


if __name__ == "__main__":
    # Part 1
    print(f"CWD:         {Path.cwd()}")
    # TODO: print script dir and whether it matches CWD

    print()

    # Part 2
    content = read_relative("sample.txt")
    lines   = content.splitlines()
    print(f"Read sample.txt: {len(lines)} lines, {len(content)} characters")
    write_relative("sample_copy.txt", content)
    print("Written sample_copy.txt to script directory.")

    print()

    # Part 3
    script_dir = Path(__file__).resolve().parent
    py_files   = list_py_files(str(script_dir))
    print(f"Python files in script dir:")
    for p in py_files:
        print(f"  {p.name:<40}{p.stat().st_size} bytes")
