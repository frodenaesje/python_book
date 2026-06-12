---
title: "Recursive Directory Tree"
id: "ex_14_08_directory_tree"
tags: ["recursion", "pathlib", "Path", "directory", "tree traversal", "linear recursion"]
difficulty: "medium"
prerequisites: ["recursion", "pathlib", "Path", "iterdir", "is_dir", "is_file"]
learning_outcomes:
  - "Apply recursion to a real file system structure"
  - "Use pathlib.Path.iterdir() to list directory contents"
  - "Understand that a directory structure is a natural recursive data structure"
  - "Produce indented tree output"
---

# Recursive Directory Tree

## Exercise

A directory structure is a natural recursive data structure: a directory
contains files and other directories, which in turn contain more files
and directories. Recursion fits this structure perfectly.

Write a recursive function `print_tree(path, indent=0)` that prints
the contents of a directory tree, indented to show the nesting level.

Use `pathlib.Path` to work with the file system:
- `Path(path).iterdir()` lists all items in a directory
- `item.is_dir()` checks if an item is a directory
- `item.is_file()` checks if an item is a file
- `item.name` gives the filename without the full path

Print directories with a `/` suffix so they are easy to spot.
Recurse into each subdirectory with `indent + 1`.

### Part 2

Extend the function to:
- Count and return the total number of files
- Accept a list of extensions to filter (e.g. only show `.py` files)

## Example run

```
print_tree(".")

ch_14_recursion/
  ex_14_01_ruler.py
  ex_14_01_ruler_start.py
  ex_14_02_flatten_nested_lists.py
  ...
  subdir/
    helper.py
    data.txt

Total files: 18
```

## Topics

- `pathlib.Path.iterdir()` for directory listing
- `item.is_dir()` / `item.is_file()`
- Recursion on a tree structure
- Indent with `"  " * indent`

---
## Instructor notes

**Learning objectives covered:** pathlib, directory recursion, tree traversal

**Why this is a great practical exercise:** Directory traversal is something
every programmer does. The recursive solution is 5 lines. Students also
reinforce pathlib from chapter 11.

**Sorting for consistent output:**
```python
for item in sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name)):
```
This sorts directories before files at each level.

**Connection to book section 14.10:** The book shows exactly this pattern.
The exercise gives hands-on practice with it.

**Part 2 extension pattern:**
```python
def print_tree(path, indent=0, extensions=None):
    count = 0
    for item in sorted(Path(path).iterdir()):
        if item.is_dir():
            print("  " * indent + item.name + "/")
            count += print_tree(item, indent + 1, extensions)
        elif extensions is None or item.suffix in extensions:
            print("  " * indent + item.name)
            count += 1
    return count
```
