# file: ex_11_01_read_text_file_start.py

def print_file(filename: str) -> None:
    """Print the contents of a text file with line numbers.

    Prints a helpful message if the file does not exist.
    """
    # TODO Part 1: open with "with open(filename, encoding='utf-8') as f:"
    #              loop over lines with "for i, line in enumerate(f, 1):"
    #              strip trailing newline: line.rstrip()
    #              print: "  1: line text"

    # TODO Part 2: wrap in try-except FileNotFoundError
    #              print: "Error: 'filename' not found."

    # TODO Part 3 (optional): restructure using try-except-else
    #              put the file reading in the else block
    pass


if __name__ == "__main__":
    print_file("sample.txt")
    print()
    print_file("missing.txt")
