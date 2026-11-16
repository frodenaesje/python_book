# Where Did the Money Go? - Extra Exercise

## Exercise

A banking app lists purchases one by one. Write a program that groups the
purchases by category and shows where the money went.

Each purchase is a tuple containing a date, a category and an amount in NOK.
Use the data supplied in the starter code:

```python
# Each transaction: (date, category, amount in NOK)
transactions = [
    ("2026-11-02", "Groceries", 412.50),
    ("2026-11-03", "Transport", 42.00),
    ("2026-11-03", "Coffee", 49.00),
    ("2026-11-05", "Groceries", 268.90),
    ("2026-11-06", "Streaming", 129.00),
    ("2026-11-07", "Coffee", 54.00),
    ("2026-11-08", "Transport", 42.00),
    ("2026-11-09", "Groceries", 531.40),
    ("2026-11-10", "Coffee", 49.00),
]
```

Write a program that:

1. Builds a dictionary of total spending per category.
2. Builds a second dictionary containing a list of the individual purchase
   amounts for each category. Use these lists to determine purchase counts.
3. Displays each category's purchase count, total spending and percentage
   share of the overall spending. Use `sorted()` with a named key function
   to put the largest category total first.
4. Displays the total number of purchases and the overall spending.
5. Uses `max()` with a named key function to find the largest individual
   purchase, and displays its amount, category and date.

Display monetary amounts to two decimal places and percentage shares rounded
to whole percentages. Exact column widths and thousands separators are optional.
Rounded shares do not always sum to exactly 100%.

You may assume a nonempty list of purchases with positive amounts and valid
three-element tuples. Refunds, empty input and interactive registration are
outside the scope of this exercise. Do not hardcode category names or calculated
results. Keep the supplied transactions unchanged. If totals tie, either category
order is acceptable; if largest purchases tie, displaying any one is sufficient.

## Hints

- Unpack each tuple in the loop. `_` can name a value you do not need there.
- Consider how to initialise a category the first time you encounter it.
  `get()` and `setdefault()` can help, but equivalent conditional logic is fine.
- Dictionary `items()` gives key-value pairs. A key function selects the part
  of each pair that sorting should compare.
- Repeated purchases still count as separate purchases, even when amounts match.

## Example run

```text
Category     Count     Total   Share
Groceries        3  1,212.80     77%
Coffee           3    152.00     10%
Streaming        1    129.00      8%
Transport        2     84.00      5%
Sum              9  1,577.80
Largest purchase: 531.40 NOK (Groceries, 2026-11-09)
```

## Topics

- Tuples as groups of related values
- Dictionaries for accumulation and grouping
- Key functions for sorted and max
- Formatted output

## Assessment criteria

| Criterion | Description | Weight (%) |
|---|---|---:|
| Category aggregation | Builds dictionaries containing the total and the list of individual amounts for each category, preserving every purchase including repeated amounts. | 40 |
| Category report | Reports each category's count, total and share of overall spending, sorted by decreasing total using sorted and a named key function. | 30 |
| Overall totals | Reports the total number of purchases and the overall amount spent, with monetary amounts displayed to two decimal places. | 10 |
| Largest purchase | Uses max with a named key function to identify the largest individual purchase and displays its amount, category and date. | 20 |
| **Total** | | **100%** |
