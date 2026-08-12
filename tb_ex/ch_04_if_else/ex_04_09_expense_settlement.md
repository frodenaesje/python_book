# Expenses Settlement

## Exercise

After a trip with friends, someone has paid for the cabin, someone for
the food, and someone for the fuel - and at some point the group needs
to settle up. Apps like the Norwegian Vipps (with its Oppgjør feature)
and Splitwise solve exactly this: everyone registers their expenses, and
the app calculates who owes whom. We will build a simplified version for
three friends on a cabin trip.

The expenses are given as variables in the starter code. All expenses are
split equally among the three:

```python
jonas_paid = 2400    # cabin rental
maria_paid = 950     # food and drinks
simen_paid = 400     # fuel
```

### Part A - Share and balance

Calculate the total and how much each person should cover (the total
divided by three). Then calculate the balance for each person: what the
person has paid, minus the share the person should cover.

- Positive balance: the person has paid too much and should get money back
- Negative balance: the person owes money

Print the total, the share, and each person's balance with two decimals.
Expected output with the numbers above:

```
Total: 3750.00 kr
Share per person: 1250.00 kr
Jonas: +1150.00 kr
Maria: -300.00 kr
Simen: -850.00 kr
```

Hint: f-strings can format with a sign and two decimals like this:
`f"{jonas_balance:+.2f}"`.

### Part B - Status per person

Use `if`-`elif`-`else` to print a status line for each person:

- Balance greater than 0: `Jonas should receive 1150.00 kr`
- Balance less than 0: `Simen should pay 850.00 kr` (use the amount without the minus sign)
- Balance equal to 0: `Maria is settled`

### Part C - Who pays whom?

Now the program should do the job the app does at the end: print the
actual payments. With three people, the settlement always requires at
most two transfers. Expected output with the numbers above:

```
Maria pays 300.00 kr to Jonas
Simen pays 850.00 kr to Jonas
```

If everyone is settled, the program should print `No payments needed`.

Hint on approach: A payment always goes from a person with a negative
balance to a person with a positive balance. The amount is the smaller of
what the debtor owes and what the recipient should receive - the `min()`
function is useful here. With three people, we can simply check every
pair: could Jonas owe Maria something? Could Jonas owe Simen something?
And so on. That gives six combinations to check, and each of them is an
`if` statement.

### Part D - Test the program

Change the expense amounts and verify that the program produces correct
payments in all situations: one person owing two, two people owing one,
and the case where one person is exactly settled. Prefer amounts where
the total is divisible by three, to avoid rounding to fractional rounding.

### Looking ahead: Why only three people?

With three people we get by with three variables and pure `if`-`else`
logic - every possible situation can be enumerated and handled
separately. That is exactly what this chapter is about.

Still, notice how repetitive the code is: three nearly identical status
blocks in part B, six nearly identical checks in part C. With four people
it would be four status blocks and twelve pair checks, and with ten
people it would get completely out of hand. To handle any number of
people, we need two things we have not learned yet: a data structure
that can hold all the participants and amounts together (lists and
dictionaries), and loops that repeat the same logic for each person. We
will return to this exact problem in a later chapter - with tools that
make today's solution shrink considerably.