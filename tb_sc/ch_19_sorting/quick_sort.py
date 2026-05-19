# File: quicksort.py
# Classic recursive quicksort implementation
# Uses first element as pivot

def quick_sort(arr):
    """
    Sort array using quicksort algorithm.
    Base case: arrays with 0 or 1 element are already sorted.
    Recursive case: partition around pivot and sort both partitions.
    """
    if len(arr) <= 1:
        return arr
    
    # Choose first element as pivot
    pivot = arr[0]
    
    # Partition into three parts:
    # - left: elements less than pivot
    # - middle: pivot itself
    # - right: elements greater than or equal to pivot (except the pivot)
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    
    # Recursively sort left and right, then combine
    return quick_sort(left) + [pivot] + quick_sort(right)

def main():
    print("=" * 60)
    print("Quicksort Implementation")
    print("=" * 60)
    
    # Test with unsorted array of 20 numbers
    arr = [64, 34, 25, 12, 22, 11, 90, 50, 45, 75, 33, 88, 19, 42, 99, 15, 67, 53, 27, 71]
    print(f"\nOriginal array: {arr}")
    sorted_arr = quick_sort(arr)
    print(f"Sorted array:   {sorted_arr}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
