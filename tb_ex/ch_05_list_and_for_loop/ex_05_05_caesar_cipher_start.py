# file: ex_05_05_caesar_cipher_start.py

message = input("Enter message: ")
shift = int(input("Enter shift: "))

def encode(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            # TODO: Shift the character by 'shift' positions
            #       Handle uppercase and lowercase separately
            #       Use wraparound with modulo 26
            #       Hint for lowercase:
            #         shifted = (ord(char) - ord('a') + shift) % 26
            #         new_char = chr(shifted + ord('a'))
            pass
        else:
            # TODO: Keep non-letter characters unchanged
            pass
    return ''.join(result)

def decode(text, shift):
    # TODO: Decoding is encoding with a negative shift
    #       Hint: reuse encode() with -shift
    pass

# TODO: Encode the message and print it
#       Example: "Encoded: Khoor, Zruog!"

# TODO: Decode the encoded message and print it
#       Example: "Decoded: Hello, World!"
