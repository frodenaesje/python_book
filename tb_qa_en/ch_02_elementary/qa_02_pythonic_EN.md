# Pythonic code – Chapter 2

These examples show the same solution at different levels — from code that works to code
that makes full use of Python. None of the levels are "wrong" — but the further down we go,
the more Pythonic the code becomes.

---

## Example 1 – Read and convert a number

**Beginner:**
```python
text = input("What is your age? ")
age = int(text)
```

**Pythonic:**
```python
age = int(input("What is your age? "))
```

---

## Example 2 – Clean up input and compare

**Beginner:**
```python
answer = input("Do you want to continue? ")
answer = answer.strip()
answer = answer.lower()
if answer == "yes":
    print("Continuing...")
```

**Pythonic:**
```python
if input("Do you want to continue? ").strip().lower() == "yes":
    print("Continuing...")
```

---

## Example 3 – Print with variables

**Beginner (C++/Java style):**
```python
name = "Ada"
age = 25
print("Hello, " + name + ", you are " + str(age) + " years old.")
```

**Pythonic – f-string:**
```python
print(f"Hello, {name}, you are {age} years old.")
```

---

## Example 4 – Calculate and format

**Beginner:**
```python
bmi = body_weight / ((body_height / 100) ** 2)
bmi_rounded = round(bmi, 2)
print("Your BMI is: " + str(bmi_rounded))
```

**Pythonic:**
```python
bmi = body_weight / ((body_height / 100) ** 2)
print(f"Your BMI is: {bmi:.2f}")
```

---

## Example 5 – Reverse a string

**Beginner:**
```python
text = "Hello"
reversed_text = ""
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]
print(reversed_text)
```

**Pythonic:**
```python
print(text[::-1])
```

*Note: the beginner version uses a for-loop and range() from Chapter 5 — it is included
here to show the contrast, not as material we are expected to master yet.*

---

## Example 6 – Random numbers

**Beginner:**
```python
import random
number = random.randint(1, 6)
print("You rolled: " + str(number))
```

**Pythonic:**
```python
import random
print(f"You rolled: {random.randint(1, 6)}")
```

---

## Example 7 – Choose a random element

**Beginner:**
```python
import random
participants = ["Alice", "Bob", "Clara"]
index = random.randint(0, len(participants) - 1)
winner = participants[index]
print(winner)
```

**Pythonic:**
```python
import random
participants = ["Alice", "Bob", "Clara"]
print(random.choice(participants))
```

`random.choice()` is designed exactly for this — avoid manual index arithmetic when a
built-in function solves it directly.
