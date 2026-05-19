# file: sc_07_04_count_occurencies.py
# Counting occurrences using dictionaries

# Example 1: Count letters in a word
word = "programming"
letter_count = {}
for letter in word:
    letter_count[letter] = letter_count.get(letter, 0) + 1

print("Letter counts in 'programming':")
for letter, count in letter_count.items():
    print(f"'{letter}': {count}")

# Example 2: Count words in a sentence
sentence = "the quick brown fox jumps over the lazy dog the fox is quick"
word_list = sentence.split()
word_count = {}

for word in word_list:
    word_count[word] = word_count.get(word, 0) + 1

print(f"\nWord counts in sentence:")
for word, count in word_count.items():
    print(f"'{word}': {count}")

# Find most common item
most_common_word = max(word_count, key=word_count.get)
print(f"\nMost common word: '{most_common_word}' with {word_count[most_common_word]} occurrences")

# Example 3: Count grades from a list
grades = ['A', 'B', 'A', 'C', 'B', 'A', 'B', 'C', 'A', 'D', 'B']
grade_count = {}

for grade in grades:
    grade_count[grade] = grade_count.get(grade, 0) + 1

print(f"\nGrade distribution:")
for grade, count in grade_count.items():
    print(f"Grade {grade}: {count} students")

# Example 4: Count colors from survey responses
survey_responses = ['red', 'blue', 'green', 'red', 'yellow', 'blue', 'red', 'green', 'blue', 'red']
color_count = {}

for color in survey_responses:
    color_count[color] = color_count.get(color, 0) + 1

print(f"\nFavorite color survey results:")
for color, count in color_count.items():
    print(f"{color}: {count} votes")

# Alternative approach without get() - using if/else
numbers = [1, 2, 3, 2, 1, 3, 1, 4, 2, 1]
number_count = {}

for num in numbers:
    if num in number_count:
        number_count[num] += 1
    else:
        number_count[num] = 1

print(f"\nNumber counts (without get()):")
for num, count in number_count.items():
    print(f"{num}: {count}")
