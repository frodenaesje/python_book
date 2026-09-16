# file sc_06_02_return_none.py
# Functions without return automatically return None
def say_hello(name):
    print(f'Hello, {name}!')

result = say_hello('Anna')   # Hello, Anna!
print(result)                # None
