# file: snippet_map_filter.py
# map() applies a function to each element; filter() keeps matching elements.
# Both return lazy iterators; list() collects their results.

numbers = [1, 2, 3]
squares = list(map(lambda x: x**2, numbers))
print(squares)

squares = [x**2 for x in numbers]
print(squares)

numbers = [1, 2, 3, 4]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
