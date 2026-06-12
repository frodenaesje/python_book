# file: ex_13_02_function_factories_start.py

def make_multiplier(n):
    """Return a function that multiplies its argument by n."""
    # TODO: return a lambda that takes one argument and returns argument * n
    pass


def make_adder(n):
    """Return a function that adds n to its argument."""
    # TODO: return a lambda that takes one argument and returns argument + n
    pass


def make_power(n):
    """Return a function that raises its argument to the power n."""
    # TODO: return a lambda that takes one argument and returns argument ** n
    pass


if __name__ == "__main__":
    double   = make_multiplier(2)
    triple   = make_multiplier(3)
    add_ten  = make_adder(10)
    square   = make_power(2)
    cube     = make_power(3)

    print(double(5))   # 10
    print(triple(4))   # 12
    print(add_ten(7))  # 17
    print(square(7))   # 49
    print(cube(3))     # 27

    numbers = [1, 2, 3, 4, 5]
    print(list(map(double, numbers)))  # [2, 4, 6, 8, 10]
    print(list(map(square, numbers)))  # [1, 4, 9, 16, 25]
    print(list(map(cube,   numbers)))  # [1, 8, 27, 64, 125]
