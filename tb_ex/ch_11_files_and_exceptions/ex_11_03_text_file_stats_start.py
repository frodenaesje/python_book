# file: ex_11_03_text_file_statstext_file_stats_start.py

def file_stats(filename: str) -> dict[str, int]:
    """Return line, word, character and unique word counts for a text file.

    Returns:
        dict with keys: lines, words, chars, unique_words
    Raises:
        FileNotFoundError if the file does not exist
    """
    # TODO: open the file with open() and with
    # TODO: read all lines
    # TODO: count lines, words, chars and unique words
    #       Hint: unique words - use a set, convert each word to lowercase
    # TODO: return a dict[str, int] with the four counts
    pass


if __name__ == "__main__":
    filename = "sample.txt"

    # TODO: call file_stats() inside a try-except block
    #       catch FileNotFoundError and print a helpful message

    # TODO: print the statistics

    # TODO: write the statistics to stats.txt
    #       Example: "File: sample.txt\nLines: 4\n..."
