# file: snippet_counting_with_dict.py
# get() supplies zero for unseen items so a dictionary can count occurrences.

# Count letters in a word
# get(letter, 0) starts unseen letters at zero.
word = "programming"
letter_count = {}

for letter in word:
    letter_count[letter] = letter_count.get(letter, 0) + 1

for letter, count in letter_count.items():
    print(f"'{letter}': {count}")


# Count words in a sentence
sentence = "the quick brown fox jumps over the lazy dog the fox is quick"
word_count = {}

for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1

# Find the most common word
# key=word_count.get makes max() compare the counts.
most_common = max(word_count, key=word_count.get)
print(
    f"Most common word: '{most_common}' with "
    f"{word_count[most_common]} occurrences"
)
