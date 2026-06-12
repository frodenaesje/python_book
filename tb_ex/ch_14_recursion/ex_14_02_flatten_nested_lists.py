# file: ex_14_02_flatten_nested_lists.py

def flatten(nested_list):
    """Recursively flatten a nested list into a single flat list."""
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


def flatten_gen(nested_list):
    """Generator version using yield from."""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_gen(item)
        else:
            yield item


if __name__ == "__main__":
    print(flatten([1, [2, 3], 4]))
    print(flatten([1, [2, [3, 4]], 5]))
    print(flatten([1, 2, 3]))
    print(flatten([1, [2, [3, [4, [5]]]]]))
    print(flatten([1, [2, 3], 4, [5, [12, 13], 6], [2, 7], 8]))

    print()
    print("Generator version:")
    print(list(flatten_gen([1, [2, [3, 4]], 5])))
