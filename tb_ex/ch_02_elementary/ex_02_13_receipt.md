# Formatted Receipt

## Exercise

Write a program that:

- Reads a name and a price for three items
- Computes the total
- Prints a receipt where the names are left-aligned and the
  prices are right-aligned, each price with two decimals and
  a thousands separator
- Prints a line of dashes and a `Total` line in the same
  format

Line the columns up using field widths in the f-string
format specifiers.

## Example run

```
Enter item 1 name: Coffee
Enter item 1 price: 45.50
Enter item 2 name: Sandwich
Enter item 2 price: 89
Enter item 3 name: Juice
Enter item 3 price: 32
Coffee              45.50
Sandwich            89.00
Juice               32.00
-------------------------
Total              166.50
```

## Topics

- Left align with `<` and right align with `>`
- Field width to make columns line up
- `,.2f` for two decimals plus a thousands separator
