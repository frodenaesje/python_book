# ex_11_01_read_text_file

See the textbook for the exercise text.

## Assessment criteria

| Criterion | Description | Weight (%) |
|---|---|---:|
| Line-by-line reading | Implements print_file(filename) and reads the file by looping directly over the file object. | 30 |
| Numbered output | Prints every line with consecutive line numbers starting at 1, removing trailing newlines. | 15 |
| Safe file handling | Uses a with statement to ensure the file is closed, including when an error occurs. | 20 |
| Missing-file handling | Catches FileNotFoundError and prints a helpful message instead of crashing. | 20 |
| Success-only file reading | Uses try-except-else with file reading in the else block, so reading occurs only after the file opens successfully. | 15 |
| **Total** | | **100%** |
