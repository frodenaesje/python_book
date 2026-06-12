---
title: "Writing and Appending to Files"
id: "ex_11_02_write_append"
tags: ["open", "write", "writelines", "append", "with", "OSError", "finally"]
difficulty: "easy"
prerequisites: ["open", "write", "with", "try-except-finally", "OSError"]
learning_outcomes:
  - "Write to a file using mode 'w' and 'a'"
  - "Understand the difference between write and append mode"
  - "Use writelines() to write a list of strings"
  - "Use finally to guarantee cleanup"
---

# Writing and Appending to Files

## Exercise

### Part 1 - Write a shopping list

Write a function `write_list(filename: str, items: list[str]) -> None`
that writes a list of strings to a file, one item per line.

Use mode `"w"` - this creates the file if it does not exist, or
overwrites it if it does. Use `writelines()` with a list comprehension
that adds `"\n"` to each item.

### Part 2 - Append to the list

Write a function `append_items(filename: str, items: list[str]) -> None`
that appends more items to the end of an existing file.

Use mode `"a"`. Note that append mode never overwrites - it always adds
to the end.

### Part 3 - Read back and verify

Write a function `read_list(filename: str) -> list[str]` that reads the
file back and returns a clean list of items (no trailing newlines).

### Part 4 - finally for cleanup

Show how `finally` works by writing a version of `write_list` that
opens the file manually (without `with`) and uses `try-finally` to
guarantee `close()` is always called, even if `write()` raises an
exception.

## Example run

```
Written 3 items to shopping.txt

After appending 2 more items:
  1. milk
  2. eggs
  3. bread
  4. butter
  5. coffee

Contents of shopping.txt verified: 5 items
```

## Topics

- `"w"` mode: create or overwrite
- `"a"` mode: append to existing
- `writelines()` with `"\n"` suffix
- `try-finally` as the manual equivalent of `with`

---
## Instructor notes

**Learning objectives covered:** write, append, writelines, finally

**writelines does not add newlines:** A common mistake. Students must
add "\n" themselves. writelines([item + "\n" for item in items]) is clean.

**try-finally pattern:**
```python
f = open(filename, "w", encoding="utf-8")
try:
    f.write(content)
finally:
    f.close()  # always runs, even if write() raises
```
This is exactly what `with` does behind the scenes. Showing both makes
the value of `with` concrete.

**CWD note:** The file is written to the CWD, which in VS Code is the
project root - not necessarily the folder where the script lives. This
is why pathlib (ex_11_09) matters.
