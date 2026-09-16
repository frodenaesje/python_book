# sc_06_06_mutability.py
def modify_int(x):
    print("Before:", x, "| id:", id(x))
    x = x + 1
    print("After:", x, "| id:", id(x))

def modify_str(s):
    print("Before:", s, "| id:", id(s))
    s = s + "!"
    print("After:", s, "| id:", id(s))

x = 10
modify_int(x)
print("Outside:", x, "| id:", id(x))

s = "Hello"
modify_str(s)
print("Outside:", s, "| id:", id(s))

def modify_list(lst):
    print("Before:", lst, "| id:", id(lst))
    lst.append(4)
    print("After:", lst, "| id:", id(lst))

lst = [1, 2, 3]
modify_list(lst)
print("Outside:", lst, "| id:", id(lst))
