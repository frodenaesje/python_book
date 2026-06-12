# file: ex_07_06_word_frequency.py
from collections import Counter

text = """to be or not to be that is the question
whether tis nobler in the mind to suffer
the slings and arrows of outrageous fortune
or to take arms against a sea of troubles"""


def word_count(text: str) -> dict:
    """Return a dict of word frequencies."""
    counts = {}
    for word in text.lower().split():
        word = word.strip('.,!?;:\'"')
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


# --- Part 1: manual ---
print("--- Part 1: manual ---")
counts = word_count(text)

print("Word counts (sorted):")
for word, count in sorted(counts.items()):
    print(f"  {word:<12}{count}")

print(f"\nUnique words: {len(counts.keys())}")

most_common_word = max(counts.items(), key=lambda item: item[1])
print(f"Most common:  {most_common_word[0]} ({most_common_word[1]} times)")

print(f"'fortune' in text: {'fortune' in counts}")

# --- Part 2: Counter ---
print("\n--- Part 2: Counter ---")

words = [w.strip('.,!?;:\'"') for w in text.lower().split() if w]
counter = Counter(words)

print("Top 5 words:")
for word, count in counter.most_common(5):
    print(f"  {word:<10}{count}")
