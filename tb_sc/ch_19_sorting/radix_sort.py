# file: radix_sort.py

# The radix sort works like this:
# 1. Sort the input array using counting sort based on the least
# significant digit (LSD)
# 2. Sort the input array again using counting sort based on 
# the next significant digit
# 3. Repeat the process until you have sorted the input array 
# based on the most significant digit (MSD)

def counting_sort_for_radix(input_array, place):
    count_array = [0] * 10
    output_array = [0] * len(input_array)

    # Count how many values fall into each digit bucket.
    for i in range(len(input_array)):
        index = (input_array[i] // place) % 10
        count_array[index] += 1

    # Convert counts into cumulative positions.
    for i in range(1, 10):
        count_array[i] += count_array[i - 1]

    # Build output from right to left to keep sorting stable.
    for i in range(len(input_array) - 1, -1, -1):
        index = (input_array[i] // place) % 10
        output_array[count_array[index] - 1] = input_array[i]
        count_array[index] -= 1

    # Copy back into input_array so the next digit pass reuses
    # this updated order.
    for i in range(len(input_array)):
        input_array[i] = output_array[i]
    print(f"After sorting on place {place}: {input_array}")


def radix_sort(input_array):
    max_num = max(input_array)

    place = 1
    # Repeat counting-sort passes from LSD to MSD.
    # place will be 1, then 10, then 100, etc., until we've processed all digits.
    while max_num // place > 0:
        # Important: input_array is updated in place, so each pass
        # builds on the result from the previous digit pass.
        counting_sort_for_radix(input_array, place)
        place *= 10

# Example usage
if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original array:", arr)
    radix_sort(arr)
    print("Radix sorted array:", arr) 
