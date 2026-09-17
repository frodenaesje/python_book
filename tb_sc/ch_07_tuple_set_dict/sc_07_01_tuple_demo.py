# file: sc_07_01_tuple_demo.py

# creating tuples in different ways
tu1 = (1, 2, 3)           # regular tuple with parentheses
tu2 = 4, 5, 6             # tuple without parentheses - also valid
tu3 = tuple([7, 8, 9])    # from list using the constructor
tu4 = ()                  # empty tuple
tu5 = (42,)               # single-value tuple - note the comma!

print("tu1:", tu1)
print("tu2:", tu2)
print("tu3:", tu3)
print("tu4:", tu4)
print("tu5:", tu5)

# immutable - cannot be changed
a_list  = [1, 2, 3]
a_tuple = (1, 2, 3)
a_list[0]  = 99  # OK
# a_tuple[0] = 99  # Uncomment to see TypeError: tuples are immutable

# creating from generator and list
tu = tuple(x for x in range(5)) # from generator
print(tu)

tu = tuple([x * 2 for x in range(5)]) # from list comprehension
print(tu)
# drop the brackets..
tu = tuple(x * 2 for x in range(5)) # same result, no throwaway list
print(tu)


tu = tuple(map(str, range(3))) # from map-function


# unpacking
a, b, c = tu1
print("Unpacked tu1:", a, b, c)

# swapping values with unpacking
x, y = 10, 20
x, y = y, x
print("Swapped x and y:", x, y)

# extended unpacking with *
tu6 = (1, 2, 3, 4, 5)
first, *middle, last = tu6
print("First:", first)
print("Middle:", middle)
print("Last:", last)