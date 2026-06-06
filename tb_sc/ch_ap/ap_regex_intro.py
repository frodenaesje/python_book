# file: ap_regex_intro.py
import re

# Python already has simple ways to search text.
s = "fizzbuzz and the number 123 in a string"

# The in operator returns True if a substring is present.
if "123" in s:
    print("in: found 123")

# find() and rfind() return the position of the first
# and last occurrence, or -1 if no match is found.
start_pos = s.find("123")
print("find():", start_pos)

last_pos = s.rfind("123")
print("rfind():", last_pos)

#### Start plain regex examples ###
s = "fizz123buzz"

# re.search() returns a match object on success,
# otherwise None.
# The regex "123" reads as: the literal text 123.
match = re.search("123", s)

if match:
    print("Found a match:", match.group())
else:
    print("No match")

# Shows the use of search() and findall().
# Note the raw string: an r before the pattern string.
# The code should have an else branch, but it is omitted
# here to save space.

# Matches three consecutive digits.
s = "fizz123buzz"
# [0-9] means one digit from 0 to 9.
# [0-9][0-9][0-9] reads as: three digits in a row.
match = re.search(r"[0-9][0-9][0-9]", s)
if match:
    # Output: Found a match: 123
    print("Found a match:", match.group())

# Same as above, but with the metasequence \d.
# \d means one digit.
# \d\d\d reads as: three digits in a row.
match = re.search(r"\d\d\d", s)
if match:
    # Output: Found a match: 123
    print("Found a match:", match.group())

# Matches any character between '1' and '3'.
s = "fizz1a3buzz"
# 1.3 reads as: '1', then any character (.), then '3'.
match = re.search(r"1.3", s)
if match:
    # Output: Found a match: 1a3
    print("Found a match:", match.group())

# Matches a period.
# Since . is a metacharacter, we must escape it with \.
s = "fizz.123buzz"
# \. reads as: a literal period.
match = re.search(r"\.", s)
if match:
    # Output: Found a match: .
    print("Found a match:", match.group())

# Demonstrates the use of anchors.
# Matches the start of the string.
s = "fizz123buzz"
# ^fizz reads as: the string must start with "fizz".
match = re.search(r"^fizz", s)
if match:
    # Output: Found a match: fizz
    print("Found a match:", match.group())

# Matches the end of the string.
s = "fizz123buzz"
# buzz$ reads as: the string must end with "buzz".
match = re.search(r"buzz$", s)
if match:
    # Output: Found a match: buzz
    print("Found a match:", match.group())

# Use findall() to find all runs of three digits.
s = "abc123def456ghi789"
# \d\d\d reads as: three digits in a row.
matches = re.findall(r"\d\d\d", s)
print(
    "All matches with findall:",
    matches,
)  # Output: ['123', '456', '789']

# Use findall() to find all occurrences of 'f' or 'b'.
s = "fizzbuzz"
# [fb] reads as: one character that is either 'f' or 'b'.
matches = re.findall(r"[fb]", s)
print(
    "All matches with findall:",
    matches,
)  # Output: ['f', 'b']

# Use findall() to find all occurrences of a 1?3 pattern.
s = "fizz1a3buzz1b3"
# 1.3 reads as: '1', any character, then '3'.
matches = re.findall(r"1.3", s)
print(
    "All matches with findall:",
    matches,
)  # Output: ['1a3', '1b3']

# fullmatch() versus findall():
# - findall() finds all partial matches in a larger text.
# - fullmatch() requires the WHOLE string to match.
s = "abc123def456"
# \d{3} reads as: exactly three digits.
print(
    "findall in larger text:",
    re.findall(r"\d{3}", s),
)  # ['123', '456']

s = "123"
# Here the whole string must be exactly three digits.
print(
    "fullmatch on '123':",
    bool(re.fullmatch(r"\d{3}", s)),
)  # True

s = "abc123"
# Here fullmatch fails because the whole string is not
# just three digits.
print(
    "fullmatch on 'abc123':",
    bool(re.fullmatch(r"\d{3}", s)),
)  # False

# Example using {n} to match exactly n occurrences.
s = "aaaabbbbcccc"
# a{4} reads as: exactly four 'a' characters in a row.
matches = re.findall(r"a{4}", s)
print("All matches with {n}:", matches)  # Output: ['aaaa']

# Example using {n,} to match at least n occurrences.
# b{2,} reads as: at least two 'b' characters in a row.
matches = re.findall(r"b{2,}", s)
print("All matches with {n,}:", matches)  # Output: ['bbbb']

# Example using {n,m} to match between n and m occurrences.
# c{2,3} reads as: two or three 'c' characters in a row.
matches = re.findall(r"c{2,3}", s)
print("All matches with {n,m}:", matches)
