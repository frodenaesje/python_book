# file: sc_02_12_input_patterns.py

# strip whitespace and convert to lowercase
answer = input("Type yes or no: ").strip().lower()
print(f"You typed: {answer}")

# validation against a list of valid answers
choice = input("Choose [yes/no] ").strip().lower()
if choice not in ["yes", "no"]:
    print("Invalid choice.")


# Repeat choice until it is valid
answer = ""
while answer not in ['a', 'b', 'c']:
    answer = input("Choose option [a/b/c]: ").strip().lower()
print(f"You chose option {answer}")

# Input with type conversion and error handling
while True:
    try:
        number = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Invalid input, try again.")

print(f"You entered the number {number}")

# input with default value
def ask(prompt, default="yes"):
    answer = input(f"{prompt} ({default}): ").strip().lower()
    return answer if answer else default

result = ask("Do you want to continue?")
print(f"You answered: {result}")
