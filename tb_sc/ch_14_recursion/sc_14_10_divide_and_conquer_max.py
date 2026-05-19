# file: sc_14_10_divide_and_conquer_max.py
# Divide and conquer approach to find the maximum in a list
def max_divide_conquer(data):
    if len(data) == 1:
        return data[0]
    mid = len(data) // 2
    left_max = max_divide_conquer(data[:mid])
    right_max = max_divide_conquer(data[mid:])
    return left_max if left_max > right_max else right_max

nums = [3, 7, 2, 9, 5, 1, 8]
print(max_divide_conquer(nums))  # 9
