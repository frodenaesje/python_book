# file: ex_07_05_scrabble_score_start.py

SCORES = {
    'A': 1,  'E': 1,  'I': 1,  'O': 1,  'U': 1,
    'L': 1,  'N': 1,  'R': 1,  'S': 1,  'T': 1,
    'D': 2,  'G': 2,
    'B': 3,  'C': 3,  'M': 3,  'P': 3,
    'F': 4,  'H': 4,  'V': 4,  'W': 4,  'Y': 4,
    'K': 5,
    'J': 8,  'X': 8,
    'Q': 10, 'Z': 10,
}

# TODO: Write scrabble_score(word: str) -> int
#       Returns the total Scrabble score for the word
#       Ignore case, skip characters not in SCORES
#       Hint: SCORES.get(char.upper(), 0)

if __name__ == "__main__":
    word = input("Enter a word: ")

    # TODO: Print each letter and its score on one line
    #       Example: "P=3  y=4  t=1  h=4  o=1  n=1"

    # TODO: Print the total score
    #       Example: "Total score for 'Python': 14"

    # TODO: Find and print the highest-scoring letter using SCORES.items()
    #       Hint: max(SCORES.items(), key=lambda item: item[1])
    #       Example: "Highest scoring letter: Q (10 points)"
