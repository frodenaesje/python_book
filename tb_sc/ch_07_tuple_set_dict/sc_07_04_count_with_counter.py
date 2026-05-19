# file: ch_07_tuple_set_dict/sc_07_04_count_with_counter.py
# Counting occurrences using collections.Counter

from collections import Counter
word = "programming"
letter_count = Counter(word)
print("Letter counts in 'programming':")
for letter, count in letter_count.items():
    print(f"'{letter}': {count}")

# Counter works wit iterables that are hashable (e.g., strings, lists, tuples)
sentence = "the quick brown fox jumps over the lazy dog the fox is quick"
word_list = sentence.split()
word_count = Counter(word_list)
print(f"\nWord counts in sentence:")
for word, count in word_count.items():
    print(f"'{word}': {count}")

# Find most common item
most_common_word, most_common_count = word_count.most_common(1)[0]
print(f"\nMost common word: '{most_common_word}' with {most_common_count} occurrences")

# Example 3: Count grades from a list
grades = ['A', 'B', 'A', 'C', 'B', 'A', 'B', 'C', 'A', 'D', 'B']
grade_count = Counter(grades)
print(f"\nGrade distribution:")
for grade, count in grade_count.items():
    print(f"Grade {grade}: {count} students")

# Example 4: Count colors from survey responses
survey_responses = ['red', 'blue', 'green', 'red', 'yellow', 'blue', 'red', 'green', 'blue', 'red']
color_count = Counter(survey_responses)
print(f"\nFavorite color survey results:")
for color, count in color_count.items():
    print(f"{color}: {count} votes")

