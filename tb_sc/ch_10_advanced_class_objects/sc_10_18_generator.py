# file: sc_10_18_generator.py
def count_up(start, stop):
    current = start
    while current < stop:
        yield current
        current += 1

for number in count_up(1, 5):
    print(number, end=" ")   # 1 2 3 4

gen = count_up(1, 5)
print(type(gen))     # <class 'generator'>
print(next(gen))     # 1
print(next(gen))     # 2

gen = count_up(1, 5)
print(list(gen))  # [1, 2, 3, 4]
print(list(gen))  # []  - exhausted

squares = (x**2 for x in range(5))   # generator expression
print(list(squares))  # [0, 1, 4, 9, 16]

# List comprehension - creates the entire list in memory
store = [x**2 for x in range(1_000_000)]
print(type(store))  # <class 'list'>

# Generator expression - computes one value at a time
store = (x**2 for x in range(1_000_000))
print(type(store))  # <class 'generator'>
print(next(store))  # 0
print(next(store))  # 1
