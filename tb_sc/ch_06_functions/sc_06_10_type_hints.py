# sc_06_10_type_hints.py

def add_two_numbers(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return "Hello, " + name

def area(width: float, height: float) -> float:
    return width * height

def is_even(number: int) -> bool:
    return number % 2 == 0

def print_message(message: str) -> None:
    print(message)

count: int = 10
name: str = "Alice"
price: float = 19.95
active: bool = True

print(add_two_numbers("Hello, ", "Python"))

def total(numbers: list[int]) -> int:
    return sum(numbers)

def average(values: list[float]) -> float:
    return sum(values) / len(values)

def print_names(names: list[str]) -> None:
    for name in names:
        print(name)

print(total([1, 2, 3]))             # 6
print(average([1.0, 2.0, 3.0]))     # 2.0

def find_name(names: list[str], search_name: str) -> str | None:
    for name in names:
        if name == search_name:
            return name
    return None

result = find_name(["Alice", "Bob", "Charlie"], "Bob")

if result is not None:
    print("Found:", result)
else:
    print("Name not found")

def format_value(value: int | float) -> str:
    return f"{value:.2f}"

print(format_value(3))    # 3.00
print(format_value(3.5))  # 3.50

def display_id(user_id: int | str) -> str:
    return f"User ID: {user_id}"
