# Craps - One Round, Two Phases - Extra Exercise

## Exercise

Write a program that plays one round of this simplified version of craps for a
single player. Use two six-sided dice, each producing a value from 1 to 6.
The program rolls automatically; no bets, money or user input are required.

The first roll has these rules:

- A total of 2, 3 or 12 means the player loses (craps).
- A total of 7 or 11 means the player wins (natural).
- Any other total (4, 5, 6, 8, 9 or 10) becomes the player's point.

If a point was established, continue rolling:

- Rolling the point again means the player wins.
- Rolling 7 means the player loses.
- Any other total means another roll. The point does not change.

For example, once the point is 5, rolling 11 does not win the round. Only 5 or 7
can end that round. Likewise, 2, 3 and 12 do not automatically lose in this phase.

Implement these functions:

1. `roll_dice() -> int`: generate two separate random dice values, display both
   values and their sum, and return the sum.
2. `play_round() -> bool`: use `roll_dice()` to play one round. Display the point
   if one is established. Return `True` for a win and `False` for a loss.

Include short docstrings. Under an `if __name__ == "__main__"` guard, call
`play_round()` once and display the final result using its return value.
Importing the module must not start a game. Exact output wording is optional,
provided the dice, point when applicable, and final result are clear.

## Hints

- `random.randint(1, 6)` includes both endpoints. Make a separate call for each die.
- Handle the first roll before starting the repeated-roll phase.
- Keep the established point separately from the changing roll total.
- A return statement inside a loop exits the entire function.

## Example runs

These are four separate possible runs. Actual results will vary.

```text
You rolled 3 + 4 = 7
You win!
```

```text
You rolled 1 + 1 = 2
You lose.
```

```text
You rolled 2 + 3 = 5
Point: 5
You rolled 5 + 6 = 11
You rolled 1 + 4 = 5
You win!
```

```text
You rolled 4 + 4 = 8
Point: 8
You rolled 2 + 2 = 4
You rolled 1 + 6 = 7
You lose.
```

## Topics

- Function decomposition and return values
- Boolean results
- Repetition with changing state
- Random simulation
- Main guard and reusable functions

## Assessment criteria

| Criterion | Description | Weight (%) |
|---|---|---:|
| Dice function | Implements roll_dice to generate two separate six-sided dice values, display both values and their sum, and return the sum. | 20 |
| First-roll rules | Uses roll_dice in play_round, returns a loss for 2, 3 or 12 and a win for 7 or 11 on the first roll, and otherwise establishes and displays the point. | 25 |
| Point phase | Keeps the original point unchanged, repeats rolls until the point or 7 appears, returns the correct boolean outcome, and continues for all other totals. | 40 |
| Main program and import behaviour | Plays one round from a guarded main program and reports the result using play_round's return value, without starting a game when the module is imported. | 15 |
| **Total** | | **100%** |
