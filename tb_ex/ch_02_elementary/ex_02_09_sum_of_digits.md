# Sum of Digits

## Exercise

Write a program that:

- Asks the user for an integer with at most three digits (0 to 999)
- Extracts each digit using the modulo (`%`) and integer
  division (`//`) operators
- Adds the digits together and prints the sum

Important: do not use loops, and do not convert the number to a
string. We do not know loops yet, so we write out all three digit
positions by hand. A number with fewer digits simply gets 0 in the
higher positions - 47 becomes hundreds = 0, tens = 4, ones = 7.

## Example run

```
Enter an integer with at most three digits: 47
The sum of the digits in 47 is 11.

Enter an integer with at most three digits: 902
The sum of the digits in 902 is 11.
```

## Topics

- Integer division `//` to shift digits down
- Modulo `%` to pick off a single digit
- Handling 1, 2 and 3 digit numbers with the same code

## Assessment criteria

| Criterion | Description | Weight (%) |
|---|---|---:|
| Integer input | Read an integer in the stated range of 0 to 999. | 20 |
| Digit extraction | Use modulo and integer division to extract the digit positions, without loops or string conversion. | 55 |
| Digit sum | Add the extracted digits and display the sum for one-, two- and three-digit inputs. | 25 |
| **Total** | | **100%** |
