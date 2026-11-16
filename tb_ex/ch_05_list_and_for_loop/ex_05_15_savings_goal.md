# Savings Goal - Extra Exercise

## Exercise

Write a program that reads a savings goal in NOK, a fixed amount saved each
month, and an annual interest rate as a percentage. Determine how many complete
years it takes to reach the goal and report the balance at the end of each year.

Use this simplified model:

- Start with a balance of zero.
- At the end of each year, first add interest on the balance from the beginning
  of that year, then deposit the entire year's savings.
- This year's deposit does not earn interest until the following year.
- Ignore taxes, fees, and changes in the interest rate.

Requirements:

1. The goal and monthly amount must be positive. The interest rate must be
   nonnegative. Report invalid values without running the simulation.
2. Use a `while` loop to calculate balances until the goal is reached or exceeded.
3. Store each end-of-year balance in a list.
4. Report the number of years, all annual balances, total deposits and earned interest.
5. Display monetary amounts rounded to whole kroner, but do not round balances
   between years. Thousands separators and exact message wording are optional.

You may assume ordinary finite numeric input in the correct format. You do not
need to handle text instead of numbers or extreme values. The goal is checked
only at year-end; do not calculate a partial final year.

## Hints

- Convert the percentage to a rate before using it in a calculation.
- The order of interest and deposits matters.
- Append one balance for each completed year.
- Separate money deposited from interest earned when producing the final summary.

## Example run

```text
Savings goal (NOK): 300000
Monthly amount saved (NOK): 3000
Annual interest rate (%): 4
Goal reached after 8 years.
Year 1: 36,000 NOK
Year 2: 73,440 NOK
Year 3: 112,378 NOK
Year 4: 152,873 NOK
Year 5: 194,988 NOK
Year 6: 238,787 NOK
Year 7: 284,339 NOK
Year 8: 331,712 NOK
Deposited: 288,000 NOK
Interest: 43,712 NOK
```

## Topics

- While loops and termination
- Lists and append
- Repeated calculations
- Formatted numerical output

## Assessment criteria

| Criterion | Description | Weight (%) |
|---|---|---:|
| Input validation | Reads the goal, monthly savings and annual percentage rate, and rejects nonpositive goals or savings and negative interest before simulating. | 15 |
| Annual savings simulation | Starts with zero balance, applies annual interest before adding that year's savings, and uses a while loop until the balance reaches or exceeds the goal, including zero-interest cases. | 40 |
| Annual balance history | Stores each end-of-year balance in a list and uses the history to report the number of years and every annual balance. | 25 |
| Financial summary and formatting | Reports total deposits and earned interest consistently with the simulated years, displays monetary values rounded to whole kroner, and retains unrounded balances during the simulation. | 20 |
| **Total** | | **100%** |
