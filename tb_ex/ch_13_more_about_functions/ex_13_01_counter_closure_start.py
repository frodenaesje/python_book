# file: ex_13_01_counter_closure_start.py

def make_counter():
    """Return a closure that increments and returns a private counter."""
    # TODO: define a local variable count = 0
    # TODO: define an inner function increment() that:
    #         - increments count (use a mutable container: state = [0],
    #           then state[0] += 1, or use nonlocal count)
    #         - returns the new count
    # TODO: return the inner function (not a call to it)
    pass


def make_counter_from(start):
    """Return a closure that starts counting from start."""
    # TODO: same pattern as make_counter() but initialise with start
    pass


if __name__ == "__main__":
    counter1 = make_counter()
    counter2 = make_counter()
    print(counter1())  # 1
    print(counter1())  # 2
    print(counter1())  # 3
    print(counter2())  # 1   (independent)

    print()
    from_ten = make_counter_from(10)
    print(from_ten())  # 11
    print(from_ten())  # 12
