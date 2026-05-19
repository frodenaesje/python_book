# file: ap_regex_hex_color.py
import re

# The pattern reads as follows:
# #            - a literal hash sign
# [0-9A-Fa-f] - one hexadecimal character
#               0-9 are digits, A-F and a-f are hex letters
# {6}          - exactly six such characters
# The whole regex therefore matches codes like #FF5733.
HEX_COLOR = re.compile(r"#[0-9A-Fa-f]{6}")


def is_valid_hex_color(s: str) -> bool:
    """Return True for a valid hex color string."""
    # fullmatch() rejects extra text before or after.
    return bool(HEX_COLOR.fullmatch(s))


def find_hex_colors(text: str) -> list[str]:
    """Find and return all hex color codes in the text."""
    # findall() looks for all matching substrings in the text.
    return HEX_COLOR.findall(text)


def main() -> None:
    # Validation of single strings
    candidates = [
        "#FF5733",   # Valid - pure orange
        "#abc123",   # Valid - mixed case
        "#FFFFFF",   # Valid - white
        "#000000",   # Valid - black
        "#GG1234",   # Invalid - G is not hex
        "#FF573",    # Invalid - only five chars
        "#FF57333",  # Invalid - seven chars
        "FF5733",    # Invalid - missing #
        "#ff5733!",  # Invalid - extra char
    ]

    print("Validation:")
    for c in candidates:
        status = (
            "valid" if is_valid_hex_color(c) else "invalid"
        )
        print(f"  {c!r:15} {status}")

    # Find all color codes in a CSS-like text
    css = """
        body { background-color: #FFFFFF; }
        body { color: #333333; }
        h1 { color: #FF5733; }
        .highlight { background: #FFD700; }
        .highlight { border: 1px solid #CCCCCC; }
        .invalid { color: #GG1234; }
    """

    print("\nColor codes found in CSS text:")
    print(find_hex_colors(css))


if __name__ == "__main__":
    main()
