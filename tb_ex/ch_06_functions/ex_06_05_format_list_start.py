# file: ex_06_05_format_list_start.py

# TODO: Write a function format_list(items: list) -> str
#       Returns a human-readable string from a list of items:
#         []              -> ""
#         ["apple"]       -> "apple"
#         ["apple", "banana"] -> "apple and banana"
#         ["apple", "banana", "cherry"] -> "apple, banana and cherry"
#
#       Hint for the general case (3+ items):
#         ", ".join(items[:-1]) + " and " + items[-1]


if __name__ == "__main__":
    # Test your function with these cases:
    print(format_list([]))
    print(format_list(["apple"]))
    print(format_list(["apple", "banana"]))
    print(format_list(["apple", "banana", "cherry"]))
    print(format_list(["a", "b", "c", "d"]))

    # TODO (extension): Add a parameter conjunction="and" with a default value
    #   so the caller can write format_list(items, "or")
