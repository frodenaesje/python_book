# Expenses Settlement

## Exercise

After a trip with friends, someone has paid for the cabin, someone for the food, and someone for the fuel - and at some point the group needs to settle up. Several apps solve exactly this problem: everyone registers what they have paid, and the app calculates who owes whom.

We will build a simplified version for three friends on a cabin trip. The solution will use only variables, conditions, and functions we already know. Later, when we introduce loops and collections, the same basic idea can be extended to any number of people.

The expenses are given as variables in the starter code:

```python
jonas_paid = 2400    # cabin rental
maria_paid = 950     # food and drinks
simen_paid = 400     # fuel
```

All expenses are split equally among the three.

### Part A - Share and balance

Calculate the total and how much each person should cover:

```text
share = total / 3
```

Then calculate the balance for each person:

```text
balance = amount paid - share
```

The balance tells us how far the person is from being settled:

* A **positive balance** means the person has paid too much and should receive money.
* A **negative balance** means the person has paid too little and should pay money.
* A balance of **zero** means the person is already settled.

Print the total, the share, and each person's balance with two decimals.

Expected output with the numbers above:

```text
Total: 3750.00
Share per person: 1250.00
Jonas: +1150.00
Maria: -300.00
Simen: -850.00
```

Hint: f-strings can format a number with an explicit sign and two decimals:

```python
f"{jonas_balance:+.2f}"
```

Notice an important property of the balances:

```text
+1150 - 300 - 850 = 0
```

The balances must always add up to zero. The money that some people have paid too much is exactly the money that the others have paid too little.

### Part B - Status per person

Use `if`-`elif`-`else` to print a status line for each person.

For a positive balance:

```text
Jonas should receive 1150.00
```

For a negative balance:

```text
Simen should pay 850.00
```

Print the amount without the minus sign.

For a zero balance:

```text
Maria is settled
```

Do this separately for Jonas, Maria, and Simen.

### Part C - Who pays whom?

Now the program should perform the actual settlement.

For the original expenses, the balances are:

```text
Jonas: +1150.00
Maria: -300.00
Simen: -850.00
```

Jonas should therefore receive money, while Maria and Simen should pay. The final output should be:

```text
Maria pays 300.00 to Jonas
Simen pays 850.00 to Jonas
```

If everyone is already settled, print:

```text
No payments needed
```

#### Think of the balances as amounts that change

The important idea is that a balance represents what is **still left to settle**.

Suppose Maria has a balance of `-300` and Jonas has a balance of `+1150`.

Maria owes 300, while Jonas should receive 1150. A payment must therefore go from Maria to Jonas:

```text
Maria → Jonas
```

How much should Maria pay?

A debtor cannot pay more than they still owe, and a recipient should not receive more than they are still owed. The payment must therefore be the smaller of the two amounts:

```python
payment = min(-maria_balance, jonas_balance)
```

Here:

```text
min(300, 1150) = 300
```

After Maria pays 300, both balances must be updated:

```python
maria_balance += payment
jonas_balance -= payment
```

The new balances are:

```text
Maria:    0
Jonas: +850
```

Maria is now settled. Jonas still needs to receive 850.

Simen has a balance of `-850`, so the next payment can be:

```text
Simen → Jonas
```

The amount is:

```text
min(850, 850) = 850
```

After updating both balances:

```text
Simen: 0
Jonas: 0
```

Everyone is now settled.

This gives us the general rule for one payment:

1. Find a person with a negative balance - a **debtor**.
2. Find a person with a positive balance - a **recipient**.
3. Transfer the smaller of what the debtor owes and what the recipient should receive.
4. Update both balances.
5. Continue until all balances are zero.

The important part is step 4. A payment changes the situation, so later payments must use the **new balances**, not the original ones.

#### Turning the rule into code

For any particular pair of people, we first check whether one owes money and the other should receive money.

For example, Maria should pay Jonas only when:

```python
maria_balance < 0 and jonas_balance > 0
```

If this condition is true, calculate the payment:

```python
payment = min(-maria_balance, jonas_balance)
```

Then print the payment and update both balances:

