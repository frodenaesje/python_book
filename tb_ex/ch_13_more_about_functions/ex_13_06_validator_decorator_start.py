# file: ex_13_06_validator_decorator_start.py

def validate_positive(func):
    """Decorator that raises ValueError if any numeric argument is <= 0."""
    def wrapper(*args, **kwargs):
        # TODO: loop over args
        #       if isinstance(arg, (int, float)) and arg <= 0:
        #           raise ValueError("All arguments must be positive.")
        # TODO: call and return func(*args, **kwargs)
        pass
    return wrapper


# TODO: Apply @validate_positive to both functions below

def rectangle_area(width, height):
    return width * height


def bmi(weight_kg, height_m):
    return round(weight_kg / height_m ** 2, 2)


# Extension: decorator factory
def validate(condition, message):
    """Decorator factory: raises ValueError if condition(arg) is False for any numeric arg."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # TODO: loop over args, check isinstance and condition
            # TODO: raise ValueError(message) if condition fails
            # TODO: call and return func(*args, **kwargs)
            pass
        return wrapper
    return decorator


@validate(lambda x: x > 0, "All arguments must be positive.")
def area(width, height):
    return width * height


if __name__ == "__main__":
    print(rectangle_area(5, 3))

    try:
        print(rectangle_area(-2, 3))
    except ValueError as e:
        print(f"ValueError: {e}")

    print(bmi(70, 1.75))

    try:
        print(bmi(70, 0))
    except ValueError as e:
        print(f"ValueError: {e}")

    print()
    print(area(4, 5))
    try:
        print(area(-1, 5))
    except ValueError as e:
        print(f"ValueError: {e}")
