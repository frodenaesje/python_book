# file: ex_07_04_morse_code.py

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

REVERSE = {v: k for k, v in MORSE.items()}


def to_morse(text: str) -> str:
    """Convert text to Morse code."""
    words = []
    for word in text.upper().split():
        chars = [MORSE.get(c, '?') for c in word]
        words.append(' '.join(chars))
    return ' / '.join(words)


def from_morse(code: str) -> str:
    """Convert Morse code to text."""
    words = []
    for word in code.split(' / '):
        chars = [REVERSE.get(c, '?') for c in word.split()]
        words.append(''.join(chars))
    return ' '.join(words)


if __name__ == "__main__":
    text = input("Enter text: ")
    morse = to_morse(text)
    print(f"Morse: {morse}")

    print()
    code = input("Enter Morse: ")
    print(f"Text: {from_morse(code)}")
