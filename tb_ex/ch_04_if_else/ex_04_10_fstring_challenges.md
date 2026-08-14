# F-string Challenges

## Exercise

Ten small challenges, one f-string each. For every challenge the
starting variables are given - write a single `print` so the output
matches the target line exactly.

We stay inside Chapter 4: f-strings, arithmetic, the ternary
expression `a if condition else b`, and string methods. No lists, no
loops, no functions.

1. **Basic interpolation.** `name = "John"`, `age = 30`. Produce:
   `John is 30 years old.`
2. **Two decimals.** `amount = 837.5`. Produce: `Amount: 837.50`
3. **Right alignment.** `a = 5`, `b = 42`, `c = 1370`. Print each on
   its own line, right-aligned in a field eight characters wide, so
   the digits line up in a column.
4. **Percent.** `correct = 27`, `total = 40`. Produce:
   `Score: 67.5%`  (one decimal, and let the format spec add the `%`).
5. **Sign and thousands separator.** `balance = 2500.0`. Produce:
   `+2,500.00`  (always show the sign, group thousands, two decimals).
6. **A different thousands separator.** `population = 5391369`. The
   format spec only offers `,` as the grouping character. Produce a
   space-grouped number instead: `5 391 369`.
7. **Method calls in the field.** `first = "john"`,
   `last = "english"`. Produce: `John ENGLISH`  (capitalise the
   first name, upper-case the last - do it inside the f-string).
8. **Ternary: even or odd.** `number = 7`. Produce: `7 is odd`
9. **Ternary: plural ending.** `count = 1`. Produce:
   `You have 1 message`  (no trailing `s` when there is exactly one).
10. **Put it together.** `quantity = 3`, `price = 49.9`. Compute the
    total in the f-string and produce:
    `3 items cost 149.70 in total`  (plural `items`, two decimals).

## Example run

```
John is 30 years old.
Amount: 837.50
       5
      42
    1370
Score: 67.5%
+2,500.00
5 391 369
John ENGLISH
7 is odd
You have 1 message
3 items cost 149.70 in total
```

## Hint

- Field width and alignment go in the format spec: `{a:>8}` means
  "right-align in width 8".
- `{value:.1%}` multiplies by 100 and appends `%`, so pass the raw
  fraction (`correct / total`), not an already-scaled number.
- `{balance:+,.2f}` combines three things: `+` (always show sign),
  `,` (group thousands) and `.2f` (two decimals).
- For challenge 6, format with `,` first, then swap the character:
  `f"{population:,}".replace(",", " ")`. Swapping for `"."` instead
  would give `5.391.369`.
- A method call is just an expression, so it can go straight inside
  the braces: `{first.capitalize()}`.
- The ternary expression is `value_if_true if condition else
  value_if_false`. For a plural ending: `{'s' if count != 1 else ''}`.

## Topics

- f-string interpolation and format specs (`.2f`, `>8`, `.1%`, `+`, `,`)
- The ternary expression inside an f-string
- Calling string methods inside a field
- Plural endings without if-blocks
