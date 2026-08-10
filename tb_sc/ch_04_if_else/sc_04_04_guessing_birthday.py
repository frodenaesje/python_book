# file: sc_04_04_guessing_birthday.py
"""
Task:
Write a program that guesses the user's birthday (day of the month, 1-31) by presenting 5 tables of numbers.
The user answers whether his/her day appears in each table, and the program calculates the day based on the answers.
Topic: lists, for loop, logic
"""
def get_y_n():
    while True:
        answer = input("Is your birthday in this table? (y/n): ").strip().lower()
        if answer in ('y', 'n'):
            return answer
        print("Invalid answer. Please answer with 'y' or 'n'.")


print("Guess your birthday!")
print("Answer 'y' or 'n' to whether your day appears in the table.")

table1 = [n for n in range(1, 32) if n & 1]
table2 = [n for n in range(1, 32) if n & 2]
table3 = [n for n in range(1, 32) if n & 4]
table4 = [n for n in range(1, 32) if n & 8]
table5 = [n for n in range(1, 32) if n & 16]

day = 0
print("\nTable 1:", table1)
if get_y_n() == 'y':
    day += 1
print("\nTable 2:", table2)
if get_y_n() == 'y':
    day += 2
print("\nTable 3:", table3)
if get_y_n() == 'y':
    day += 4
print("\nTable 4:", table4)
if get_y_n() == 'y':
    day += 8
print("\nTable 5:", table5)
if get_y_n() == 'y':
    day += 16

print(f"\nYou were born on day {day} of the month!")

# Why does this code work?
#
# Every number from 1 to 31 can be written as a unique sum of the
# powers of two: 1, 2, 4, 8 and 16. This is exactly the number's
# binary representation. For example:
#
#     19 = 16 + 2 + 1  =  10011 in binary
#
# Table k contains precisely the numbers that have bit k set:
# table1 holds the numbers where the 1-bit is set (n & 1), table2
# the numbers where the 2-bit is set (n & 2), and so on. So 19
# appears in table 1, table 2 and table 5 — and in no others.
#
# When the user tells us which tables contain their day, they are
# in effect revealing the day's bit pattern, one bit per answer.
# We rebuild the number by adding the table's power of two for
# every "yes". Five yes/no answers give 2**5 = 32 possible
# combinations, which is exactly enough to distinguish the days
# 1 to 31 (the pattern of five "no" answers would mean 0).
#
# The magic trick is therefore no magic at all: we are simply
# asking the user to spell out their birthday in binary.