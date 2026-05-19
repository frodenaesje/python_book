# file: sc_06_01_basic_functions.py

# define the function
def add_two_numbers(a, b):
    return a + b

# use it
svar1 = add_two_numbers(1,2)
svar2 = add_two_numbers(3,4)
print(svar1)
print(svar2)

def calc_grade(score):
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
    
# use the function
score1 = 85
grade1 = calc_grade(score1)
print(grade1)

score2 = 92
grade2 = calc_grade(score2)
print(grade2)

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
