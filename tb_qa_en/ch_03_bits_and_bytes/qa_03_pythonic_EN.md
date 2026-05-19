# Pythonic code – Chapter 3

Chapter 3 is more about *what happens under the hood* than about Python idioms, so this
file is shorter than for Chapter 2. But there are a few places where Python saves us a
lot of work if we know the built-in functions.

---

## Example 1 – Convert a binary string to a decimal number

**Beginner (building from scratch):**
```python
binary_string = "1011"
result = 0
pos = len(binary_string) - 1
for ch in binary_string:
    result = result + int(ch) * 2 ** pos
    pos -= 1
print(result)   # 11
```

**Pythonic:**
```python
print(int("1011", 2))   # 11
```

*Note: the beginner version uses a for-loop from Chapter 5 — it is included here to
show the contrast, not as material we are expected to master yet.*

---

## Example 2 – Print a number in binary

**Beginner (manual conversion):**
```python
number = 13
result_str = ""
while number > 0:
    result_str = str(number % 2) + result_str
    number = number // 2
print(result_str)   # 1101
```

**Pythonic:**
```python
print(bin(13))            # '0b1101'
print(bin(13)[2:])        # '1101'  – without prefix
print(f"{13:b}")          # '1101'  – without prefix via f-string
print(f"{13:08b}")        # '00001101' – with leading zeros to 8 bits
```

---

## Example 3 – Print a number in hexadecimal

**Beginner:**
```python
hex_str = format(255, 'x').upper()
print("0x" + hex_str)   # 0xFF
```

**Pythonic:**
```python
print(hex(255))           # '0xff'
print(f"{255:x}")         # 'ff'
print(f"{255:X}")         # 'FF' – uppercase letters
print(f"{255:02X}")       # 'FF' – two digits, uppercase
print(f"0x{255:02X}")     # '0xFF' – with prefix
```

---

## Example 4 – Check whether a number is even using bitwise AND

**Beginner:**
```python
number = 14
if number % 2 == 0:
    print("Even")
```

**Pythonic (for those who want to play with bits):**
```python
number = 14
if number & 1 == 0:
    print("Even")
```

**Even more Pythonic (exploiting truthiness):**
```python
number = 14
if not number & 1:
    print("Even")
```

*All three variants are perfectly fine — the first is the most common and most readable.
The second is a classic bit trick worth knowing: the last bit in a binary number
determines whether it is even (`0`) or odd (`1`). The third exploits the fact that `0`
is falsy and all other integers are truthy — `not number & 1` means "the last bit is
not 1".*
