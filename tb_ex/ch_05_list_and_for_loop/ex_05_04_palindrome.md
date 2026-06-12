---
title: "Palindrome"
id: "ex_05_04_palindrome"
tags: ["for", "enumerate", "slicing", "str", "while"]
difficulty: "easy"
prerequisites: ["for", "str", "slicing", "while"]
learning_outcomes:
  - "Iterate over a string with a for loop"
  - "Use slicing to reverse a string"
  - "Ignore spaces when checking for palindromes"
---

# Palindrome

## Exercise

A string is a palindrome if it reads the same forwards and backwards.
Examples: "racecar", "level", "anna".

### Part 1

Write a program that reads a string from the user and determines whether
it is a palindrome. Use slicing to reverse the string.

### Part 2

Extend the program to also handle multi-word palindromes by ignoring
spaces. Examples: "go dog", "race a car" (not a palindrome), 
"never odd or even".

## Example run

```
Enter a string: racecar
"racecar" is a palindrome.

Enter a string: hello
"hello" is not a palindrome.

Enter a string: never odd or even
"never odd or even" is a palindrome (ignoring spaces).
```

## Topics

- String slicing `[::-1]` to reverse
- `replace()` to remove spaces
- Case normalization with `.lower()`

---
## Instructor notes

**Learning objectives covered:** slicing, string methods, normalization

**Part 1 hint:** `text == text[::-1]` is the elegant one-liner.
Alternatively, compare character by character using a loop and enumerate.

**Part 2 hint:** `text.replace(" ", "")` removes all spaces before
comparing. Also worth normalizing case with `.lower()`.

**Connection to ch 4:** ISBN-10 was deferred here from ch 2. If students
ask why, this is a good moment to show how loops make previously clunky
code elegant.
