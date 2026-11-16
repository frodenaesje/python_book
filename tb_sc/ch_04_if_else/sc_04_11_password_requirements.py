# file: sc_04_11_password_requirements.py
MIN_LENGTH = 12

password = input("Choose a password: ")
length = len(password)

if not password:
    print("No password entered.")
elif length < MIN_LENGTH:
    print(f"Too short: {length} characters, at least {MIN_LENGTH} required.")
elif password.count(" ") > 0:
    print("Spaces are not allowed in this example.")
elif password.lower() == password:
    print("No uppercase letters - add at least one.")
elif password.upper() == password:
    print("No lowercase letters - add at least one.")
elif password.isalnum():
    print("Add at least one special character.")
else:
    print(f"Password meets the requirements ({length} characters).")
