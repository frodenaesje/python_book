# file: tim_insertion_sort.py
# Difference from ordinary insertion sort:
# This version sorts only a subarray [left, right], while the
# ordinary version always sorts the full array [0, len(array) - 1].
def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    for i in range(left + 1, right + 1):
        key = array[i]
        j = i - 1

        while j >= left and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array