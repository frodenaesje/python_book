# file: ex_07_04_morse_code_start.py

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

# TODO: Build REVERSE dict from MORSE using a dict comprehension
#       {morse_code: letter for letter, morse_code in MORSE.items()}

# TODO: Write to_morse(text: str) -> str
#       Convert each character to Morse using MORSE.get(char.upper(), '?')
#       Separate characters with ' ' and words with ' / '

# TODO: Write from_morse(code: str) -> str
#       Split on ' / ' to get words, split each word on ' ' to get chars
#       Look up each code in REVERSE
#       Join words with ' '

if __name__ == "__main__":
    text = input("Enter text: ")
    morse = to_morse(text)
    print(f"Morse: {morse}")

    print()
    code = input("Enter Morse: ")
    print(f"Text: {from_morse(code)}")
