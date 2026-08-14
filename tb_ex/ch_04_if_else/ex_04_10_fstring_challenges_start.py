# file: ex_04_10_fstring_challenges_start.py
#
# Ten small f-string challenges. For each one, write a single print
# so the output matches the target in the comment. Use only
# f-strings, arithmetic, the ternary expression (a if cond else b),
# and string methods - no lists, loops or functions.

# --- 1. Basic interpolation ---
name = "John"
age = 30
# TODO: print  ->  John is 30 years old.

# --- 2. Two decimals ---
amount = 837.5
# TODO: print  ->  Amount: 837.50

# --- 3. Right alignment (width 8) ---
a = 5
b = 42
c = 1370
# TODO: print each on its own line, right-aligned in width 8

# --- 4. Percent (one decimal) ---
correct = 27
total = 40
# TODO: print  ->  Score: 67.5%   (let the format spec add the %)

# --- 5. Sign and thousands separator ---
balance = 2500.0
# TODO: print  ->  +2,500.00

# --- 6. A different thousands separator ---
population = 5391369
# TODO: print  ->  5 391 369   (space, not comma - use replace())

# --- 7. Method calls inside the field ---
first = "john"
last = "english"
# TODO: print  ->  John ENGLISH

# --- 8. Ternary: even or odd ---
number = 7
# TODO: print  ->  7 is odd

# --- 9. Ternary: plural ending ---
count = 1
# TODO: print  ->  You have 1 message   (no trailing s for exactly one)

# --- 10. Put it together ---
quantity = 3
price = 49.9
# TODO: print  ->  3 items cost 149.70 in total
