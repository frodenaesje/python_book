# file: ex_02_17_fstring_challenges_start.py

# --- Exercise 1 - Decimal places ---
price = 19.9876
# TODO: use an f-string to print "Price: 19.99" - do not use round()


# --- Exercise 2 - Field width and alignment ---
product = "Coffee"
price = 42.5
# TODO: use an f-string to print "Coffee         42.50"
#       product field: 12 characters, price field: 8 characters, right-aligned, 2 decimals


# --- Exercise 3 - Thousands separator ---
population = 5834127
# TODO: print "Population: 5,834,127" using the , format specifier
# TODO: then print the same number using _ as the separator instead


# --- Exercise 4 - Percentage ---
correct = 17
total = 20
# TODO: print "Score: 85.0%" using the percentage format specifier (%)
#       do not multiply by 100 yourself


# --- Exercise 5 - A small table ---
name1 = "Alice"
score1 = 87.456
name2 = "Christopher"
score2 = 91.2
# TODO: print a header line "Name              Score"
# TODO: print name1/score1 and name2/score2 so the columns line up,
#       using field width and alignment (not manually typed spaces)


# --- Exercise 6 - User-controlled decimal places ---
# TODO: ask the user for a number (value) and a number of decimal places (decimals)
# TODO: print "Result: ..." using a format specifier built from the decimals variable
#       hint: f"{value:.{decimals}f}"


# --- Exercise 7 - Singular or plural? ---
apples = 1
# TODO: use one f-string with a conditional expression to print:
#       "There is 1 apple."   when apples == 1
#       "There are 5 apples." when apples == 5
#       (change the value of apples and re-run to check both cases)


# --- Exercise 8 - Dynamic receipt ---
# TODO: ask the user for: product, quantity, price per item, decimal places
# TODO: compute the total cost
# TODO: print a single f-string such as:
#       "3 notebooks cost 37.50 in total."
#       "1 notebook costs 12.50 in total."
#       using conditional expressions for the plural/verb form,
#       and the user's chosen decimal places in the format specifier
