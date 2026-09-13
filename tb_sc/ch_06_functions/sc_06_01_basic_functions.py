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
def calc_grade(score : int) -> str:
    """Returns a letter grade based on score (0-100).

    score:   integer between 0 and 100
    Returns: string - one of "A", "B", "C", "D", "E", "F"
    """
    if score >= 90:   return 'A'
    elif score >= 80: return 'B'
    elif score >= 60: return 'C'
    elif score >= 50: return 'D'
    elif score >= 40: return 'E'
    else:             return 'F'

achieved_score1 = 85
achieved_score2 = 92
grade1 = calc_grade(achieved_score1)   # 'B'
grade2 = calc_grade(achieved_score2)   # 'A'
print(grade1)
print(grade2)
print(calc_grade.__doc__) # a function is also an object...

def modify_int(x):
    print("Inside function (before change):", x, "| id:", id(x))
    x = x + 1
    print("Inside function (after change):", x, "| id:", id(x))

def modify_str(s):
    print("Inside function (before change):", s, "| id:", id(s))
    s = s + "!"
    print("Inside function (after change):", s, "| id:", id(s))

def modify_list(lst):
    print("Inside function (before change):", lst, "| id:", id(lst))
    lst.append(4)
    print("Inside function (after change):", lst, "| id:", id(lst))

# Test the functions
x = 10
modify_int(x)
print("Outside function:", x, "| id:", id(x))

s = "Hello"
modify_str(s)
print("Outside function:", s, "| id:", id(s))

lst = [1, 2, 3]
modify_list(lst)
print("Outside function:", lst, "| id:", id(lst))
