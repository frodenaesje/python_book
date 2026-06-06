# File: ap_demo_paths.py
"""Demonstrate the difference between PATH and sys.path.

- PATH (environment variable): used by the operating system to find executables
  such as "python", "git", or "ffmpeg".
- sys.path (Python variable): used by Python to find importable modules/packages.
"""

from pathlib import Path
import os
import sys


def print_path_env() -> None:
    """Show PATH as one directory per line."""
    raw_path = os.environ.get("PATH", "")
    print("PATH entries (OS executable lookup):")
    for entry in raw_path.split(os.pathsep):
        if entry:
            print(f"  - {entry}")
    print()


def print_sys_path() -> None:
    """Show sys.path as one directory per line."""
    print("sys.path entries (Python import lookup):")
    for entry in sys.path:
        print(f"  - {entry}")
    print()


def main() -> None:
    print_path_env()
    print_sys_path()

    # Build a path relative to this file's location.
    # __file__ points to the current script file.
    this_file = Path(__file__).resolve()
    project_root = this_file.parent.parent
    local_modules = project_root / "my_modules"

    print(f"Script file (__file__): {this_file}")
    print(f"Project root (derived): {project_root}")
    print(f"Candidate module folder: {local_modules}")
    print()

    local_modules_str = str(local_modules)

    # Append: searched late (after earlier entries in sys.path).
    if local_modules_str not in sys.path:
        sys.path.append(local_modules_str)
        print("Appended local_modules to sys.path")

    # Insert at index 0: searched first (can shadow other modules).
    if local_modules_str in sys.path:
        sys.path.remove(local_modules_str)
    sys.path.insert(0, local_modules_str)
    print("Inserted local_modules at index 0 in sys.path")
    print()

    print_sys_path()


if __name__ == "__main__":
    main()
