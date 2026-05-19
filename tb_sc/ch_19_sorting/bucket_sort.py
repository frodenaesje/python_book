# file: bucket_sort.py
def bucket_sort(input_array):
    if len(input_array) == 0:
        return input_array

    # Create buckets and distribute the elements of the input array
    # into the buckets
    bucket_count = len(input_array)
    buckets = [[] for _ in range(bucket_count)]

    for num in input_array:
        index = int(num * bucket_count)
        buckets[index].append(num)

    # Sort each bucket and concatenate the sorted buckets
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))

    return sorted_array

# Example usage
if __name__ == "__main__":
    arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
    sorted_arr = bucket_sort(arr)
    print("Bucket sorted array:", sorted_arr)