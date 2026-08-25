# Parking Fee

## Exercise Parking fee

A parking house sets its prices with the model below. Write a program that reads the details of
a single parking session and prints the fee. The model is fictional but consistent.

## The price model

| Time / situation      | Price                                          |
|-----------------------|------------------------------------------------|
| Daytime 08–18         | 30 per hour                                    |
| Evening 18–22         | 15 per hour                                    |
| Night 22–08           | free                                           |
| Weekend               | 50% discount                                   |
| Electric vehicle      | 50% discount (can be combined with weekend)    |
| First 15 min          | free                                           |
| Disability permit     | free up to 6 hours                             |
| Max price / day       | 250                                            |

## How the rules combine (read carefully)

1. **Hourly rate is decided by the start hour**, and applies to the whole session:
   `08 ≤ start < 18` gives 30, `18 ≤ start < 22` gives 15, otherwise 0 (night).
2. **Free period.** First **15 minutes** free; a **disability permit** extends this to the first
   **6 hours** (360 min). Only time beyond the free period is charged. (The 6-hour period already
   covers the 15-minute rule; they do not add up.)
3. **Base cost** is `rate × billable_minutes / 60`, where `billable = duration − free_minutes`
   (never below 0).
4. **Discounts.** Weekend halves the price; electric halves it again. They **stack**: a weekend
   electric car pays 25%.
5. **Daily cap.** Never more than **250** (applied last, after the discounts).
6. Print the result with **2 decimals**.

**Assumptions:** inputs are valid; a session is at most 24 hours and does not cross midnight.

## Your task

The code that reads the five values from the user is already written for you in the start file.
Below it, add logic that computes the fee and prints it, for example:

```
Parking fee: 22.50
```

## The heart of it: mixing conditions

The interesting part is not any single rule; it is making several apply *together*. The one to
watch is the pair of discounts:

> A weekend **and** electric car must get **both** halvings (25%).

If you write the two discounts as an `if / elif` chain, only the first match fires and the second
discount is silently lost:

```python
if weekend:
    cost = cost * 0.5
elif electric:          # never runs when weekend is also True — a bug
    cost = cost * 0.5
```

Because weekend and electric can **both** be true at once, they are **independent** conditions,
so they need **two separate `if` statements**, not an `elif` chain:

```python
if weekend:
    cost = cost * 0.5
if electric:
    cost = cost * 0.5
```

The rule of thumb: use `elif` for alternatives that exclude each other (the time bands); use
separate `if`s for conditions that can occur together (the discounts).

## Examples (inputs and printed result)

| start_hour | duration_min | weekend | electric | disability | Prints    |
|-----------:|-------------:|:-------:|:--------:|:----------:|:----------|
| 10         | 60           | no      | no       | no         | 22.50     |
| 20         | 120          | no      | no       | no         | 26.25     |
| 3          | 300          | no      | no       | no         | 0.00      |
| 10         | 10           | no      | no       | no         | 0.00      |
| 10         | 60           | no      | yes      | no         | 11.25     |
| 12         | 60           | yes     | no       | no         | 11.25     |
| 12         | 135          | **yes** | **yes**  | no         | **15.00** |
| 9          | 300          | no      | no       | yes        | 0.00      |
| 9          | 420          | no      | no       | yes        | 30.00     |
| 8          | 600          | no      | no       | no         | 250.00    |

The bold row is the combination case: 120 billable minutes at rate 30 is 60, then ×0.5 (weekend)
×0.5 (electric) = 15.00. Run the program and check a few of these by hand.

## Hints

- Time band: one `if / elif / else` on `start_hour`.
- `if disability:` sets `free_minutes = 360`, else `15`.
- Clamp: `if billable < 0: billable = 0`.
- Discounts: two separate `if`s (weekend, electric).
- Cap: `if cost > 250: cost = 250`.
- Print: `print(f"Parking fee: {cost:.2f}")`.
