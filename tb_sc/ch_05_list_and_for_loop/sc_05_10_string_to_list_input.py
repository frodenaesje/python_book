# file: sc_05_10_string_to_list_input.py
list1 = []
print("Enter 3 numbers, one per line")
for i in range(3):
    number = int(input(f"Number {i+1}: "))
    list1.append(number)
print("The numbers you entered are:", list1)

s = input("Enter three numbers on one line, separated by spaces:")
list2 = s.split()

# write code that converts strings in list2 to integers
for i in range(len(list2)):
    list2[i] = int(list2[i])
print("The numbers you entered are:", list2)

# alternatively we can use list comprehension
list3 = [int(x) for x in s.split()]
print("The numbers you entered are:", list3)
