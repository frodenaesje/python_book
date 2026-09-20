# Temperature Log

## Exercise

A weather station logged the temperature (in Celsius) once a day for two weeks.
The 14 readings are kept in one list. In this exercise we pull the list apart
with slicing and build new lists with comprehensions - no loops needed. Every
step is a single slice or a single comprehension.

We start with this list:

    temps = [18, 21, 19, 24, 27, 22, 20, 16, 23, 25, 28, 17, 19, 21]

Write a program that:

1. Prints the first week (the first 7 days) and the second week (the last 7 days)
2. Prints every other day, starting from the first
3. Prints the list reversed, and separately the last three days
4. Prints every temperature converted to Fahrenheit, as whole degrees
5. Prints the warm days (22 or higher) from the second week only
6. Prints a label for each day: "warm" if it is 22 or higher, otherwise "cool"

Rules:
- Do not write a loop - each step is one slice or one comprehension

## Hints

Steps 1 and 2 need only basic slicing - try them without help first.

- Step 3: a negative step walks the list backwards; a negative index counts from the end
- Step 4: build a new list with a comprehension, converting each value with `c * 9 / 5 + 32` and rounding with `round(...)`
- Step 5: a comprehension can run over a slice, and a filter after the `for` keeps only some of the elements
- Step 6: a comprehension can decide each value with a conditional expression placed in front of the `for`

## Example run

```
First week: [18, 21, 19, 24, 27, 22, 20]
Second week: [16, 23, 25, 28, 17, 19, 21]
Every other day: [18, 19, 27, 20, 23, 28, 19]
Reversed: [21, 19, 17, 28, 25, 23, 16, 20, 22, 27, 24, 19, 21, 18]
Last three: [17, 19, 21]
Fahrenheit: [64, 70, 66, 75, 81, 72, 68, 61, 73, 77, 82, 63, 66, 70]
Warm second-week days: [23, 25, 28]
Labels: ['cool', 'cool', 'cool', 'warm', 'warm', 'warm', 'cool', 'cool', 'warm', 'warm', 'warm', 'cool', 'cool', 'cool']
```

## Topics

- Slicing: start and stop, a step, reverse, and negative indices
- List comprehension to transform every element
- Filtering inside a comprehension, applied to a slice
- Conditional expression inside a comprehension

## Assessment criteria

| Criterion | Description | Weight (%) |
|---|---|---:|
| List slicing | Uses one slice per requested result to print both weeks, every other day starting from the first, the reversed readings, and the last three days. | 40 |
| Temperature conversion | Uses a single list comprehension to convert all readings to Fahrenheit, round them to whole degrees, and print the resulting list. | 20 |
| Warm-day filtering | Uses a single filtering list comprehension applied to a slice to print only second-week readings of 22 or higher. | 20 |
| Daily labels | Uses a single list comprehension with a conditional expression to print a warm or cool label for every reading, treating 22 or higher as warm. | 20 |
| **Total** | | **100%** |
