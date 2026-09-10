# sc_06_10_type_hints.py
# Basic type hints: parameter: type  ->  return_type

def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return 'Hello, ' + name

def is_even(n: int) -> bool:
    return n % 2 == 0

def print_msg(msg: str) -> None:  # no return value
    print(msg)

# Type hints on variables:
count: int   = 10
name: str    = 'Alice'
price: float = 19.95

# Lists:
def total(numbers: list[int]) -> int:
    return sum(numbers)

# Optional return (str or None):
def find(lst: list[str], key: str) -> str | None:
    for item in lst:
        if item == key: return item
    return None