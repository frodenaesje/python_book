# file: sc_07_09_count_python_keywords.py

from collections import Counter

# Python also provides its current keyword list in the keyword module:
# import keyword
# KEYWORDS = set(keyword.kwlist)
#

KEYWORDS = {
    "False", "None", "True", "and", "as", "assert",
    "async", "await", "break", "class", "continue", "def",
    "del", "elif", "else", "except", "finally", "for",
    "from", "global", "if", "import", "in", "is",
    "lambda", "nonlocal", "not", "or", "pass", "raise",
    "return", "try", "while", "with", "yield"
}

print("Enter code, finish with an empty line:")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

words = " ".join(lines).split()


# Novice version: count occurrences manually with a dictionary.
keyword_counts = {}

for word in words:
    if word in KEYWORDS:
        keyword_counts[word] = keyword_counts.get(word, 0) + 1

print("\nManual counting:")
for keyword, count in sorted(keyword_counts.items()):
    print(f"{keyword:10} {count}")


# More Pythonic: filter the words with a generator expression
# and let Counter perform the counting.
keyword_counts = Counter(
    word for word in words if word in KEYWORDS
)

print("\nUsing Counter:")
for keyword, count in sorted(keyword_counts.items()):
    print(f"{keyword:10} {count}")