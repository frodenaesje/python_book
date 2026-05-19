# file: selection_sort.py

"""Simple selection sort implementation.

Provides a function `selection_sort` which sorts the list in-place and
also returns it for convenience. The algorithm repeatedly selects the
smallest remaining element and swaps it into the next position of the
sorted prefix.
"""

def selection_sort(array):
    """Sort *array* using selection sort and return it.

    The sort is performed in-place; the returned reference is the same
    list object.
    """
    n = len(array)
    for i in range(n):
        # assume the minimum is at position i
        min_idx = i
        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        # swap if we found a smaller element
        array[i], array[min_idx] = array[min_idx], array[i]
    return array


if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]
    print("Original:", data)
    selection_sort(data)
    print("Sorted:  ", data)
