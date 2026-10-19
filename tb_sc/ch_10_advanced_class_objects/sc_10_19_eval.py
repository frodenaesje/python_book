# file: sc_10_19_eval.py
# eval() evaluates a Python expression given as a string.
# Use only trusted expressions: eval() can execute arbitrary code.

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f"({self._x}, {self._y})"        # readable

    def __repr__(self):
        return f"Point({self._x}, {self._y})"   # the state

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self._x == other._x \
        and self._y == other._y


print(eval("2 + 2"))       # 4
print(eval("[1, 2, 3]"))   # [1, 2, 3]

p = Point(3, 4)
print(str(p))             # (3, 4)
print(repr(p))            # Point(3, 4)

# repr(p) produces 'Point(3, 4)'; eval() creates a new Point from it.
# The name Point must be available where the expression is evaluated.
p2 = eval(repr(p))
print(p2)                 # (3, 4)
print(p == p2)            # True: equal coordinates (requires __eq__)
print(p is p2)            # False: two distinct objects

# A reconstructible repr() is a convention, not a requirement.
# An open file's repr() is informative, but cannot reconstruct the file object.
with open(__file__, "r", encoding="utf-8") as file:
    print(__file__)
    print(repr(file))

# __repr__() should be unambiguous and useful to a developer.
# The REPL uses __repr__(), rather than __str__(), to display objects.
