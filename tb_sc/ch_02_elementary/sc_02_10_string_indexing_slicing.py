# file: sc_02_10_string_indexing_slicing.py
text = "Hello, world!"
print(text[0])   # H
print(text[7])   # w
# print(text[13])  # IndexError: string index out of range
print(text[-1])  # !, last character
print(text[-2])  # d, second to last character
print(text[0:5]) # Hello (slice from index 0 to 4)
print(text[7:])  # world! (slice from index 7 to end)
print(text[::2])  # Hlo ol! (every other character)
print(text[::-1]) # !dlrow ,olleH. reverse string
