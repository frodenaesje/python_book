# File: sc_11_04_make_own_exception.py

class InvalidPasswordError(Exception):
    """Raised when password doesn't meet requirements"""
    pass

def validate_password_basic(password):
    """Basic password validation with custom exception"""
    if len(password) < 8:
        raise InvalidPasswordError("Password must be at least 8 characters long")
    if password.isalpha():  # Only letters
        raise InvalidPasswordError("Password must contain numbers or symbols")   

# Test basic custom exception
try:
    validate_password_basic("abc")
except InvalidPasswordError as e:
    print(f"Password error: {e}")

print()