```python
print(f"Maria pays {payment:.2f} to Jonas")

maria_balance += payment
jonas_balance -= payment
```

The complete check is therefore:

```python
if maria_balance < 0 and jonas_balance > 0:
    payment = min(-maria_balance, jonas_balance)
    print(f"Maria pays {payment:.2f} to Jonas")
    maria_balance += payment
    jonas_balance -= payment
```

Notice what happens to the signs. Maria starts with a negative balance, so adding the payment moves her balance **up toward zero**. Jonas starts with a positive balance, so subtracting the payment moves his balance **down toward zero**.

The same logic works regardless of which two people are involved.

#### Checking all possible payment directions

With three people, there are six possible payment directions:

```text
Jonas → Maria
Jonas → Simen

Maria → Jonas
Maria → Simen

Simen → Jonas
Simen → Maria
```

We have not learned loops yet, so write these possibilities explicitly as six `if` statements.

Each check follows exactly the same pattern:

```text
Is the first person a debtor?
        AND
Is the second person a recipient?

        ↓

Calculate payment

        ↓

Print payment

        ↓

Update both balances
```

For example, the opposite direction between Jonas and Maria would be:

```python
if jonas_balance < 0 and maria_balance > 0:
    payment = min(-jonas_balance, maria_balance)
    print(f"Jonas pays {payment:.2f} to Maria")
    jonas_balance += payment
    maria_balance -= payment
```

Do the same for the remaining possible directions.

These should be separate `if` statements, not one large `if`-`elif` chain. After one payment changes the balances, another payment may still be necessary.

For example, with:

```text
Jonas: -500
Maria: +200
Simen: +300
```

one payment can settle Maria:

```text
Jonas pays 200 to Maria
```

leaving:

```text
Jonas: -300
Maria:    0
Simen: +300
```

A later `if` statement can then use these updated balances and make the second payment:

```text
Jonas pays 300 to Simen
```

The balances are now:

```text
Jonas: 0
Maria: 0
Simen: 0
```

This is why updating the balances after every payment is useful: every new check sees the current state of the settlement.

#### Could we solve the three-person case differently?

Yes. Three people are a special case. Because the balances always sum to zero, the possible situations are limited enough that we could derive a shorter solution that examines the original balances and handles the possible patterns directly.

That would work for three people, but it would rely on properties of this particular case.

Instead, we deliberately update the balances after each payment. This is slightly more work here, but it introduces the same basic mechanism we will later use when the number of participants is not fixed.

### Part D - Test the program

Change the expense amounts and verify that the program produces correct payments in different situations:

* one person owes the other two
* two people owe one person
* one person is already settled
* everyone is settled

Also try changing which person is the debtor or recipient so that different payment directions are tested.

Prefer amounts where the total is divisible by three to avoid fractional rounding while testing the settlement logic.

### Looking ahead: From three people to many

The settlement rule itself does not depend on there being exactly three people:

```text
find debtor and recipient
        ↓
calculate payment
        ↓
update balances
        ↓
repeat
```

What changes when there are more people is how we represent the participants and how we repeat the operation.

With three people, we can store everything in individual variables and write the possible payment directions explicitly. That is manageable because there are only six.

With four people there are twelve possible payment directions. With ten people there are ninety. Writing every possibility as a separate `if` statement would quickly become impractical.

More importantly, with more participants there may be several debtors and several recipients at the same time. A payment may settle one person while leaving the other with a remaining balance. The program must then continue from that updated state.

For example:

```text
-500, -100, +300, +300
```

If the first debtor pays 300 to one recipient, the balances become:

```text
-200, -100, 0, +300
```

The settlement is not finished. The remaining balances determine what should happen next.

The algorithm, however, has not changed. We still find a debtor and a recipient, transfer:

```python
min(amount_owed, amount_to_receive)
```

update their balances, and continue.

To make that practical for any number of people, we need two tools that we have not learned yet:

* **collections**, such as lists and dictionaries, to keep participants and balances together
* **loops**, to repeat the same settlement operation instead of writing every possible pair by hand

When we introduce those tools later, we can replace the repetitive code with a much more general solution - without changing the basic settlement logic developed here.
