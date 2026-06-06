# file: ap_regex_email.py
import re

# Note: complete email validation is very complicated.
# This pattern covers common cases, not absolutely all cases.
# The pattern reads as follows:
# [\w.+-]+ - one or more word chars, dots, pluses, or hyphens
# @         - a literal at sign
# [\w-]+    - one or more word chars or hyphens
# \.        - a literal dot
# [\w.-]+   - one or more word chars, dots, or hyphens
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")


def validate_email(email: str) -> bool:
    """Return True if the whole string is a valid email."""
    # fullmatch() requires the entire string to match.
    return bool(EMAIL.fullmatch(email))


def find_emails(text: str) -> list[str]:
    """Find all email addresses in the text."""
    # findall() returns every matching part inside the text.
    return EMAIL.findall(text)


def main() -> None:
    addresses = [
        "user@example.com",      # Valid
        "user.name@domain.co",   # Valid
        "user+tag@example.org",  # Valid - + is allowed locally
        "invalid-email",         # Invalid - missing @
        "user@domain",           # Invalid - missing top domain
        "user@domain.c",         # Valid - short top domain
        "user@example.com!!!",   # Invalid - extra trailing chars
    ]

    print("Validation:")
    for address in addresses:
        status = (
            "valid" if validate_email(address) else "invalid"
        )
        print(f"  {address!r:30} {status}")

    text = (
        "Contact us: support@example.com or sales@example.org"
    )
    print("\nFound in text:", find_emails(text))


if __name__ == "__main__":
    main()
