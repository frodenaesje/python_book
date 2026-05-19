# file: insertion_sort.py
# Textbook insertion sort (sorts the whole array)

def insertion_sort(array):
    # Start with array[0] as the sorted part.
    # Then grow the sorted prefix from left to right.
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array


if __name__ == "__main__":
    values = [42, 7, 19, 3, 25, 1, 9]
    print("Original:", values)
    insertion_sort(values)
    print("Sorted:", values)
