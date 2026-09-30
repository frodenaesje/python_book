# Chapter 3 – Answer Key: Review Questions

## Understanding

**1. Bit, nibble and byte**
A bit is the smallest unit of information — either 0 or 1. A nibble is 4 bits. A byte is 8 bits.

**2. The character `'1'` vs. the number `1`**
`'1'` is a one-character Unicode string whose character has code point U+0031; ASCII also assigns decimal value 49 to that character. `1` is the integer value one. These character codes and illustrated bit patterns are not complete Python object memory layouts. Adding the string and integer raises `TypeError`; an explicit conversion is needed.

**3. `ord()`**
`ord()` returns the internal numeric value (Unicode code point) of a character. `ord('A')` returns `65`.

**4. The prefixes `0b` and `0x`**
`0b` indicates a binary number (base 2), e.g. `0b1010` is 10 in decimal. `0x` indicates a hexadecimal number (base 16), e.g. `0xFF` is 255 in decimal.

**5. Conversion expressions — value and data type**
```
a) int("1011", 2)  →  11   (int)
b) bin(11)         →  '0b1011'  (str)
c) hex(255)        →  '0xff'    (str)
```

**6. Why binary ↔ hexadecimal conversion is so simple**
Each hexadecimal digit represents exactly 4 bits (one nibble). This means we can convert group by group without going via decimal — for example `1111` is always `F`, regardless of context.

**7. Bitwise operators**
`&` (AND) - sets a bit to 1 only if both bits are 1.
`|` (OR) - sets a bit to 1 if at least one bit is 1.
`^` (XOR) - sets a bit to 1 if the bits are different.
`~` (NOT) - complements an integer: `~x == -(x + 1)`. It is not always negative; for example, `~-1 == 0`.
`<<` (shift left) - for a non-negative shift count `n`, `x << n` is equivalent to `x * 2**n`.
`>>` (shift right) - for a non-negative shift count `n`, `x >> n` is equivalent to floor division `x // 2**n`.

---

## Practical

**8. Calculate by hand, then check in REPL**
```
a) bin(13)         →  '0b1101'
b) hex(255)        →  '0xff'
c) int("1010", 2)  →  10
d) int("FF", 16)   →  255
```

**9. Bitwise operations — set up in binary, calculate bit by bit**

```
a) 12 & 10
   12 = 1100
   10 = 1010
   &  = 1000  →  8

b) 12 | 10
   12 = 1100
   10 = 1010
   |  = 1110  →  14

c) 12 ^ 10
   12 = 1100
   10 = 1010
   ^  = 0110  →  6

d) 5 << 2
   5 = 0101  →  shift left 2: 010100  →  20

e) 20 >> 1
   20 = 10100  →  shift right 1: 01010  →  10
```

**10. Character to numeric value**

```python
char = input("Enter one character: ")
value = ord(char)
print(f"The character '{char}' has numeric value {value}")
print(f"Binary: {bin(value)}")
print(f"Hexadecimal: {hex(value)}")
```

Note: `ord()` returns an `int`, so we can use it directly in `bin()` and `hex()` — and in f-string formatting. Note that `bin()` and `hex()` return strings with a prefix (`0b` / `0x`), not plain numbers.

**11. Integer in binary and hexadecimal**

```python
number = int(input("Enter an integer between 0 and 255: "))
print(f"{number} in binary is {number:08b} and in hexadecimal is {number:02X}")
```

The format specifier `08b` means binary form (`b`) with width 8 and leading zeros (`0`). `02X` means hexadecimal with uppercase letters (`X`) and at least 2 digits with a leading zero. This is a good opportunity to revisit f-string formatting from Chapter 2 in a new context.
