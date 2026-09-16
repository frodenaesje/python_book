# file: snippet_generics_and_type_aliases.py
# A type parameter is a placeholder for a type; a type alias gives a type a name.
# These generic definitions and type statements require Python 3.12+.

def first[T](items: list[T]) -> T:
    return items[0]

print(first([1, 2, 3]))        # 1
print(first(["a", "b", "c"]))  # a

type Vector = list[float]
type Matrix[T] = list[list[T]]

def scale(v: Vector, factor: float) -> Vector:
    return [x * factor for x in v]

def first_row(m: Matrix[int]) -> list[int]:
    return m[0]

print(scale([1.0, 2.0, 3.0], 2.0))  # [2.0, 4.0, 6.0]
print(first_row([[1, 2], [3, 4]]))   # [1, 2]
