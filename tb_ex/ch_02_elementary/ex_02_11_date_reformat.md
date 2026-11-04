# Date Reformat

## Exercise

Write a program that:

- Asks the user for a date written as `YYYY-MM-DD`
- Uses slicing to pull out the year, month and day
- Prints the date in European format `DD.MM.YYYY`

Use slicing only - do not use `split()` or loops.

## Example run

```
Enter a date (YYYY-MM-DD): 2024-01-15
In European format: 15.01.2024
```

## Topics

- Slicing with fixed start and stop positions
- The characters at positions 4 and 7 are the dashes
- Reassembling the parts in a new order

## Assessment criteria

| Criterion | Description | Weight (%) |
|---|---|---:|
| Date input | Read a date string in the stated YYYY-MM-DD format. | 20 |
| Slicing | Extract the year, month and day using slicing, without split() or loops. | 55 |
| Reformatted date | Display the date as DD.MM.YYYY while preserving leading zeros. | 25 |
| **Total** | | **100%** |
