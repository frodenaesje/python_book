# High Score Board

## Exercise

A small arcade game keeps the scores from today's players in a list. In this
exercise we work with the whole list at once - no loops needed. Every step can
be solved with one built-in function, one list method, slicing, the in
operator, or a short calculation.

We start with this list:

    scores = [420, 380, 510, 295, 620, 380]

Write a program that:

1. Prints how many players played today
2. Prints the total of all scores, and the highest and lowest score
3. Prints the average score, rounded to one decimal
4. A late player scored 450 - add it to the end of the list
5. The score at index 0 was registered wrong - it should be 440. Correct it
6. One player was disqualified - remove the score 295 from the list
7. Prints the three highest scores, highest first
8. Prints how many players scored exactly 380
9. Prints the position (index) of the score 620
10. Prints whether anyone reached 620
11. Prints all scores from best to worst

Rules:
- Do not use a loop - each step can be done without one
- The average is sum() divided by len()
- The three best come from sorted() plus slicing

## Example run

```
Players today: 6
Total: 2605
Highest: 620  Lowest: 295
Average: 434.2
Three best: [620, 510, 450]
Scored 380: 2
Position of 620: 3
Anyone reached 620? True
Best to worst: [620, 510, 450, 440, 380, 380]
```

## Topics

- `len()`, `sum()`, `max()`, `min()`, `sorted()`
- List methods: `append()`, `remove()`, `index()`, `count()`
- Changing an element by index
- Slicing to take the first three elements
- The `in` operator for membership
