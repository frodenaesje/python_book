# file: ex_14_02_flatten_nested_lists.py

def flatten(nested_list):
    """Recursively flatten a nested list into a single flat list."""
    flat_list = []
    for item in nested_list:
        # TODO: if item is a list, call flatten recursively and extend flat_list
        #       Hint: flat_list.extend(flatten(item))
        # TODO: if item is not a list, append it directly
        pass
    return flat_list


if __name__ == "__main__":
    print(flatten([1, [2, 3], 4]))               # [1, 2, 3, 4]
    print(flatten([1, [2, [3, 4]], 5]))           # [1, 2, 3, 4, 5]
    print(flatten([1, 2, 3]))                     # [1, 2, 3]
    print(flatten([1, [2, [3, [4, [5]]]]]))       # [1, 2, 3, 4, 5]
    print(flatten([1, [2, 3], 4, [5, [12, 13], 6], [2, 7], 8]))
    # [1, 2, 3, 4, 5, 12, 13, 6, 2, 7, 8]
