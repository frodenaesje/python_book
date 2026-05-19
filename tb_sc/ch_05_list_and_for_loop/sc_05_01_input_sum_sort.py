# file: sc_05_01_input_sum_sort.py
# read 10 integers into a list, compute the sum and sort

integer_list = []
for i in range(10):
    number = int(input(f"Enter integer {i + 1} of 10: "))
    integer_list.append(number)

total = sum(integer_list)
print("The sum of the entered numbers is:", total)
integer_list.sort()
print("The numbers, sorted:", integer_list)
