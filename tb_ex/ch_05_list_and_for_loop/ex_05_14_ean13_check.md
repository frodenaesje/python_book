# EAN-13 Check Digit - Extra Exercise

## Exercise

An EAN-13 barcode contains thirteen digits. Its last digit is a check digit
calculated from the first twelve. Write a program that reads a barcode as text
and checks whether its check digit is correct.

1. Require exactly thirteen characters, all digits from `0` to `9`. Report
   invalid input and do not continue the calculation. Preserve leading zeros.
2. Starting at the left, assign weights of 1 and 3 alternately to the first
   twelve digits. Use a loop with `enumerate()` to add the products of each
   digit and its weight.
3. Find the digit from 0 to 9 that must be added to the sum to make it divisible
   by 10. If the sum is already divisible by 10, the check digit is 0.
4. Report whether the supplied check digit matches. If it does not, show both
   the supplied and the expected digit.

Leading and trailing whitespace may be removed before validation. A correct
check digit does not prove that a barcode is registered to a product.
Exact message wording is not required, provided the requested information is clear.

## Hints

- Keep the input as a string; converting the entire code to an integer loses leading zeros.
- A slice can select the digits used in the calculation.
- The index tells you which weight to use. Remember that indices start at zero.
- Consider separately what should happen when the sum is already divisible by 10.

## Example runs

```text
Enter a 13-digit barcode: 9780134685991
Check digit is correct: 1
```

```text
Enter a 13-digit barcode: 9780134685994
Invalid check digit: 4.
Expected: 1.
```

```text
Enter a 13-digit barcode: 123
A barcode must have exactly 13 digits.
```

## Topics

- Strings and slicing
- Iteration with enumerate
- Accumulation and modulo
- Input validation

## Assessment criteria

| Criterion | Description | Weight (%) |
|---|---|---:|
| Input validation | Preserves leading zeros, accepts exactly 13 digits from 0 to 9, and reports invalid length or characters without attempting the checksum calculation. | 20 |
| Weighted sum | Uses a loop with enumerate to process the first twelve digits with alternating weights of 1 and 3, starting with 1, and accumulates the products correctly. | 40 |
| Check digit calculation | Determines the required check digit from 0 to 9, including 0 when the weighted sum is already divisible by 10. | 25 |
| Verification and output | Compares the calculated and supplied check digits, reports whether they match, and shows both values when they differ. | 15 |
| **Total** | | **100%** |
