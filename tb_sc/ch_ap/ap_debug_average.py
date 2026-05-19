# file: sc_debug_average.py
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

data = [10, 20, 30, 40]
result = calculate_average(data)
print(result)