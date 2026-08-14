# Expenses Settlement

## Exercise

After a trip with friends, someone has paid for the cabin, someone for
the food, and someone for the fuel - and at some point the group needs
to settle up. Several apps can solve exactly this: everyone registers their expenses, and
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
Total: 3750.00
Share per person: 1250.00
Jonas: +1150.00
Maria: -300.00
Simen: -850.00
```

Hint: f-strings can format with a sign and two decimals like this:
`f"{jonas_balance:+.2f}"`.

### Part B - Status per person

Use `if`-`elif`-`else` to print a status line for each person:

- Balance greater than 0: `Jonas should receive 1150.00`
- Balance less than 0: `Simen should pay 850.00` (use the amount without the minus sign)
- Balance equal to 0: `Maria is settled`

### Part C - Who pays whom?

Now the program should do the job the app does at the end: print the
actual payments. With three people, the settlement always requires at
most two transfers. Expected output with the numbers above:

```
Maria pays 300.00 to Jonas
Simen pays 850.00 to Jonas
```

If everyone is settled, the program should print `No payments needed`.

**How to think about it:** Each person's balance says where they stand.
A positive balance means the person has paid too much and should get money
back (a recipient); a negative balance means the person owes money (a
debtor). A single payment always goes from a debtor to a recipient, and its
size is limited on both sides: a debtor cannot pay more than they owe, and a
recipient cannot take more than they are owed. So the amount is the smaller
of the two - `min(what the debtor owes, what the recipient should receive)`
- which fully settles at least one of them in that one payment.

With three people, one payment settles at most one person, so we may need
more than one. Two facts keep it manageable. First, the balances always sum
to zero: what one person overpaid is exactly what the others owe. Because of
that, three people can always be settled in at most two transfers, and only
two basic patterns can occur when nobody is already even - either one debtor
pays the two recipients, or two debtors pay the one recipient. If someone is
already at zero, it collapses to a plain two-person settlement between the
other two.

Here is why each block stands on its own. In both patterns the lone person
on the single side has exactly enough to cover each of the others in full:
the one debtor owes the two recipients combined, so at least each of them,
and the one recipient is owed the two debtors combined, so at least each of
them. That means every `min()` comes out equal to the counterpart's full
amount - no payment is ever partial. Because nothing is left half-paid,
there is no remainder to carry forward, and no check ever has to update a
balance or hand a number to the next check. Each of the six checks reads the
original balances and is a self-contained, stateless `if`.

The key point is that to know who pays whom, we have to look at each person
against both of the others, not one at a time. A debtor might end up paying
one recipient, the other, or both, depending on the whole picture, so we
cannot treat the people in isolation - we compare them pairwise. Concretely,
we check every debtor-recipient pair: could Jonas owe Maria something? Could
Jonas owe Simen? And so on. Because we do not have loops yet, we cannot say
"go through all debtors and all recipients" and let the machine find the
pairs; we write the cases out by hand with `if`-`else`, classifying each
balance as positive, negative, or zero, and setting up the transfers between
the specific pairs explicitly. The `min()` function gives each transfer
amount, and conditions are often combined with `and` when a person has to be
judged against both of the others at once.

**Worked example:** suppose the three balances come out as -200 (owes 200),
+150 (should receive 150) and +50 (should receive 50). The first person is
the only debtor. They pay the +150 person `min(200, 150)` = 150; that
recipient is now settled and the debtor still owes 50. They pay the +50
person `min(50, 50)` = 50; now everyone is settled. Two transfers, exactly
as the zero-sum balance guarantees.

### Part D - Test the program

Change the expense amounts and verify that the program produces correct
payments in all situations: one person owing two, two people owing one,
and the case where one person is exactly settled. Prefer amounts where
the total is divisible by three, to avoid fractional rounding.

### Looking ahead: Why only three people?

With three people we get by with three variables and pure `if`-`else`
logic - every possible situation can be enumerated and handled
separately. That is exactly what this chapter is about.

Still, notice how repetitive the code is: three nearly identical status
blocks in part B, six nearly identical checks in part C. With four people
it would be four status blocks and twelve pair checks, and with ten
people it would get completely out of hand.

But repetition is only the surface reason. The deeper one is the partial
payment. Everything above worked because at most one side ever had two
people, so every `min()` cleared a pair in full and left no remainder. With
four people that breaks: we can have two debtors and two recipients at once,
both sides "two". Now a debtor may not have enough to cover a recipient in
full, or a recipient may need more than any single debtor can give. A
payment then settles a pair only partly and leaves a remainder, and the next
payment has to take that remainder into account. That is the exact moment we
can no longer read the original balances and treat each pair on its own: we
need balances that we update as we go, and a loop that keeps going until
everyone is settled.

To handle any number of people, then, we need two things we have not learned
yet: a data structure that can hold all the participants and amounts
together (lists and dictionaries), and loops that repeat the same logic for
each person.