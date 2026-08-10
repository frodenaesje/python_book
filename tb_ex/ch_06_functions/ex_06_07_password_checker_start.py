# file: ex_06_07_password_checker_start.py

# TODO: Write a function is_good_password(password: str) -> bool
#       Returns True if the password meets ALL of these requirements:
#         - At least 8 characters long
#         - Contains at least one uppercase letter
#         - Contains at least one lowercase letter
#         - Contains at least one digit
#
#       Hint: check each condition with a loop or any():
#         has_upper = any(c.isupper() for c in password)

if __name__ == "__main__":
    password = input("Enter a password: ")

    # TODO: Check each requirement separately and print which ones fail
    #       Example:
    #         "Too short (minimum 8 characters)."
    #         "Missing uppercase letter."
    #         "Missing lowercase letter."
    #         "Missing digit."

    # TODO: Print final verdict
    #       "Password is good!"  or  "Password is not good."
    pass
