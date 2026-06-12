---
title: "Morse Code"
id: "ex_07_04_morse_code"
tags: ["dict", "lookup", "str", "join", "for"]
difficulty: "easy"
prerequisites: ["dict", "for", "str", "join", "get"]
learning_outcomes:
  - "Use a dict as a lookup table"
  - "Translate characters using dict lookup"
  - "Handle characters not in the dict gracefully"
---

# Morse Code

## Exercise

Morse code represents letters and digits as sequences of dots and dashes.
A dictionary is the perfect data structure for this mapping.

Write a program with two functions:

1. `to_morse(text: str) -> str` - converts a text string to Morse code.
   Separate characters with a single space and words with " / ".
   Unknown characters are replaced with "?".

2. `from_morse(code: str) -> str` - converts Morse code back to text.

Use this partial Morse code dictionary (you may extend it):

```python
MORSE = {
    'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.',    'F': '..-.', 'G': '--.',  'H': '....',
    'I': '..',   'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--',   'N': '-.',   'O': '---',  'P': '.--.',
    'Q': '--.-', 'R': '.-.',  'S': '...',  'T': '-',
    'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----','1': '.----','2': '..---','3': '...--',
    '4': '....-','5': '.....','6': '-....','7': '--...',
    '8': '---..',  '9': '----.',
}
```

## Example run

```
Enter text: Hello World
Morse: .... . .-.. .-.. --- / .-- --- .-. .-.. -..

Enter Morse: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
Text: HELLO WORLD
```

## Topics

- Dict as lookup table
- `get()` for safe lookup
- Reversing a dict with dict comprehension
- `join()` for building output strings

---
## Instructor notes

**Learning objectives covered:** dict lookup, get(), reverse dict comprehension

**Reversing the dict for decoding:**
```python
REVERSE = {v: k for k, v in MORSE.items()}
```
This is a natural dict comprehension use case - worth pointing out explicitly.

**Word separator:** Using " / " between words means splitting on " / "
for decoding, then splitting each group on " " for individual characters.
