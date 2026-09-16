# file: snippet_keyword_arguments.py
# Keyword arguments pass values by parameter name.
# They can be supplied in a different order from the parameters.

def create_greeting(name, greeting):
    return f"{greeting}, {name}!"

msg1 = create_greeting(name="Ola", greeting="Hello")
msg2 = create_greeting(greeting="Hi", name="Kari")
print(msg1)  # Hello, Ola!
print(msg2)  # Hi, Kari!
