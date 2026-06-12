# file: ex_07_06_word_frequency_start.py
from collections import Counter

text = """to be or not to be that is the question
whether tis nobler in the mind to suffer
the slings and arrows of outrageous fortune
or to take arms against a sea of troubles"""

# --- Part 1: manual approach ---

# TODO: Write word_count(text: str) -> dict
#       Count how often each word appears
#       Normalize: lowercase and strip punctuation with word.strip('.,!?;:\'"')
#       Use: counts[word] = counts.get(word, 0) + 1

# TODO: Call word_count() and use the result to:
#       - Print all words and counts sorted alphabetically using .items()
#       - Print the number of unique words using len() on .keys()
#       - Find the most common word using .values() and .items()
#       - Check if 'fortune' appears using 'in' (checks keys by default)


# --- Part 2: Counter ---

# TODO: Rewrite word_count using Counter
#       Hint: Counter(words_list) where words_list is the normalized word list

# TODO: Use .most_common(5) to display the 5 most frequent words
