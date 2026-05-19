# file: sc_09_01_calculate.py

def calculate(a, b, operation):
    """Perform a simple arithmetic operation on two numbers.

    Args:
        a: first number
        b: second number
        operation: string, "add" for addition or "sub" for
            subtraction

    Returns:
        The result as a number, or None if the operation is unknown.
    """
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    else:
        return None
