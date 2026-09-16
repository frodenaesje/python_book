# file: snippet_returning_multiple_values.py
# Multiple return values are packed into a tuple.
# The caller can unpack them into separate variables.

def calculate_sum_and_average(a, b, c):
    total = a + b + c
    average = total / 3
    return total, average

sum1, avg1 = calculate_sum_and_average(3, 6, 9)
print("Sum:", sum1)      # 18
print("Average:", avg1)  # 6.0
