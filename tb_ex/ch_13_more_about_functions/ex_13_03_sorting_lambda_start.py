# file: ex_13_03_sorting_lambda_start.py

students = [
    {"name": "Alice",   "gpa": 3.8, "age": 20},
    {"name": "Bob",     "gpa": 3.2, "age": 22},
    {"name": "Clara",   "gpa": 3.9, "age": 19},
    {"name": "David",   "gpa": 3.2, "age": 21},
    {"name": "Emma",    "gpa": 3.7, "age": 20},
]

def show(label, result):
    names = ", ".join(f"{s['name']} {s['gpa']}" for s in result)
    print(f"{label}:\n  {names}\n")

# TODO 1: Sort by GPA descending
#          Hint: sorted(..., key=lambda x: x["gpa"], reverse=True)
# show("By GPA descending", ...)

# TODO 2: Sort by name alphabetically
# show("By name", ...)

# TODO 3: Sort by age ascending, then by name for equal ages
#          Hint: key=lambda x: (x["age"], x["name"])
# show("By age then name", ...)

# TODO 4: Sort by GPA descending, then by name for equal GPAs
#          Hint: negate GPA to sort descending: key=lambda x: (-x["gpa"], x["name"])
# show("By GPA desc then name", ...)

# TODO 5: Sort by the length of the name
# show("By name length", ...)
