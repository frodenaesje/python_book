# file: sc_14_11_binary_search_recursive.py
# recursive binary search implementation
def binary_search(arr, target, low, high):
    # if the range is invalid, the target is not present
    if low > high:
        return -1  # Target not found

    mid = (low + high) // 2  # Find the middle index

    # Check if the target is present at mid
    if arr[mid] == target:
        return mid
    # If target is smaller than mid, search in the left half
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    # If target is larger than mid, search in the right half
    else:
        return binary_search(arr, target, mid + 1, high)
    
    # Example usage:
if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    result = binary_search(data, target, 0, len(data) - 1)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in array")