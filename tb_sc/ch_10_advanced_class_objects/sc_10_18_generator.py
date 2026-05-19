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
