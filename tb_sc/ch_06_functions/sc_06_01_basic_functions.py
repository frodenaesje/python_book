# file: sc_06_01_basic_functions.py

# define the function
def add_two_numbers(a, b):
    return a + b

# use it
result1 = add_two_numbers(1, 2)   # result1 = 3
result2 = add_two_numbers(3, 4)   # result2 = 7
print(result1) # 3
print(result2) # 7

# More useful: grade calculator
def calc_grade(score):
    """Returns a letter grade based on score (0-100).

    score: integer between 0 and 100
    Returns: string - one of "A", "B", "C", "D", "E", "F"
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"

achieved_score1 = 85
achieved_score2 = 92
grade1 = calc_grade(achieved_score1)
grade2 = calc_grade(achieved_score2)
print(grade1)  # B
print(grade2)  # A

# Multiple return values are packed into a tuple.
# The caller can unpack them into separate variables.

def calculate_sum_and_average(a, b, c):
    total = a + b + c
    average = total / 3
    return total, average

sum1, avg1 = calculate_sum_and_average(3, 6, 9)
print("Sum:", sum1)      # 18
print("Average:", avg1)  # 6.0
