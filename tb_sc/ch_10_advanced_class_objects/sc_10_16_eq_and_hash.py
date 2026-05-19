# file: sc_10_16_eq_and_hash.py
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

# Step 1: no override, using object defaults.
p1 = Point(3, 4)
p2 = Point(3, 4)
print(p1 == p2)    # False: object compares identity, not value.
print(hash(p1))    # OK: object __hash__() is based on id().

# Step 2: override __eq__(), but forget __hash__().
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y

p1 = Point(3, 4)
p2 = Point(3, 4)
print(p1 == p2)    # True: now we compare value.
print(hash(p1))    # TypeError: unhashable type: 'Point'
                   # Python automatically set __hash__ to None.

# Step 3: override both.
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y

    def __hash__(self):
        return hash((self._x, self._y))   # Tuples are hashable.

p1 = Point(3, 4)
p2 = Point(3, 4)
print(p1 == p2)              # True
print(hash(p1) == hash(p2))  # True: equal objects, same hash.

lookup = {p1: "near-origin"}
print(lookup[p2])            # Works because the hashes are equal.
