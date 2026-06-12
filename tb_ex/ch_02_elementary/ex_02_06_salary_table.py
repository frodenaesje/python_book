# file: ex_02_06_salary_table.py

# --- Part 1: hardcoded field widths ---

name1 = input("Enter name 1: ")
age1 = int(input("Enter age 1: "))
salary1 = float(input("Enter monthly salary 1: "))

name2 = input("Enter name 2: ")
age2 = int(input("Enter age 2: "))
salary2 = float(input("Enter monthly salary 2: "))

name3 = input("Enter name 3: ")
age3 = int(input("Enter age 3: "))
salary3 = float(input("Enter monthly salary 3: "))

print()
print(f"{'Name':20}{'Age':6}{'Monthly salary':18}")
print(f"{name1:20}{age1:6}{salary1:18,.2f}")
print(f"{name2:20}{age2:6}{salary2:18,.2f}")
print(f"{name3:20}{age3:6}{salary3:18,.2f}")


# --- Part 2: variables as format specifiers ---

name_width = 20
age_width = 6
salary_width = 18

print()
print(f"{'Name':{name_width}}{'Age':{age_width}}{'Monthly salary':{salary_width}}")
print(f"{name1:{name_width}}{age1:{age_width}}{salary1:{salary_width},.2f}")
print(f"{name2:{name_width}}{age2:{age_width}}{salary2:{salary_width},.2f}")
print(f"{name3:{name_width}}{age3:{age_width}}{salary3:{salary_width},.2f}")
