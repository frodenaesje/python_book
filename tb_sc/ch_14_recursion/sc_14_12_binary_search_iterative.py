# file: sc_14_12_binary_search_iterative.py
# iterative binary search implementation
def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Find the middle index

        # Check if the target is present at mid
        if arr[mid] == target:
            return mid
        # If target is smaller than mid, search in the left half
        elif arr[mid] > target:
            high = mid - 1
        # If target is larger than mid, search in the right half
        else:
            low = mid + 1

    return -1  # Target not found

# Example usage:
if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    result = binary_search_iterative(data, target)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in array")