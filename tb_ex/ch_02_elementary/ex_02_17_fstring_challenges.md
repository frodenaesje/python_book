# F-string Challenges

## Exercise 1 - Decimal places

Given:

```python
price = 19.9876
```

Use an f-string to produce:

```
Price: 19.99
```

Do not use `round()`.

## Exercise 2 - Field width and alignment

Given:

```python
product = "Coffee"
price = 42.5
```

Use an f-string to produce:

```
Coffee         42.50
```

Let the product occupy a field of 12 characters and the price a field of 8 characters, right-aligned with two decimal places.

## Exercise 3 - Thousands separator

Given:

```python
population = 5834127
```

Use an f-string to display the number with a thousands separator:

```
Population: 5,834,127
```

Then find out how to use `_` instead of `,` as the separator.

## Exercise 4 - Percentage

Given:

```python
correct = 17
total = 20
```

Calculate the proportion of correct answers and use an f-string to produce:

```
Score: 85.0%
```

Use the percentage format specifier rather than multiplying the value by 100 ourselves.

## Exercise 5 - A small table

Given:

```python
name1 = "Alice"
score1 = 87.456
name2 = "Christopher"
score2 = 91.2
```

Use f-strings with field widths and alignment to produce:

```
Name              Score
Alice             87.46
Christopher       91.20
```

Try to make the columns line up without adding spaces manually between the values.

## Exercise 6 - User-controlled decimal places

Ask the user for a number and how many decimal places should be displayed:

```
Enter a number: 3.14159265
Number of decimal places: 4
```

The program should produce:

```
Result: 3.1416
```

Build the number of decimal places into the format specifier using a variable.

Hint:

```python
f"{value:.{decimals}f}"
```

> **Note:** Exercises 7 and 8 use conditional expressions (`x if condition else y`), which rely on `if`/`else` logic. If we haven't covered conditionals in this chapter yet, we can safely skip these two for now and come back to them once we have.

## Exercise 7 - Singular or plural?

Given:

```python
apples = 1
```

Use one f-string and a conditional expression to produce:

```
There is 1 apple.
```

If we change the value to:

```python
apples = 5
```

the same f-string should produce:

```
There are 5 apples.
```

Try to handle both `is`/`are` and `apple`/`apples` inside the f-string.

## Exercise 8 - Dynamic receipt

Ask the user for:

- the name of a product
- the quantity
- the price per item
- the number of decimal places to display

For example:

```
Product: notebook
Quantity: 3
Price per item: 12.5
Decimal places: 2
```

Use a single f-string for the final output:

```
3 notebooks cost 37.50 in total.
```

The same code with a quantity of `1` should produce:

```
1 notebook costs 12.50 in total.
```

Use conditional expressions inside the f-string to choose the correct plural ending and `cost`/`costs`, and use the user's choice of decimal places as part of the format specifier.

## Topics

- f-string format specifiers: `.2f`, `,`, `_`, `.1%`
- Field width and alignment: `<`, `>`, `^`
- Nested/variable format specifiers: `{value:.{decimals}f}`
- Conditional expressions inside f-strings: `{'a' if condition else 'b'}`
