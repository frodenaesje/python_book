# file: ex_07_03_anagram_start.py

# TODO: Write are_anagrams(word1: str, word2: str) -> bool
#       Returns True if word1 and word2 are anagrams (ignore case)
#       Hint: sorted(word.lower()) gives a sorted list of characters
#             two anagrams produce identical sorted lists

# TODO: Write are_phrase_anagrams(phrase1: str, phrase2: str) -> bool
#       Same as above but ignores spaces
#       Hint: use .replace(" ", "") to remove spaces before sorting

if __name__ == "__main__":
    # Part 1 - single words
    print(f'"listen" and "silent": {are_anagrams("listen", "silent")}')
    print(f'"hello" and "world":   {are_anagrams("hello", "world")}')

    print()

    # Part 2 - phrases
    print(f'"William Shakespeare" and "I am a weakish speller": '
          f'{are_phrase_anagrams("William Shakespeare", "I am a weakish speller")}')
    print(f'"astronomer" and "moon starer": '
          f'{are_phrase_anagrams("astronomer", "moon starer")}')
    print(f'"the eyes" and "they see": '
          f'{are_phrase_anagrams("the eyes", "they see")}')
