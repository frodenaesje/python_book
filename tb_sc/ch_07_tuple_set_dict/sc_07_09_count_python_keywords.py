# file: sc_07_09_count_python_keywords.py

KEYWORDS = {
    'False', 'None', 'True', 'and', 'as', 'assert',
    'async', 'await', 'break', 'class', 'continue', 'def',
    'del', 'elif', 'else', 'except', 'finally', 'for',
    'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
    'return', 'try', 'while', 'with', 'yield'
}

print("Skriv inn kode, avslutt med en tom linje:")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

words = " ".join(lines).split()
keyword_counts = {}
for word in words:
    if word in KEYWORDS:
        keyword_counts[word] = keyword_counts.get(word, 0) + 1

for keyword, count in sorted(keyword_counts.items()):
    print(f"{keyword:10} {count}")